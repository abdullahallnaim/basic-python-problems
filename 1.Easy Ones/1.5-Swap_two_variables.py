# Problem : Swap two variables.

# To swap two variables: the value of the first variable will become the value of the second variable. On the other hand, the value of the second variable will become the value of the first variable.



var1 = int(input('Enter a number : '))
var2 = int(input('Enter another number : '))

print(f"Before swap Var1 = {var1} and Var2 = {var2}")

# Method One : 

temp = var1
var1 = var2
var2 = temp

# Method two : 

var1, var2 = var2, var1

# Method three : 

var1 = var1 + var2
var2 = var1 - var2
var1 = var1 - var2

print(f"After swap Var1 = {var1} and Var2 = {var2}")


