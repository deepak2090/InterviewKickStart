
def evalRPN(tokens):
    operators = ['+', '-', '*', '/']
    stack = []
    output = 0
    val = None
    for element in tokens:
        if element in operators:
            #stacklist.append(element)
            if val is None: 
                x = stack.pop()
                y = stack.pop()
            else:
                x = val
                y = stack.pop()
            val = f'{x} {element} {y}'
            val = eval(val)
            
        else:
            stack.append(element)
    return val

print(evalRPN(["2","1","+","3","*"]))