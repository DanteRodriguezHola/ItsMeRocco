class MinHeap:
    def __init__(self):
        self.heap:list = [None]
        self.size:int = 0

    def insert(self, data):
        self.heap.append(data)
        self.size += 1

        self._arrange()

    def _arrange(self):
        current_index:int = self.size
        
        while current_index > 1:
            min_child, parent = current_index, current_index // 2

            if self.heap[min_child] < self.heap[parent]:
                self._swap(min_child, parent)
                current_index = parent
                continue

            else: 
                return

    def remove_root(self):
        if self.isEmpty():
            print("Min heap is empty!")
            return None

        self._swap(1, -1)
        removed_root = self.heap.pop(-1)
        self.size -= 1

        self._sink(1)

        return removed_root
    
    def remove_any(self, index:int):
        if self.isEmpty():
            print("Min heap is empty!")
            return None

        if index < 1 or index > self.size:
            print("Invalid index!")
            return

        self._swap(index, -1)
        removed_element = self.heap.pop(-1)
        self.size -= 1

        self._sink(index)

        return removed_element

    def heap_sort(self):
        sorted_list:list = []

        while self.size > 0:
            sorted_element = self.remove_root()
            sorted_list.append(sorted_element)

        return sorted_list

    def isEmpty(self):
        return self.size == 0

    def show(self):
        print(self.heap[1:])

    def _swap(self, index_1:int, index_2:int):
            self.heap[index_1], self.heap[index_2] = self.heap[index_2], self.heap[index_1]

    def _sink(self, current_index:int):
        while current_index * 2 <= self.size:
            min_child, parent = self._min_child(current_index), current_index

            if self.heap[min_child] < self.heap[parent]:
                self._swap(min_child, parent)
                current_index = min_child
                continue

            else:
                return
    
    def _min_child(self, indice:int):
            left_child = indice * 2
            right_child = (indice * 2) + 1
    
            if right_child > self.size:
                return left_child
            
            if self.heap[left_child] < self.heap[right_child]:
                return left_child
    
            else:
                return right_child

class PriorityQueueHeap:
    def __init__(self):
        self.heap:list = [None]
        self.size = 0

    def enqueue(self, new_data, new_priority):
        new_element:tuple = (new_data, new_priority)

        self.heap.append(new_element)
        self.size += 1
        
        self._arrange()
        
    def _arrange(self):
        current_index:int = self.size
        
        while current_index > 1:
            min_child, parent = current_index, current_index // 2

            if self.heap[min_child][1] < self.heap[parent][1]:
                self._swap(min_child, parent)
                current_index = parent
                continue

            else: 
                return

    def _swap(self, index_1:int, index_2:int):
        self.heap[index_1], self.heap[index_2] = self.heap[index_2], self.heap[index_1]