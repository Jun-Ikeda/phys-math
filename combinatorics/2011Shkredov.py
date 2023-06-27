import matplotlib.pyplot as plt
import numpy as np
from utility import *

# 2011 Shkredov, Schoen, 14/9 On Sumsets of convex sets
# Lemma 7
""""
cardA, cardB = 20, 20
cardAprime = random.randint(1, cardA)
A = random_convex_set(cardA, [0, 1], 2)
B = random_set(cardB)
Q = random_subset(range(1, cardA + 1), cardAprime)

print('A =', A)
print('Q =', Q)

# multiline string
init = " folder \"\" {\n  I = [1 ... length(A)] @{ color: \"#c74440\" }\n\n  A_p = [A[q] for q = Q] @{ color: \"#2d70b3\" }\n\n  l(alpha, beta) = [(q + alpha, A[q] + beta) for q = Q] @{ color: \"#6042a6\" }\n} @{ collapsed: true }\n"
A_text = "A = [" + ", ".join(str(a) for a in A) + "] @{ color: \"#c74440\" }\n"
Q_text = "Q = [" + ", ".join(str(q) for q in Q) + "] @{ color: \"#388c46\" }\n"
B_text = "B = [" + ", ".join(str(b) for b in B) + "] @{ color: \"#2d70b3\" }\n"


L_text = "folder \"\" {\n"
for alpha in range(1, cardA + 1):
    for beta in B:
        L_text += "l(" + str(alpha) + ", " + str(beta) + ") @{ color: \"#2d70b3\", lines: @{ opacity: 0.9, width: 2.5 } }\n\n"
L_text += " } @{ collapsed: true }\n"

print(init + A_text + Q_text + B_text + L_text)
"""
