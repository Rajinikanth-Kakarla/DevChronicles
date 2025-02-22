class Solution:
    def decimaltobinary(self, deb):
        if deb == 0:
            return [0]
        binary_list = []
        while deb > 0:
            binary_list.insert(0, deb % 2)
            deb = deb // 2
        return binary_list

    def binarytodecimal(self, bid):
        decimal, i = 0, 0
        while bid != []:
            dec = bid.pop()
            decimal = decimal + dec * pow(2, i)
            i += 1
        return decimal

    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        summ = 0
        for i in range(len(nums)):
            binary_representation = self.decimaltobinary(i)
            if binary_representation.count(1) == k:
                decimal_index = self.binarytodecimal(binary_representation)
                summ += nums[decimal_index]
        return summ