#################
## reading
#################

# approximating the square root using exhaustive enumeration
# x = int(input("enter an integer: "))
# epsilon = 0.01 # how close do you want the approximation to get 
# step = epsilon ** 2
# num_guesses = 0
# ans = 0.0
# while abs(ans ** 2 - x) >= epsilon and ans <= x: # VAO: both have to be true; i.e., if any is false, loop is over
#                                                  # first one checks if your guess is close enough to the epsilon "margin of error"
#                                                  # or better, approximation threshold, delta etc.
#                                                  # second one determines how many time you should run the loop for?
#                                                  # not sure what it does, as that is covered by the first one too...
#                                                  # FROM LECTURE: I'm right into what each one does, but I'm wrong in thinking that accuracy tracker (epsilon) handles size of loop
#                                                  # i.e., without second condition, you can "overshoot" the X, i.e., guess**2 gets close enough to X but not within range,
#                                                  # and then next guess overshoots it, and from there it just keeps increasing
#                                                  # from lec6: "and ans <= x" measures how reasonable the guess is
#     ans += step # increase ans by 0.01^2 each time, the approximation delta we decided above
#                 # this will be extremely slow, as you're only adding small increments; i.e., loop will take forever
#                 # e.g., 19975 guesses to find out sqrt de 4
#     num_guesses += 1
# print("number of guesses =", num_guesses)
# if abs(ans ** 2 - x) >= epsilon:
#     print("Failed on square root of", x)
# else:
#     print(ans, "is close to square root of", x)

# and now using bisection search, which should really cut down on execution time
x = int(input("enter an integer: "))
epsilon = 0.01
num_guesses, low = 0, 0
high = max(1, x)
ans = (high + low) / 2
while abs(ans ** 2 - x) >= epsilon: # funny enough, x = 4 never triggers this (i.e., 0 < epsilon), and there are zero guesses
    print("low =", low, "high =", high, "ans =", ans, num_guesses)
    num_guesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2
print("number of guesses =", num_guesses)
print(ans, "is close to square root of", x)

# VAO: finger exercise, p 56: What would the code in figure 3-5 (bisection, above, ln 27) do if x = -25?
### ANSWER: it would run forever, since the loop condition would never break the loop, i.e., ans**2 - (-25) would never be < epsilon.
            # Also, low never changes from zero (if statement), not sure why HIGH and ANS also return zero. Maybe they go to zero after a few runs?
            # Debugging (s/while/for), I can confirm that they start as I thought (1 and 0.5, respectively) but quickly go to zero.

# VAO: finger exercise, p 56: What would have to be changed to make the code in figure 3-5 (bisection, above, ln 27) 
# work for finding an approximation to the cube root of both negative and positive numbers?
# Hint: think about changing low to ensure that the answer lies within the region to be searched.

# first solution feels like "cheating"? i.e., having the same code run with abs(x), and adding the if statement at the end to "convert" +/- root
# x = int(input("enter an integer: "))
# epsilon = 0.01
# num_guesses, low = 0, 0
# high = max(1, abs(x))
# ans = (high + low) / 2
# while abs(ans ** 3 - abs(x)) >= epsilon:
#     print("low =", low, "high =", high, "ans =", ans, num_guesses)
#     num_guesses += 1
#     if ans ** 3 < abs(x):
#         low = ans
#     else:
#         high = ans
#     ans = (high + low) / 2
# print("number of guesses =", num_guesses)
# if x < 0:
#     print(-ans, "is close to cube root of", x)
# else:
#     print(ans, "is close to cube root of", x)

# second solution, changing the ranges per the hint, w/o abs()
# x = int(input("enter an integer: "))
# epsilon = 0.01
# num_guesses = 0
# if x < 0: # VAO: same as professor did in lec 6, nice
#     low = x
#     high = 0
# else:
#     low = 0
#     high = x
# ans = (high + low) / 2
# while abs(ans ** 3 + x) >= epsilon:
#     print("low =", low, "high =", high, "ans =", ans, num_guesses)
#     num_guesses += 1
#     if ans ** 3 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low) / 2
# print("number of guesses =", num_guesses)
# print(ans, "is close to cube root of", x)

# VAO: finger exercise, p 56: The Empire State Building is 102 stories high. A man wanted to know the highest floor from which he could drop
# an egg without the egg breaking. He proposed to drop an egg from the top floor. If it broke, he would go down a floor, and try it again. 
# He would do this until the egg did not break. At worst, the method requires 102 eggs. Implement a method that at worst uses seven eggs.
# low, high = 1, 102
# ideal_floor = int((low + high) / 2)
# eggs = 0
# result = ""
# while high - low > 1:
#     result = input(f"Dropping an egg from floor {ideal_floor}. Did the egg break? (Y/N)\n")
#     eggs += 1
#     if result == "Y" or result == "y":
#         high = ideal_floor
#     else:
#         low = ideal_floor
#     ideal_floor = int((high + low) / 2) # any input other than Y/N will go to this, and ultimately reduce to 1. But that's fine.
# print(f"the highest floor from which you can drop an egg without breaking is {ideal_floor}. It took {eggs} eggs to figure that out")

#################
## EXAMPLE: successive addition
#################

# 0.125 is a perfect power of 2
# x = 0
# for i in range(10):
#     x += 0.125
# print(x == 1.25)

#######

# 0.1 is not a perfect power of 2
# x = 0
# for i in range(10):
#     x += 0.1
# # print(x == 1)

# print(x, '==', 10*0.1)

