# problem : For a given number, find all the numbers smaller than the number. Numbers should be divisible by 3 and also by 5.

user_input = int(input('Enter a number : '))

divisible_by_3_5 = [i for i in range(user_input) if i % 3 == 0 and i % 5 == 0]
print(f"Numbers that are divisible by 3 and 5 are : {divisible_by_3_5}")
