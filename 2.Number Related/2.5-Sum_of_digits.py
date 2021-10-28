# problem : For a given number, get the sum of digits in the number

user_input = int(input('Enter a number : '))


# Method 1 : using recursive function
def get_sum_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + get_sum_digits(n//10)
print(f"Sum of the digits : {get_sum_digits(user_input)}")


# Method 2 : using list
sum_of_digits = sum(list(map(int, list(str(user_input)))))
print(f"Sum of digits using list : {sum_of_digits}")
 


