s = input()
n = int(input())
if n >= 0:
    print(s*n)
else:
    print(s[::-1]*(-n))
