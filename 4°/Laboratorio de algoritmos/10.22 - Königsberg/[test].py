vertex_data = ['A', 'B', 'C', 'D']

edge_data = [
    [0, 1, 1, 1], # edges for A
    [1, 0, 1, 0], # edges for B
    [1, 1, 0, 0], # edges for C
    [1, 0, 0, 0], # edges for D
]

class Graph:
    def __init__(self, size):
        self.size = size

        self.vertex_data = [''] * size
        self.edge_data = [[0] * size for _ in range(size)]

    def add_vertex(self, vertex, data):
        if 0 <= vertex <= self.size:

            self.vertex_data[vertex] = data

    def add_edge(self, vertex1, vertex2):
        if 0 <= vertex1 <= self.size and 0 <= vertex2 <= self.size:

            self.edge_data[vertex1][vertex2] = 1
            self.edge_data[vertex2][vertex1] = 1

    def print_vertex_data(self):
        print('Vertex: ', end = '')

        for i in range(len(self.vertex_data)):
            
            print(self.vertex_data[i], end = ', ')

        print()

    def print_edge_data(self):
        for i in range(len(self.edge_data)):

            print(self.edge_data[i])

    def print_vertex_edges(self):
        for i in range(len(self.edge_data)):

            print(f'{self.vertex_data[i]}: ', end = '')

            for j in range(len(self.edge_data[i])):

                if self.edge_data[i][j]:
                    print(self.vertex_data[j], end = ', ')

            print()

graph1 = Graph(size = 4)

# adding vertex A, B, C and D
graph1.add_vertex(vertex = 0, data = 'A')
graph1.add_vertex(vertex = 1, data = 'B')
graph1.add_vertex(vertex = 2, data = 'C')
graph1.add_vertex(vertex = 3, data = 'D')
graph1.print_vertex_data()

# adding edges for A
graph1.add_edge(0, 1)
graph1.add_edge(0, 2)
graph1.add_edge(0, 3)

# adding edges for B
graph1.add_edge(1, 0)
graph1.add_edge(1, 2)

# adding edges for C
graph1.add_edge(2, 0)
graph1.add_edge(2, 1)

# adding edges for D
graph1.add_edge(3, 0)

graph1.print_edge_data()
graph1.print_vertex_edges()