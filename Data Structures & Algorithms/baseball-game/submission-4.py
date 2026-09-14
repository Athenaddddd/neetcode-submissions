class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        op = {"+","D","C"} #set

        for i in range(len(operations)):
            if operations[i] not in op:
                stack.append(int(operations[i]))
            elif operations[i] == "+" :
                stack.append(int(stack[-1]) + int(stack[-2]))
            elif operations[i] == "D" :
                stack.append(int(stack[-1]) * 2)
            elif operations[i] == "C" :
                stack.pop()

        return sum(stack)
