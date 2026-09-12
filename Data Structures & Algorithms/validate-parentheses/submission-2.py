class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            ")":"(",
            "]":"[",
            "}":"{",
        }

        for i in range(len(s)):
            if s[i] in ["(","[","{"]:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if pair[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        else:
            return False

        


        