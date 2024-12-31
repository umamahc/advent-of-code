def read_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.readlines()[0]


def get_house(move: str, house: list[int]) -> list[int]:
    if move == '^':
        new_house = [house[0]+1, house[1]]
    if move == 'v':
        new_house = [house[0]-1, house[1]]
    if move == '>':
        new_house = [house[0], house[1]+1]
    if move == '<':
        new_house = [house[0], house[1]-1]
    return new_house


def get_houses_set(output: str) -> int:
    houses_set = {(0, 0)}
    house = [0, 0]
    for move in output:
        new_house = get_house(move, house)
        houses_set.add(tuple(new_house))
        house = new_house
    return houses_set


def get_num_houses(output: str) -> int:
    houses_set = get_houses_set(output)
    return len(houses_set)


def get_robo_moves(output: str) -> str:
    robo_moves = ''
    for i in range(len(output)):
        if i % 2 == 0:
            robo_moves += output[i]
    return robo_moves


def get_santa_moves(output: str) -> str:
    santa_moves = ''
    for i in range(len(output)):
        if i % 2 != 0:
            santa_moves += output[i]
    return santa_moves


def get_robo_santa_houses(output: list[str]) -> int:
    santa_moves = get_santa_moves(output)
    santa_set = get_houses_set(santa_moves)

    robo_moves = get_robo_moves(output)
    robo_set = get_houses_set(robo_moves)

    houses_set = santa_set.union(robo_set)
    return len(houses_set)


if __name__ == "__main__":
    output1 = '>'
    output2 = '^>v<'
    output3 = '^v^v^v^v^v'

    output = read_input('day3.txt')
    print(get_robo_santa_houses(output))
