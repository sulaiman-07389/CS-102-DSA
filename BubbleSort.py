import ast
lst = input()
lst = ast.literal_eval(lst)

def bubble_sort(arr):
    n = len(arr)
    if len(arr) == 0 or len(arr) == 1:
        print(lst)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(arr)

bubble_sort(lst)
