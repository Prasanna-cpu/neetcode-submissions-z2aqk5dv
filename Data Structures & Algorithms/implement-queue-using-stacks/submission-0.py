class MyQueue:

    def __init__(self):
        self.stack_push = []  # Stack for enqueue operations
        self.stack_pop = []   # Stack for dequeue operations

    def push(self, x: int) -> None:
        self.stack_push.append(x)

    def pop(self) -> int:
        self.move_elements()
        return self.stack_pop.pop()

    def peek(self) -> int:
        self.move_elements()
        return self.stack_pop[-1]

    def empty(self) -> bool:
        return not self.stack_push and not self.stack_pop

    def move_elements(self) -> None:
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()