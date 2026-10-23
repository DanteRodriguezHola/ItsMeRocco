def main():

    graph = {
        'a': ['b', 'c', 'd'],
        'b': ['a', 'c'],
        'c': ['a', 'b'],
        'd': ['a'],

    }

    for vertex, edges in graph.items():
        print(f'{vertex}: {edges}')

if __name__ == '__main__':
    main()