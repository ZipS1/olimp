from math import sqrt

x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

surf = 0.5*abs((x1*y2 + x2*y3 + x3*y4 + x4*y1 - x2*y1 - x3*y2 - x4*y3 - x1*y4))

print(f"{surf:.3f}")
