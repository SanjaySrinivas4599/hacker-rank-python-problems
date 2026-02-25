n = int(input())
s = set(map(int, input().split()))
N = int(input())
while N > 0:
    imp = input().split()
    cmd = imp[0]
    match cmd:
        case "pop":
            s.pop()
        case "discard":
            s.discard(int(imp[-1]))
        case "remove":
            s.remove(int(imp[-1]))
    N -= 1
print(sum(s))
