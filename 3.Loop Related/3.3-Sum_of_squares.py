# Problem : Take a number as input. Then get the sum of the numbers. If the number is n. Then get 0^2+1^2+2^2+3^2+4^2+.............+n^2


# Method 1 : using list comprehension
lst = [str(i**2) for i in range(int(input("Enter a number : ")) + 1)]
sum = sum(list(map(int,lst)))
print(" + ".join(lst), end=" " )
print(" = ",sum)

# output : 

"""
Enter a number : 12
0 + 1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100 + 121 + 144 =  650

"""

# Method 2 : 
sum = 0
for i in range(int(input("Enter a number : ")) + 1):
    sum += i**2
    print(i**2, end=" + ", sep="")
print(" = ",sum)

# output : 
"""
Enter a number : 12
0 + 1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100 + 121 + 144 +  =  650
"""



# Method 3 : using formula

n = int(input("Enter a number : "))
sum = (n*(n+1)*(2*n + 1))/6
print("Sum Of the series : ",sum)

# Output

"""
Enter a number : 12
Sum Of the series :  650.0
"""

