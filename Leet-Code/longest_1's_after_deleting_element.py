class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        count_zeros = 0
        max_length = 0
        
        while right < len(nums):
            if nums[right] == 0:
                count_zeros += 1
            
            # Shrink the window if the number of zeros exceeds 1
            while count_zeros > 1:
                if nums[left] == 0:
                    count_zeros -= 1
                left += 1
            
            # Update the maximum length
            max_length = max(max_length, right - left)
            
            right += 1
        
        return max_length