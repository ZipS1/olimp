from functools import reduce
import operator
from math import sqrt, degrees, atan2

def dist(ax, ay, bx, by):
    return sqrt((bx-ax)**2 + (by-ay)**2)

with open("37_input.txt", "r") as f:
    n = int(f.readline())
    n_coords = [int(i) for i in f.readline().split()]
    n_coords = [(n_coords[i], n_coords[i+1]) for i in range(0, 2*n, 2)]
    m = int(f.readline())
    m_coords = [int(i) for i in f.readline().split()]
    m_coords = [(m_coords[i], m_coords[i+1]) for i in range(0, 2*m, 2)]

if m == 1:
    distton = [dist(*m_coords[0], *n_coords[i]) for i in range(n)]
    indmin = distton.index(min(distton))
    n_coords = [(i[1], i[0]) for i in enumerate(n_coords)]
    print(n_coords)
    coords = [(0, 1), (1, 0), (1, 1), (0, 0)]
    center = tuple(map(operator.truediv, reduce(lambda x, y: map(operator.add, x, y), coords), [len(coords)] * 2))
    print(sorted(coords, key=lambda coord: (-135 - degrees(atan2(*tuple(map(operator.sub, coord, center))[::-1]))) % 360))

