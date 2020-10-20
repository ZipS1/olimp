from __future__ import division 

def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):                  #TODO: check if it intersects after line ends
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False

xa, ya, xb, yb = map(int, input())
n, m = map(int, input())
stars = []
planets = []

for i in range(n):
    x, y = map(int, input())
    stars.apppend((x, y))

for i in range(m):
    x, y = map(int, input())
    planets.apppend((x, y))

for s in stars:
    for p in planets:
        xs, ys = s
        xp, yp = p

        if xs 
