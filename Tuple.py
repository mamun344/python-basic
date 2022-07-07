import os
os.system('clear')

"""

Tuple is similar to a list. The difference is, we can't the change the elements of a tuple once it is assigned.

"""


# A tuple is created by placing all the items (elements) inside parentheses (), separated by commas.
# The parentheses are optional, however, it is a good practice to use them.

a = (2, 5, 10, ['a', 'b'])
print(a)


# A tuple can also be created without using parentheses. This is known as tuple packing.

a = 4, 7, 'john'

# tuple unpacking is also possible

x, y, z = a
print(x, y, z)



# Creating a tuple with one element is a bit tricky.

# Having one element within parentheses is not enough.
# We will need a trailing comma to indicate that it is, in fact, a tuple.

a = (5) # int
print(type(a))

a = (5,) # tuple
print(type(a))



a = (2, 5, 10, ['a', 'b'])


""" ACCESS """

# Same as LIST



""" ADD """

# Not Possible



""" UPDATE """

# update will possible only to item which itself is mutable (e.g. nested list, nested dictionary)

# a[3] = 'y' # will throw TypeError
a[3][0] = 'x' # valid
print(a)



""" DELETE """

# Not Possible



""" METHODS """

# sort, copy, reverse will not work
# others as well



""" ITERATE """

# Same as LIST



a = """ OTHERS """

# Concatening & Repeating same as LIST



""" COMPREHENSION """

# Same as LIST



# Advantages of Tuple over List

# We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
# Since tuples are immutable, iterating through a tuple is faster than with list. So there is a slight performance boost.
# Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
# If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.

