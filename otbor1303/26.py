n = int(input())
lst = list(map(int, input().split()))
even = []
for i in lst:
    if i % 2 == 0:
        even.append(i)
        lst.remove(i)
lst.reverse()
print(*even, *lst)
