class PriorityQueue:
    def __init__(self):
        self.array = []

    def enqueue(self, data:any, priority:int):
        new_node:tuple = (data, priority)

        if self.isEmpty():
            self.array.append(new_node)
            return

        for index in range(self.size() - 1, -1, -1):
            current_node:tuple = self.array[index]
            print(current_node)

            if current_node[1] <= new_node[1]:
                self.array.insert(index + 1, new_node)
                return

            if index - 1 == -1:
                self.array.insert(0, new_node)
                return

    def dequeue(self):
        if self.isEmpty():
            print("Priority queue is empty!")
            return None

        dequeued_node = self.array.pop(0)
        return dequeued_node

    def peek(self):
        if self.isEmpty():
            print("Priority queue is empty!")
            return None

        return self.array[0]
    
    def size(self):
        return len(self.array)

    def isEmpty(self):
        return self.size() == 0

    def show(self):
        print(self.array)

if __name__ == "__main__":
    pq = PriorityQueue()

    pq.dequeue()
    pq.peek()
    
    pq.enqueue("Dog", 1)
    pq.show()

    pq.enqueue("Cat", 4)
    pq.show()

    pq.enqueue("Lizard", 2)
    pq.show()

    pq.enqueue("Bird", 5)
    pq.show()

    pq.enqueue("Turle", 2)
    pq.show()

    pq.enqueue("Wallaby", 3)
    pq.show()

    print(pq.dequeue())
    pq.show()

    pq.enqueue("Horse", 1)
    pq.show()

    pq.enqueue("Duck", 1)
    pq.show()

    pq.dequeue()
    pq.show()

    print(pq.peek())

    while not pq.isEmpty():
        pq.dequeue()
        pq.show()
    