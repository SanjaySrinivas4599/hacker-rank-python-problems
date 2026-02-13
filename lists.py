if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        command = input().split(" ")
        cmd = command[0]
        if cmd == "insert":
            list.insert(int(command[1]), int(command[2]))
        elif cmd == "append":
            list.append(int(command[1]))
        elif cmd == "remove":
            list.remove(int(command[1]))
        elif cmd == "sort":
            list.sort()
        elif cmd == "pop":
            list.pop()
        elif cmd == "reverse":
            list.reverse()
        elif cmd == "print":
            print(list)