#############
## EXAMPLE
# protip: use Python Tutor to go step-by-step: http://pythontutor.com/
#############

# x = float(input('Enter a decimal number between 0 and 1: '))

# p = 0
# while ((2**p)*x)%1 != 0:
#     print(f'Remainder = {str((2**p)*x - int((2**p)*x))}')
#     p += 1

# num = int(x*(2**p))

# result = ''
# if num == 0:
#     result = '0'
# while num > 0:
#     result = str(num%2) + result
#     num = num//2

# for i in range(p - len(result)):
#     result = '0' + result
# result = result[0:-p] + '.' + result[-p:] # VAO: not 100% sure I get this. OK, Claude was a great help in getting over this.
#                                           # first one: start at 0, step -p. Does that "force" it to before the first entry? Wouldn't -1 do the trick?
#                                           # NO! -p doesn't take it to before the first entry, but to "before however many entries are needed in your specific case"
#                                           # it can, however, be rewritten as "[:-p]" for consistency with the second entry
#                                           # second one: isn't this the same as [0:-p]? Also, what's with the colon after -p? does this mean anything else?
#                                           # NO! It's not the same. [0:-p] means everything from the start but not the last p characters.
#                                           # While [-p:] (or [-p:0] means everything after the first p characters (including the first one)
#                                           # i.e., [0:-p] or [:-p] excludes the last p characters, while [-p:] or [-p:0] includes the last p characters
# print(f'The binary representation of the decimal {str(x)} is {str(result)}')


################
## EXAMPLE: Approximation by epsilon increments
## Incrementally fixing code as we find issues with approximation
################

# try with 36, 24, 2, 12345
# x = 36
# epsilon = 0.01
# num_guesses = 0
# guess = 0.0
# increment = 0.0001
# while abs(guess**2 - x) >= epsilon:
#     guess += increment
#     num_guesses += 1
# print(f'num_guesses = {num_guesses}')
# print(f'{guess} is close to square root of {x}')

###########

# Caution, you'll need to "Restart Kernel" in the shell if you run this code
# x = 54321
# epsilon = 0.01
# num_guesses = 0
# guess = 0.0
# increment = 0.0001
# while abs(guess**2 - x) >= epsilon:
#     guess += increment
#     num_guesses += 1
#     if num_guesses%100000 == 0:
#         print(f'Current guess = {guess}')
#         print(f'Current guess**2 - x = {abs(guess*guess - x)}')
#     if num_guesses%1000000 == 0:
#         input('continue?')
# print(f'num_guesses = {num_guesses}')
# print(f'{guess} is close to square root of {x}')

##########

# Add an extra stopping condition 
# and check for why the loop terminated
# x = 54321
# epsilon = 0.01
# num_guesses = 0
# guess = 0.0
# increment = 0.0001  # try with 0.00001
# while abs(guess**2 - x) >= epsilon and guess**2 <= x:
#     guess += increment
#     num_guesses += 1
# print(f'num_guesses = {num_guesses}')
# if abs(guess**2 - x) >= epsilon:
#     print(f'Failed on square root of {x}')
#     print(f'Last guess was {guess}')
#     print(f'Last guess squared is {guess*guess}')
# else:
#     print(f'{guess} is close to square root of {x}')
    
#######


#################################################
######################## AT HOME ##########################
#################################################
# 1. If you are incrementing from 0 by 0.022, how many increments 
# can you do before you get a floating point error? 
# x = 0
# count = 20     # check different numbers here
# for i in range(count):
#     x += 0.022 # increment
#     print(x)      # check this value for floating point error

# VAO: on the fifth increment, you get 0.109999 instead of 0.11

# 2. Automate the code from the previous problem. Suppose you are 
# just given an increment value. Write code that automatically
# determines how many times you can add increment to itself 
# until you start to get a floating point error.

# your code here
# increment = float(input("what should be the increment? "))
# count = 1
# sum, mult = increment, increment
# while sum == mult: # a solução abaixo está quase idêntica, mas otimiza quando coloca
#                    # a multiplicação dentro da condicional do loop, em vez de repetir o statement
#     count += 1
#     sum += increment
#     mult = count * increment
# print(f"{count - 1} is when you get floating point error: {sum - increment} != {(count - 1) * increment}")
# se não tirar incremento, mostra errado, i.e., o próximo valor de sum e mult, em vez do valor que saiu do loop

#################################################
#################################################
#################################################

# VAO: finger exercise elc 5: Assume you are given a string variable named `my_str`. Write a piece of Python code that
# prints out a new string containing the even indexed characters of `my_str`.
# For example, if `my_str = "abcdefg"` then your code should print out `aceg`.
my_str = str(input("Enter any sentence: ")) # change whatever input to string 
even_str = ""
for c in range(0, len(my_str), 2):
        even_str += my_str[c] # debug: só com += c, ele tenta adicionar o index à string; porque o "in range" iterar
                              # por uma sequência de números, não pela string
print(even_str)

#################################################
################ ANSWER TO AT HOME ##########################
#################################################
# Automate the code. Suppose you are 
# just given an increment value. Write code that automatically
# determines how many times you can add increment to itself 
# until you start to get a floating point error.

# VAO: foi o que fiz antes com sum e mult
# n = 0.022
# N = 1
# x = n
# while x == n*N:
#     print(x)
#     x += n
#     N += 1
# # note that the x and N increments one extra time 
# print(f'count is {N-1} where {x-n} != {n*(N-1)}')

#################################################
#################################################
#################################################