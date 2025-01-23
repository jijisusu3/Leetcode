class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        idx = 0

        for num in nums:
            if nums != 0:
                nums[idx] = num
                idx += 1

        while idx < len(nums):
            nums[idx] = 0
            idx += 1

