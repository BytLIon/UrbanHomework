def sum_num_line(structure):
    global s

    for data in structure:
        if isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
            sum_num_line(data)
        elif isinstance(data, dict):
            for key, val in data.items():
                sum_num_line((key, val))
        elif isinstance(data, int):
            s += data
        elif isinstance(data, str):
            s += len(data)
        else:
            print(data)



if __name__ == '__main__':
    s = 0

    data_structure = [
        [1, 2, 3],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]

    sum_num_line(data_structure)
    print(s)


