class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """

        common = set(nums[0])
        for i in range(1, len(nums)):
            common &= set(nums[i])
        return sorted(list(common))