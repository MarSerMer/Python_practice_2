name = 'Alex'
age = None
data = 0
while data < 100:
    data += 3
    print (data, end=' ')
    if data % 19 == 0:
        continue
    data += 1
    print (data)
    if data % 40 == 0:
        break
else:
    data += 5
print(data)