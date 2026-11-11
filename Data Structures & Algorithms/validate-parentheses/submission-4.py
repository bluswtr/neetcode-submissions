class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenMap = { "}" : "{", ")" : "(", "]" : "[" }

        for c in s:
            if c in parenMap:
                if stack and parenMap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)


        # we _should_ have an empty stack by now. If not return False
        if len(stack) == 0:
            return True
        return False
