class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_len = 0
        for ch in s:
            if ch == "(":
                stack.append(ch)
            elif ch == ")":
                stack.pop()
            max_len = max(max_len, len(stack))
        return max_len