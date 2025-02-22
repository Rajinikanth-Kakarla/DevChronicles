class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)): # 0 1 2 3 4 5
            a = nums[i]            # 0 2 1 5 3 4
            b = nums[a]            # 0 1 2 4 5 3
            l.append(b)
        return l