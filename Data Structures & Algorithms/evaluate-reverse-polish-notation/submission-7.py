class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok == '+':
                stack.append(stack.pop() + stack.pop())
            elif tok == '*':
                stack.append(stack.pop() * stack.pop())
            elif tok == '-':
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(t2-t1)
            elif tok == '/':
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(int(t2/t1))
            else:
                stack.append(int(tok))
        return int((stack[0]))
        