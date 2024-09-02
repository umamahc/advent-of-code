def read_input(filename: str) -> list[str]:
    '''Returns file content as list of strings'''
    with open(filename, "r") as f:
        return f.readlines()


def depth_measurement_increases(depth_list: list[str]) -> int:
    num_increases = 0
    for i in range(len(depth_list)):
        if not i == 0:
            if int(depth_list[i]) > int(depth_list[i-1]):
                num_increases += 1
    return num_increases


def depth_window_increases(depth_list: list[str]) -> int:
    for i in range(len(depth_list)):
        depth_list[i] = int(depth_list[i])

    window_list = []
    for i in range(len(depth_list)-2):
        window_list.append(depth_list[i] + depth_list[i+1] + depth_list[i+2])

    num_increases = 0
    for i in range(1, len(window_list)):
        if window_list[i] > window_list[i-1]:
            num_increases += 1
    return num_increases


if __name__ == '__main__':

    test_depth_list = ['199', '200', '208', '210',
                       '200', '207', '240', '269', '260', '263']
    depth_list = read_input('day1.txt')
    print(depth_measurement_increases(depth_list))
    print(depth_window_increases(depth_list))
