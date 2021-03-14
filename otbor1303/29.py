n = int(input())
a = list(map(int, input().split()))
count = 0
prevd = 0
for i in range(1, n):
    d = a[i] - a[i-1]
    if d >= 0 and prevd < 0:
        count += 1
    prevd = d
if d < 0:
    count += 1
print(count)
