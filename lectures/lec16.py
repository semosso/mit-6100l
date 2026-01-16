###############
## Fibonacci with a dictionary
#################


def fib_recur(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_recur(n - 1) + fib_recur(n - 2)


# print(fib_recur(34))


def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n - 1, d) + fib_efficient(n - 2, d)
        d[n] = ans
        return ans


d = {1: 1, 2: 1}
# print(fib_efficient(34, d))


def score_count(x):
    """Returns all the ways to make a score
    of x by adding 1, 2, and/or 3 together.
    Order doesn't matter."""
    if x == 1:
        return 1  # 1+0
    elif x == 2:
        return 2  # 2+0 or 1+1
    elif x == 3:
        return 3  # 3+0 or 2+1 or 1+1+1
    else:
        # make a score of x-1 then add 1
        # and make a score of x-2 then add 2
        # and make a score of x-3 then add 3
        return score_count(x - 1) + score_count(x - 2) + score_count(x - 3)


print(score_count(4))  # prints 6
print(score_count(6))  # prints 20
print(score_count(13))  # prints 1431


## sum of a list, iterative
def total_iter(L):
    result = 0
    for e in L:
        result += e
    return result


test = [30, 40, 50]
# print(total_iter(test))


## sum of a list, recursive
def total_recur(L):
    if L == []:
        return 0
    else:
        return L[0] + total_recur(L[1:])


test = [30, 40, 50]
# print(total_recur(test))


############### YOU TRY IT ###############
# Modify the code we wrote to return the total length
# of all strings inside L:
# VAO: my code


def total_len_recur(L):
    if len(L) == 1:
        return len(L[0])  # VAO: I had return 1, caught it in time
    else:
        return len(L[0]) + total_len_recur(L[1:])


test = ["ab", "c", "defgh"]
print(total_len_recur(test))  # should print 8

##########################################


## is an element in a list?
## incorrect
def in_list(L, e):
    if len(L) == 1:
        return L[0] == e
    else:
        return in_list(L[1:], e)


test = [2, 5, 8, 1]
# print(in_list(test, 0))  # good

test = [2, 5, 8, 1]
# print(in_list(test, 1))  # good

test = [2, 1, 5, 8]
# print(in_list(test, 1))  # bad!


## is an element in the list
## correct (look at the first elem in the list)
def in_list(L, e):
    if len(L) == 1:
        return L[0] == e
    else:
        if L[0] == e:  # VAO: why do you need the base case above?
            # it just checks if it is a one element list
            return True
        else:
            return in_list(L[1:], e)


test = [2, 1, 5, 8]
print(in_list(test, 1))  # bad!


## another correct (look at the last elem in the list)
def in_list(L, e):
    if len(L) == 1:
        return L[0] == e
    else:
        if L[-1] == e:
            return True
        else:
            return in_list(L[:-1], e)


## another correct and simplified implementation
def in_list(L, e):
    if len(L) == 0:
        return False
    elif L[0] == e:
        return True
    else:
        return in_list(L[1:], e)


test = [2, 5, 8, 1]
# print(in_list(test, 1))

test = [1, 2, 5, 8]
# print(in_list(test, 1))

test = [2, 5, 8]
# print(in_list(test, 1))


## flatten a list containing sublists of ints
def flatten(L):
    """
    L is a list containing lists with integer elements
    Returns a list containing elements that are the
    integers in the sublists of L in the same order.
    """
    if len(L) == 1:
        return L[0]
    else:
        return L[0] + flatten(L[1:])  # concatenation, adds elements into same list


test = [[1]]
# print(flatten(test))

test = [[1, 2], [3, 4], [9, 8, 7]]
print(flatten(test))


################### YOU TRY IT ##############
def in_lists_of_list(L, e):
    """
    L is a list whose elements are lists containing ints
    Returns True if e is an element within the lists of L
    and False otherwise.
    Hint, the in operator is useful here, i.e. e in something
    """
    # your code here
    # VAO: my code
    if len(L) == 1:
        return e in L[0]  # L[0], not L, because it's still a list of lists
    elif e in L[-1]:
        return True
    else:
        return in_lists_of_list(L[:-1], e)


