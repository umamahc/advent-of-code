def read_input(filename: str) -> list[str]:
    with open(filename, 'r') as f:
        return f.readlines()


def format_output(file_output: list[str]) -> list[list[str, int]]:
    new_output = []
    for command in file_output:
        new_command = []
        split_command = command.split(' ')
        new_command.append(split_command[0])
        new_command.append(int(split_command[1]))
        new_output.append(new_command)
    return new_output


def calculate_horizontal(new_output: list[list[str, int]]):
    horizontal = 0
    for command in new_output:
        if command[0] == 'forward':
            horizontal += command[1]
    return horizontal


def calculate_vertical(new_output: list[list[str, int]]):
    vertical = 0
    for command in new_output:
        if command[0] == 'up':
            vertical -= command[1]
        if command[0] == 'down':
            vertical += command[1]
    return vertical
    ...


def multiply_directions(new_output: list[list[str, int]]):
    vertical = calculate_vertical(new_output)
    horizontal = calculate_horizontal(new_output)
    return vertical*horizontal


if __name__ == '__main__':
    test_data= ['forward 5', 'down 5',
                'forward 8', 'up 3', 'down 8', 'forward 2']
    filename = 'day2.txt'
    file_output = read_input(filename)
    new_output = format_output(filename)
    result = multiply_directions(new_output)
    print(result)
