def main():

    adj_list = {

        'a': ['b', 'c', 'd'],
        'b': ['a', 'c'],
        'c': ['a', 'b'],
        'd': ['a'],

    }

    for node, edges in adj_list.items():
        print(f"{node}: {edges}")


if __name__ == '__main__':
    main()