class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        Value = 0
        for i in range(len(operations)):
            if operations[i] == "--X":
                Value -=1
            elif operations[i] == "X--":
                Value -=1
            elif operations[i] == "++X":
                Value +=1
            elif operations[i] == "X++":
                Value +=1
        return Value