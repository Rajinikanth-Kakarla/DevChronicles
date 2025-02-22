class Solution:
    def tribonacci(self, n: int) -> int:
        #code goes here
        """a = 0
        b = 1
        dp = []
        itr = 0
        while itr < n:
            dp.append(a)
            temp = a+b
            a = b
            b = temp
            itr += 1
        sum = dp[n-1] + dp[n-2] + dp[n-3]
        return sum"""
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            t0, t1, t2 = 0, 1, 1
    
    # Calculate the Tribonacci number iteratively
            for _ in range(n - 2):
                t0, t1, t2 = t1, t2, t0 + t1 + t2
            
            return t2