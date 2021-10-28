# Problem : Find the largest of the three numbers.


num1 = int(input('First Number : '))
num2 = int(input('Second Number : '))
num3 = int(input('Third Number : '))

# Method one :

largest = num1

if num2 > num1 and num2 > num3:
        largest = num2
elif num3 > num1 and num3 > num2:
        largest = num3
else:
    largest = num1
print(f"{largest} is the largest of the three numbers")

# Method two :

print(f"{max(num1,num2,num3)} is the largest of the three numbers")
    
