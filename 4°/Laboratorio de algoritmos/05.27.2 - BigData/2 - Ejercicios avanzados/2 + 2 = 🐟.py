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

def fish_fight(A, B):
    auxiliary_stack = Stack()
    alive_count = 0

    UP = 0
    DOWN = 1

    for index in range(len(B)):
        size = A[index]
        direction = B[index]

        if direction == UP:
            auxiliary_stack.push(size)

        elif direction == DOWN:
            alive = True

            while not auxiliary_stack.isEmpty():
                if auxiliary_stack.peek() > size:
                     alive = False

                     break

                else:
                    auxiliary_stack.pop()

            if alive:
                alive_count += 1 

    fishes_alive = auxiliary_stack.size() + alive_count
    return fishes_alive

if __name__ == "__main__":
    print(fish_fight(A = [1, 5, 10], 
                     B = [0, 0, 1]))