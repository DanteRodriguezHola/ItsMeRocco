def main():

    graph = {
        'vertex': ['a', 'b', 'c', 'd'],

        'edges': [
            [0, 1, 1, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 0],
            [1, 0, 0, 0],
            ],

    }

    for i in range (len(graph['edges'])):

        print(f'{graph["vertex"][i]}: ', end = '')

        for j in range(len(graph['edges'][i])):

            if graph['edges'][i][j]:
                print(graph["vertex"][j], end = ', ')

        print()

if __name__ == '__main__':
    main()