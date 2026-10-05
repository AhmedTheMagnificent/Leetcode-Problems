class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(ch)
            else:
                if s[i - 1] == "(":
                    score += 2 ** (len(stack) - 1)
                stack.pop()
        return score