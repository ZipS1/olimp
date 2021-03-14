from math import sqrt

x1, y1, x2, y2, x3, y3 = map(int, input().split())

def findpoint(x1,y1,x2,y2,x3,y3):
    if x3 != x2:
        tan1 = (y3 - y2)/(x3-x2)
    else:
        return (0, 0)
    if x3 != x1:
        tan2 = (y3-y1)/(x3-x1)
    else:
        return (0, 0)

    if tan1 == 0:
        point_y = int(x1*tan2)
        point_x = int(y2 // tan2)
        return point_x, point_y

    if tan2 == 0:
        point_y = int(x2*tan1)
        point_x = int(y1 // tan1)
        return point_x, point_y
    return f"tans: {tan1}, {tan2}"


print(findpoint(x3,y3,x2,y2,x1,y1))
print(findpoint(x3,y3,x1,y1,x2,y2))
print(findpoint(x1,y1,x2,y2,x3,y3))
print(findpoint(x1,y1,x3,y3,x2,y2))
print(findpoint(x2,y2,x1,y1,x3,y3))
print(findpoint(x2,y2,x3,y3,x1,y1))



