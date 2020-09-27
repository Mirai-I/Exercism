import re
def is_valid(isbn):
    c =list(re.sub(r'[^X \d]+', '', isbn))
    for i in range(len(c)):
        if c[i] == "X":
            if i != 9:
                return False
            c[i] = 10

    if len(c) != 10:
        return False


    result = True if sum([int(c[i])*(10-i) for i in range(10)]) % 11 == 0 else False

    return result
