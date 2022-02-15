import ast
lst = input()
lst = ast.literal_eval(lst)

def selection_sort(lst):
    for i in range(len(lst)):
        small = i
        for j in range(i+1, len(lst)):
            if lst[small] > lst[j]:
                small = j
      
        lst[i], lst[small] = lst[small], lst[i]
        print(lst)
    
    

selection_sort(lst)

