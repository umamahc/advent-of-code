def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()[0]


def get_floor(output: list[str]) -> int:
    floor = 0
    for parenthesis in output:
        if parenthesis == '(':
            floor += 1
        if parenthesis == ')':
            floor -= 1
    return floor


def get_basement_pos(output: list[str]) -> int:
    floor = 0
    for i in range(len(output)):
        if output[i] == '(':
            floor += 1
        if output[i] == ')':
            floor -= 1
        if floor < 0:
            return i+1


if __name__ == "__main__":
    filename = 'day1.txt'
    output = read_input(filename)
    floor = get_floor(output)
    print(floor)
    print(get_basement_pos(output))
