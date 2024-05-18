def calculate_structure_sum(element):
    print(element)
    total_sum = 0

    if isinstance(element, int):
        total_sum += element
    elif isinstance(element, str):
        total_sum += len(element)
    elif isinstance(element, list) or isinstance(element, tuple) or isinstance(element, set):
        for item in element:
            total_sum += calculate_structure_sum(item)
    elif isinstance(element, dict):
        for key, value in element.items():
            if isinstance(key, str):
                total_sum += len(key)
            else:
                total_sum += key
            total_sum += calculate_structure_sum(value)

    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))
