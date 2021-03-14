a, b, c = map(int, input().split())

if a + b > c and a + c > b and b + c > a:
    print(1)
else:
    print(0)
