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

def is_nested(string):
    hashmap = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    auxiliary_stack = Stack()

    for character in string:
        if character in hashmap.values():
            auxiliary_stack.push(character)

        elif hashmap[character] == auxiliary_stack.peek():
            if auxiliary_stack.isEmpty():
                return False
            
            auxiliary_stack.pop()

    return auxiliary_stack.isEmpty()

if __name__ == "__main__":
    print(is_nested("[{()}]"))