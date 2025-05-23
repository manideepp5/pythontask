def calc(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b
    return "Invalid operator"

print(calc(10, 5, '+'))
print(calc(10, 5, '/'))
