class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def longest(target):
            left = 0
            count = 0
            ans = 0
            for right in range(len(answerKey)):
                if answerKey[right] != target:  count += 1
                while count > k:
                    if answerKey[left] != target:   count -= 1
                    left += 1
                ans = max(ans, right - left + 1)
            return ans
        return max(
            longest('T'),
            longest('F')
        )