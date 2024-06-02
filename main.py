from functools import partial
from functools import reduce
from itertools import *
import time

# List comprehention
#  [<expression> for <item> in <iterable> (if <condition>)]
listCom = [x for x in range(-1, 3)]
print (listCom)
# Set comprehention
#  {<expression> for <item> in <iterable> (if <condition>)}
even_numbers_set = {x for x in range(21) if x % 2 == 0}
print(even_numbers_set)
# Dict comprehension
#  {<key_expression>: <value_expression> for <item> in <iterable> (if <condition>)}
squares_dict = {x: x**2 for x in range(10)}
print(squares_dict)

print("------------------------------------------------")
# all(<iterable>) function:the all() function is a built-in function 
#  that returns True if all elements of an iterable are true
#  (or if the iterable is empty), and False otherwise.
my_tuple = (True, False, True)
result = all(my_tuple)
print(result)  # Output: False

def custom_all(iterable):
   for element in iterable:
      if not element:
         return False
   return True

print(custom_all([True, False, True]))

print("------------------------------------------------")
# any(<iterable>) function: returns True if at least one element of an iterable
#  is true (or if the iterable is not empty), and False otherwise
my_set = {False, False, False, True}
result = any(my_set)
print(result)

def my_any(iterable):
   for element in iterable:
      if element:
         return True
   return False

print(my_any([False, False, True, False]))  

print("------------------------------------------------")
# zip(*<iterable>) :takes multiple iterables as arguments 
#  and returns an iterator of tuples where the i-th tuple 
#  contains the i-th element from each of the input iterables. 
#  If the input iterables are of different lengths, the resulting iterator will 
#  have the length of the shortest iterable.
list1 = [1, 2, 3]
list2 = ['a', 'b']
zipped = zip(list1, list2)
print(list(zipped)) 

def custom_zip(*iterables):
   min_length = min(len(iterable) for iterable in iterables)

   for i in range(min_length):
      yield tuple(iterable[i] for iterable in iterables)

list1 = [1, 2, 3]
list2 = ['a', 'b']
zipped = custom_zip(list1, list2)
print(list(zipped))

print("------------------------------------------------")
# zip_longest(*<iterables>, (<fillvalue=None>)): available in the itertools module 
#  and is used to zip together multiple iterables of potentially unequal lengths. 
#  Unlike the built-in zip() function, zip_longest() continues iterating 
#  until the longest iterable is exhausted, filling in missing values 
#  with a specified fill value (default is None).
list1 = [1, 2, 3]
list2 = ['a', 'b']
zipped = zip_longest(list1, list2)
print(list(zipped))

def custom_zip_longest(*iterables, fillvalue=None):
   for i in range(max(len(iterable) for iterable in iterables)):
      yield tuple(iterable[i] if i < len(iterable) 
                              else fillvalue for iterable in iterables)
      
list1 = [1, 2, 3]
list2 = ['a', 'b']
zipped = custom_zip_longest(list1, list2)
print(list(zipped))

print("------------------------------------------------")
# Anonymus function: It is also lambda like in the Haskell
x = [1,2,3,4]
y = [5,6,7]
x1 = x + y
print(list(map(lambda x: x*x, x)))

print("------------------------------------------------")
# -------------------------------------------------
# Curried function
def curry(f):
    def curried(*args, **kwargs):
        if len(args) + len(kwargs) >= f.__code__.co_argcount:
            return f(*args, **kwargs)
        return partial(curried, *args, **kwargs)
    return curried

def multi(x, y, z):
    return x * y * z

curried_add = curry(multi)
print(curried_add(3)(2)(3)) # Output = 18
print(curried_add(3, 2)(3)) # Output = 18 
print(curried_add(3)(2, 3)) # Output = 18 

print("------------------------------------------------")
# Function composition
def f(x):
   return x + 2

def g(x):
   return x * 3

def h(x):
   return f(g(x))

print(h(4)) # Output = 14

print("------------------------------------------------")
# Apply to all: map function the same as map in Haskell
list1 = [1,2,3,4,5]
list2 = [5,6,7]

def multi(x, y):
   return x*y

print(list(map(multi, list1, list2)))

def custom_map(func, *iterables):
  iterators = [iter(it) for it in iterables]
  while True:
    try:
      args = [next(it) for it in iterators]
      yield func(*args)
    except StopIteration:
      return

multi_numbers = list(custom_map(multi, list1, list2))

print(multi_numbers)  # Output: [5, 12, 21]

print("------------------------------------------------")
# Filter: the same as Filter in Haskell
listFilter = [1,2,3,4,5,6,7,8,9,10]

def is_even(x):
   return x % 2 == 0

print(list(filter(is_even, listFilter)))

def custom_filter(func, iterable):
   for item in iterable:
      if func(item):
         yield item

print(list(custom_filter(is_even, listFilter)))  

print("------------------------------------------------")
# Insert left/Insert right: Fold left in Haskell
listFoldLeftRight = [1,2,3,4]

def fold_left(func, inital, lst):
   return reduce (func, lst, inital)

def fold_right(func, initial, lst):
    return reduce (lambda x, y: func(y, x), reversed(lst), initial)

def sumEle (x , y):
   return x + y

def mulEle (x, y):
   return x * y

lst = ["a", "b", "c"]
result = fold_left(lambda acc, x: acc + x, "o", lst)  # Concatenate strings
print(result)
result1 = fold_right(lambda x, acc: x + acc, "o", lst)  # Concatenate strings
print(result1)  # Output: "abc"

result = fold_left(sumEle, 0, listFoldLeftRight)  # Sum of elements
result1 = fold_right(sumEle, 0, listFoldLeftRight)
print(result)  # Output: 10
print(result1) 

# Using custom_reduce which is the break down of the reduce function
#  Reduce it is like fold left in Haskell
def custom_reduce(func, sequence, initial):
    accumulator = initial
    for item in sequence:
        accumulator = func(accumulator, item)
    return accumulator

def fold_left(func, inital, lst):
   return custom_reduce (func, lst, inital)

lst = "abc"
result = fold_left(lambda acc, x: acc + x, "o", lst)  # Concatenate strings
print(result)

print("------------------------------------------------")
# Function as parameter in Python function is treat like other values
#   Assigned to a variable
def foo(a, b):
  return a + b
x = foo
print (x(3, 4))
#   Passed into another function as a parameter
def foo(f, x):
   return f(x)

def pow2(x):
   return x ** 2

print(foo (pow2, 4))
#   Returned as a value
def f(x):
   def g(y):
      return x * y
   return g

expFuncVal = f(3)
print(expFuncVal(4))

print("------------------------------------------------")
# Closure = function + bìding ò iits free vriables
def make_power_function(power):
   def powwer_function(x):
      return x ** power
   return powwer_function

expSquare = make_power_function(2)
expCube = make_power_function(3)

print("Example closure square:", expSquare(4))
print("Example closure cube:", expCube(4))

print("------------------------------------------------")
# Decorator: A decorator in Python is a design pattern that allows you to add 
# new functionality to an existing object without modifying its structure. 
# Decorators are very useful for implementing 
# cross-cutting concerns such as logging, authorization, and caching.
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b

@log_function_call
def multiply(a, b):
    return a * b

result1 = add(3, 5)
result2 = multiply(4, 7)

def timing(func):
   def wrapper(*args, **kwargs):
      start_time = time.time()
      result = func(*args, **kwargs)
      end_time = time.time()
      print(f"Function {func.__name__} took {end_time - start_time} seconds")
      return result
   return wrapper

@timing
def slow_function():
   time.sleep(2)
   return "Finished"














