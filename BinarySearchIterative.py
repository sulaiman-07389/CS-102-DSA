import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())
def binary_search_iterative(lst,item):\

    low = 0
    high = len(lst) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        if lst[mid] < item:
            low = mid + 1
 
        elif lst[mid] > item:
            high = mid - 1
 
        else:
            return mid
 
    return -1
 

print(binary_search_iterative(lst, item))
