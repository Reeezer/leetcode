class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # O(n)
        longest_len = 0
        i = 0
        last_seen: dict[str, int] = {}
        for j in range(len(s)):
            # If already seen, jump i,j
            if s[j] in last_seen and last_seen[s[j]] >= i:
                i = last_seen[s[j]] + 1
            
            last_seen[s[j]] = j
            if j - i + 1 > longest_len:
                longest_len = j - i + 1

        return longest_len