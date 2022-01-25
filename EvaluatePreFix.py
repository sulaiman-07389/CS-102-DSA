expression = input()

def EvaluatePrefix(expression):
    OperandStack = []
    expressionlist = expression.split()
    reversedlist = expressionlist[::-1]
    for x in reversedlist:
        if x.isdigit():
            OperandStack.append(int(x))
        else:
            op1 = OperandStack.pop()
            op2 = OperandStack.pop()
            
            if x == '+':
                OperandStack.append(op1 + op2)
 
            elif x == '-':
                OperandStack.append(op1 - op2)
 
            elif x == '*':
                OperandStack.append(op1 * op2)
 
            elif x == '/':
                OperandStack.append(op1 / op2)
                
                
    return int(OperandStack.pop())
    

print(EvaluatePrefix(expression))
