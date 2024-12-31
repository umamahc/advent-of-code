def read_output(filename):

    with open(filename, 'r') as f:
        output = [line.strip()for line in f.readlines()]
        return output


def get_column(output, i):
    column_str = ''
    for line in output:
        column_str += line[i]
    return column_str


def most_frequent_bit(column_str):
    count_0 = column_str.count('0')
    count_1 = column_str.count('1')
    if count_0 <= count_1:
        return '1'
    return '0'


def least_frequent_bit(column_str):
    count_0 = column_str.count('0')
    count_1 = column_str.count('1')
    if count_0 <= count_1:
        return '0'
    return '1'


def get_gamma_str(output):
    gamma_str = ''
    len_diagnostic = len(output[0])
    for i in range(len_diagnostic):
        column = get_column(output, i)
        gamma_str += most_frequent_bit(column)

    return gamma_str


def get_epsilon_str(output):
    epsilon_str = ''

    len_diagnostic = len(output[0])
    for i in range(len_diagnostic):
        column = get_column(output, i)
        epsilon_str += least_frequent_bit(column)

    return epsilon_str


def get_power_consumption(output):
    gamma_int = int(get_gamma_str(output), 2)
    epsilon_int = int(get_epsilon_str(output), 2)
    return gamma_int*epsilon_int


def get_oxygen_str(output):
    output_copy = output.copy()
    len_diagnostic = len(output_copy[0])

    while len(output_copy) != 1:
        for i in range(len_diagnostic):
            column = get_column(output_copy, i)
            freq_no = most_frequent_bit(column)
            for line in output_copy:
                if line[i] != freq_no:
                    output_copy.remove(line)
    return output_copy[0]


def get_co2_str(output):
    output_copy = output.copy()
    len_diagnostic = len(output_copy[0])

    while len(output_copy) != 1:
        for i in range(len_diagnostic):
            column = get_column(output_copy, i)
            freq_no = least_frequent_bit(column)
            for line in output_copy:
                if line[i] != freq_no:
                    output_copy.remove(line)
    return output_copy[0]


if __name__ == "__main__":

    test_list = ["00100", "11110", "10110", "10111", "10101", "01111",
                 "00111", "10000", "11001", "00010", "01010"]
    # output = read_output('day3.txt')

    # power_consumption = get_power_consumption(output)
    # print(power_consumption)

    print(get_oxygen_str(test_list))
