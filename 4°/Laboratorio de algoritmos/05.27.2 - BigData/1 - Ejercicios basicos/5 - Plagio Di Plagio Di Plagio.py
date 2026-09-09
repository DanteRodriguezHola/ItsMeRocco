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
        pass

def invert_list(list):
    auxiliary_stack = Stack()

    while list:
        new_value = list.pop(0)

        auxiliary_stack.push(new_value)

    while not auxiliary_stack.isEmpty():
        new_item = auxiliary_stack.pop()

        list.append(new_item)

if __name__ == "__main__":
    list = [1, 3, 5, 6]

    invert_list(list)

    print(list)