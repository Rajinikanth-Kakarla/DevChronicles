class Solution:
    def climbStairs(self, n: int) -> int:
        # reverse fib == staircase
        nl = 1
        nl2 = 1
        count = 0
        dp = []
        while count<n:
            dp.append(nl)
            nl_ = nl + nl2
            nl = nl2
            nl2 = nl_
            count += 1
        if n == 1:
            return 1
        else:
            sum = dp[-1]+dp[-2]
        return sum