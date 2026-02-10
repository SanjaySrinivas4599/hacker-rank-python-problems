if __name__ == '__main__':
    n = int(input())
    l = [i for i in range(1, n+1)]
    l = map(str, l)
    result = "".join(l)
    print(result)
