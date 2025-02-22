class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        char_count = {}
        
        # Count the frequency of each character
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Initialize the length of the longest palindrome
        palindrome_length = 0
        odd_count_found = False
        
        # Calculate the length of the longest palindrome
        for count in char_count.values():
            if count % 2 == 0:
                palindrome_length += count
            else:
                palindrome_length += count - 1
                odd_count_found = True
        
        # If there was any character with an odd count, add one to the length
        # (for the middle character)
        if odd_count_found:
            palindrome_length += 1
        
        return palindrome_length