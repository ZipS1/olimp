f = [list(map(int, input().split())) for i in range(10)]
curx, cury, = 0, 0
maxx, maxy = 0, 0

for i in range(10):
    for j in range(10):
        if j == 0 and curx != 0:
            if curx > maxx:
                maxx = curx
            curx = 0
        if f[i][j] == 0:
            curx += 1
        elif curx != 0:
            if curx > maxx:
                maxx = curx
                curx = 0

        if j == 0 and cury != 0:
            if cury > maxy:
                maxy = cury
            cury = 0
        if f[j][i] == 0:
            cury += 1
        elif cury != 0:
            if cury > maxy:
                maxy = cury
                cury = 0

print(max(maxx, maxy))
