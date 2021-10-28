# problem : For a given string, remove all duplicate characters from that string.

user_input = input('Enter a string : ')
name = ''
for i in user_input:
    if i not in name:
        name += i
print(name)
