def adj_list_to_matrix(fadj_list:dict):

    matrix = [[0] * len(fadj_list) for _ in range(len(fadj_list))]

    nodes = list(fadj_list.keys())
    edges = list(fadj_list.values())

    for i in range(len(nodes)):

        from_node = i

        for j in range(len(edges[i])):

            to_node = nodes.index(edges[i][j])

            matrix[from_node][to_node] = 1

    return matrix


def main():

    adj_list = {

        'a': ['b', 'c', 'd'],
        'b': ['a', 'c'],
        'c': ['a', 'b'],
        'd': ['a'] }

    matrix = adj_list_to_matrix(fadj_list = adj_list)
    print(matrix)
    
if __name__ == '__main__':
    main()