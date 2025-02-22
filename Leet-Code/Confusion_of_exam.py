class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        '''
        :type answerKey: str
        :type k: int
        :rtype: int
        '''
        """newList = '' # T ,T
        count = 0
        for i in range(len(answerKey)):         # 0    1
            for j in range(1,len(answerKey)):   # 1    2
                if answerKey[i] == answerKey[j]:# T=T  T!=F
                    newList+answerKey[i]
                    newList+answerKey[j]
                    break                       # break
                else:
                    while k!=0:      # 1
                        count = 1              # 1
                        if answerKey[i] != answerKey[j] and answerKey[i] == 'T':
                            answerKey[j] = answerKey[i]
                            newList+answerKey[j]
                            break
                        elif answerKey[i] != answerKey[j] and answerKey[i] == 'F':
                            answerKey[j] = answerKey[i]
                            newList+answerKey[j]
                            break
                        k-=1
                        break
                j+=1                            # j = 2
                break                           # break
            i+=1                                # i = 1

        return len(newList)
"""
        n = len(answerKey)
        maxLen = 0
        maxT = 0
        maxF = 0
        countT = 0
        countF = 0
        left = 0

        for right in range(n):
            if answerKey[right] == 'T':
                countT += 1
                maxT = max(maxT, countT)
            else:
                countF += 1
                maxF = max(maxF, countF)

            windowSize = right - left + 1
            if windowSize - max(maxT, maxF) > k:
                if answerKey[left] == 'T':
                    countT -= 1
                else:
                    countF -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen