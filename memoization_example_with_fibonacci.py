import functools


# help(functools)

# functools.lru_cache(maxsize=128, typed=False)
#
#
# def fib(num):
#     if num < 2:
#         return num
#     else:
#         print(fib(num - 1) + fib(num - 2))
#         return fib(num - 1) + fib(num - 2)
#
# functools.cached_property(fib(4))

# def doSomeExpensiveCalculation(self, input):
#     if input not in self.cache:
#         return fib(num-1) + fib(num-2) # Do expensive calculation
#         #self.cache[input] = result
#     return self.cache[input]
#
# doSomeExpensiveCalculation(1,6)


# def factorial(n, _cache={1: 1}):
#     try:
#         return _cache[n]
#     except IndexError:
#         _cache[n] = factorial(n - 1) * n
#         return _cache[n]
#
#
# factorial(5)



def memoize(obj):
    cache = obj.cache = {}

    @ functools.wraps(obj)
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = obj(*args, **kwargs)
        return cache[key]

    return memoizer

memoize(5)