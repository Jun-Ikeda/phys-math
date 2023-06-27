# Some new inequalities in additive combinatorics
import math

# p: prime, q: p^s for any s, F_q: finite field of order q
# F_q^*: multiplicative group of F_q: { n | 1 <= n <= q - 1, gcd(n, q) = 1 }
# g: primitive root of q, n: divisor of totient(q)
# gamma: subgroup of F_q^*, 

p = 2
s = 3
n = 2

q = p ** s
F_q = range(q)
F_q_star = [n for n in range(1, q) if math.gcd(n, q) == 1]
Gamma = []


