# problem : For a given list, get the sum of each number in the list

input_list = [1,2,3,4,5,6,7,8,9,10]

# Method 1 :
def get_sum_from_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

# Method 2 :
get_sum = sum(input_list)
print(f"Sum of the input lists : {get_sum}")

print(f"Sum of the input lists : {get_sum_from_list(input_list)}")