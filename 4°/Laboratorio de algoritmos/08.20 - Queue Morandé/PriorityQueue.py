class PriorityQueue:
    def __init__(self):
        self.array:list = []
        self.size:int = 0

    def enqueue(self, new_data:any, new_priority:int):
        new_element:tuple = (new_data, new_priority)

        if self.isEmpty():
            self.array.append(new_element)
            self.size += 1
            return

        for index in range(self.size):
            current_element:tuple = self.array[index]
            current_priority:int = current_element[1]

            if current_priority > new_priority:
                self.array.insert(index, new_element)
                self.size += 1
                return

            elif current_priority <= new_priority:
                if index + 1 == self.size:
                    self.array.append(new_element)
                    self.size += 1
                    return

                next_element:tuple = self.array[index + 1]
                next_priority:int = next_element[1]

                if next_priority > new_priority:
                    self.array.insert(index + 1, new_element)
                    self.size += 1
                    return

    def dequeue(self):
        if self.isEmpty():
            print("Priority queue is empty!")
            return None

        return self.array.pop(0)

    def peek(self):
        if self.isEmpty():
            print("Priority queue is empty!")
            return None
        
        return self.array[0]
    
    def isEmpty(self):
        return self.size == 0
    
    def show(self):
        print(self.array)

if __name__ == "__main__":
    pq = PriorityQueue()

    pq.enqueue("Perro", 1)
    pq.show()
    print()

    pq.enqueue("Gato", 3)
    pq.show()
    print()

    pq.enqueue("Gusano", 5)
    pq.show()
    print()

    pq.enqueue("Lagarto", 3)
    pq.show()
    print()

    pq.enqueue("Dinosaurio", 2)
    pq.show()
    print()

    pq.enqueue("Leon", 0)
    pq.show()
    print()

    pq.enqueue("Cucaracha", 3)
    pq.show()
    print()

    pq.enqueue("Tigre", 4)
    pq.show()
    print()

    pq.dequeue()
    pq.show()
    print()

    pq.dequeue()
    pq.show()
    print()

    print(pq.peek())
    print()