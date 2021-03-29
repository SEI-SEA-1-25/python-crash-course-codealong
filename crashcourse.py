# single line comments 

# multiline
# comment

'''
bad way to make 
multiline comments
=(
'''

# varaibles are snake_case
my_salutation = 'hello snakes 🐍'

# lets make a function!
# functions start with the def keyword
def greeting(greeting_string):
  # indentation blocks are inside the function
  print(greeting_string)
  print('im in the function scope!')
    # print('im indented wrong')

# greeting(my_salutation)

# ## # ## # ## # ## #
# DATA TYPES

# None = undefined, capitol None 
None # is falsey

# Booleans are capitol
True
False

# boolean operators
# && || !: in js
# and or not: python
# console.log(undefined && true)
# print(None and True)
# console.log(true && false)
# print(True and False)
# print(True and True)

# or like js ||
# print(True or None)

# not is like ! in js
#console.log(!false)
print(not False)

truth = True # this is truthy
untruth = False # this is falsey
none = None # this is falsey

if none:
  print('its true! I dont like spam with my eggs!')
elif untruth or truth:
  # else if -- needs a condition
  print('i wont ever print')
else:
  print('i actually like spam and eggs')

# ## # ## # ## # ## 
# NUMBER DATA TYPES

# integers have no deciaml
int
my_int = 14

# floats
# floats are decimals
float 
my_float = 3.1

# complex numbers
complex
6+9j

# arithimitic works like how you would expect
# addition between ints
print(9 + 14)
# addition between floats
print(9 + 14.1)

print('subtraction', 20 - 10)

# two types of division

# division
print('division', 20 / 3)
# forced integer division
print('forced int division', 20 // 3)

# two types of mutliplacation

# regular
print('reg mult', 3 * 3)

# exponential
print('exponents', 3 ** 3)

# modulo
# gives the remainder of divsion
print('modulus', 6 % 5)

my_num = 5
# no plus plus
# my_num++
my_num += 1
print(my_num)
#  all the plus math ones: +=, -=, *=, /=, //=, **=, %=,
my_num //= 3.7
print(my_num)

complex_addition = 1+2j + 3 + 9j
print('complex math is complex', complex_addition)

# comparision of numbers
# two number is !=
print('!=', 1 != 0)
print('==', 1 == 1)
print('>', 3 > 0)
print('<', 9 < 6)
# >= <= these exist too

# ## # ## # ## # ##
# SCOPE

# make a variable in the global scope
my_global_var = 'im global!'

# one function will update the global var
def update_global():
  # tell python you mean THE GLOBAL ONE
  global my_global_var
  # dynamic typing
  # let myGlobalVar = 55
  my_global_var = 55
  my_scoped_var = 'inside scope'
  print('hello from in the function', my_global_var)

# one will print it out
def print_global():
  print(my_global_var)

# update_global()
# print_global()

# ## # ## # ## ## 
# STRINGS

my_string = 'spam and eggs'

# dir will show us the built in methods
print(dir(my_string))
#  __this_dunder_method_is_private__

# built in type methods
print(my_string.upper())

# formatting strings

s = 'spam'

# doouble qoutes/single qoutes == string
e = "eggs"

# format strings 
print('but i dont like {} with my {}'.format(s, e))

# string format templates use keyword argumanets OR kwargs
template = 'My name is {name} and i do like {food} with my {other_food}'
formatted = template.format(name='Wes', food=s, other_food=e)
print(formatted)

# f strings are like interpolation from javascript
order = f'Ill take the {s} {s} {s} {s} baked beans and {s} and {e}'
print(order)

# string concatenation

s_e = s + ' and ' + e
print(s_e)

print(len(s_e))
# string splicing
print(s_e[-4])
print(s_e[3:8])
print(s_e[:8])
print(s_e[3:])
print(s_e[::2])
print(s_e[::-1])

# ## # ## # ## # ##
# LISTS aka js arrays

# split chars into list
l = list(s_e)
print(l)

# lists us square brackets 
breakfast = ['spam', 34, 'baked beans']

# length of list
print(len(breakfast))

spam_times_5 = ['spam'] * 5
# list concatenation
print(breakfast + spam_times_5)

# make a list from a range of numbers
range_list = list(range(10))
print(range_list)

# ranges work on lists
# this returns a new list -- does not mutate the list
print(breakfast[1:])

# mutate the list with built in methods
range_list.insert(3, 'eggs')
print(range_list)

# looping 
for thing in range_list:
  print(thing)

# chek if something is in a list
if 'spam' in range_list:
  print('spam is in the list')
else:
  print('spam is not in the list')

# iterative looping
# for i in range(len(range_list)):
#   # f is the backticks
#   print(f'index {i} is {range_list[i]}')

for i, item in enumerate(range_list):
  print(f'index {i} is {item} (this is the other one)')

# while loops -- careful bout them infinite loops
index = 0
while index < len(range_list):
  print(range_list[index])
  index += 1

# ## # ## # ## # ##
# DICTS aka objects

# dictionaries 

# NO DOT NOTATION!!!!!

# ALL DATATYPES CAN BE KEYS

# STRINGS MUST BE IN QUOTES AS KEYS LIKE JSON

meal = {
  'spam': 5,
  'baked beans': 1,
  True: 'woa',
  10: 'this is nuts'
}

# grab a value from a dict
print(meal['spam'])

# for food in meal:
  # print(f'my meal has {meal[food]} {food} in it')

# print(dir(meal))

# ## # ## # ## # ##
# INPUT

# input('the user will see this string')

# prompt = '>'

# print('enter your age, user')
# age = input(prompt)
# age = int(age)
# print(f'wow! You actually look like your {age - 5} years old')
