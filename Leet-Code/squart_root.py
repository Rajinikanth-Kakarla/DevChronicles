class Solution:
    def mySqrt(self, x: int) -> int:
#initialising left and right
        left = 1
        right = x
#if x value is less than 2 return x
        if x < 2 :
            return x
#else
        while left < right :
            mid = left + math.floor((right-left)/2)
            if mid * mid == x :
                return mid
            elif mid * mid > x :
                right = mid
            elif mid * mid < x :
                left = mid + 1
        
        return left - 1
        