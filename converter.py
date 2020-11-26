def conv(num, ns):
    converted = ""
    while num >= ns:
        converted = str(num % ns) + converted
        num = num // ns
    converted = int(str(num % ns) + converted)
    return converted

num = int(input())
syst = int(input())
print( "Result:" ,conv(num, syst))
