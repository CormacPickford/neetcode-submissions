class MinStack:

    def __init__(self):
        self.stack = []
        self.length = 0
        self.minimum = (2**31)-1
        self.mstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.length +=1
        self.minimum = min(val,self.minimum)
        self.mstack.append(self.minimum)
        print(self.mstack)

        

    def pop(self) -> None:
        self.stack.pop()
        self.length -=1
        self.mstack.pop()
        if self.length != 0 :
            self.minimum = self.mstack[-1]
        else:
            self.minimum = (2**31)-1


        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum




        
