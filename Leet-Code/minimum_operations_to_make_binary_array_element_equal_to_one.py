class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operations = 0
        
        # Traverse through the array to find the number of flips needed
        for i in range(1, len(nums)):
            # When there's a transition, we need to count it as a required flip
            if nums[i] != nums[i - 1]:
                operations += 1
        
        # If the first element is 0, we need an additional operation to start the process
        if nums[0] == 0:
            operations += 1
        
        return operations