n, m, x, y = map(int, input().split())
if m > n:
    n, m = m, n
paths = (m - x, x, n - y , y)
print(min(paths))
