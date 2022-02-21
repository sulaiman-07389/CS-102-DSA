import ast
lst = input()
lst = ast.literal_eval(lst)
column = int(input())

def sort_matrix_by_columnNumber(lst, column):
    for i in range(len(lst)):
        small = i
        for j in range(i+1, len(lst)):
            if lst[small][column] > lst[j][column]:
                small = j
      
        lst[i], lst[small] = lst[small], lst[i]
    return (lst)
    

print(sort_matrix_by_columnNumber(lst, column))
