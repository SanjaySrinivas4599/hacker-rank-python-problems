# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
elm = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    op, l = input().split()
    getattr(elm, op)(set(map(int, input().split())))
print(sum(elm))
