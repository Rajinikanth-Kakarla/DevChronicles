class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        gcd_length = gcd(len(str1), len(str2)) # 3 3

        substring = str1[:gcd_length] # :3 --> 0,1,2

        if substring * (len(str1) // gcd_length) == str1 and substring * (len(str2) // gcd_length) == str2: # ABC * 2 = Str1 true 
            return substring
        
        else:
            return ""