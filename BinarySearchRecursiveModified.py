import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())
low = int(input())
high = int(input())

def binary_search_recursive_modified(lst,item,low,high):
    if high >= low:
 
        mid = (high + low) // 2
 
        if lst[mid] == item:
            return mid
 
        elif lst[mid] > item:
            return binary_search_recursive_modified(lst, item, low, mid - 1)
 
        else:
            return binary_search_recursive_modified(lst, item, mid + 1, high)
 
    else:
        lst.append(item)
        lst.sort()
        return lst.index(item)
    
print(binary_search_recursive_modified(lst, item, low, high))
