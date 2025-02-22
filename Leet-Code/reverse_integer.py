class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        p = (pow(2,31))-1
        q = pow(-2,31)
        if x>=0:
            while x!=0:
                rem = x%10
                rev = rev*10+rem
                x/=10
            if rev < p:
                return rev
            else:
                return 0
            
        elif x<0:
            x=x*-1
            while x!=0:
                rem = x%10
                rev = rev*10+rem
                x/=10
            if q < rev*-1:
                return rev*-1
            else:
                return 0
        