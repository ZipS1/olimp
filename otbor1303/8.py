num = input()
rnum = ''
for i in range(len(num) - 1, -1, -1):
    rnum += num[i]

if int(num) == int(rnum):
    print(1)
else:
    print(0)
