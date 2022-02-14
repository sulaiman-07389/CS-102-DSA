import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())
def finding_multiple(lst,item):
    finallist =[]
    for x in range(len(lst)):
        if lst[x] == item:
            finallist.append(x)
            
    return finallist
print(finding_multiple(lst, item))
