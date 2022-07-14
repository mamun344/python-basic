import os
os.system('clear')


"""

Dictionary is an unorderred collection of items. 

Each item of a dictionary has a key-value pair.

Keys and vlaues can be any data type. 
But keys must be immutable data type like number, string, tuple.

"""

d = {}
print('dict init :', type(d))

d = dict()
print('dict init :', type(d))

d = {1: 'one', 2:'two'}
print('Init by same type keys : ', d)

d = {'a': 23, 5: 'five', 'profile': ('mamun', 33, 'm'), ('name', 'age'): ('mamun', 33)}
print('Init by different type keys & values : ',d)

d = dict({1: 'one', 2:'two'})
print('Init by dict : ', d)

d = dict([(1, 'One'), ('a', 97), ('name', 'mamun')])
print('Init by list of tuples : ', d)

d = dict(((1, 'One'), ('a', 97), ('name', 'mamun')))
print('Init by tuple of tuples : ', d)

d = dict({(1, 'One'), ('a', 97), ('name', 'mamun')})
print('Init by set of tuples : ', d)


# fromkeys() method creates a dictionary from the given sequence of keys and an optional value.
# syntax : fromkeys(keys, value)
# keys could be any iterable collection like list, set, string, tuple
# value is optional. If not provided None will be consider

d = dict.fromkeys(['a', 'b', 'c'], 2)
print('fromKeys with a value:', d)

d = dict.fromkeys(['a', 'b', 'c'])
print('fromKeys without value:', d)


""" ACCESS """

d = {1: 'one', 2:'two'}
print(d[1])
# If keys does not exist, will throw KeyError
# print(d[3]) 

# get syntax : get(key, default)
# will return value for key if key exist. Otherwise will return default.
# default is optional. if value not found for given key, default will return. Default value of default is None.

print(d.get(2))
print(d.get(2, 'TWO'))

print(d.get(3))
print(d.get(3, 'THREE'))




""" ADD """

d[3] = 'Three'

# setdefault syntax : dict.setdefault(key, value)
# if key is not present, the value will set for given key. Otherwise will ignore.
# returns the value of the given key

r = d.setdefault(2, 'TWO') # key exist, will not change
print(d, r)

r = d.setdefault(4, 'Four') # key doesn't exist, will set as key-value pair
print(d, r)




""" UPDATE """

d = {1: 'one', 2:'two'}
d[1] = 'ONE'
print(d)

# will update the dict itself by given iterable collection like another Dictionary, list of Tuples, tuple of Tuples, set of Tuples etc

d.update({3: 'THREE', 4: 'FOUR'}) # by dict
print(d)

d.update([(5, 'Five'), (6, 'Six')]) # by list of Tuples
print(d)

d.update(((5, 'F-i-v-e'), (6, 'S-i-x'))) # by tuple of Tuples
print(d)

d.update({(7, 'seven'), (8, 'eight')}) # by set of Tuples
print(d)



""" DELETE """

# by del or pop 

# del
d = {1: 'one', 2:'two'}

del d[1] # if key does not exist, will thorw KeyError
print('after del: ', d)


# pop
# syntax : pop(key, default)
# default is optional. It has no default value.
# if key is found will return corresponding value.
# if key is not found and default is provided, default will return. Otherwise will throw KeyError

d = {1: 'one', 2:'two'}

print('pop :', d.pop(1, 'o-n-e')) # return one
print('pop :', d.pop(3, 'three'))
# print('pop :', d.pop(3)) # KeyError

# Removes and returns an arbitrary item (key, value). Raises KeyError if the dictionary is empty.
print('popitem :', d.popitem()) 

del d
# print(d) # KeyError



""" METHODS """

d = {1: 'one', 2:'two'}


# keys() method extracts the keys of the dictionary and returns the list of keys as a view object.
print('Keys :', d.keys())
print('Keys type :', type(d.keys()))

for key in d.keys():
    print('key :', key)


# values() method extracts the values of the dictionary and returns the list of values as a view object.
print('Values :', d.values())
print('Values type :', type(d.values()))

for val in d.values():
    print('value :', val)


# items() method returns a view object that displays a list of a given dictionary's (key, value) tuple pair.
print('Items :', d.items())
print('Items type :', type(d.items()))

for item in d.items():
    print('item :', item)

print('sorted keys:', sorted(d))

print('length:', len(d))

d.clear()
print('clear :', d)

