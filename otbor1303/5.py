num = input()
nums = map(int, list(num))
m = 1
s = 0

for num in nums:
    m*= num
    s += num

print(s)
print(m)
