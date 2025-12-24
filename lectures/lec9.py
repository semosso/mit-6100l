# #########################
# ## reading
# #########################
# testing a function
def find_extreme_divisors(n1, n2):
    """Assumes that n1 and n2 are positive ints
    Returns a tuple containing the smallest common divisor > 1 and
    the largest common divisor of n1 & n2. If no common divisor other
    than 1, returns (None, None)"""
    min_val, max_val = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            if min_val is None:
                min_val = i
            max_val = i
    return min_val, max_val


# min_divisor, max_divisor = find_extreme_divisors(100, 200)
# VAO: yep, I was right, book says will print (2, 200), but it's (2, 100)
print(find_extreme_divisors(100, 200))


# finger exercise, p 93: Write an expression that evaluates to the mean of a tuple of
# numbers. Use the function sum.
# VAO: my code
def mean_tuple(t):
    """t is a tuple of numbers
    Returns, as a float, the mean of the numbers in the tuple"""
    return sum(t) / len(t)


t1 = (1, 2, 3, 4, 5)
print(mean_tuple(t1))

# finger exercise, p 105: Write a list comprehension that generates all non-primes
# between 2 and 100.
# VAO: my code
[x for x in range(2, 101) if any(x % y == 0 for y in range(2, x))]


# #########################
# ## lecture
# #########################
def apply(criteria, n):
    """criteria is a function that takes in a number and returns a Boolean
        n is an int
    Returns how many ints from 0 to n (inclusive) match the criteria
    (i.e. return True when criteria is applied to them)
    """
    count = 0
    for i in range(0, n + 1):
        if criteria(i):
            count += 1
    return count


def is_even(x):
    return x % 2 == 0


def is_5(x):
    return x == 5


# print('apply with is_5:',apply(is_5,10))
# print('apply with anon fcn:', apply(lambda x: x==5, 100))


# Shown another way, the following are equivalent:
# is_even(8)              # returns True
# (lambda x: x%2==0)(8)   # returns True


# 1. What does this print?
# print(apply(lambda x: x%2==0, 10))

# 2. Call apply on n=100 and a lambda func
#    that takes in a parameter and returns
#    whether the parameter is a multiple of 10
#    What does it print?
# your code here


def do_twice(n, fn):
    return fn(fn(n))


# print(do_twice(3, lambda x: x**2))


###################
### example with returning a tuple with many values
###################
def quotient_and_remainder(x, y):
    q = x // y
    r = x % y
    return (q, r)


# result = quotient_and_remainder(10,3)
# print(result)

# (quot, rem) = quotient_and_remainder(5,2)
# print('quotient is:', quot)
# print('remainder is:', rem)


############### YOU TRY IT #####################
# Write a function that meets these specifications:
def char_counts(s):
    """s is a string of lowercase chars
    Returns a tuple where the first value is the
    number of vowels in s and the second value
    is the number of consonants in s
    """
    # your code here
    # VAO: my code
    vowels, cons = 0, 0
    for c in s:
        if c in "aeiou":
            vowels += 1
        else:
            cons += 1
    return (vowels, cons)  # don't need to return a tuple for it to become a tuple


print(char_counts("abcd"))  # prints (1,3)
print(char_counts("zcght"))  # prints (0,5)

##################################################


###################
### example of variable number of arguments
###################
def mean(*args):
    """
    Assumes at least one argument and all arguments are numbers.
    Returns the mean of the arguments.
    """
    tot = 0
    for a in args:
        tot += a
    return tot / len(args)


# print(mean(1,2,3,4,5,6))
# print(mean(6,0,9))


## Compare above code with this one:
# Note args vs *args and mean((6,0,9)) vs mean(6,0,9)
def mean(args):
    tot = 0
    for a in args:
        tot += a
    return tot / len(args)


# print(mean((1,2,3,4,5,6)))
# print(mean((6,0,9)))


##################
## EXAMPLE: sum element values in a list
##################
def list_sum(L):
    total = 0
    for e in L:
        total += e
    return total


# print(list_sum([1,3,5]))


###################
## EXAMPLE: sum lengths of string elements
####################
def len_sum(L):
    total = 0
    for s in L:
        total += len(s)
    return total


# print(len_sum(['ab', 'def', 'g']))


#################################################


