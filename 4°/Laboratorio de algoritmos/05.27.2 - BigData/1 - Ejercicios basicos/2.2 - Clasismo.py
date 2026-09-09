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

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, new_value):
        self.queue.append(new_value)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        
        else:
            return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"

        else:
            return self.queue[0]

    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.queue)

if __name__ == "__main__":
    stack = Stack()

    stack.push(2)
    stack.push(4)
    stack.push(8)
    stack.push(16)

    stack.pop()
    stack.pop()

    print(stack.peek())

    print(stack.isEmpty())

    print(stack.size())


    queue = Queue()

    queue.enqueue(3)
    queue.enqueue(9)
    queue.enqueue(27)
    queue.enqueue(81)

    queue.dequeue()
    queue.dequeue()

    print(queue.peek())

    print(queue.isEmpty())

    print(queue.size())
