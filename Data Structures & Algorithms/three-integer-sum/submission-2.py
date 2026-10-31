class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []
        n = len(nums)

        for i in range(0, n):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            complement = - sorted_nums[i]
            l = i + 1
            r = n - 1

            while l < r:

                if sorted_nums[l] + sorted_nums[r] > complement:
                    r -= 1
                elif sorted_nums[l] + sorted_nums[r] < complement:
                    l += 1
                else:
                    result.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    r -= 1
                    l += 1

                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1
                    
        return result