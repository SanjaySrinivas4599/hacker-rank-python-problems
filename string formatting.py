def print_formatted(n):
    w=len(bin(n)[2:])
    for num in range(1,n+1):
        a = str(num)
        b = oct(num)[2:]
        c = hex(num)[2:].upper()
        d = bin(num)[2:]
        print(a.rjust(w),b.rjust(w),c.rjust(w),d.rjust(w))
    




if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
