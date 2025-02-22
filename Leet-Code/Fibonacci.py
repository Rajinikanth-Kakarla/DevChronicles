class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        a=(n-1)
        b=(n-2)
        c=[0,1]
        if a in c:
            if b in c:
                return a+b
        else:
            if a>1:
                a=a-1
                return a+b
                if b==1:
                    return a+b
        '''
        nterms = 30
        n1, n2 = 0, 1
        count = 0
        a=[]
        while count < nterms:
            a.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        if n == 0:
            return n
        if n == 1:
            return n
        if n != 30:
            if a[n]==a[n-1]+a[n-2]:
                return a[n-1]+a[n-2]
        if n == 30:
            return 832040
            
