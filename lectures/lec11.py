## remove from a list
from ty_extensions import Unknown
L = [2,1,3,6,3,7,0]
L.remove(2)
L.remove(3)
del(L[1])
print(L.pop()) # unlike other methods, .pop() also returns something (the removed element)


#############
## Removing elements
#############

# L = [2,1,3,6,3,7,0]
# L.pop(5)
# print(L)
# L.remove(3)
# print(L)
# L.pop()
# print(L)


############ YOU TRY IT ###############
# This one is similar to remove_elem from lec10 except that remove_elem
# returns a new list and this one mutates the parameter L (and returns None)
def remove_all(L, e):
    """
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns None.
    """
    # your code here
    # VAO: my code
    # lecture suggested we should first remove all from L, then add from the copy. Difference?
    # no difference, it's just because class hadn't covered .remove() at that point
    # in fact, it gets even easier with .remove(), no need for the copy, just 'while elem in L, L.remove(e)'

    L_copy = L[:]
    # for i in range(len(L_copy)): # VAO: why doesn't this work?
                                   # 'builtin_function_or_method' object is not subscriptable
                                   # figure this out
    #     if L_copy[i] == e:
    #         L.pop[i]
    for elem in L_copy:
        if elem == e:
            L.remove(elem)


Lin = [1,2,2,2]
remove_all(Lin, 2)
print(Lin)    # prints [1]

Lin = [1,2,2,2]
remove_all(Lin, 1)
print(Lin)    # prints [2, 2, 2]

Lin = [1,2,2,2]
remove_all(Lin, 0)
print(Lin)    # prints [1, 2, 2, 2]

#######################################


def remove_all(L, e):
    """
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns None.
    """
    while e in L:
        L.remove(e)


# Lin = [1,2,2,2]
# remove_all(Lin, 2)
# print(Lin)    # prints [1]


## this function does not do the right thing
def remove_all(L, e):
    """
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns None.
    """
    for elem in L:
        if elem == e:
            L.remove(e)


# Lin = [1,2,2,2]
# remove_all(Lin, 2)
# print(Lin)    # INCORRECTLY prints [1,2]


#############
## TRICKY EXAMPLE 4: removing element as you are mutating a list
#############
## this is an incorrect way to do it
def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)


# L1 = [10, 20, 30, 40]
# L2 = [10, 20, 50, 60]
# remove_dups(L1, L2)
# print(L1)


## this is an incorrect way to do it
def remove_dups(L1, L2):  # noqa: F811
    L1_copy = L1  # not actually a copy, just an alias!!
    for e in L1:
        if e in L2:
            L1.remove(e)


# L1 = [1, 2, 3, 4]
# L2 = [1, 2, 5, 6]
# remove_dups(L1, L2)
# print(L1)


## this is the CORRECT way to do it
def remove_dups(L1, L2):
    L1_copy = L1[:]  # actually a copy aka clone
    for e in L1_copy:
        if e in L2:
            L1.remove(e)


# L1 = [1, 2, 3, 4]
# L2 = [1, 2, 5, 6]
# remove_dups(L1, L2)
# print(L1)


############################
############################
# VAO: all cmmts below are mine
# Control copying, alises
old_list = [[1,2],[3,4],[5,'foo']]
new_list = old_list # this is aliasing; two names referencing the exact same object

new_list[2][1] = 6
print("New list:", new_list) # both will change 'foo' to 6, they point to the same object
print("Old list:", old_list) # both will change 'foo' to 6, they point to the same object

# Control copying, shallow copy
import copy 
old_list = [[1,2],[3,4],[5,6]]
new_list = copy.copy(old_list) # shallow copy, just like list[:], it will copy only the top level structure
                                                                      # meaning: to the extent any top level element is mutable,
                                                                      # it will copy the reference to those objects stored in memory, not the values
                                                                      # i.e., if those objects change, new_list will change too

old_list.append([7,8]) # this is not one of the objects copied by new_list, so it's only added to old_list
old_list[1][1] = 9 # this will be changed in both lists; because it changes 4 to 9 in the object that is referenced by both of them
print("New list:", new_list)
print("Old list:", old_list)

# Control copying, deep copy
import copy
old_list = [[1,2],[3,4],[5,6]]
new_list = copy.deepcopy(old_list) # deep copy: it actually copies all the values in the original object
                                                                          # i.e., unlike shallow, it doesn't copy a reference to the same objects from reference list,
                                                                          # but the actual values and stores them in new objects

