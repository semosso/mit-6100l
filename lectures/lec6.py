#####################
## reading
#####################
# finger exercise, p 61: Add some code to the implementation of Newton-Raphson that keeps
# track of the number of iterations used to find root. Use that code as part of a program
# that compares the efficiency of Newton-Raphson and bisection search. (You should discover
# that Newton-Raphson is far more efficient.)

# Newton-Raphson for square root
# Find X such that x**2 - 24 is within an epsilon of 0
k = int(input("enter an integer to find out its approximation root: "))
epsilon = 0.01
guess = k / 2
counter_NR = 0
while abs(guess ** 2 - k) >= epsilon:
    guess = guess - ((guess ** 2 - k) / (2 * guess))
    counter_NR += 1
print(f"square root of {k} is about {guess}. This took {counter_NR} iterations.")

# # now bisection search
bs_low = 0.0
bs_high = k
bs_guess = (bs_high + bs_low) / 2
counter_BS = 0
while abs(bs_guess ** 2 - k) >= epsilon:
    print(bs_high, bs_low, bs_guess)
    if bs_guess ** 2 < k:
        bs_low = bs_guess
    else:
        bs_high = bs_guess
    bs_guess = (bs_high + bs_low) / 2
    counter_BS += 1
print(f"square root of {k} is about {bs_guess}. This took {counter_BS} iterations.")

# Recall the approximation method code to find the square root
x = 54321
epsilon = 1 # try reducing or increasing
num_guesses = 0
guess = 0.0
increment = 0.00001   # try it with 0.00001
while abs(guess**2 - x) >= epsilon and guess**2 <= x:
    # abs(guess**2 - x) >= epsilon finds a "good enough" answer
    # guess**2 <= x ensures we stop looking when the guess becomes unreasonable
    guess += increment
    num_guesses += 1
print(f'num_guesses = {num_guesses}')

# # this "if" is for the case when we stopped the loop due to an unreasonable guess
if abs(guess**2 - x) >= epsilon:
    print(f'Failed on square root of {x}')
    print(f'Last guess was {guess}')
    print(f'Last guess squared is {guess*guess}')
# # this "else" is for the case when we stopped the loop due to being within epsilon of x
else:
    print(f'{guess} is close to square root of {x}')


#####################
## EXAMPLE: fast square root using bisection search
#####################

# x = 54321  # try 0.5
# epsilon = 0.01
# num_guesses = 0
# low = 0.0
# high = x
# guess = (high + low)/2

# while abs(guess**2 - x) >= epsilon:
#     # uncomment to see each step's guess, high, and low 
#     #print(f'low = {str(low)} high = {str(high)} guess = {str(guess)}')
#     if guess**2 < x:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2.0
#     num_guesses += 1
# print(f'num_guesses = {str(num_guesses)}')
# print(f'{str(guess)} is close to square root of {str(x)}')



############### YOU TRY IT ###################
x = 0.5
epsilon = 0.01
# choose the low endpoint
low = x # VAO: low at 0.5 and high at 1 seems to work
# choose the high endpopint
high = 1

guess = (high + low)/2

while abs(guess**2 - x) >= epsilon:
    print(f'low = {str(low)} high = {str(high)} guess = {str(guess)}') # VAO: doesn't need str()
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
print(f'{str(guess)} is close to square root of {str(x)}')

#####################################################


#####################
## Code for square root with all x values
#####################
#x = 0.5
#epsilon = 0.01
#if x >= 1:
#    low = 1.0
#    high = x
#else:
#    low = x
#    high = 1.0
#guess = (high + low)/2
#
#while abs(guess**2 - x) >= epsilon:
#    print(f'low = {str(low)} high {str(high)} guess = {str(guess)}')
#    if guess**2 < x:
#        low = guess
#    else:
#        high = guess
#    guess = (high + low)/2.0
#print(f'{str(guess)} is close to square root of {str(x)}')


################# YOU TRY IT #######################
# Write code to use bisection search to find the cube 
# root of positive cubes to within some epsilon

cube = 27
epsilon = 0.01
low = 0
high = cube

# your code here
guess = (low + high) / 2
while abs(guess ** 3 - cube) > epsilon:
    if guess ** 3 > cube:
        high = guess
    else:
        low = guess
    guess = (low + high) / 2
print(f"{guess} is close to the cube root of {cube}")

#####################################################


######## Cube root for all cubes ############
cube = -27
neg = False
if cube < 0:
    neg = True
cube = abs(cube)
epsilon = 0.01
low = 0
high = cube
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube :
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
if neg is True:
    guess = -guess
print(f'{guess} is close to the cube root of {cube}')


########################
## EXAMPLE: Newton-Raphson to find roots
######################
# epsilon = 0.01
# k = 54231  # try 54321
# guess = k/2.0
# num_guesses = 0

# while abs(guess*guess - k) >= epsilon:
#     num_guesses += 1
#     guess = guess - (((guess**2) - k)/(2*guess))
# print(f'num_guesses = {str(num_guesses)}')
# print(f'Square root of {str(k)} is about {str(guess)}')

# Finger exercise: Assume you are given an integer 0 <= N <= 1000.
# Write a piece of Python code that uses bisection search to guess N. The code prints two lines:
#   `count:` with how many guesses it took to find N, and 
#   `answer:` with the value of N.
# Hints: If the halfway value is exactly in between two integers, choose the smaller one.
num = int(input("choose an integer between 0 and 1000 (including): "))
low = 0
high = 1000
guess = round((low + high) / 2)
count = 1
if guess == num: # just in case input is "500" 
    print(f"count: {count}\nanswer: {guess}")
else:
    while guess != num:
        if guess > num: # you can pick whatever equality comparison you want
                        # but the adjustment to the threshold has to be adapted accordingly
            high = guess
        else:
            low = guess
        guess = round((low + high) / 2)
        count += 1
    print(f"count: {count}\nanswer: {guess}")

#################################################################
################# ANSWERS TO YOU TRY IT #######################
#################################################################
# Write code to use bisection search to find the cube 
# root of positive cubes to within some epsilon

# cube = 27
# epsilon = 0.01
# low = 0
# high = cube
# guess = (high + low)/2.0
# while abs(guess**3 - cube) >= epsilon:
#     if guess**3 < cube :
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2.0
#     numGuesses += 1
# print('numGuesses =', numGuesses)
# print(guess, 'is close to the cube root of', cube)

#################################################################
#################################################################
#################################################################