class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:

            if ch == '(':
                stack.append(0)
            if ch == '{':
                stack.append(1)
            if ch == '[':
                stack.append(2)
            if len(stack) == 0:
                return False
            if ch == ')':
                if stack[-1] != 0:
                    return False
                stack.pop()

            if ch == '}':
                if stack[-1] != 1:
                    return False
                stack.pop()
            if ch == ']':
                if stack[-1] != 2:
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        return False

        