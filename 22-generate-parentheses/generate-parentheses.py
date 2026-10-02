class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        paranth = []
        def backtrack(current, opening, closing):
            if len(current) == 2 * n:
                paranth.append(current)
                return
            if opening < n:
                backtrack(current + "(", opening + 1, closing)
            if closing < opening:
                backtrack(current + ")", opening, closing + 1)

        backtrack("", 0, 0)
        return paranth

