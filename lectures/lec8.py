# #########################
# ## reading
# #########################
# finger exercise, p 85: Write a lambda expression that has two numeric parameters. If the
# second argument equals zero, it should return `None`. Otherwise it should return the value of
# dividing the first argument by the second argument. Hint: use a conditional expression.
# VAO: my code here
x = 4
y = 2
print(
    (lambda x, y: None if y == 0 else x / y)(x, y)
)  # this works, but I had a HARD TIME figuring out the exact structure
# including the lambda arguments in () at the end of the lambda function
# including () around lambda itself
# most of the time I was getting the object type (function) being printed; thanks, chatGPT

# finger exercise, p 87: What does s.find(sub) return if `sub` does not occur in `s`?  (s = "abcbc")
s = "abcbc"
print(
    s.find("sasksks")
)  # returns -1, why is that? it's a design choice, looked up documentation
s.find("abc")


# # finger exercise, p 87: Use 'find' to implement a function satisfying the specification
def find_last(s, sub):
    """s and sub are non empty strings
    Returns the index of the last occurence of sub in s
    Returns None if sub does not occur in s"""
    # inv_sub = sub[::-1] # don´t need this anymore, just went straight up with a loop
    # a lot is going on here; I tried asking find() to go from end to start, but it doesn´t work for >1 letter strings
    # so inverting both the string and the target string made sense to start from the end
    # result = s[::-1].find(inv_sub)
    # result = s.find(inv_sub, len(s) - 1, 0) # doesn´t work because it can´t go backwards, there's no -1 step
    result = -1
    counter = 0
    while counter <= len(s) - 1:
        if s.find(sub, counter) != -1:
            result = counter
        counter += 1  # this works, but feels bad; maybe improve with a for(), or figure out a better way to pass on counter to return
    if result == -1:
        return None
    else:
        return result  # because of the inversion, you get the index w/r/t the inverted string, so this fixes for the original one
        # VAO: this doesn´t work either; it matches the first index of the match,
        # which in multi letter strings will be the last, not the first


s = "abcdefdefeddedefefabc"
sub = "abc"
print(find_last(s, sub), len(s))


# #########################
# ## EXAMPLE: combinations of print and return
# #########################
# def is_even_with_return(i):
#     """
#     Input: i, a positive int
#     Returns True if i is even, otherwise False
#     """
#     print("with return")
#     remainder = i % 2
#     return remainder == 0


# # is_even_with_return(3)          # -> False
# # print(is_even_with_return(3))  # -> print(False)


# def is_even_without_return(i):
#     """
#     Input: i, a positive int
#     Returns None
#     """
#     print("without return")
#     remainder = i % 2
#     has_rem = remainder == 0
#     print(has_rem) # VAO: could be print(remainder == 0), same thing
#     ##return None


# # is_even_without_return(3)          # -> None
# # print(is_even_without_return(3))  # -> print(None)


# ############### YOU TRY IT #######################
# # What does this print to the console?
# # Think first, then run it.
# def add(x, y):
#     return x + y


# def mult(x, y):
#     print(x * y)

# VAO: answers
# # add(1,2) # nothing is printed
# # print(add(2,3)) # 5
# # mult(3,4) # 12
# # print(mult(4,5)) # 20, None

# ##################################################
#


# ############ YOU TRY IT ####################
# # Fix this buggy code so it works according to the specification:
def is_triangular(n):
    """n is an int > 0
    Returns True if n is triangular, i.e. equals a continued
    summation of natural numbers (1+2+3+...+k)
    """
    total = 0
    #     for i in range(n):
    #         total += i
    #         if total == n:
    #             print(True)
    #     print(False)
    # VAO: my answer
    for i in range(n + 1):  # fixing range to cover 1
        total += i
        if total == n:
            return True  # return and not print; remember that whenever return is hit, it breaks
    return False  # remember that whenever return is hit, it breaks


