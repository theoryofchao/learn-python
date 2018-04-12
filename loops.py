list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(len(list))

## iterate through all items
for item in list:
  print(item)

for item in list:
  if item == 10:
    print(item)

## iterate within range
for x in range(0, 7):
  print(list[x])

## while 
i = 10
while i < 11:
  print(i)
  i += 1

i = 0
while i < 1000:
  print(i)
  i += 100