from sympy import *
init_printing()

# 記号xを定義
x1, y1, z1, t1, c1 = symbols("x_1 y_1 z_1 t_1 c_1")
x2, y2, z2, t2, c2 = symbols("x_2 y_2 z_2 t_2 c_2")

r1 = Matrix([c1*t1, x1, y1, z1])
r2 = Matrix([c2*t2, x2, y2, z2])

L12 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]])

print(ma)

print(r1)
print(r2)

# nup = symbols("nuprime")

# f = log(nup)
# g = sin(nup)

# print(latex(f))
# print(g)