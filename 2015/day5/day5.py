def read_input(filename: str) -> list[str]:
    '''Returns file as a list of strings.'''
    with open(filename, "r") as f:
        return f.readlines()


def has_3_vowels(s: str) -> bool:
    '''Returns True if string contains at least 3 vowels.'''
    vowel_count = 0
    vowels = 'aeiou'
    for lett in s:
        if lett in vowels:
            vowel_count += 1
    if vowel_count >= 3:
        return True
    return False


def has_doubles(s: str) -> bool:
    '''Returns True if double letters found in string.'''
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False


def not_forbidden(s: str) -> bool:
    '''Returns True if string does not contain forbidden letter combos.'''
    forbidden = ['ab', 'cd', 'pq', 'xy']
    forbidden_count = 0
    for combo in forbidden:
        if combo in s:
            forbidden_count += 1
    if forbidden_count == 0:
        return True
    return False


def is_nice_1(s: str) -> bool:
    '''Returns True if string meets 'nice' criteria.'''
    if has_3_vowels(s) and has_doubles(s) and not_forbidden(s):
        return True
    return False


def count_nice_1(output: list[str]) -> int:
    '''Returns number of strings that meet 'nice' criteria.'''
    nice_count = 0
    for s in output:
        if is_nice_1(s):
            nice_count += 1
    return nice_count


def pair_appears_twice(s: str) -> bool:
    '''Returns True if pair of two letters appear twice in the string'''
    pair_list = []
    for i in range(len(s)-1):
        pair = f'{s[i]}{s[i+1]}'
        if pair in pair_list and pair != pair_list[-1]:
            return True
        else:
            pair_list.append(pair)
    return False


def check_substr(substr: str) -> bool:
    '''Returns true if str meets xyx format'''
    if substr[0] == substr[2]:
        return True
    return False


def check_substr_list(s: str) -> bool:
    substr_list = []
    for i in range(len(s)-2):
        substr = f'{s[i]}{s[i+1]}{s[i+2]}'
        substr_list.append(substr)
    valid_substr_count = 0
    for str in substr_list:
        if check_substr(str):
            valid_substr_count += 1
    if valid_substr_count > 0:
        return True
    return False


def is_nice_2(s: str) -> bool:
    '''Returns True if string meets 'nice' criteria.'''
    if pair_appears_twice(s) and check_substr_list(s):
        return True
    return False


def count_nice_2(output: list[str]) -> int:
    '''Returns number of strings that meet 'nice' criteria.'''
    nice_count = 0
    for s in output:
        if is_nice_2(s):
            nice_count += 1
    return nice_count


if __name__ == "__main__":
    test = ['ugknbfddgicrmopn', 'aaa',
            'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']
    output = read_input('day5.txt')
    nice_count = count_nice_1(output)
    print(nice_count)

    test1 = ['qjhvhtzxzqqjkmpb', 'xxyxx',
             'uurcxstgmygtbstg', 'ieodomkazucvgmuy']
    nice_count_2 = count_nice_2(output)
    print(nice_count_2)
