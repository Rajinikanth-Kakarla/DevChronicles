class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge of lists
        for i in nums2:
            nums1.append(i)
        # sort the list
        nums1.sort()
        left = 0
        right = len(nums1)
        mid = (left+right)//2
        # if list size == odd return mid
        if len(nums1)%2 != 0:
            return nums1[mid]
        # if list size == even return mid = (m-1 + m+1)/2
        else:
            val = (nums1[mid-1] + nums1[mid]) / 2
            return val