import os
os.system('clear')


"""

List is an ordered sequence of items. Its mutable. Items data type can be different.

"""


a = []
a = [2, 4, 7]
print("a :", a)

b = [1, 3, 'Mamun', 9.8, [1.5, 2.4]]
print("b :", b)


""" ACCESS """

print("First item :", b[0])
print("5th item :", b[4])
print("Nested Indexing :", b[4][1]) 
# print("Out of Index :", b[5]) # IndexError
print("2nd to 4th :", b[1:4]) 
print("2nd to last : ", b[1:]) 
print("First to 3rd :", b[:3]) 
print("First to last :", b[:]) 

#negetive indexing works from last and as one based index. -1 means last item, -2 means 2nd last.
print("Neg-last :", b[-1])  #last
print("Neg-3rd :", b[-3]) # 3rd last
# print("Neg-Out of Index:", b[-6]) # IndexError


x = [2, 4, 6, 8]



""" ADD """

x.append(10)
print("Added :", x)

x.extend([12, 14])
print("Extended :", x)

x.insert(1, 9)
print("Insert single item at index:", x)

x[2:2] = [13, 17] # at 3rd index
print("Insert multiple items at index:", x)



""" UPDATE """

x[1] = 5
print("Update with index :", x)

x[0:3] = [-1, -2, -3]
print("Update with range :", x)



""" DELETE """
# with 'del' keyword or assigning empty array

del x[2] # delete 3rd item
print("Delete at index :", x)

del x[0:2] # delete first 2 items
print("Delete with range :", x)


x[0:1] = []  # delete first item
print("Delete single item with empty array :", x)

x[0:3] = [] # delete first 3 items
print("Delete multiple items with empty array :", x)

x.clear()
print("Delete all items :", x)

del x # delete entire list from memory. will throw error after futher access  
# print(x)


v = ['a', 'e', 'i', 'o', 'u']

v.remove('a') # non exist item will throw ValueError
print("removed :", v)

v.pop() # pop last item if index not provided. Empty list pop will throw IndexError
print("pop without index :", v)


v.pop(1)  # invalid index will throw IndexError
print("pop with index :", v)

v.pop(-1)  # negetive indexing works as well
print("pop with negative index :", v)




""" METHODS """

v = ['a', 'e', 'i', 'o', 'u', 'b']

print("Index :", v.index('i')) # if item does not exist will throw ValueError

print("Count :", v.count('i')) # no error will throw if item does not exist

v.sort()
print("Sort :", v) 

v.reverse()
print("Reverse :", v) 

w = v.copy()
print("Copy :", w) 

print("Length :", len(v)) 

print("Is Empty :", not v) 

print("Exist :", 'a' in v) 

print("Not Exist :", 'w' not in v) 

print('Max :', max([3, 1, 2, 5, 0]))

print('Min :', min([3, 1, 2, 5, 0]))

print('Sorted :', sorted([3, 1, 2, 5, 0]))

print('Sum :', sum([3, 1, 2, 5, 0]))



""" ITERATE """

v = ['a', 'e', 'i', 'o', 'u']

for c in v:
    print('char :', c)


# enumerate syntax: enumerate(iterable_collection, start=0)
# enumerate return list of tuple containig index and item

for t in enumerate(v):
    print(t)

for t in enumerate(v):
    print('Index : {0}, Item: {1}'.format(t[0], t[1]))

for i, c in enumerate(v, 5):
    print('Index : {0}, Item: {1}'.format(i, c))



""" OTHERS """

# Concatening
v = [1, 2, 3]
w = v + [5, 6, 7]
print('Concatening :', w)

# Repeating
print('Repeating :', v * 4)



""" COMPREHENSION """

# List comprehension is an elegant and concise way to create a new list from an existing list in Python.

# A list comprehension consists of an expression followed by for statement inside square brackets.

p = [x*2 for x in [1, 2, 3]] 
print(p)

# A list comprehension can optionally contain more 'for' or 'if' statements.
# An optional if statement can filter out items for the new list.

p = [x**2 for x in range(1, 11) if x % 2 == 1]
print(p)


p = [(x,y) for x in range(1, 4) for y in ['a', 'b']]
print(p)

p = [(x,y) for x in range(1, 4) if x % 2 == 0 for y in ['a', 'b']]
print(p)

p = [(x,y) for x in range(1, 4) if x % 2 == 0 for y in ['a', 'b'] if y == 'a']
print(p)


# a,b,c = [1, 2, 3]
# print(a, b, c)
