from hashlib import md5


def get_result(secret_key: str) -> str:
    result = md5(secret_key.encode())
    return result.hexdigest()


def check_result_5(result: str) -> bool:
    if result[:5] != '00000':
        return False
    return True


def check_result_6(result: str) -> bool:
    if result[:6] != '000000':
        return False
    return True


def get_pos_num(test_key: str) -> int:
    new_res = ''
    for char in test_key:
        if not char.isalpha():
            new_res += char
    return int(new_res)


def get_key(secret_key: str) -> str:
    num = 1
    while True:
        test_key = secret_key + str(num)
        result = get_result(test_key)
        if check_result_6(result):
            return get_pos_num(test_key)
        num += 1


if __name__ == "__main__":
    print(get_key(secret_key='ckczppom'))
