def swap_case(s):
    new_s = ""
    for character in s:
        if character.isupper():
            new_s+=character.lower()
        elif not character.isupper():
            new_s+=character.upper()
    return new_s


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
