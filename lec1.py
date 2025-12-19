# reading 1
print("Yankees rule!")
print("But not in Boston!")
print("Yankees rule,", "but not in Boston!")

pi = 3
radius = 11
area = pi * (radius**2)
radius = 14  # this assignment has no effect on the value to which area was bound, because it came later
print(area)

side = 1  # length of sides of a unit square
radius = 1  # radius of a unit circle
# subtract area of unit circle from area of unit square
area_circle = pi * radius**2
area_square = side * side
difference = area_square - area_circle
print(difference)

x, y = 2, 3
x, y = (
    y,
    x,
)  # all expressions on the right-side are evaluated before any bindings are changed
print("x =", x)
print("y =", y)

print("hello, world!")

# lecture 1
## TYPE THIS IN THE CONSOLE - CHECK THE TYPE OF OBJECTS ##
type(5)
type(3.0)

## TYPE THIS IN THE CONSOLE - CONVERT TO ANOTHER TYPE ##
float(3)
int(3.9)
round(3.9)

## TYPE THIS IN THE CONSOLE - EXPRESSIONS ##
3 + 2
(4 + 2) * 6 - 1
type((4 + 2) * 6 - 1)
float((4 + 2) * 6 - 1)

## TYPE THIS IN THE CONSOLE - VARIABLES ##
pi = 355 / 113

# Compute approximate value for pi
pi = 355 / 113
radius = 2.2
area = pi * (radius**2)
circumference = pi * (radius * 2)

## CODE STYLE ##

# Example 1
# do calculations
a = 355 / 113 * (2.2**2)
c = 355 / 113 * (2.2 * 2)

# Example 2
p = 355 / 113
r = 2.2
# multiply p with r squared
a = p * (r**2)
# multiply p with r times 2
c = p * (r * 2)

# Example 3
# calculate area and circumference of a circle using an approximation for pi
pi = 355 / 113
radius = 2.2
area = pi * (radius**2)
circumference = pi * (radius * 2)

## CHANGING BINDINGS ##
pi = 3.14
radius = 2.2
area = pi * (radius**2)
radius = radius + 1


## DEBUG THIS - SWAP VALUES ##
# Given x and y below, the code incorrectly swaps the values. Fix it!
x = 1
y = 2
# Buggy example
# y = x
# x = y
# Fix it here!
temp = x
x = y
y = temp
print(x, y)

#########################################
############### EXERCISES ##########################
#########################################

# Finger exercise 1
# Assume 3 variables are already defined for you: `a`, `b`, and `c`.
# Create a variable called `total` that adds `a` and `b` then multiplies the result by `c`.
# Include a last line in your code to print the value: `print(total)`

#########################################
############### EXERCISES ##########################
#########################################

# Finger exercise 1
# Assume 3 variables are already defined for you: `a`, `b`, and `c`.
# Create a variable called `total` that adds `a` and `b` then multiplies the result by `c`.
# Include a last line in your code to print the value: `print(total)`
a = 1
b = 2
c = 3
total = (a + b) * c
print(total)

# problem set 0
# Write a program that does the following in order:
# 1. At the top of your file and type: import numpy
# 2. Now write a line that sets a variable named x to 5.
# 3. Now write a line that sets a variable named y to 8.
# 4. Add variables x and y, and save the result to a variable named z.
# 5. Now save the result of this command: numpy.log2(z) to a variable named a.
import numpy

x = 5
y = 8
z = x + y
a = numpy.log2(z)

# old pset 0: 1. Asks the user to enter a number “x”
# 2. Asks the user to enter a number “y”
# 3. Prints out number “x”, raised to the power “y”.
# 4. Prints out the log (base 2) of “x”.
x = int(input('Enter a number "x":'))  # converts input from string to int
y = int(input('Enter a number "y":'))  # same
print(x**y)
print(numpy.log2(x))