test = [[1, 2], [3, 4], [5, 6, 7]]
print(in_lists_of_list(test, 3))  # prints True

test = [[1, 2], [3, 4], [5, 6, 7]]
print(in_lists_of_list(test, 0))  # prints False

###############################################


## reverse a list's elements
def my_rev(L):
    if len(L) == 1:
        return L
    else:
        return my_rev(L[1:]) + [L[0]]


# test = [1, 2, "abc"]
# print(my_rev(test))

# test = ["abc", ['d'], ['e', ['f', 'g']]]
# print(my_rev(test))


## reverse a list's elements (and its list elems, etc, recursively)
def deep_rev(L):
    if len(L) == 1:
        if type(L[0]) != list:
            return L
        else:
            return [deep_rev(L[0])]
    else:
        if type(L[0]) != list:
            return deep_rev(L[1:]) + [L[0]]
        else:
            return deep_rev(L[1:]) + [deep_rev(L[0])]


# test = [1, 2, "abc"]
# print(my_rev(test))

# test = ["abc", ['d'], ['e', ['f', 'g']]]
# print(deep_rev(test))


## cleaned up code to reverse a list's elements (and its list elems, etc, recursively)
def deep_rev(L):
    if L == []:
        return L
    elif type(L[0]) != list:
        return deep_rev(L[1:]) + [L[0]]
    else:
        return deep_rev(L[1:]) + [deep_rev(L[0])]


# test = [1, 2, "abc"]
# print(my_rev(test))

# test = ["abc", ['d'], ['e', ['f', 'g']]]
# print(deep_rev(test))


## EXTRA CONTENT: towers of hanoi
def print_move(fr, to):
    print("move from " + str(fr) + " to " + str(to))


def towers(n, fr, to, spare):
    if n == 1:
        print_move(fr, to)
    else:
        towers(n - 1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n - 1, spare, to, fr)


# towers(4, 'a', 'b', 'c')


###########################################
########## ANSWERS TO YOU TRY IT #############
###########################################


def total_len_recur(L):
    """Returns the total length of all strings inside L"""
    if len(L) == 1:
        return len(L[0])
    else:
        return len(L[0]) + total_len_recur(L[1:])


# test = ["ab", "c", "defgh"]
# print(total_len_recur(test))  # should print 8


def in_lists_of_list(L, e):
    """
    L is a list whose elements are lists containing ints
    Returns True if e is an element within sublists of L
    and False otherwise.
    """
    if len(L) == 1:
        return e in L[0]
    else:
        if e in L[0]:
            return True
        else:
            return in_lists_of_list(L[1:], e)


# test = [[1,2], [3,4], [5,6,7]]
# print(in_lists_of_list(test, 3))  # prints True

# test = [[1,2], [3,4], [5,6,7]]
# print(in_lists_of_list(test, 0))  # prints False


######################################################
################### AT HOME ##############
######################################################
# Q1. Memoize the code to find possible scores in basketball
def score_count(x, d):
    if x in d:  # VAO: all the base cases are moved to the dict
        return d[x]
    else:
        # VAO: do the calculations w/o returning anything
        answer = score_count(x - 1, d) + score_count(x - 2, d) + score_count(x - 3, d)
        d[x] = answer
        return answer


d = {1: 1, 2: 2, 3: 3}
print(score_count(4, d))  # prints 6
print(score_count(6, d))  # prints 20
print(score_count(13, d))  # prints 1431


# Q2.
def in_list_of_lists_mod(L, e):
    """
    L is a list whose elements are either
        * lists containing ints or
        * ints
    Returns True if e is an element within L or
    sublists of L and False otherwise.
    """
    # your code here
    # VAO: my code
    if len(L) == 1 and type(L[0]) is not list:
        return e == L[0]
    elif len(L) == 1 and type(L[10]) is list:
        return e in L
    elif type(L[0]) is list:
        if e in L[0]:
            return True
        else:
            return in_list_of_lists_mod(L[1:], e)
    elif type(L[0]) is not list:
        if e == L[0]:
            return True
        else:
            return in_list_of_lists_mod(L[1:], e)


