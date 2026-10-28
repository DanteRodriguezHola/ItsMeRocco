class Graph:

    def __init__(self, cadj_list:dict):

        self.nodes = list(cadj_list.keys())
        self.size = len(self.nodes)

        self.matrix = self._adj_list_to_matrix(fadj_list = cadj_list)

        for column in self.matrix:
            print(column)


    def _adj_list_to_matrix(self, fadj_list:dict):

        matrix = [[0] * len(fadj_list) for _ in range(len(fadj_list))]

        nodes = list(fadj_list.keys())
        edges = list(fadj_list.values())

        for i in range(len(nodes)):

            from_node = i

            for j in range(len(edges[i])):

                to_node = nodes.index(edges[i][j])

                matrix[from_node][to_node] = 1

        return matrix


    def depth_first_search(self, start_node:int):
    
        visited_nodes:list = [] # array
        backtracking:list = [start_node] # stack

        while backtracking:

            recently_visited:int = backtracking.pop()
            visited_nodes.append(recently_visited)

            to_nodes:list = self.matrix[recently_visited]

            for i in range(len(to_nodes)):

                if to_nodes[i] and not i in visited_nodes:

                    backtracking.append(i)

        self._print_visited_nodes(fvisited_nodes = visited_nodes)


    def _print_visited_nodes(self, fvisited_nodes):

        for index in fvisited_nodes:

            print(self.nodes[index], end = ', ')


def main():

    adj_list = {

        'a': ['b', 'c', 'd'],
        'b': ['a'],
        'c': ['a', 'e', 'f'],
        'd': ['a'],
        'e': ['c', 'g', 'h'],
        'f': ['c'],
        'g': ['e', 'i'],
        'h': ['e'],
        'i': ['g']}

    my_graph = Graph(cadj_list= adj_list)

    my_graph.depth_first_search(start_node = 2)
    
if __name__ == '__main__':
    main()