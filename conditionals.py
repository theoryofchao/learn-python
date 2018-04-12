## Datatypes (capitalized)
print(True)
print(False)

## == conditional
print(True == False) ## False
print(True == True) ## True

## != conditiaonal
print(True != False) ## True

false_statement = False
true_statement = True

print(not true_statement == false_statement) ## True

print(true_statement is True) ## True

for i in range(0, 50):
  if(i % 3 == 0):
  	print(str(i) +  " modulo 3")
  elif(i % 2):
  	print(repr(i) + " modulo 2")
  else:
  	print(str(i))

## isistance returns boolean if the first parameter the type as defined by the second parameter
if isinstance("string", str):
	print('is string')

x = 0
list_1 = ['a', 'b', 'c', 1, 2, 3]
list_2 = []

index = 0

for item in list_1:
  if isinstance(item, int):
    list_2.append(item)

print(list_1)
print(list_2)