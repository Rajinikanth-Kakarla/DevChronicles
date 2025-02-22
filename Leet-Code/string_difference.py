class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = sum(map(ord, t)) - sum(map(ord, s))
        return chr(diff)


        