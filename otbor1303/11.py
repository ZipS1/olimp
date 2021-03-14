n = int(input())
s1 = 0
s2 = 0
n1 = 0
n2 = n-1
for i in range(n):
    l = list(map(int, input().split()))
    s1 += l[n1]
    s2 += l[n2]
    n1 += 1
    n2 -= 1
print(s1, s2)
