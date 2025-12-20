# Problem 1 - Bisection Search Practise
# Write a program using bisection search to find the forth root of a number inputted by the 
# user. Print the forth root calculated with max error of 0.01. 

# from multiprocessing.connection import answer_challenge
# VAO: my code
# x = float(input("Using bisection search calculate the forth root of: " ))
# epsilon = 0.01
# low = 0
# high = x
# ans = (low + high) / 2
# if x < 0:
#     print("does not exist")
# while abs(ans ** 4 - x) > epsilon:
#     if ans ** 4 > x:
#         high = ans
#     else:
#         low = ans
#     ans = (low + high) / 2
# print(f"the fourth root of {x} is close to {ans}")


# Problem 2 - Functions 
# Write a Python function to check whether a number falls in a given range.
# VAO: my code
# def in_range(x, y, z):
#     return (x in range(y, z + 1)) is True # alternatively, x >= start and x <= end

# number, range_start, range_end = \
#     int(input("enter a number: ")),\
#     int(input("enter the start of the range: ")),\
#     int(input("enter the end of the range: "))

# print(in_range(number, range_start, range_end))

# Problem 3 - Functions 
# Write a Python function to check whether a number is perfect or not.
# (In number theory, a perfect number is a positive integer that is equal 
# to the sum of its proper positive divisors, excluding the number itself).
# VAO: my code
def is_perfect(x):
    sum = 0
    for n in range(1, x):
        if x % n == 0:
            sum += n
    if sum == x:
        print(f"{x} is a perfect number")
    #else:
     #   print("no")
for i in range(1, 1000):
    is_perfect(i)

# Problem 4 - Approximation Algorithm (see Lecture 5 slides for similar problem)
# Write an approximation algorithm to calculate the forth root of some 
# number inputted by the user. 
# Print the result and the number of iterations required to reach that result. 
# The program should not accept negative numbers. Initial parameters epsilon 
# (i.e. accuracy), initial guess, increment and num_guesses are defined below.

# example initial parameters
epsilon = 0.01
ans = 0.0
increment = 0.001
num_guesses = 0
number = int(input("enter a positive number: "))
while abs(ans ** 4 - number) > epsilon and ans ** 4 <= number:
    ans += increment
    num_guesses += 1
print(f"by approximation, the fourth root of {number} is close to {ans}")