from math import sqrt

n = int(input())
phi = 0.5 + 0.5 * sqrt(5.0)
a = phi * n
print(n == 0 or abs(round(a) - a) < 1.0 / n)
