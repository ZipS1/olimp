n = int(input())
def is_prime(n):
    if n & 1 == 0:
        return True
    d = 3
    while d * d <= n:
        if n % d == 0:
            return True
        d= d + 2
    return False
print(is_prime(n))
