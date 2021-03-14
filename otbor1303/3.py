from math import sqrt, acos

x1, y1, x2, y2 = map(int, input().split())

cos = (x1*x2 + y1*y2)/(sqrt(x1**2 + y1**2)*sqrt(x2**2 + y2**2))
angle = acos(cos)

print(f"{angle:.5f}")