################## YOU TRY IT ###################
def sum_and_prod(L):
    """L is a list of numbers
    Return a tuple where the first value is the
    sum of all elements in L and the second value
    is the product of all elements in L
    """
    # your code here
    # VAO: my code
    sm, prod = (
        0,
        1,
    )  # doens't interfere with the end result at all. Adapting: sm, prod = L[0], L[0]
    for num in L:  # adaptation: for i in range(1, len(L))
        sm += num  # adaptation: sm += L[i]
        prod *= num
    return (sm, prod)


print(sum_and_prod([4, 6, 2, 5]))  # prints (17, 240)


#############################################
################## ANSWERS TO YOU TRY IT ####################
#############################################
def char_counts(s):
    """s is a string of lowercase chars
    Returns a tuple where the first value is the
    number of vowels in s and the second value
    is the number of consonants in s
    """
    vowels, cons = 0, 0
    for i in s:
        if i in "aeiou":
            vowels += 1
        else:
            cons += 1
    return (vowels, cons)


# print(char_counts("abcd"))  # prints (1,3)
# print(char_counts("zcght"))  # prints (0,5)


def sum_and_prod(L):
    """L is a list of numbers
    Return a tuple where the first value is the
    sum of all elements in L and the second value
    is the product of all elements in L
    """
    s, p = 0, 1

    for i in L:
        s += i
        p *= i
    return (s, p)


# print(sum_and_prod([1,2,3,4]))   # prints (10, 24)
# print(sum_and_prod([12,6,2,7]))   # prints (27, 1008)


#############################################
################## AT HOME ####################
#############################################


# Trace this code:
# Figure out what it returns and then run it to check yourself.
def always_sunny(t1, t2):
    """t1, t2 are non-empty"""
    sun = ("sunny", "sun")
    first = t1[0] + t2[0]
    return (sun[0], first)


always_sunny(("cloudy"), ("cold",))  # returns what?
# VAO: note that "cloudy" is not a tuple, no comma inside the (); "cold" is a tuple; the outer () are from the function call
# VAO: so t1[0] is the first index of the "cloudy" string
# VAO: if there was a comma after "cloudy", then it becomes a tuple itself, and passes on "cloudy" as t1


def max_of_both(n, f1, f2):
    """n is an int
        f1 and f2 are functions that take in an int and return a float
    Applies f1 and f2 on all numbers between 0 and n (inclusive).
    """
    # your code here
    # VAO: exact same as last time around. But missing the return specification,
    # which should be the max result of all
    max = f1(n)
    for num in range(n + 1):
        if f1(num) > max:
            max = f1(num)
        if f2(num) > max:
            max = f2(num)
    return max


print(max_of_both(2, lambda x: x - 1, lambda x: x + 1))  # prints 3
print(max_of_both(10, lambda x: x * 2, lambda x: x / 2))  # prints 20


def sublist_sum(L):
    """L is a list whose elements are lists with int elements
    Returns the sum of all int elements."""
    # your code here
    # VAO: my code
    sum_all = 0
    for e in L:
        for (
            e1
        ) in (
            e
        ):  # this looks so brute force and not scalable; e.g., what if there's another sublevel?
            # answer below suggests this + a for e in L, sum(e), which is also not scalable
            sum_all += e1
    return sum_all


print(sublist_sum([[1, 2], [4, 5, 6]]))  # prints 18


#############################################
################## ANSWERS TO AT HOME ####################
#############################################


def max_of_both(n, f1, f2):
    """n is an int
        f1 and f2 are functions that take in an int and return a float
    Applies f1 and f2 on all numbers between 0 and n (inclusive).
    Returns the maximum value of all these results.
    """
    # your code here
    maxval = f1(0)
    for i in range(n + 1):
        if f1(i) > maxval:
            maxval = f1(i)
        if f2(i) > maxval:
            maxval = f2(i)
    return maxval


# print(max_of_both(2, lambda x:x-1, lambda x:x+1))  # prints 3
# print(max_of_both(10, lambda x:x*2, lambda x:x/2))  # prints 20


def sublist_sum(L):
    """L is a list whose elements are lists with int elements
    Returns the sum of all int elements."""
    ## One way by using the sum function over the sublist
    tot = 0
    for subL in L:
        tot += sum(subL)
    return tot
    ## Alternate way by nesting a for loop that
    ## iterates over the sublist's int elements
    tot = 0
    for subL in L:
        for e in subL:
            tot += e
    return tot


# print(sublist_sum([[1,2], [4,5,6]])) # prints 18
