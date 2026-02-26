# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
englishpeople = list(map(int, input().split()))

m = int(input())
frenchpeople = list(map(int, input().split()))

peepls = (set(englishpeople) - set(frenchpeople))
print(len(peepls))
