
def parse_input_2_column_list(data: list) -> tuple[list[int], list[int]]:
    list_1 = []
    list_2 = []
    for line in data:
        a, b = line.split()
        list_1.append(int(a))
        list_2.append(int(b))
    return (list_1, list_2)
