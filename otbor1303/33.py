n = int(input())
yard = [list(map(int, input().split())) for i in range(n)]
s = yard [n-1][0]
x, y = 0, n-1
while (x, y) != (n-1, 0):
    if x != n - 1:
        if yard[y][x+1] > yard[y-1][x]:
            s += yard[y][x+1]
            (x, y) = (x+1, y)
        else:
            s += yard[y-1][x]
            (x, y) = (x, y-1)
    else:
        s += yard[y-1][x]
        (x, y) = (x, y-1)
print(s)

