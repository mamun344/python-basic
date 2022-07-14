import os
os.system('clear')


"""
A string is a sequence of characters.


A character is simply a symbol. For example, the English language has 26 characters.

Computers do not deal with characters, they deal with numbers (binary). Even though you may see characters on your screen, internally it is stored and manipulated as a combination of 0s and 1s.

This conversion of character to a number is called encoding, and the reverse process is decoding. ASCII and Unicode are some of the popular encodings used.

In Python, a string is a sequence of Unicode characters.


String is one kind of Tuple (immutable) where every elements are character.

"""


# Strings can be created by enclosing characters inside a single quote or double-quotes. 
# Even triple quotes can be used in Python but generally used to represent multiline strings and docstrings.

a = 'Hello'
b = "There"
c = '''Hi'''
d = """Oie"""


print(a, b, c, d)

e = """multiline
string"""

print(e)



"""

All kind of Access, Add, update, Delete, iterate same as like Tuple

"""



""" OTHERS """

# Concatening
v = "What is " + "your name?"
print('Concatening :', v)

# Repeating
print('Repeating :', "Hi " * 3)

# Writing two string literals together also concatenates them like + operator.
v = "How old " "are you?"
print('Concatening :',v)

# If we want to concatenate strings in different lines, we can use parentheses.
v = ("How old "
"are you?")
print('Concatening :',v)

a = "a"
b = "b"



""" Escape Sequence """

# He said, "What's there?"

# single quotes
print('He said, "What\'s there?"')

# double quotes
print("He said, \"What's there?\"")

# tripple quotes-single
print('''He said, "What's there?"''') # tripple double quotes does not work

# 
print('\x48-\x45-\x58')

# raw string
print(r"This is \x48-\x45-\x58 representation")



""" FORMATTING """

# default (implicit) order
print("deault > Name is {}, age is {}".format('Mamun', 32))

# positional argument
print("positional > Name is {0}, age is {1}".format('Mamun', 32))

# positional argument
print("positional > Name is {1}, age is {0}".format(32, 'Mamun'))

# keyword argument
print("keyword > Name is {n}, age is {a}".format(n = 'Mamun', a = 32))


# formatting numbers

print('binary of {0} is {0:b}'.format(5)) # int only
print('float of {0} is {0:f}'.format(5)) 
print('Exponent of {0} is {0:e}'.format(5.4554)) # int, float

print('Round {0:.2f}'.format(1/3)) 


# Justify : left-right-center

print('|{0:<10}|{1:^10}|{2:>10}'.format('Hi', 'Hello', 'There'))
print('|{:<10}|{:^10}|{:>10}'.format('Hi', 'Hello', 'There'))


# Old Style

x = 3.4567
print('The value of x is %.2f' %x)



""" String METHODS """

print('Lower :', 'pRogRam'.lower())

print('Upper :', 'pRogRam'.upper())


# SPLIT

# syntax: string.split(separator, maxsplit) 
# return list of string
# separator (optional) : by default whitespace
# maxsplit (optional) : if not provided there is no limit. no of items will be maxsplit + 1

x = 'A long string example'
print('Split no sperator :', x.split()) 
print('Split with whitespace sperator :', x.split(' ')) 
print('Split with a sperator :', x.split('-')) # one item's list

print('Split with maxsplit 2:', x.split(' ', 0)) # max no of item will be 2


# JOIN

# syntax : string.join(iterable_object)
# join works with list, tuple, set, string and dictionary.
# For dictionary keys should be string type and for others, items should be string type.

print('Join list :', '-'.join(['A', 'Seperated', 'string']))
print('Join tuple :', '-'.join(('A', 'Seperated', 'string')))
print('Join string :', '-'.join(('ABC')))
print('Join set :', '-'.join(({'5', '7', '9'})))
print('Join dictionnary :', '-'.join(({'A': 1, 'B': '2', 'C': 3}))) # join keys


# FIND

# syntax : string.find(sub_string, start, end)
# start, end are optionals. If provided, the search will perform in range of [star: end]. Otherwise will search in full string
# returns int. If exist returns the first occureence's substring index. Otherwise -1.

x = 'are you okay?'
print('Find :', x.find('you'))
print('Find in range :',x.find('you', 4, 13)) # will search in 'you okay?'
print('Find in range :',x.find('you', 4, 6)) # will search in 'yo'
print(x.find('me'))


# REPLACE

# syntax : string.replace(old, new, count)
# count is optional. THe number of times old sub-string will replace by new-substring. If count not provided, replace will apple for all old sub-strings
# replace return new string, where original string does not change

x = 'are you sure you are okay?'
print(x.replace('you', 'U'))
print(x.replace('you', 'U', 1))
print(x.replace('You', 'U'))

