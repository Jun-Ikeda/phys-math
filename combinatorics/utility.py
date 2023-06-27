import numpy as np
import random

# DEFAULT_MAX = 1

def random_subset(A, k):
    output = list()
    while len(output) < k:
        relm = random.choice(tuple(A))
        if relm not in output:
            output.append(relm)
    return sorted(output)

def sumset(A, B):
    return set(a + b for a in A for b in B)

def random_set(k):
    output = list()
    while len(output) < k:
        output.append(random.random())
    return output

def random_convex_set(k, init_2_list = [0, 1], MAX_EXP = 2):
    output = list(init_2_list)
    assert(len(output) == 2)
    assert(k >= 2)
    while len(output) < k:
        a_nminus2 = output[-2]
        a_nminus1 = output[-1]
        delta_nminus1 = a_nminus1 - a_nminus2
        a_n_min = a_nminus1 + delta_nminus1
        a_n_max = a_nminus1 + delta_nminus1 * MAX_EXP
        a_n = random.uniform(a_n_min, a_n_max)
        while not (a_n_min < a_n and a_n < a_n_max):
            a_n = random.uniform(a_n_min, a_n_max)
        output.append(a_n)
    return output

def is_convex(A):
    A = sorted(A)
    for i in range(2, len(A)):
        if (A[i] - A[i - 1] < A[i - 1] - A[i - 2]):
            return False
    return True

def scale_list(A, k):
    return set(int(a * k) for a in A)

def uniform_set(a, b, k):
    return [a * i + b for i in range(k)]

def shifted_set(A, s):
    return [a + s for a in A]

def delta(A, B, x):
    output = 0
    for a in A:
        for b in B:
            if a - b == x:
                output += 1
    return output

def sigma(A, B, x):
    output = 0
    for a in A:
        for b in B:
            if a + b == x:
                output += 1
    return output