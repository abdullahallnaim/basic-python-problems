# Problem : Take numbers from a user and show the average of the numbers the user entered.


user_input = int(input("How many numbers do you want to average ? "))

# collecting inputs : method 1
numbers = [int(input()) for _ in range(user_input)]

# collecting inputs : method 2
numbers = list(map(int, input().split()))

# solution : 
avg = sum(numbers)/len(numbers)


print(f"Average of the {len(numbers)} numbers: {avg}")
    