class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in range(len(s)):
            # push all types of open parens
            if c == "{" or c == "[" or c == "(":
                stack.append(c)
            # return False if a non-matching pair are found
            elif c == "}" and stack[-1] != "{":
                return False
            elif c == ")" and stack[-1] != "(":
                return False
            elif c == "]" and stack[-1] != "[":
                print("]")
                return False

        # we _should_ have an empty stack by now. If not return False
        if len(stack) == 0:
            return True
        return False
