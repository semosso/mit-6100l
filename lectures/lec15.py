##########
# reading
##########
# finger exercise, p 125: The harmonic sum of an integer, n > 0, can be calculated
# using the formula 1 + 1/2 + ... + 1 / n. Write a recursive function that computes this.
def harmonic_sum(n):
    if n == 1:  # base case, i.e., 1 / n == 1 / 1 == 1
        return n
    return (1 / n) + harmonic_sum(n - 1)


print(harmonic_sum((4)))


## multiplying a*b using a for loop


def mult(a, b):
    total = 0
    for n in range(b):
        total += a
    return total


# print(mult(5,4))


####################################


## a*b using a while loop
def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result


# print(mult_iter(5,4))


## a*b recursive
def mult_recur(a, b):
    if b == 1:
        return a
    else:
        return a + mult_recur(a, b - 1)


# print(mult_recur(5,4))


def mult_recur_verbose(a, b):
    if b == 1:
        print("call with", a, b)
        return a
    else:
        print("call with", a, b)
        calc = mult_recur_verbose(a, b - 1)
        print(f"returning {a}+{calc} for call with {a} and {b}")
        return a + calc


# print(mult_recur_verbose(5,4))


############### YOU TRY IT #################
# Calculate n**p recursively by writing this function
# VAO: my code
def power_recur(n, p):
    if p == 0:
        return 1
    elif p == 1:  # you don't really need the if/elif, either one solves it
        return n
    else:
        return n * power_recur(n, p - 1)


print(power_recur(2, 3))  # prints 8

################################################


## factorial iterative
def factorial_iter(n):
    print(f"this is fact({n})")
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod


# factorial_iter(5)


## factorial recursive
def fact_recur(n):
    print(f"this is fact({n})")
    if n == 1:
        return 1
    else:
        return n * fact_recur(n - 1)


# fact_recur(5)


####################################################
############### ANSWERS TO YOU TRY IT #################
####################################################
# Calculate n**p recursively by writing this function
def power_recur(n, p):
    if p == 0:
        return 1
    elif p == 1:
        return n
    else:
        return n * power_recur(n, p - 1)


# print(power_recur(2,3))   # prints 8


#######################################################
################ AT HOME ##############################
#######################################################
# Q1. Rewrite this to calculate b+b+b... a times
def mult(a, b):
    # your code here
    # VAO: my code
    if a == 1:
        return b
    else:
        return b + mult(a - 1, b)


print(mult(5, 4))

# Q2. If we evaluate mult_recur(3,4), how many times is the
# procedure mult_recur called (including initial call)?
# Hint: add a print inside the function!
# VAO: five - 4, 3, 2, 1, 0


def mult_recur(a, b):
    print("called it")  # VAO: yep, 5 times
    if b == 0:
        return 0
    else:
        return a + mult_recur(a, b - 1)


mult_recur(3, 4)


# Q3. Calculate a+b recursively. Assume the only math operation
# you are allowed to do are adding and subtracting 1
def add(a, b):
    """Uses recursion to calculate a+b as adding
    a to 1, b times."""
    # your code here
    # VAO: my code
    if b == 0:
        return a
    else:
        return 1 + add(a, b - 1)  # got there by drawing it out
        # if only operation is +/- 1, this is it
        # adjusted after answers; I got it right, just the specs were not 100%


print(add(3, 4))  # prints 7


# Q4. Calculate a+b recursively by 1's. Assume the only math operation
# you are allowed to do are adding and subtracting 1
def add_by_ones(a, b):
    """Uses recursion to calculate a+b as adding
    1, a times then adding 1, b times."""
    # your code here
    # VAO: my code
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return add(1, b - 1) + add(a - 1, 1)  # either one -1 works
        # 1 + recur, because both elements are made of 1
        # adjusted after answers; I got it right, just the specs were not 100%


print(add_by_ones(3, 4))  # prints 7


# finger exercise: Implement the functions that meets the specifications below
def recur_power(base, exp):
    """
    base: int or float.
    exp: int >= 0

    Returns base to the power of exp using recursion.
    Hint: Base case is when exp = 0. Otherwise, in the recursive
    case you return base * base^(exp-1).
    """
    # Your code here
    # VAO: my code
    if exp == 0:
        return 1
    else:
        return base * recur_power(base, exp - 1)


# Examples:
print(recur_power(2, 5))  # prints 32


#######################################################
################ ANSWERS TO AT HOME ###################
#######################################################
# Q1. Rewrite this to calculate b+b+b... a times
def mult(a, b):
    total = 0
    for n in range(a):
        total += b
    return total


# print(mult(5,4))


# Q2. If we evaluate mult_recur(3,4), how many times is the
# procedure mult_recur called (including initial call)?
# Hint: add a print inside the function!
def mult_recur(a, b):
    print("inside")  # add this!
    if b == 0:
        return 0
    else:
        return a + mult_recur(a, b - 1)


# mult_recur(3,4)


# Q3. Calculate a+b recursively. Assume the only math operation
# you are allowed to do are adding and subtracting 1
def add(a, b):
    """Uses recursion to calculate a+b as adding
    a to 1, b times."""
    # base case
    if b == 0:
        return a
    else:
        # recursive case
        return 1 + add(a, b - 1)


# print(add(3,4))   # prints 7


# Q4. Calculate a+b recursively by 1's. Assume the only math operation
# you are allowed to do are adding and subtracting 1
def add_by_ones(a, b):
    """Uses recursion to calculate a+b as adding
    1, a times then adding 1, b times."""
    # base case
    if b == 0:
        return a
    if a == 0:
        return b
    else:
        # recursive case
        return add(1, b - 1) + add(a - 1, 1)


# print(add_by_ones(3,4))   # prints 7