test = [[1, 2], 3, 4, 5, 6, 7]
print(in_list_of_lists_mod(test, 3))  # prints True
test = [[1, 2], [3, 4, 5], 6, 7]
print(in_list_of_lists_mod(test, 3))  # prints True
test = [[1, 2], [3, 4, 5], 6, 7]
print(in_list_of_lists_mod(test, 10))  # prints False


# Q3.
def my_deepcopy(L):
    """
    L is a list, containing lists or list of lists, etc.
    Returns a new list with the same structure as L that
    contains copies (recursively) of every sublist
    """
    # your code here
    # VAO: my code; totally wrong, couldn't make it work
    if type(L[0]) is not list:
        return [L[0]] + my_deepcopy(L[1:])  # L[0] kept as list element
    else:
        return [my_deepcopy(L[0])] + my_deepcopy(
            L[1:]
        )  # since L[0] is a list, you run it through again to dive into deeper levels,
    # returning it as list elements back again (hence the [])


myL = ["abc", ["d"], ["e", ["f", "g"]]]
my_newL = my_deepcopy(myL)
print(myL)
print(my_newL)
# myL[2][1][0] = 1
# print(myL)      # should be ['abc', ['d'], ['e', [1, 'g']]]
# print(my_newL)  # should be ['abc', ['d'], ['e', ['f', 'g']]]


# Q4. Here are 3 recursive functions that are incorrectly implemented.
# Debug them to have them do what the specs say.
def f(L):
    """L is a non-empty list of lowercase letters.
    Returns the letter earliest in the alphabet."""
    if len(L) == 1:
        return L[0]
    # else:
    #     if L[0] < f((L[0])):
    #         return L[0]
    # VAO: my code, I changed it quite a bit, but works fine
    elif L[0] < L[-1]:
        return f(L[:-1])
    else:
        return f(L[1:])


print(f(["z", "a", "b", "c", "d"]))  # should print 'a'


def g(L, e):
    """L is list of ints, e is an int
    Returns a count of how many times e occurrs in L"""
    # VAO: these are the base cases, no change
    if len(L) == 0:
        return 0
    elif len(L) == 1:
        if e == L[0]:
            return 1
        else:
            return 0
    # VAO: now for the recursive part
    else:
        if L[0] == e:
            return 1 + g(L[1:], e)  # VAO: missing a return
        else:
            return g(L[1:], e)


print(g([1, 2, 3, 1], 1))  # should print 2
print(g([1, 1, 2, 3, 1, 1], 1))  # should print 4


def h(L, e):
    """L is list, e is an int
    Returns a count of how many times e occurrs in L or
    (recursively) any sublist of L
    """
    if len(L) == 0:
        return 0
    else:
        if type(L[0]) is int:
            if L[0] == e:
                return 1 + h(L[1:], e)
            else:
                return h(L[1:], e)
        elif type(L[0]) is list:
            if e in L[0]:
                return h(L[0], e) + h(
                    L[1:], e
                )  # you need the first element to call the list again
            # it might be a list of lists, with additional target elements
            # same as my_deepcopy(), deep_rev() and others
            else:
                return h(L[1:], e)


print(h([1, 2, [3], 1], 1))  # should print 2
print(h([1, 2, [3, 1, [1, [1]]]], 1))  # should print 4


# finger exercise: Implement the functions that meets the specifications below
def flatten(L):
    """
    L: a list
    Returns a copy of L, which is a flattened version of L
    """
    # Your code here
    # VAO: my code; can't figure out how to take the [3] out of nested list
    # nor can I understand why it's there
    if len(L) == 1:
        return L
    else:
        if type(L[0]) is not list:
            return [L[0]] + flatten(L[1:])  # I guess the issue is here?
        elif type(L[0]) is list:
            return flatten(L[0]) + flatten(L[1:])


# VAO: the solution uses .append() and .extend(), which is fine, but now how
# the classes have been tought, were we were expected to not use them