# # # start by runing it on simple test cases
# # print(is_triangular(4))  # print False
# # print(is_triangular(6))  # print True
# # print(is_triangular(1))  # print True

# ##############################################


# #########################
# ### EXAMPLE: bisection square root as a function
# #########################
def bisection_root(x, y):
    epsilon = y
    low = 0
    high = x
    ans = (high + low) / 2.0
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    #    print(ans, 'is close to the root of', x)
    return ans


# print(bisection_root(4, 0.01))
# print(bisection_root(123, 0.01))


###################### YOU TRY IT ######################
def count_nums_with_sqrt_close_to(n, epsilon):
    """n is an int > 2
        epsilon is a positive number < 1
    Returns how many integers have a square root within epsilon of n"""
    # your code here
    # VAO: my code here
    # two ways of going about this
    # (n-e)^ and (n+e)^2 are the boundaries
    lower = (n - epsilon) ** 2
    higher = (n + epsilon) ** 2
    # I can just add the integers between these boundaries to the power of 2?
    count = 0
    for i in range(
        int(lower), int(higher)
    ):  # maybe this is why alternative 2 should be preferred, because this truncates the result?
        count += 1
    return count
    # alternatively
    count = 0
    # use bisection to find sqrt of all numbers from 1 to n^3 (exaggeration)
    for i in range(
        1, n**3
    ):  # alternatively, flag when counter is no longer being reached after the first increment, then break
        root = bisection_root(i, epsilon)
        # filter out those that are outside the range
        if (
            root >= n - epsilon and root <= n + epsilon
        ):  # alternatively, if abs(n - sqrt) < epsilon; same as in algo for search and approximation
            count += 1
    return count


print(
    count_nums_with_sqrt_close_to(10, 0.1)
)  # both alternatives above evaluate to 4; TBH, I think #1 is more straightforward

# #############################################################


# #########################
# ## Scope example: paste this into the Python Tutor
# ########################
# def f(x):
#     x = x + 1
#     print("in f(x): x =", x)
#     return x


# # x = 3
# # z = f( x )


# ###########################
# #### EXAMPLE: shows accessing variables outside scope
# ###########################
# def f(y):
#     x = 1
#     x += 1
#     print(x)


# # # x = 5
# # # f(x)
# # # print(x)


# def g(y):
#     print(x)
#     print(x + 1)


# # # x = 5
# # # g(x)
# # # print(x)


# def h(y):
#     x += 1  # leads to an error without line `global x` inside h


# # # x = 5
# # # h(x)
# # # print(x)


# #############
# ## EXAMPLE: functions as parameters
# ## Run it in the Python Tutor if something doesn't make sense
# ############
# def calc(op, x, y):
#     return op(x, y)


# def add(a, b):
#     return a + b


# def sub(a, b):
#     return a - b


# def mult(a, b):
#     return a * b


# def div(a, b):
#     if b != 0:
#         return a / b
#     print("Denominator was 0.")


# # print(calc(add, 2, 3))
# # print(calc(div, 2, 0))


# ## trace the scope progression of this code
# def func_a():
#     print("inside func_a")


# def func_b(y):
#     print("inside func_b")
#     return y


# def func_c(f, z):
#     print("inside func_c")
#     return f(z)


# # print(func_a())
# # print(5 + func_b(2))
# # print(func_c(func_b, 3))


# ############## YOU TRY IT ###############
def apply(criteria, n):
    """criteria is a function that takes in a number and returns a Boolean
        n is an int
    Returns how many ints from 0 to n (inclusive) match the criteria
    (i.e. return True when criteria is applied to them)
    """
    # your code here
    count = 0
    for num in range(n + 1):
        if criteria(num):
            count += 1
    return count


def is_even(x):
    return x % 2 == 0


how_many = apply(is_even, 10)
print(how_many)


# ############## YOU TRY IT ###############
# # Write a function that takes in an int and two functions as
# # parameters (each takes in an int and returns a float).
# # It applies both functions to numbers between 0 and n (inclusive)
# # and returns the maximum value of all outcomes.


