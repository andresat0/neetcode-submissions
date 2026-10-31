class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        max_container = []

        while l < r:

            area = (r - l) * min(heights[l], heights[r])

            max_container.append(area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return max(max_container)