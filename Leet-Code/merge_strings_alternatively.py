from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newString = "".join(''.join(x) for x in zip_longest(word1,word2,fillvalue = ""))
        return newString