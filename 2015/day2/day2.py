def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()


def format_output(file_output: list[str]) -> list[list[int]]:
    list_dimensions = []
    for string in file_output:
        split_string = string.split('x')
        list_of_ints = [int(num) for num in split_string]
        list_dimensions.append(list_of_ints)
    return list_dimensions


def find_surface_area(dimensions: list[int]) -> int:
    side1 = dimensions[0]*dimensions[1]*2
    side2 = dimensions[1]*dimensions[2]*2
    side3 = dimensions[2]*dimensions[0]*2
    return side1 + side2 + side3


def find_slack_measurement(dimensions: list[int]) -> int:
    sorted_d = sorted(dimensions)
    return sorted_d[0]*sorted_d[1]


def find_wrapping_per_present(surface_area: int, slack_measurement: int) -> int:
    return surface_area + slack_measurement


def find_tot_wrapping_required(formatted_file_output: list[list[int]]) -> int:
    tot_wrapping = 0
    for dimensions in formatted_file_output:
        surface_area = find_surface_area(dimensions)
        slack_measurement = find_slack_measurement(dimensions)
        tot_wrapping += (surface_area + slack_measurement)
    return tot_wrapping


def ribbon_per_gift(dimensions: list[int]) -> int:
    sorted_d = sorted(dimensions)
    multiplied_tot = 1
    for num in dimensions:
        multiplied_tot *= num
    return (sorted_d[0]*2) + (sorted_d[1]*2 + multiplied_tot)


def find_tot_ribbon_required(formatted_file_output: list[list[int]]) -> int:
    tot_ribbon = 0
    for dimensions in formatted_file_output:
        tot_ribbon += ribbon_per_gift(dimensions)
    return tot_ribbon


if __name__ == "__main__":
    filename = 'day2.txt'
    file_output = read_input(filename)
    formatted_file_output = format_output(file_output)
    tot_wrapping = find_tot_wrapping_required(formatted_file_output)
    print(tot_wrapping)
    tot_ribbon_required = find_tot_ribbon_required(formatted_file_output)
    print(tot_ribbon_required)
