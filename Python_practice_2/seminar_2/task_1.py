a: int = 10
b: str = 'New string'
c: bool = False

print(type(a))
print(type(b))
print(type(c))

if type(c) == str:
    print("OK")
else:
    print("NOT A STRING")

isinstance(c, int)