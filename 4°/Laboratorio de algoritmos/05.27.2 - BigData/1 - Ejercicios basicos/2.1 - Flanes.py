stack = []

stack.append(2) # === push ===
stack.append(7)
stack.append(6)
stack.append(3)

stack.pop(-1) # === pop ===
stack.pop(-1)

if len(stack) == 0: # === peek ===
    print("Stack is empty") 

else:
    print(stack[-1])

print(len(stack) == 0) # === isEmpty ===

print(len(stack)) # === size ===

queue = []

queue.append(1) # === enqueue ===
queue.append(3)
queue.append(3)
queue.append(7)

queue.pop(0) # === dequeue ===
queue.pop(0)

if len(queue) == 0: # === peek ===
    print("Stack is empty") 

else:
    print(queue[0])

print(len(queue) == 0) # === isEmpty ===

print(len(queue)) # === size ===