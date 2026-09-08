class Solution(object):
    def sortedSquares(self, nums):
        for i in range (0, len(nums)):
            nums[i] = nums[i] ** 2

        sorted_nums = sorted(nums)

        return sorted_nums

        