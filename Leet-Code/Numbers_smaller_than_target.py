class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        list1 = []
        for i in range(len(nums)):
            count = 0
            currValue = nums[i]
            for j in range(len(nums)):
                if nums[j] < currValue:
                    count += 1
            list1.append(count)
        return list1