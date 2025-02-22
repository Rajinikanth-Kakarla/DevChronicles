class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, graph = 0, {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
                        
        for sym, val in collections.Counter(s).items():
            result += graph[sym]*val
        
        for sub in ["IV", "IX", "XL", "XC", "CD", "CM"]:
            result -= s.count(sub)*2*graph[sub[0]]        
            
        return result