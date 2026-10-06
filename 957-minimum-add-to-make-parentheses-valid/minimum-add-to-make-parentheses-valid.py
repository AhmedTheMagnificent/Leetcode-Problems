class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        nonstack = []
        for ch in s:
            if ch == "(":
                stack.append(ch)
            else:
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    nonstack.append(ch)
        return len(nonstack) + len(stack)
                    