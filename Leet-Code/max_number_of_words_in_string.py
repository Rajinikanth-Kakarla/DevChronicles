class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        list1 = []
        for i in range(len(sentences)):
            count = 0
            if True:
                count = len(sentences[i].split())
            list1.append(count)
        return max(list1)