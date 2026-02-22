# Enter your code here. Read input from STDIN. Print output to STDOUT
n_shoes=input()
all_size=list(map(int,input().split()))
n_costumers=int(input())
customer_want = [tuple(map(int, input().split())) for _ in range(int(n_costumers))]

gains=[]
for custom in customer_want:
    if custom[0] in all_size:
        all_size.remove(custom[0])
        gains.append(custom[1])
        
print(sum(gains))
