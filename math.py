items = ['abc', 'def', 12.34, 56.78, 'ghi', 'jkl', 3]

for item in items:
  if (isinstance(item, float)):
    print(item)

unsorted_integers = [5, 2, 8, 1, 9, 3]
print(unsorted_integers)

unsorted_integers.sort()
print(unsorted_integers)

unsorted_integers.sort(reverse=True)
print(unsorted_integers)

sorted_items = sorted(unsorted_integers)
print(sorted_items)

reverse_sorted_items = sorted(unsorted_integers, reverse=True)
print(reverse_sorted_items)

summation = sum(unsorted_integers)
print(summation)

## watch for division, integers divided by integer will become a rounded integer