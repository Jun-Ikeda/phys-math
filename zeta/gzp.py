import sympy as sp

x, y, n, m, j = sp.symbols('x y n m j')

expr = x**2 + y + 1

# print(expr.subs(x, 1))
# print(sp.zeta(2))
# print(sp.Sum(1/n**2, (n, 1, sp.oo)).evalf())

# m = 1
for m in range(10):
  print(-2*sp.Sum(sp.zeta(2*j) * sp.zeta(6*m - 2*j), (j, 0, 3*m)).evalf() == ((1 - 6*m) * sp.zeta(6*m)).evalf())

m = 10
print(-6*sp.Sum(sp.zeta(6*j) * sp.zeta(6*m - 6*j), (j, 0, m)).evalf())
print(2*sp.Sum(1/n**(6*m) * (sp.exp(2*sp.pi*sp.I/3)*sp.pi*n * sp.cot(sp.exp(2*sp.pi*sp.I/3)*sp.pi*n) + sp.exp(2*sp.pi*sp.I*2/3)*sp.pi*n * sp.cot(sp.exp(2*sp.pi*sp.I*2/3)*sp.pi*n)),(n,1,1000)).evalf() + (1-6*m)*sp.zeta(6*m).evalf())

# -2\beta \sum _{j=0}^{\lfloor \frac{s}{\beta }\rfloor }\alpha ^{2\beta j}\zeta \left(2\beta j\right)\zeta \left(2s-2\beta j\right)=\sum _{n=1}^{\infty }\frac{1}{n^{2s}}\sum _{\nu =0}^{\beta -1}\left(\alpha e^{2\pi i\frac{\nu }{2\beta }}\pi n\cot \left(\alpha e^{2\pi i\frac{\nu }{2\beta }}\pi n\right)+\alpha ^{2s}\frac{e^{2\pi i\frac{\nu }{2\beta }\left(1+2\mu \right)}}{\alpha }\pi n\cot \left(\frac{e^{2\pi i\frac{\nu }{2\beta }}}{\alpha }\pi n\right)\right)