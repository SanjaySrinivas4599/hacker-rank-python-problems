# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int, input().split())
A = []
B = []
for _ in range(n):
    A.append(str(input()))
for _ in range(m):
    B.append(str(input()))
    
for c in B:
    indices = ""
    for i,j in enumerate(A):
        if j == c:
            indices += f"{i+1} "
    print("-1" if indices == "" else indices)
