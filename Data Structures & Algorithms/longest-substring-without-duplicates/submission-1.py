class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        L = 0
        max_counter = 0
        seen = set()

        for R in range(0, n):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
            seen.add(s[R])

            max_counter = max(max_counter, R - L + 1)

        return max_counter
