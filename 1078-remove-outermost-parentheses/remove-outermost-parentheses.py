class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        st = ""
        for ch in s:
            if ch == "(":
                if len(stack) > 0:
                    st += ch
                stack.append(ch)
            else:
                stack.pop()
                if len(stack) > 0:
                    st += ch

        return st
            
            