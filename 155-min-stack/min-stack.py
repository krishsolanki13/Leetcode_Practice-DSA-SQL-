# class MinStack:

#     def __init__(self):
#         self.stack = []
    
#     def push(self, val:int) -> None:
#         self.stack.append(val)
    
#     def pop(self) -> int:
#         return self.stack.pop()
    
#     def top(self) -> int:
#         return self.stack[-1]
    
#     def getMin(self) -> int:
#         temp = []
#         mini = self.stack[-1]

#         while self.stack:
#             mini = min(mini, self.stack[-1])
#             temp.append(self.stack.pop())

#         while temp:
#             self.stack.append(temp.pop())
        
#         return mini
    
class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
    
    def push(self, val: int):
        self.stack.append(val)
        self.minstack.append(min(val, self.minstack[-1] if self.minstack else val))

    def pop(self) -> int:
        self.minstack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.minstack[-1]
    