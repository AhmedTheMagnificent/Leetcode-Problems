class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []        
        for token in tokens:
            if token.lstrip('-').isdigit():
                numStack.append(int(token))
            else:
                b = numStack.pop()
                a = numStack.pop()
                if token == "+":
                    numStack.append(a + b)
                elif token == "-":
                    numStack.append(a - b)
                elif token == "*":
                    numStack.append(a * b)
                else:
                    numStack.append(int(a / b))
        return numStack[0]

        