old_list.append([7,8])
old_list[1][1] = 9
print("New list:", new_list) # since new_ is a deep copy of old_, the mutation above doesn't impact it, so [1][1] remains 4, not 9
print("Old list:", old_list)


## EXAMPLE: aliasing
a = 1
b = a 
print(a) # 1 
print(b) # 1

warm = ['red', 'yellow', 'orange']
hot = warm # points to the same object in memory as warm, ["red", "yellow", "orange"]
hot.append('pink') # both hot and warm will add "pink" to the end,
                   # because they are different aliases pointing to the same object in memory
print(hot)
print(warm)

# EXAMPLE: cloning
cool = ['blue', 'green', 'grey']
chill = cool[:] # shallow copy of cool; won't be changed if cool changes
                                     # if any of the elements in cool were mutable (e.g., lists), then that could be an issue
chill.append('black')
print(chill)
print(cool) # won't print black

# EXAMPLE: sorting with/without mutation
warm = ['red', 'yellow', 'orange']
sortedwarm = warm.sort()
print(warm) # as a side effect of .sort() method, warm gets sorted just by calling it
            # i.e., .sort() mutates the original list, so warm now points to a sorted list in memory
            # sortedwarm, however, points to None, because the alias was assigned to the return of .sort()
print(sortedwarm) # None

cool = ['grey', 'green', 'blue']
sortedcool = sorted(cool) # this return the sorted list, unlike .sort()
print(cool) # sorted() doesn't mutate the original list
            # i.e., sortedcool is an alias pointing to a different object in memory
            # i.e., cool remains unsorted, sortedcool is the only sorted one
print(sortedcool) 

# EXAMPLE: lists of lists of lists...
warm = ['yellow', 'orange']
hot = ['red']
brightcolors = [warm] # alias is not pointing to the same object in memory
                                                           # it is actually point to a list including that object
                                                           # i.e., brightcolors is [['yellow', 'orange']]
brightcolors.append(hot) # adds the list 'hot' to the object that was referenced by 'brightcolors'
                         # now brightcolors is [['yellow', 'orange'], ['red']] (i.e., list with 2 elem, list with 1 elem)
                         # also, .append() adds the list, not its elements, which is why it's not 'red' but ['red']
                         # warm is still the same as before, because bs = [warm] is a different object than 'warm'
print(brightcolors)
hot.append('pink') # now 'hot' becomes ['red', 'pink']
print(hot)
print(brightcolors) # since 'hot' was appended, bs is now [['yellow', 'orange'], ['red', 'pink']]

# VAO: DAMN, I GOT THEM ALL RIGHT!!! thanks, Anna Bell


############ YOU TRY IT AT HOME ###################
# Step through the code below without running it
# Write down what values each variable has
# Draw the memory diagram to help you keep track of aliases and clones

cool = ['blue', 'green']
warm = ['red', 'yellow', 'orange']
print(cool) # same list above, no changes
print(warm) # same list above, no changes

colors1 = [cool] # not the same object as cool, but a new one, a list which cool is the single element
print(colors1) # [['blue', 'green']], list of a list
colors1.append(warm) # this adds the list object referenced by 'warm' to the list referenced by 'colors1'
                     # so the object referenced by colors1 is now [['blue', 'green'], ['red', 'yellow', 'orange']], list with 2 lists
                     # note that the object referenced by 'warm' was added, so any future changes to it will be reflected in 'colors1'
                     # 'warm' remains unchanged, no mutation, its object was only added somewhere
print('colors1 = ', colors1) # [['blue', 'green'], ['red', 'yellow', 'orange']]

colors2 = [['blue', 'green'],
          ['red', 'yellow', 'orange']] # same elements of colors1, but w/o any reference to it, so it's a totally different object
print('colors2 =', colors2)

warm.remove('red') # warm gets changed to ['yellow', 'orange']
print('colors1 = ', colors1) # the second element in colors1 referenced the same object that warm does
                             # so colors1 is now [['blue', 'green'], ['yellow', 'orange']]
print('colors2 =', colors2) # colors2 is unchanged, it cointained the same elements as colors1, but it was a different object

for e in colors1: # side note: e is only the iterable, it doesn't translate to elements
                  # it just so happens that in lists, the iterable are the elements
    print('e =', e) # prints 'e =' and each color pair; colors1 has two elements, it's a list with 2 elements
                    # e = ['blue', 'green'], e = ['yellow', 'orange']

