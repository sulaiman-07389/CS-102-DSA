seq = input()

def isCorrect(seq):
    balancedcount = 0
    for x in seq:
        if x == "(":
            balancedcount += 1
        elif x == ")":
            balancedcount -= 1
            if balancedcount < -1:
                break
            
    if balancedcount == 0:
        return "Yes"
    else:
        return "No"
    
print(isCorrect(seq))
