class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = [0, 0, 0]  # To count numbers with remainders 0, 1, and 2 respectively
        
        for num in nums:
            count[num % 3] += 1
            
        # For numbers with remainder 1 or 2, it takes 1 operation to make them divisible by 3
        return count[1] + count[2]