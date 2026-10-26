class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        max_consecutive = 0

        for x in numbers:

            if x - 1 not in numbers:
                consecutive = 1
                starting_value = x

                while starting_value + 1 in numbers:
                    consecutive += 1
                    starting_value += 1

                if consecutive > max_consecutive:
                    max_consecutive = consecutive

        return(max_consecutive)
