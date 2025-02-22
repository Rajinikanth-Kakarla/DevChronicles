class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        list1 = []
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            list1.append(summ)
        return list1