s=input()
TypesOfBraces = {'(': ')','{': '}','[': ']'}

def balanced_braces(s):
    stack = []
    for i in s:
        if i in TypesOfBraces:
            stack.append(i)
            continue
        try:
            OpeningBrace = stack.pop()
        except IndexError:  
            return False
        if not(i == TypesOfBraces[OpeningBrace]):  
            return False
    if len(stack) == 0:
        return True
    else:
        return False
        

print(balanced_braces(s))


#https://bradfieldcs.com/algos/stacks/balanced-parentheses/#
#HELP TAKEN FROM THIS SITE#
