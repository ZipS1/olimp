s = input("Enter string: ")
symbols = ('(', ')', '[', ']', '{', '}')

for i in s:
    if i not in symbols:
         s = s.replace(i, '')

while True:
    if s.find("()") != -1:
        s = s.replace('()', '')
    elif s.find("[]") != -1:
        s = s.replace('[]', '')
    elif s.find(r"{}") != -1:
        s = s.replace(r'{}', '')
    elif s == '':
        print("correct")
        break
    else:
        print("incorrect")
        break
