n = int(input())
lst = list(map(int, input().split()))
arr = []
left = 0
right = len(lst) - 1
for i in range(n//2):
    arr.append(lst[left])
    arr.append(lst[right])
    left += 1
    right -= 1
print(*arr)
