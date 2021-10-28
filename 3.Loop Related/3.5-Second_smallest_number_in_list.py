# problem : For a list, find the second smallest element in the list

def second_smallest_number(lst):
    
    # method 1 :
    smallest = lst[0]
    second_smallest = lst[0]
    for i in range(1, len(lst)):
        if  lst[i] < smallest:
            second_smallest = smallest
            smallest = lst[i]
            
        elif  lst[i]< second_smallest:
            second_smallest = lst[i]
    return second_smallest
    
    # method 2 :
    smallest = min(lst)
    lst.remove(smallest)
    return min(lst)

print(second_smallest_number([5,2,23,4,1]))
