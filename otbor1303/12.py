def sort(el):
    return list.count(el)
n = int(input())
votes = list(map(int, input().split()))
m = []
mx = 0
for  i in votes:
    count = votes.count(i)
    if count > mx:
        mx = count
        num = i
m.sort(reverse=True)
print(num)
