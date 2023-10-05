l = [10,20,30,255]
b = bytes(l)
ba = bytearray(l)

print(ba[0])
ba[0]  = 40
print(ba[0])
#print(ba[0])