import operator
from multiprocessing import Queue
from random import randint
from threading import Thread

__all__ = ["operator"]

MUL = operator.mul
ADD = operator.add
SUB = operator.sub

OP_TEXT_MAP = {MUL: " * ", ADD: " + ", SUB: " - "}


def make_resolve_func(op):
    """Give a function that resolves expressions using given operator."""
    WEAK_OPS = (ADD, SUB)

    def resolve(number, right_expr):
        """Pack expression and result."""
        return (op, (number, ), right_expr, op(number, right_expr[-1]))

    if op in WEAK_OPS:
        return resolve

    def rewrite(number, right_expr):
        """Pack expression and result rewriting right_expr if needed."""
        if right_expr[0] in WEAK_OPS:
            rop, rl, rr, _ = right_expr
            lequal = op(number, rl[-1])
            return (rop, (op, (number, ), rl, lequal), rr, rop(lequal, rr[-1]))
        return resolve(number, right_expr)

    return rewrite


__all__.extend(["make_resolve_func", "resolve", "rewrite"])


def generate(digits):
    """Generate every allowed expression from digits."""
    states = [(digits, len(digits) - 1, None)]
    state_add, state_pop = states.append, states.pop
    resolve_funcs = list(map(make_resolve_func, (MUL, ADD, SUB)))
    result = []
    while states:
        remaining, length, expr = state_pop()
        number = int(remaining[length:])
        if expr is not None:
            outcomes = [resolve(number, expr) for resolve in resolve_funcs]

        else:
            outcomes = [(number, )]
        if length:
            new_remaining = remaining[:length]
            length -= 1
            state_add((remaining, length, expr))
            for outcome in outcomes:
                state_add((new_remaining, length, outcome))
        else:
            for outcome in outcomes:
                result.append(outcome)
    return result


__all__.append("generate")


def render(expression):
    """Give expression as a string with infix operations."""
    if len(expression) == 1:
        return str(expression[0])
    return OP_TEXT_MAP[expression[0]].join(map(render, expression[1:-1]))


__all__.append("render")


def solve(target, expressions):
    """For expressions give all that evaluate to target."""
    result = []
    for expr in expressions:
        if expr[-1] == target:
            result.append(expr)
    return result


__all__.append("solve")


def ten_digits(digits):
    if digits and len(digits) <= 10 and set("0123456789").issuperset(digits):
        return digits
    raise ValueError("Must be string of up to 10 digits: {!r}".format(digits))


__all__.append("ten_digits")


def num_gen(difficulty):
    """Generates random numbers based on the selected difficulty level"""
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

    return num, expr_numbers


__all__.append("num_gen")


def expr_gen(difficulty, code=None):
    """
    Generates a random expression that evaluates to a random number.
    """
    num, expr_numbers = num_gen(difficulty)
    if code is None:
        expressions = []
        while not expressions:
            match = None
            while not match:
                num, expr_numbers = num_gen(difficulty)
                que = Queue()
                t = Thread(
                    target=lambda q, arg1, arg2: q.put(solve(arg1, arg2)),
                    args=(que, num, generate(expr_numbers)))
                t.start()
                t.join(5)
                match = que.get()
            for expr in match:
                expressions.append(expr)
        rendered_exprs = []
        for expr in expressions:
            rendered_exprs.append(render(expr))
        expr = rendered_exprs[randint(0, len(rendered_exprs) - 1)]

    else:
        expressions = []
        while not expressions:
            match = None
            while not match:
                num, expr_numbers = num_gen(difficulty)
                que = Queue()
                t = Thread(
                    target=lambda q, arg1, arg2: q.put(solve(arg1, arg2)),
                    args=(que, int(code), generate(expr_numbers)))
                t.start()
                t.join(5)
                match = que.get()
            for expr in match:
                expressions.append(expr)
        rendered_exprs = []
        for expr in expressions:
            rendered_exprs.append(render(expr))
        expr = rendered_exprs[randint(0, len(rendered_exprs) - 1)]

    return expr


__all__.append("expr_gen")
