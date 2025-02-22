
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        length = max(len(num1), len(num2))
        num1 = num1.zfill(length)
        num2 = num2.zfill(length)

        result = []
        carry = 0

        for i in range(length - 1, -1, -1):
            digit_sum = int(num1[i]) + int(num2[i]) + carry
            result.append(str(digit_sum % 10))
            carry = digit_sum // 10

        if carry:
            result.append(str(carry))

        return ''.join(result[::-1])