class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # b = universal set of numbers()
        # c = b - arr
        # return c[k]
        # k = 5
        n = len(arr)
        missing = 0
        i = 0
        current = 1
        while missing < k:
            if i < n and arr[i] == current:
                i += 1
            else:
                missing += 1
                if missing == k:
                    return current
            current += 1
        return -1
