s = input("Enter string: ")                    #TODO: refactorig breaks (lines 17, 20) with in another way
symbols = ('(', ')', '[', ']', '{', '}')

for i in s:
    if i not in symbols:
         s = s.replace(i, '', 1)
while True:
    if s.find("()") != -1:
        s = s.replace('()', '')
    elif s.find("[]") != -1:
        s = s.replace('[]', '')
    elif s.find(r"{}") != -1:
        s = s.replace(r'{}', '')
    else:
        if s == '':
            print("correct")
            break
        else:
            print("incorrect")
            break
