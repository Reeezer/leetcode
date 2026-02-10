import os
import re

ROOT_DIR: str = os.path.dirname(os.path.abspath(__file__))
README_PATH: str = os.path.join(ROOT_DIR, "README.md")
SOLUTION_DIRS: dict[str, tuple[str, str]] = {
    "1.easy": ("Easy", "brightgreen"),
    "2.medium": ("Medium", "orange"),
    "3.hard": ("Hard", "red"),
}


def count_solutions() -> dict[str, int]:
    """
    Count the number of ``.py`` solution files per difficulty folder.

    Returns
    -------
    dict[str, int]
        A mapping from folder name to solution count.
    """
    counts: dict[str, int] = {}
    for folder in SOLUTION_DIRS:
        folder_path: str = os.path.join(ROOT_DIR, folder)
        count: int = 0
        if os.path.isdir(folder_path):
            for f in os.listdir(folder_path):
                if f.endswith(".py"):
                    count += 1
        counts[folder] = count
    return counts


def update_badges(counts: dict[str, int]) -> None:
    """
    Update the difficulty badges in the README.

    Parameters
    ----------
    counts : dict[str, int]
        A mapping from folder name to solution count.
    """
    with open(README_PATH, "r", encoding="utf-8") as f:
        content: str = f.read()

    for folder, (label, color) in SOLUTION_DIRS.items():
        content = re.sub(
            rf"(!\[{label}\]\(https://img\.shields\.io/badge/{label}-)\d+(-{color}\))",
            rf"\g<1>{counts[folder]}\2",
            content,
        )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    for folder, (label, _) in SOLUTION_DIRS.items():
        print(f"Updated badge: {label}-{counts[folder]}")


def main() -> None:
    """Count solutions per difficulty and update the README badges."""
    counts: dict[str, int] = count_solutions()
    update_badges(counts)


if __name__ == "__main__":
    main()
