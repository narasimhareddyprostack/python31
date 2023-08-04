l = [10,20,30,255]
b = bytes(l)
ba = bytearray(l)

print(b)
print(type(b))
print(ba)
print(type(ba))

print("*** bytes vs bytearray")

# bytes - are immutable
# bytearray is mutable object