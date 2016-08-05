keys = ['a', 'b', 'c', 'd', 'e']
values = ['c', 'd', 'e', 'd', 'c']

print keys
print values
print dict(zip(keys, values))
print zip(values, keys)
print dict(zip(values, keys))