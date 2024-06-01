from functools import partial
from functools import reduce
from itertools import *
import time

# Anonymus function: It is also lambda like in the Haskell
x = [1,2,3,4]
y = [5,6,7]
x1 = x + y
print(list(map(lambda x: x*x, x)))

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
print(curried_add(3)(2)(3))  # Outputs: 6
print(curried_add(3, 2)(3))  # Outputs: 6
print(curried_add(3)(2, 3))  # Outputs: 6

# Function composition
def compose(f, g):
   return lambda x: f(g(x))

def f(x):
   return x + 2

def g(x):
   return x + 3

h = compose(f, g)
print(h(4))

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

# Closure = function + bìding ò iits free vriables
def make_power_function(power):
   def powwer_function(x):
      return x ** power
   return powwer_function

expSquare = make_power_function(2)
expCube = make_power_function(3)

print("Example closure square:", expSquare(4))
print("Example closure cube:", expCube(4))

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














