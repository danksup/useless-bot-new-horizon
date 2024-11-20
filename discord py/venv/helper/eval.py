from functools import reduce

def eval(expression, steps=False):
    if isinstance(expression, list):    
        expr = expression
    else:
        expr = expression.split(' ')

    def op_search(op):
        after_op = expr.index(op) + 1 
        before_op = expr.index(op) - 1 

        ret = float(expr[before_op]), float(expr[after_op])

        return list(ret), before_op, after_op

    exp = '^'
    mul = '*'
    add = '+'
    sub = '-'
    div = '/'

    result = ''
    step_log = [] 

    while len(expr) > 1: 
        if not any(item in expr for item in [exp]):
            break
        if steps:
            step_log.append(' '.join(expr))
        if exp in expr:
            search, before, after = op_search(exp)
            result = reduce(lambda x, y: x ** y, search)
            expr[before:after+1] = [str(result)]

    while len(expr) > 1: 
        if not any(item in expr for item in [mul, div]):
            break
        if steps:
            step_log.append(' '.join(expr))
        if mul in expr or div in expr:
            if mul in expr:
                search, before, after = op_search(mul)
                result = reduce(lambda x, y: x * y, search)
                expr[before:after+1] = [str(result)]
            elif div in expr:
                try:
                    search, before, after = op_search(div)
                    result = reduce(lambda x, y: x / y, search)
                    expr[before:after+1] = [str(result)]
                except Exception as e:
                    return f'error:\n ```{e}```'

    while len(expr) > 1: 
        if not any(item in expr for item in [add, sub]):
            break
        if steps:
            step_log.append(' '.join(expr))
        if add in expr:
            search, before, after = op_search(add)
            result = reduce(lambda x, y: x + y, search)
            expr[before:after+1] = [str(result)]
        elif sub in expr:
            search, before, after = op_search(sub)
            result = reduce(lambda x, y: x - y, search)
            expr[before:after+1] = [str(result)]

    if steps:
        step_log.append(' '.join(expr))  

    return '\n= '.join(step_log) if steps else result

