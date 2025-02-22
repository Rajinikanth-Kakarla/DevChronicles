class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        numRequests = len(requests)
        maxAchievable = 0
        
        for mask in range(1 << numRequests):
            outgoing = [0] * n
            incoming = [0] * n
            
            for i in range(numRequests):
                if (mask >> i) & 1:
                    fromBuilding, toBuilding = requests[i]
                    outgoing[fromBuilding] += 1
                    incoming[toBuilding] += 1
            
            if all(x == y for x, y in zip(outgoing, incoming)):
                maxAchievable = max(maxAchievable, bin(mask).count('1'))
        
        return maxAchievable