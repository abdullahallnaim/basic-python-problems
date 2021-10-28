# Problem : Find the largest element of a list.


given_list = [1,2,4,34,23,56]

# Method 1 : using custom function
def find_largest_element(lst):
    max = lst[0]
    for i in lst:
        if i > max:
            max = i
    return max
print(f"The largest element of list {given_list} : {find_largest_element(given_list)} ")


# Method 2 : using max function
print(f"The largest element of list {given_list} : {max(given_list)} ")

