from MathNode import MathNode, MathNodeType

symbol = MathNodeType('symbol', None, ('C', ), lambda x: x, lambda x: str(x))
add = MathNodeType('add', (('C', ), ('C', )), ('C', ), lambda x, y: x + y, lambda x, y: f'{str(x)}+{str(y)}')
multiply = MathNodeType('multiply', (('C', ), ('C', )), ('C', ), lambda x, y: x * y, lambda x, y: f'{str(x)}*{str(y)}')
divide = MathNodeType('divide', (('C', ), ('C', )), ('C', ), lambda x, y: x / y, lambda x, y: f'{str(x)}/{str(y)}')
subtract = MathNodeType('subtract', (('C', ), ('C', )), ('C', ), lambda x, y: x - y, lambda x, y: f'{str(x)}-{str(y)}')
power = MathNodeType('power', (('C', ), ('C', )), ('C', ), lambda x, y: x ** y, lambda x, y: f'{str(x)}^{str(y)}')

f = MathNodeType('f', (('C', ), ('C', )), ('C', ), lambda x, y: x + 2*y, lambda x, y: f'f({str(x)}, {str(y)})')

iterate = MathNodeType('iterate', (('C', ), ), ('P(C)', ), lambda n: range(1, n+1), lambda n: f'{{1, 2, ..., {str(n)}}}')

sigma = MathNodeType('sigma', (('C', ), ('P(C)', )), ('C', ), lambda x, y: sum([]), lambda x, y: f'sigma({str(x)}, {str(y)})')

x = MathNode(symbol, ('x', ))
two = MathNode(symbol, (2, ))
x_plus_two = MathNode(add, (x, two))

print(x_plus_two)

x_plus_two_plus_two = MathNode(add, (x_plus_two, two))
print(x_plus_two_plus_two)

x_plus_two_times_two = MathNode(multiply, (x_plus_two, two))
print(x_plus_two_times_two)

x_plus_two_times_x_plus_two = MathNode(multiply, (x_plus_two, x_plus_two))
print(x_plus_two_times_x_plus_two)

x_plus_two_power_x_plus_two = MathNode(power, (x_plus_two, x_plus_two))
print(x_plus_two_power_x_plus_two)

f_x_plus_two = MathNode(f, (x_plus_two, two))
print(f_x_plus_two)

iterate_x_plus_two = MathNode(iterate, (x_plus_two, ))
print(iterate_x_plus_two)