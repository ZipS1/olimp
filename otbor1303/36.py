n, m = map(int, input().split())
details = [0 for i in range(n)]
for i in map(int, input().split()):
    details[i-1] = 1

shorten = ""
inrange = False
for i in range(n):
    if i != n-1:
        if details[i] == 1:
            if details[i+1] == 0 and not inrange:
                shorten += f"{i+1},"
            elif not inrange:
                inrange = True
                start = i
            elif inrange and details[i+1] == 0:
                inrange = False
                end = i
                shorten += f"{start+1}-{end+1},"
    elif details[i] == 1:
        if inrange:
            end = i
            shorten += f"{start+1}-{end+1},"
        else:
            shorten += f"{i+1},"
print(shorten[:-1])
