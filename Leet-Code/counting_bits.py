class Solution:
    def countBits(self, n: int) -> List[int]:
        a = []
        for i in range(n+1):
            b = str(bin(i))
            a.append(b.count('1'))
        return a