# Examples:
L = [[1, 4, [6], 2], [[[3]], 2], 4, 5]
print(flatten(L))  # prints the list [1,4,6,2,3,2,4,5]


#####################################################


####################################################################
############## ANSWERS TO AT HOME #######################
####################################################################
# Q1. Memoize the code to find possible scores in basketball
def score_count(x, d):
    if x in d:
        return d[x]
    else:
        score = score_count(x - 1, d) + score_count(x - 2, d) + score_count(x - 3, d)
        d[x] = score
        return score


# d = {1:1, 2:2, 3:3}
# print(score_count(4, d))  # prints 6
# print(score_count(6, d))  # prints 20
# print(score_count(13, d))  # prints 1431


# Q2
def in_list_of_lists_mod(L, e):
    """
    L is a list whose elements are either
        * lists containing ints or
        * ints
    Returns True if e is an element within L or
    sublists of L and False otherwise.
    """
    if len(L) == 1 and type(L[0]) != list:
        return e == L[0]
    elif len(L) == 1 and type(L[0]) == list:
        return e in L[0]
    elif type(L[0]) != list:
        if e == L[0]:
            return True
        else:
            return in_list_of_lists_mod(L[1:], e)
    elif type(L[0]) == list:
        if e in L[0]:
            return True
        else:
            return in_list_of_lists_mod(L[1:], e)


# test = [[1,2],3,4,5,6,7]
# print(in_list_of_lists_mod(test, 3))  # prints True
# test = [[1,2],[3,4,5],6,7]
# print(in_list_of_lists_mod(test, 3))  # prints True
# test = [[1,2],[3,4,5],6,7]
# print(in_list_of_lists_mod(test, 10))  # prints False


# Q3
def my_deepcopy(L):
    """
    Implements a recursive version of copy.deepcopy().
    L is a list, containing lists or list of lists, etc.
    Returns a new list with the same structure as L that
    contains copies (recursively) of every sublist
    """
    pass
    if len(L) == 0:
        return []
    elif type(L[0]) != list:
        return [L[0]] + my_deepcopy(L[1:])
    else:
        return [my_deepcopy(L[0])] + my_deepcopy(L[1:])


# myL = ["abc", ['d'], ['e', ['f', 'g']]]
# my_newL = my_deepcopy(myL)
# print(myL)
# print(my_newL)
# myL[2][1][0] = 1
# print(myL)      # should be ['abc', ['d'], ['e', [1, 'g']]]
# print(my_newL)  # should be ['abc', ['d'], ['e', ['f', 'g']]]


# Q4
def f(L):
    """L is a non-empty list of lowercase letters.
    Returns the letter earliest in the alphabet."""
    if len(L) == 1:
        return L[0]
    else:
        if L[0] < f((L[1:])):
            return L[0]
        else:
            return f(L[1:])


# print(f(['z', 'a', 'b', 'c', 'd']))  # should print 'a'


def g(L, e):
    """L is list of ints, e is an int
    Returns a count of how many times e occurrs in L"""
    if len(L) == 0:
        return 0
    elif len(L) == 1:
        if e == L[0]:
            return 1
        else:
            return 0
    else:
        if L[0] == e:
            return 1 + g(L[1:], e)
        else:
            return g(L[1:], e)


# print(g([1,2,3,1], 1))     # should print 2
# print(g([1,1,2,3,1,1], 1)) # should print 4


def h(L, e):
    """L is list, e is an int
    Returns a count of how many times e occurrs in L or
    (recursively) any sublist of L
    """
    if len(L) == 0:
        return 0
    else:
        if type(L[0]) == int:
            if L[0] == e:
                return 1 + h(L[1:], e)
            else:
                return h(L[1:], e)
        elif type(L[0]) == list:
            if e in L[0]:
                return h(L[0], e) + h(L[1:], e)
            else:
                return h(L[1:], e)


# print(h([1,2,[3],1], 1))        # should print 2
# print(h([1,2,[3,1,[1,[1]]]], 1))  # should print 4
