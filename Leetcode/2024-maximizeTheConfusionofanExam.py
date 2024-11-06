# Leetckode Maximize the confusion of an exam

# A teacher is writing a test with n questions, where answerKey[i] is original answer to ith questions. 
# given an int K, max no. of times you may perfoom the following operations;
#       change answer key fir any question to 'T or 'F

# Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.

def maxConsecutiveAnswers(answerKey, k):
    n = len(answerKey)
    left = 0
    right = 0
    maxCount = 0
    count = 0
    while right < n:
        if answerKey[right] == answerKey[left]:
            count += 1
            right += 1
            maxCount = max(maxCount, count)
        elif k > 0:
            k -= 1
            count += 1
            right += 1
            maxCount = max(maxCount, count)
        else:
            if answerKey[left] == 'T':
                while left < right and answerKey[left] == 'T':
                    count -= 1
                    left += 1
            else:
                while left < right and answerKey[left] == 'F':
                    count -= 1
                    left += 1
            left += 1
            right += 1
    return maxCount
