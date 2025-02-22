class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        '''if jewels not in stones:
            return 0
        count = 0
        if jewels in stones:
            for j in range(len(jewels)):
                f = jewels[j]
                if stones.count(f)!=0:
                    count += stones.count(f)
            return count
'''

        count = 0
        for s in stones:
            if s in jewels:
                count += 1
        return count