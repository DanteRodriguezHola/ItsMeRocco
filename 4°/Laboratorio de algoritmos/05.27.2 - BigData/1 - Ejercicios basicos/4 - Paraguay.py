class Stack:
    def __init__(self):
        self.stack = []

    def push(self, new_value):
        self.stack.append(new_value)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"

        else:
            return self.stack.pop(-1)
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"

        else:
            return self.stack[-1]

    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.stack)
    
    def clear(self):
        if not self.isEmpty():
            self.pop()
            self.clear()

if __name__ == "__main__":
    stack = Stack()

    stack.push(6)
    stack.push(7)
    stack.push(6)
    stack.push(9)

    print(stack.stack)

    stack.clear()

    print(stack.stack)