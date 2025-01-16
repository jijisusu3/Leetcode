class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first_min = float('inf')
        second_min = float('inf')
        for i in nums:
            if i <= first_min:
                first_min = i
            elif i <= second_min:
                second_min = i
            else:
                return True
        return False