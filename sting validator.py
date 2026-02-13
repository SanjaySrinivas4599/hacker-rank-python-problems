s = input() 
actions = ['isalnum','isalpha','isdigit','islower','isupper']
for action in actions:
        print(any([getattr(string,action)() for string in s]))
