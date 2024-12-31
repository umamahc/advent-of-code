def read_output(filename):
    with open(filename, 'r') as f:
        output = [line.strip() for line in f.readlines()]
    return output


def split_rucksack_compartment(s: str) -> list[str]:
    if len(s) % 2 != 0:
        raise ValueError("Input must be even")
    len_compartment = int(len(s)/2)
    compartment_list = [s[:len_compartment], s[len_compartment:]]
    return compartment_list


def compare_compartments(s_list: list[str]) -> str:
    for char in s_list[0]:
        if char in s_list[1]:
            return char


def get_item_priority(char: str) -> int:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = alphabet.upper()
    lower_priority = list(enumerate(alphabet, start=1))
    upper_priority = list(enumerate(alphabet_upper, start=27))
    for priority, letter in lower_priority:
        if letter == char:
            return priority
    for priority, letter in upper_priority:
        if letter == char:
            return priority


def sum_item_priorities(output):
    sum = 0
    for s in output:
        compartment_list = split_rucksack_compartment(s)
        common_char = compare_compartments(compartment_list)
        priority_int = get_item_priority(common_char)
        sum += priority_int

    return sum


if __name__ == "__main__":
    test_file = ['vJrwpWtwJgWrhcsFMMfFFhFp',
                 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
                 'PmmdzqPrVvPwwTWBwg',
                 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
                 'ttgJtRGJQctTZtZT',
                 'CrZsJsPPZsGzwwsLwLmpwMDw']
    output = read_output(filename='day3.txt')
    print(sum_item_priorities(output))
