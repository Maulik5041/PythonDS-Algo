"""Given a string of arithmetic expression.
The usual way for humans to evaluate is: A + B (Infix)
But for computers, it is not easy to evaluate like this.
Thus there are 2 ways to handle this: Prefix and Postfix
Prefix: + A B
Postfix: A B +
Our solution is going to utilize Postfix approach"""


# create Token class to track value and operator
class Token:

    def __init__(self, value, is_operator):
        self.value = value
        self.is_operator = is_operator


def is_operator(c):
    return c == '+' or c == '-' or c == '*' or c == '/'


# check the precedence of operators
def preced(op1, op2):

    if op1 == '*' or op1 == '/':
        return True

    if op1 == '+' or op1 == '-':
        if op2 == '+' or op2 == '-':
            return True

    return False


# check if the given character is a digit
def is_digit(ch):
    return ch >= '0' and ch <= '9'


def str_to_double(s, i):
    n = len(s)
    if i >= n:
        return None

    temp = []

    while i < n and (s[i] == ' ' or s[i] == '\t'):
        i += 1

    if i >= n:
        return None

    if s[i] == '-':
        temp.append('-')
        i += 1

    while i < n:
        ch = s[i]
        if ch != '.' and not is_digit(ch):
            break

        temp.append(ch)
        i += 1

    temp_str = "".join(temp)
    return float(temp_str), i


def convert_to_postfix(expr):

    post_fix = []
    operators = []

    n = len(expr)
    i = 0

    while i < n:

        ch = expr[i]

        if ch == ' ' or ch == '\t':
            i += 1
            continue

        if is_operator(ch):

            while operators and preced(operators[-1], ch):
                post_fix.append(Token(operators.pop(), True))
            operators.append(ch)
            i += 1

        else:
            d, i = str_to_double(expr, i)
            post_fix.append(Token(d, False))

    while operators:
        post_fix.append(Token(operators.pop(), True))

    return post_fix


def evaluate1(post_fix):
    operands = []

    for x in post_fix:

        if x.is_operator:

            val2 = operands.pop()
            val1 = operands.pop()

            op = x.value

            if op == '+':
                operands.append(val1 + val2)

            elif op == '-':
                operands.append(val1 - val2)

            elif op == '*':
                operands.append(val1 * val2)

            elif op == '/':
                operands.append(val1 / val2)

        else:
            val = x.value
            operands.append(val)

    return operands.pop()


def evaluate(expr):
    return evaluate1(convert_to_postfix(expr))


print("evaluate(3+6*5-1/2.5) = " + str(evaluate("3+6*5-1/2.5")))
