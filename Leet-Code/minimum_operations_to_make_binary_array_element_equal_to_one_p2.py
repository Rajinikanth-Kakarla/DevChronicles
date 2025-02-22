class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        operations = 0
        
        for i in range(n - 2):  # We only need to check until the third last element
            if nums[i] == 0:
                # Flip the current element and the next two elements
                nums[i] = 1 - nums[i]
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]
                operations += 1
        
        # Check if the last three elements are all 1s
        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        
        return operations