l = [10,20,30,255]
b = bytes(l)

print(type(b))

print(b)   #b'\n\x14\x1e\xff'

for value in b:
    print(value)
