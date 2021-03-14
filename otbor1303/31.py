from math import sqrt

def is_prime(num):
    if(num==1):
        return False
    if(num==2):
        return True
    if(num%2==0):
        return False

    i = 3
    while(i < sqrt(num)+1):
        if num%i==0:
            return False
        i += 2
    return True

n = int(input())
a = list(map(int, input().split()))
print(a)

for i in a:
    print(i)
    if is_prime(i):
        a.remove(i)
print(*a)
