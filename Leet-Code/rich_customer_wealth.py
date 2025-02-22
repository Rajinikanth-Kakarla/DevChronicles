class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        summ = []
        for i in range(len(accounts)):
            summ.append(sum(accounts[i]))
        return max(summ)
        