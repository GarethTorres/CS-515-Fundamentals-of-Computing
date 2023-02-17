def correctName(s):
    space_position = ' '
    end = s.find(space_position)
    return s[:1].upper() + s[1:end].lower() + s[end:end+2].upper() + s[end+2:].lower()
example1 = correctName('dIrK noWitZKi')
print(example1)

def stringShortener(s,n):
    return s[:n]
example11 = stringShortener('jksakd jkafk', 5)
print(example11)

def changeList(L,n):
    a = L[n]
    L.append(a)
    return L
example111 = changeList([1,2,3,4,5],3)
print(example111)

