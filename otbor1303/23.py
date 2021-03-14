s = input()
for i in range(1, 10):
    s = s.replace(str(i), "")
s = s.lower()
ind = ord(s[0])
alpha = True
for i in range(1, len(s)):
    ind += 1
    if s[i] != chr(ind):
        print(s[i])
        quit()
print(0)
