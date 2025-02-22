from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        LeftSum = []
        RightSum = []
        Result = []

        left_sum = 0
        for num in nums:
            left_sum += num
            LeftSum.append(left_sum)

        right_sum = 0
        for num in reversed(nums):
            right_sum += num
            RightSum.append(right_sum)
        RightSum.reverse()

        for i in range(len(nums)):
            Result.append(abs(LeftSum[i] - RightSum[i]))

        return Result