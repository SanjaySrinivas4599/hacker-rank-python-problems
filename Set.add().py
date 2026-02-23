# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())

counter = 0
distinct_country_stamps = set()

for i in range(N):
    country = input()
    
    if country not in distinct_country_stamps:
        distinct_country_stamps.add(country)
        counter += 1
    
print(counter)
