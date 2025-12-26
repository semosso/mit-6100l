# Problem 1: Lamba Functions Practice
# a) Write a lambda function that calculates the cube root of a given number
# passed in as an argument
# INSERT CODE BELOW HERE
# VAO: my code; duh, took me a long time to do this vs. trying to approximage/gnc
f1 = lambda x: x ** (1 / 3)

# b) Write a lambda function that takes in two arguments and outputs the product
# of those two numbers.
# INSERT CODE BELOW HERE
# VAO: my code
f2 = lambda x, y: x * y


# uncomment to test function
print(f1(8))
print(f1(4))
print(f2(1, 2))
print(f2(4, 5))


#############################################################################
# Problem 2: Practice working with Tuples:
# Write a function that counts the number of times the number 1 appears
# in an inputted tuple.
# INSERT CODE BELOW HERE
# VAO: my code
def count_number_one(t1):
    counter = 0
    for e in t1:
        if e == 1:
            counter += 1
    return counter


# uncomment to test function
print(count_number_one((1, 2, 3, 4, 5, 1, 1)))


#############################################################################
# Problem 3: Practice working with Python Tuples
# Write a Function that takes in two tuples and outputs a single tuple containing
# only common elements of both tuples.
# INSERT CODE BELOW HERE
# VAO: my code
def common_elements(t1, t2):
    t_common = ()
    for e in t1:
        for elem in t2:
            if e == elem:
                t_common += (e,)  # I though I had tried this w/ no success...
    return t_common


# uncomment to test function
print(common_elements((2, 3, 4), (3, 4, 5, 6)))


#############################################################################
# Problem 4: Practice working with Python Lists
# Write a Python program to remove sublists from a given list of lists, which
# contain an element outside a given range.
# e.g
# Original list:
# [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
# After removing sublists from a given list of lists, which contain an
# element outside the given range of 12 - 20 (inclusive):
# [[13, 14, 15, 17]]
# INSERT CODE BELOW HERE
# VAO: my code
def remove_list_range(ls, low, high):
    revised = []
    for e in ls:
        for elem in e:  # alternatively, only one for, with min() and max() of list
            # because the prompt was to remove the entire sublist, not elements from multiple lists
            # in this particular case, answer is the same, but I was wrong
            if elem >= low and elem <= high:
                revised += [elem]  # I was adding "e" and getting different result
    return revised


# uncomment to test function
print(
    remove_list_range(
        [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]], 13, 17
    )
)
