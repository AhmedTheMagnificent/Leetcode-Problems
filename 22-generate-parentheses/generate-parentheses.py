class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        brackets = []
        def backtrack(s, open, close):
            if len(s) == 2 * n: brackets.append(s)
            if open < n:        backtrack(s + "(", open + 1, close)
            if close < open:    backtrack(s + ")", open, close + 1)
        backtrack("", 0, 0)
        return brackets