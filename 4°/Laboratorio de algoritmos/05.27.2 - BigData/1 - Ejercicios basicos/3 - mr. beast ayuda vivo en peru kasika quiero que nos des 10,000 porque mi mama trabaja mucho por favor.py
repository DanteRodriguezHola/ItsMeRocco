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

def transfer(S, T):
    while not S.isEmpty():
        new_value = S.pop()

        T.push(new_value)

        print(S.stack)
        print(T.stack)

if __name__ == "__main__":
    S = Stack()

    S.push(4)
    S.push(8)
    S.push(10)
    S.push(5)

    T = Stack()

    transfer(S, T)


