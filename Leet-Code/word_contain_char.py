class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        list1 = []
        for i in range(len(words)):
            if x in words[i]:
                list1.append(i)
        return list1