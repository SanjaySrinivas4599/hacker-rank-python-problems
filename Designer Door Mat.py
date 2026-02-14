# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, input().split())
t = "WELCOME"
p = ".|."

# Upper-triangle
for i in range((N//2)):
    pattern = p*((2*i)+1)
    pattern = pattern.center(M, "-")
    print(pattern)

# Main-text
print(t.center(M, "-"))

# Lower-inverted-triangle
for i in range((N//2)-1, -1, -1):
    pattern = p*((2*i)+1)
    pattern = pattern.center(M, "-")
    print(pattern)
