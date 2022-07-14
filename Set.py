import os
os.system('clear')

"""

A Set is an unordered collection if items.

Every set elements is unique and immutable.

But, set itself is mutable. We can add or remove item from it.

Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.

"""

# Set can't have mutable elements like lists, dictionaries, sets 

a = {2, 3, 4}
print(a)

a = {2, 3, 4, 2, 3} 
print(a)

# Set from List
a = set(['a', 'b', 'a', 'd'])
print(a)


# Creating Empty Set

# Empty curly braces {} will make an empty dictionary in Python. 
# To make a set without any elements, we use the set() function without any argument.


""" ACCESS """

# Set is an unordered collection. As a result it's not possible to access with index



""" ADD/UPDATE """

# Add single element

a.add('c')
print(a)


# Add multiple elements

a.update(['x', 'y', 'z']) # by list
print(a)

a.update(('l', 'm')) # by tuple
print(a)

a.update({'o', 'p'}) # by set
print(a)

a.update(['s', 't'], {'o', 'p'}) # by mix: list & set
print(a)



""" DELETE """

# A particular item can be removed by discard() or remove()
# the difference between discard and remove is, if item does not exist remove() will throw error. discard will not.

a = {2, 4, 6, 8}
a.discard(2)
print(a)

a.discard(10)
print(a)

a.remove(4)
print(a)

# a.remove(2) # will throw KeyError, since item does not exist 


# pop() will also remove item. But in random way. Will throw KeyError if set be empty.

a.pop()
print(a)



""" SET OPERATIONS """

A, B = {1, 3, 5, 7}, { 5, 7, 8, 9}

# union
print('Union: ', A | B)
print('Union: ', A.union(B))

# Intersection
print('Intersection: ', A & B)
print('Intersection: ', A.intersection(B))

# Difference
print('Difference: ', A - B)
print('Difference: ', A.difference(B))

# Symmetric Difference  ( like XOR )
print('Difference: ', A ^ B)
print('Difference: ', A.symmetric_difference(B))


# Intersection Update
A, B = {1, 3, 5, 7}, { 5, 7, 8, 9}
A.intersection_update(B)
print('Intersection Update: ', A, B)

# Difference Update
A, B = {1, 3, 5, 7}, { 5, 7, 8, 9}
A.difference_update(B)
print('Difference Update: ', A, B)

# Symmetric Difference Update
A, B = {1, 3, 5, 7}, { 5, 7, 8, 9}
A.symmetric_difference_update(B)
print('Symmetric Difference Update: ', A, B)

# Subset
A, B = {1, 5}, { 1, 5, 7, 8, 9}
print('Subset', A.issubset(B)) # true
print('Subset', B.issubset(A)) # false

# Superset
print('Superset', A.issuperset(B)) # false
print('Superset', B.issuperset(A)) # true


# disjoint
# if two sets dont have any common items between them

A, B, C = {1, 2, 3}, {4, 5, 6}, {6, 7, 8}
print('Disjoint', A.isdisjoint(B)) # true
print('Disjoint', B.isdisjoint(C)) # false


# disjoin with others iterable collection
# for dictionary, consider only keys

A = {'a', 'e', 'i', 'o', 'u'}   # set
B = ['d', 'e', 'f']             # list
C = {1 : 'a', 2 : 'b'}          # dic
D = {'a' : 1, 'b' : 2}          # dic

print('Disjoint set-list', A.isdisjoint(B)) # false
print('Disjoint set-dic', A.isdisjoint(C)) # true
print('Disjoint set-dic', A.isdisjoint(D)) # false






