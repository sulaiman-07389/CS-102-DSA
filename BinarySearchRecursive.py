import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())
low = int(input())
high = int(input())
def binary_search_recursive(lst,item,low,high):
    if high >= low:
 
        mid = (high + low) // 2
 
        if lst[mid] == item:
            return mid
 
        elif lst[mid] > item:
            return binary_search_recursive(lst, item, low, mid - 1)
 
        else:
            return binary_search_recursive(lst, item, mid + 1, high)
 
    else:
        return -1
print(binary_search_recursive(lst, item, low, high))
