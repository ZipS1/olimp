n = int(input())
lst = list(map(int, input().split()))
print(lst.index(min(lst))+1, len(lst) - lst[::-1].index(max(lst)))
