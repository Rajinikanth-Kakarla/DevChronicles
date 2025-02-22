class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        neg_row = 0
        total = 0

        for row in bank:
            cur_row_count = self.calc(row)
            if cur_row_count == 0:
                continue

            total += cur_row_count * neg_row
            neg_row = cur_row_count

        return total

    def calc(self, s):
        return sum(int(c) for c in s)