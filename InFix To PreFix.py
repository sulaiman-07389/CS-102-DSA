
expression = input()

def Infix_to_Prefix(expression):
    op_stack = []
    infix = expression.split()
    
    rev_infix = []
    length = len(infix)-1
    while length != -1:
        if infix[length] == '(':
            rev_infix.append(')')
        elif infix[length] == ')':
            rev_infix.append('(')
        else:
            rev_infix.append(infix[length])
        length = length - 1
    #return(rev_infix)
    output = []        
    for i in range(len(rev_infix)):
        if rev_infix[i] not in '()+-/*':
            output.append(rev_infix[i])
        elif rev_infix[i] == '(':
            op_stack.append(rev_infix[i])
        elif rev_infix[i] == ')':
            j = i - 1
            while rev_infix[j] != '(':
                if rev_infix[j] in '+-/*':
                    output.append(op_stack.pop())
                
                    #    op_stack.pop()
                j = j - 1
            output.append(op_stack.pop())
            output.append(rev_infix[i])
        if rev_infix[i] in '+-/*':
            if rev_infix[i] == '/':
                if('/' or '*') in op_stack:
                    index = len(op_stack)-1
                    while index != -1:
                        if (op_stack[index] == '/' or op_stack[index] == '*')and (op_stack[index] != '('):
                            output.append(op_stack.pop(index))
                        elif op_stack[index] == '(':
                            break
                        index = index - 1
                op_stack.append('/')
            if rev_infix[i] == '*':
                if ('/' or '*') in op_stack:
                    index = len(op_stack)-1
                    while index != -1:
                        if (op_stack[index] == '/' or op_stack[index] == '*') and (op_stack[index] != '('):
                            output.append(op_stack.pop(index))
                        elif op_stack[index] == '(':
                            break
                        index = index - 1
                op_stack.append('*')
            if rev_infix[i] == '+':
                if op_stack:
                    index = len(op_stack)-1
                    while index != -1:
                        if (op_stack[index] == '+' or op_stack[index] == '-' or op_stack[index] == '/' or op_stack[index] == '*') and (op_stack[index] != '('):
                            output.append(op_stack.pop(index))
                        elif op_stack[index] == '(':
                            break
                        index = index - 1
                op_stack.append('+')
            
            if rev_infix[i] == '-':
                if op_stack:
                    index = len(op_stack)-1
                    while index != -1:
                        if (op_stack[index] == '+' or op_stack[index] == '-' or op_stack[index] == '/' or op_stack[index] == '*') and (op_stack[index] != '('):
                            output.append(op_stack.pop(index))
                        elif op_stack[index] == '(':
                            break
                        index = index - 1
                op_stack.append('-')
    if not op_stack == False:
        while len(op_stack) != 0:
            if op_stack[len(op_stack)-1] != '(' and op_stack[len(op_stack)-1] != ')':
                output.append(op_stack.pop())
            else:
                op_stack.pop()
    output_str = ''                
    for k in output:
        if k == '(' or k == ')':
            pass
        else:
            output_str = output_str + k + ' '
    #print(output_str)
    prefix = ''
    length_out = len(output_str)-2
    while length_out != -1:
        prefix = prefix + output_str[length_out]
        length_out = length_out - 1
            
    return(prefix)

    #return output_str

print(Infix_to_Prefix(expression))
