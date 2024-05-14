#decorators-1.py
# Decorators, as simple as it gets :)

# Decorators are functions that compliment other functions,
# or in other words, modify a function or method.

# In the example below, we have a function named `decorated`.
# This function just prints "This happened".
# We have a decorator created named `inner_decorator()`.
# This decorator function has an function within, which
# does some operations (print stuff for simplicity) and then
# returns the return-value of the internal function.

# How does it work?
# a) The function `decorated()` gets called.
# b) Since the decorator `@my_decorator` is defined above
# `decorated()`, `my_decorator()` gets called.
# c) my_decorator() takes a function name as args, and hence `decorated()`
# gets passed as the arg.
# d) `my_decorator()` does it's job, and when it reaches `myfunction()`
# calls the actual function, ie.. decorated()
# e) Once the function `decorated()` is done, it gets back to `my_decorator()`.
# f) Hence, using a decorator can drastically change the behavior of the
# function you're actually executing.


def my_decorator(my_function):  # <-- (4)
    def inner_decorator():  # <-- (5)
        print("This happened before!")  # <-- (6)
        my_function()  # <-- (7)
        print("This happens after ")  # <-- (10)
        print("This happened at the end!")  # <-- (11)

    return inner_decorator
    # return None


@my_decorator  # <-- (3)
def decorated():  # <-- (2) <-- (8)
    print("This happened!")  # <-- (9)


if __name__ == "__main__":
    decorated()  # <-- (1)


'''
O/P-
This happened before!
This happened!
This happens after 
This happened at the end!
'''