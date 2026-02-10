import os
import re

ROOT_DIR: str = os.path.dirname(os.path.abspath(__file__))
SKIP: set[str] = {".git", "__pycache__", "rename_files.py", "README.md"}


def should_skip(name: str) -> bool:
    """
    Check if a file or directory should be skipped.

    Parameters
    ----------
    name : str
        The file or directory name.

    Returns
    -------
    bool
        True if the name is in the skip set.
    """
    return name in SKIP


def transform_name(name: str) -> str:
    """
    Transform a file or directory name to lowercase with underscores.

    Keeps the dot after a leading number pattern (no space).
    e.g. ``"812. Largest Triangle Area.py"`` -> ``"812.largest_triangle_area.py"``

    Parameters
    ----------
    name : str
        The original file or directory name.

    Returns
    -------
    str
        The transformed name.
    """
    match: re.Match[str] | None = re.match(r"^(\d+\.)\s", name)
    if match:
        prefix: str = match.group(1)
        rest: str = name[len(match.group(0)) :]
        rest = rest.lower().replace(" ", "_")
        return prefix + rest
    else:
        return name.lower().replace(" ", "_")


def collect_entries(root: str) -> list[str]:
    """
    Collect all files and directories, deepest first.

    Parameters
    ----------
    root : str
        The root directory to walk.

    Returns
    -------
    list[str]
        A list of absolute paths to files and directories.
    """
    entries: list[str] = []
    for dirpath, dirnames, filenames in os.walk(root, topdown=True):
        dirnames[:] = [d for d in dirnames if not should_skip(d)]

        for f in filenames:
            if should_skip(f):
                continue
            entries.append(os.path.join(dirpath, f))

        if os.path.abspath(dirpath) != os.path.abspath(root):
            entries.append(dirpath)

    # Reverse so deepest paths are renamed first
    entries.sort(key=lambda p: p.count(os.sep), reverse=True)

    return entries


def main() -> None:
    """
    Main entry point.

    Lists all renameable entries, previews changes,
    and renames upon user confirmation.
    """
    entries: list[str] = collect_entries(ROOT_DIR)

    renames: list[tuple[str, str]] = []
    for path in entries:
        parent: str = os.path.dirname(path)
        name: str = os.path.basename(path)
        new_name: str = transform_name(name)
        if new_name != name:
            renames.append((path, os.path.join(parent, new_name)))

    if not renames:
        print("Nothing to rename.")
        return

    print(f"Found {len(renames)} item(s) to rename:\n")
    for old, new in renames:
        print(f"  {os.path.relpath(old, ROOT_DIR)}")
        print(f"    -> {os.path.relpath(new, ROOT_DIR)}\n")

    confirm: str = input("Proceed with renaming? [y/N] ").strip().lower()
    if confirm != "y":
        print("Aborted.")
        return

    for old, new in renames:
        os.rename(old, new)
        print(f"Renamed: {os.path.relpath(old, ROOT_DIR)} -> {os.path.relpath(new, ROOT_DIR)}")

    print("\nDone!")


if __name__ == "__main__":
    main()
