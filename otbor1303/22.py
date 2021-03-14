def sort(s):
    return len(s)

s = input()
s = s.split()
print(len(min(s, key=sort)))
