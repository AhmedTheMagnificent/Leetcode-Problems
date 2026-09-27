class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]

        for ch in s:
            if ch == "(":
                stack.append([])
            elif ch == ")":
                stack[-2].extend(stack[-1][::-1])
                stack.pop()
            else:
                stack[-1].append(ch)

        return "".join(stack[0])