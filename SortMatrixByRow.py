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
        return lst
        
def sort_matrix_by_row(x):
    for lst in x:
        for i in range(len(lst)):
            small = i
            for j in range(i+1, len(lst)):
                if lst[small] > lst[j]:
                    small = j
          
            lst[i], lst[small] = lst[small], lst[i]
    return x
        
        
        
    
    
print(sort_matrix_by_row(lst))
