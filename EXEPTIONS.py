# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    a,b = input().split(' ')
    
    try:
        print(int(a)//int(b))
    except ZeroDivisionError:
        print('Error Code: integer division or modulo by zero')
    except ValueError as e:
        print(f'Error Code: {e}')
