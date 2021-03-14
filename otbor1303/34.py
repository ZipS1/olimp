def sort(n):
    return n[0]

n, *t = map(int, input().split())
t = [(t[i], i) for i in range(len(t))]
t.sort(key=sort, reverse=True)

time = 0
for i in range(len(t)):
    m = i + 1
    time += t[i][0]*m
print(time, *[i[1]+1 for i in t])
