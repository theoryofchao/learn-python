items = ['abc', 'def', 12.34, 56.78, 'ghi', 'jkl', 3]

def parselist(test_list):
  str_list = []
  num_list = []
  for i in test_list:
    if isinstance(i, float) or isinstance(i, int):
      num_list.append(i)
    elif isinstance(i,str):
      str_list.append(i)
    else:
      pass
  return str_list, num_list

print(parselist(items))

def mysum(test_list):
  total = 0
  for i in test_list:
    if isinstance(i, float) or isinstance(i, int):
      total+=i
  return total

print(mysum(items))

def myaverage(test_list):
  my_sum = 0
  my_length = 0
  for i in test_list:
    if isinstance(i, float) or isinstance(i, int):
      my_sum += i
      my_length += 1
  return my_sum / my_length

print(myaverage(items))