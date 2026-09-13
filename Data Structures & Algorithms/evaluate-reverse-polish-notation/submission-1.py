class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = {"+","-","*","/"}
        stack = []

        for i in range(len(tokens)):
            if tokens[i] not in operator:
                stack.append(int(tokens[i]))
            else:
                new = stack.pop()
                result = stack.pop()
                if tokens[i] == "+":
                    stack.append(result + new)
                elif tokens[i] == "-":
                    stack.append(result - new)
                elif tokens[i] == "*":
                    stack.append(int(result * new))
                elif tokens[i] == "/":
                    stack.append(int(result / new))

        return stack.pop()


        