# def max_of_both(n, f1, f2):
#     """n is an int
#         f1 and f2 are functions that take in an int and return a float
#     Applies f1 and f2 on all numbers between 0 and n (inclusive).
#     Returns the maximum value of all these results.
#     """
#     # your code here


# # print(max_of_both(2, lambda x:x-1, lambda x:x+1))  # prints 3
# # print(max_of_both(10, lambda x:x*2, lambda x:x/2))  # prints 20


# ################################


# ###################################
# ############# ANSWERS TO YOU TRY IT #######################
# ###################################


# def how_many_sqrt_close_to(n, epsilon):
#     """n is an int > 0
#         epsilon is a number
#     Returns how many integers have a square root within epsilon of n"""
#     count = 0
#     for i in range(n**3):
#         if n - epsilon < bisection_root(i) < n + epsilon:
#             count += 1
#     return count


# # print(how_many_sqrt_close_to(10, 0.1))


# def apply(criteria, n):
#     """criteria is a function that takes in a number and returns a Boolean
#         n is an int
#     Returns how many ints from 0 to n (inclusive) match the criteria
#     (i.e. return True when criteria is applied to them)
#     """
#     pass
#     count = 0
#     for i in range(0, n + 1):
#         if criteria(i):
#             count += 1
#     return count


# def is_even(x):
#     return x % 2 == 0


# # what = apply(is_even,10)
# # print(what)

# # print(apply(lambda x: x==5, 100))


# ###################################
# ############# AT HOME #######################
# ###################################


# def is_palindrome(s):
#     """s is a string
#     Returns True if s is a palnidrome and False otherwise.
#     A palindrome is a string that contains the same
#     sequence of characters forward and backward"""
#     # your code here


# # For example:
# # print(is_palindrome("222"))   # prints True
# # print(is_palindrome("2222"))   # prints True
# # print(is_palindrome("abc"))   # prints False


# def f_yields_palindrome(n, f):
#     """n is a positive int
#         f is a function that takes in an int and returns an int
#     Returns True if applying f on n returns a number that is a
#     palindrome and False otherwise."""
#     # your code here


# # For example:
# def f(x):
#     return x + 1


# def g(x):
#     return x * 2


# def h(x):
#     return x // 2


# # print(f_yields_palindrome(2, f))   # prints True
# # print(f_yields_palindrome(76, f))   # prints True
# # print(f_yields_palindrome(11, g))   # prints True
# # print(f_yields_palindrome(123, h))   # prints False

# ###################################
# ##################################
# ###################################


# ###################################
# ############# ANSWERS TO AT HOME ##################
# ###################################
# def is_palindrome(s):
#     """s is a string
#     Returns True if s is a palindrome and False otherwise.
#     A palindrome is a string that contains the same
#     sequence of characters forward and backward"""
#     # your code here
#     for i in range(len(s)):
#         if s[i] != s[len(s) - i - 1]:
#             # returning here essentially breaks the loop
#             # as soon as we find an inconsistency
#             return False
#     return True


# # For example:
# # print(is_palindrome("222"))   # prints True
# # print(is_palindrome("2222"))   # prints True
# # print(is_palindrome("abc"))   # prints False


# def f_yields_palindrome(n, f):
#     """n is a positive int
#         f is a function that takes in an int and returns an int
#     Returns True if applying f on n returns a number that is a
#     palindrome and False otherwise."""
#     # your code here
#     f_on_n = f(n)
#     return is_palindrome(str(f_on_n))


# # For example:
# def f(x):
#     return x + 1


# def g(x):
#     return x * 2


# def h(x):
#     return x // 2


# # print(f_yields_palindrome(2, f))   # prints True
# # print(f_yields_palindrome(76, f))   # prints True
# # print(f_yields_palindrome(11, g))   # prints True
# # print(f_yields_palindrome(123, h))   # prints False


# ###################################
# ##################################
# ###################################
