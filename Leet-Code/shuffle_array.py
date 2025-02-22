class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        list1 = []
        list2 = []
        list3 = []
        for i in range(0,n):
            list1.append(nums[i])
        for j in range(n,len(nums)):
            list2.append(nums[j])
        for k in range(n):
            list3.append(list1[k])
            list3.append(list2[k])
        return list3