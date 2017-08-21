import threading
from multiprocessing import Queue
def threaded(f, daemon=False):

    def wrapped_f(q, *args, **kwargs):
        '''this function calls the decorated function and puts the 
        result in a queue'''
        ret = f(*args, **kwargs)
        q.put(ret)

    def wrap(*args, **kwargs):
        '''this is the function returned from the decorator. It fires off
        wrapped_f in a new thread and returns the thread object with
        the result queue attached'''

        q = Queue()

        t = threading.Thread(target=wrapped_f, args=(q,)+args, kwargs=kwargs)
        t.daemon = daemon
        t.start()
        t.join(10)
        t.result_queue = q        
        return t

    return wrap

@threaded
def expr_gen(difficulty, code=None):
    """
    Generates a random expression that evaluates to a random number.
    """

    if difficulty == 1:
        num = randint(0, 9)
        expr_numbers = str(randint(1000000, 9999999))
    elif difficulty == 2:
        num = randint(10, 99)
        expr_numbers = str(randint(10000000, 99999999))
    elif difficulty == 3:
        num = randint(100, 999)
        expr_numbers = str(randint(100000000, 999999999))
    elif difficulty == 4:
        num = randint(1000, 9999)
        expr_numbers = str(randint(1000000000, 9999999999))
    
    if code is None:
        expressions = []
        while not expressions:
            match = solve(num, generate(expr_numbers))
            for expr in match:
                expressions.append(expr)
        rendered_exprs = []
        for expr in expressions:
            rendered_exprs.append(render(expr))
        expr = rendered_exprs[randint(0, len(rendered_exprs) - 1)]

    else:
        expressions = []
        while not expressions:
            match = solve(int(code), generate(expr_numbers))
            for expr in match:
                expressions.append(expr)
        rendered_exprs = []
        for expr in expressions:
            rendered_exprs.append(render(expr))
        expr = rendered_exprs[randint(0, len(rendered_exprs) - 1)]
        
    return expr