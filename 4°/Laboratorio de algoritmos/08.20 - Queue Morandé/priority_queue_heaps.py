class PriorityQueue:
    def __init__(self):
        self.heap = [None]

    def enqueue(self, data:any, priority:int):
        new_node:tuple = (data, priority)

        self.heap.append(new_node)
        self._arrange()

    def dequeue(self):
        if self.isEmpty():
            print("Min heap is empty!")
            return None

        self._swap(1, -1)
        removed_root = self.heap.pop(-1)

        self._sink(1)

        return removed_root

    def peek(self):
        if self.isEmpty():
            print("Priority queue is empty!")
            return None

        return self.heap[1]

    def size(self):
        return len(self.heap) - 1

    def isEmpty(self):
        return self.size() == 0

    def show(self):
        print(self.heap[1:])

    def _arrange(self):
        current_index:int = self.size()

        while current_index > 1:
            min_child, parent = current_index, current_index // 2

            if self.heap[min_child][1] < self.heap[parent][1]:
                self._swap(min_child, parent)
                current_index = parent
                continue

            else: 
                return

    def _sink(self, current_index:int):
        while current_index * 2 <= self.size():
            min_child, parent = self._min_child(current_index), current_index

            if self.heap[min_child][1] < self.heap[parent][1]:
                self._swap(min_child, parent)
                current_index = min_child
                continue

            else:
                return
    
    def _min_child(self, indice:int):
        left_child = indice * 2
        right_child = (indice * 2) + 1

        if right_child > self.size():
            return left_child
        
        if self.heap[left_child][1] < self.heap[right_child][1]:
            return left_child

        else:
            return right_child

    def _swap(self, index_1, index_2):
        self.heap[index_1], self.heap[index_2] = self.heap[index_2], self.heap[index_1]

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
    