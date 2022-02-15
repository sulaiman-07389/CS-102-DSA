import ast
lst = input()
lst = ast.literal_eval(lst)

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j = j - 1
        lst[j+1] = key
        print(lst)

insertion_sort(lst)
