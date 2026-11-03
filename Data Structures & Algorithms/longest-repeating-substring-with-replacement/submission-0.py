class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        L = 0
        counts = {}
        max_counter = 0

        for R in range(0, n):
            counts[s[R]] = counts.get(s[R], 0) + 1

            while R - L + 1 - max(counts.values()) > k:
                counts[s[L]] -= 1
                L += 1

            max_counter = max(max_counter, R - L +1)

        return max_counter
                    