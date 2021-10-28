# Prob : Find the max number of two numbers.

num1 = int(input('Enter a number : '))
num2 = int(input('Enter another number : '))

# Method one : 

if num1 > num2:
    print(f'{num1} is greater than {num2}')
else:
    print(f'{num2} is greater than {num1}')

# Method two : 

print(f"Max number of two numbers is {max(num1, num2)}")