for e in colors1:
    if type(e) == list: # yes, each element in colors1 is a list, so both match 
        for e1 in e: # this means to iterate over the iterables (i.e., elements) of the list elements
            print(e1) # this prints each of the colors: blue, green, yellow, orange
    else: # won't be triggered
        print(e)

flat = cool + warm # concatenation creates a different object composed of the elements from the two lists
                                        # i.e., ['blue', 'green', 'yellow', 'orange'], because 'red' was removed from warm
print('flat =', flat)

print(flat.sort()) # flat.sort() will sort 'flat' based on the type of iterable; if str, alphabetically
                   # however, that mutation will be done as a "side effect" of the method, not as its return
                   # this because .sort() has no return, it returns None
print('flat =', flat) # prints the sorted list; if it were print(flat.sort()), it would print None

new_flat = sorted(flat, reverse = True) # new_flat is flat sorted in reverse alphabeticall (because str)
print('flat =', flat) # sorted() doesn't mutate the original string, unlike .sort()
                      # so this will print the sorted, not reverse sorted, string
print('new_flat =', new_flat) # this will print the sorted string

cool[1] = 'black' # changes the object to which cool refers; cool is now ['blue', 'black']
print(cool)
print(colors1) # the first element in colors1 is a list containing the same object that cool refers to
               # so colors1 becomes [['blue', 'black'], ['yellow', 'orange']]

###############################


############################################
################### AT HOME ######################
############################################
def repeat(L, n):
    """L is a list of ints
        n is a positive int
    Mutates L to contain whatever elements L has right now repeated n times."""
    # your code here


# Lin = [1,2,3]
# repeat(Lin, 3)
# print(Lin)    # prints [1, 2, 3, 1, 2, 3, 1, 2, 3]


# Think about why the following solution does not work!
# VAO: 'Lin' inside the function scope is not the same as 'Lin' outside the function scope, 
# i.e., just assigning Lin = Lnew inside the function scope doesn't mean that Lin is mutated
# my initial solution ignored that "Mutates L", suggesting a return, so this a revised fix
def repeat(L, n):
    """L is a list of ints
        n is a positive int
    Mutates L to contain whatever elements L has right now repeated n times."""
    # your code here
    # VAO: my code
    Lnew = []
    si_ze = len(L) # as a way to iterate over index of L without mutating L beforehand;
    for i in range(n - 1): # trial and error
        for e in range(si_ze):
            L.append(L[e])
    # Lin = Lnew  # hint, even thought we reuse the name Lin here, we make it point to a NEW object!
    
    # VAO: alternatively
    Lnew = L[:]
    for i in range(n - 1):
        for e in Lnew:
            L.append(L[e])


Lin = [1,2,3]
repeat(Lin, 3)
print(Lin)   # prints [1, 2, 3] which is wrong!


#######################################
########## ANSWERS TO YOU TRY IT ###############
###########################################


def remove_all(L, e):
    """
    L is a list
    Mutates L to remove all elements in L that are equal to e
    """
    Lnew = L[:]
    L.clear()
    for elem in Lnew:
        if elem != e:
            L.append(elem)


# L = [1,2,2,2]
# remove_all(L, 1)
# print(L)    # prints [2, 2, 2]

# L = [1,2,2,2]
# remove_all(L, 2)
# print(L)    # prints [1]

# L = [1,2,2,2]
# remove_all(L, 0)
# print(L)    # prints [1, 2, 2, 2]


#######################################
########## ANSWERS TO AT HOME ###############
###########################################
def repeat(L, n):
    """L is a list of ints
        n is a positive int
    Mutates L to contain whatever elements L has right now repeated n times."""
    # your code here
    rep = len(L)
    for i in range(n - 1):
        for j in range(rep):
            L.append(L[j])


# Lin = [1,2,3]
# repeat(Lin, 3)
# print(Lin)    # prints [1, 2, 3, 1, 2, 3, 1, 2, 3]

############################
## FINGER EXERCISE
############################
# Implement the function that meets the specifications below:
def remove_and_sort(Lin, k):
    """ Lin is a list of ints
        k is an int >= 0
    Mutates Lin to remove the first k elements in Lin and 
    then sorts the remaining elements in ascending order.
    If you run out of items to remove, Lin is mutated to an empty list.
    Does not return anything.
    """
    # Your code here
    # VAO: my code; I don't think I need a copy
    if len(Lin) <= k:
        Lin.clear
    for n in range(k):
        L.pop(n)
    L.sort()

# Examples:
L = [1,6,3]
k = 1
remove_and_sort(L, k)
print(L)   # prints the list [3, 6]
