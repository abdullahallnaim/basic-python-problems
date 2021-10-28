# Problem : For a list, find the second largest number in the list.

def second_largest_number(lst):
    # method 1
    lst = list(set(lst))
    lst.sort(reverse=True)
    return lst[1]

    # method 2 :
    lst = set(lst)
    lst.remove(max(lst))
    return max(lst)
    
    # method 3 :
    lst = list(set(lst))
    largest = lst[0]
    second_largest = lst[0]
    for i in range(1,len(lst)):
        if lst[i]>largest:
            second_largest = largest
            largest = lst[i]
            
        elif lst[i] > second_largest:
            second_largest = lst[i]
    return second_largest
            

print(second_largest_number([1,2,45,23,23,45,21]))