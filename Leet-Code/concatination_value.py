class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        while len(nums) > 0:
            n = len(nums)
            if n == 1:
                res += nums[0]
                nums = []
            else:
                res += int(str(nums[0]) + str(nums[-1]))
                nums = nums[1:-1]
        return res