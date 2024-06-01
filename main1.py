from functools import partial

def curry(f):
    def curried(*args, **kwargs):
        if len(args) + len(kwargs) >= f.__code__.co_argcount :
            return f(*args, **kwargs)
        if args[0] % 2 != 0:
          return partial(curried, *args, **kwargs)
    return curried

# Example usage
def add(x, y, z):
    return x + y + z

curried_add = curry(add)
print(curried_add(1, 2), (3))  # Outputs: 6
