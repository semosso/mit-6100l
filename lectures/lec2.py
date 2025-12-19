# ##reading 2
if int(input("numero:")) % 2 == 0:
    print("even")
else:
    print("odd")
print("done with conditional")

# breaking lines with \, but preferrable with (), [], {}
A = 1000000000 + 2000000000 + 3000000000

B = 1000 + 2000 + 3000

# #nested conditional statements (elif), mesmo não indented está nested

x = 1
y = 2
z = 3

if x < y and x < z:
    print("x is least")
elif y < z:
    print("y is least")
else:
    print("z is least")

# #fex1: write a program that examines three variables (x, y, z), and prints the
# #largest odd number among them. If none of them are odd, it should print the
# #smallest value of the three. Resposta é do livro.

answer = min(x, y, z)  # para a segunda metade da pergunta, none of them odd
if x % 2 != 0:  # checando se eles são odd, e substituindo valor de answer, que tinha um provisional value
    answer = x
if y % 2 != 0 and y > answer:
    answer = y
if z % 2 != 0 and z > answer:
    answer = z
print(answer)

# #conditional expressions (i.e., x = y if y > z) are also allowed

x = 4
y = 2
z = 3

print((x if x > z else z)) if x > y else (y if y > z else z)  # print greatest of

# #strings are of the "sequence" type, and length, indexing and slicing apply

len("abc")

"abc"[0]  # returns 'a', indexing is zero-based
"abc"[-1]  # returns 'c', negative numbers index from the end

"abc"[1:3]  # returns 'bc', i.e., end is end-1
"abc"[0 : len("abc")]  # returns 'abc', the full size, because of the end vs end-1 above

"abc"[:] == "abc"[0 : len("abc")]  # returns True, values default to start and end

'123456789'[0:9:2] #returns every second number from 0 to 9

#type conversions or type casts

num = 30000000
fraction = 1/2
print(num*fraction, 'is', fraction*100, '%', 'of', num)
print(num*fraction, 'is', str(fraction*100) + '%', num)
#ln 78 doesn't produce space between 50.0 and %, because of conversion to string
#and concatenation (instead of different str arguments passed on to print in ln 77)

print(int(num*fraction), 'is', str(fraction*100) + '%', num)
#ln 82 converts result to int from float, because fraction is float

print(f'{int(num*fraction)} is {fraction*100}% of {num}')
print(f'{int(num*fraction):,.0f} is {fraction*100}% of {num:,}')
#ln 85 is an f-string, a formatted string literal, inserindo expressions nas strings
#aceita modificadores, introduzidos por ':', como por exemplo para truncar

abc = f'{int(num*fraction)} is {fraction*100}% of {num}'
print(abc[0:10])
## query, como fica o slicing nesse caso? ele acontece depois de evaluate a expressão?
##YES, se der erro nas expressões, dá erro mesmo no slicing sozinho

#fex2: write code that asks the user to enter their birthday in the form of
#mm/dd/yyy, and then prints a string of the form "you were born in the year yyyy."

dob = input('informe sua data de nascimento (formato mm/dd/yyyy): ')
print(f'você nasceu no ano de {dob[6:10]}')
print(f'você nasceu no ano de {dob[-4:len(dob)]}')

# #########################################
# ############### LECTURE #################
# #########################################


## TYPE THIS IN THE CONSOLE -- STRINGS ##
a = 'me'
b = "myself"
c = a + b
d = a + " " + b
silly = a * 3

s = "abc"
len(s)

## TYPE THIS IN THE CONSOLE -- INDEXING ##
s = "abc"
s[0]
s[1]
s[2]
#s[3]  # this is an error
s[-1]
s[-2]
s[-3]

## TYPE THIS IN THE CONSOLE -- SLICING ##
s = "abcdefgh"
s[3:6]
s[3:6:2]
s[:]
s[::-1]
s[4:1:-2]

## TYPE THIS IN THE CONSOLE - MANIPULATION ##
s = "car"
#s[0] = 'b'  # this is an error
s = 'b'+s[1:len(s)]

#########################################
############### LECTURE #################
#########################################

## PRINTING ##
a = "the"
b = 3
c = "musketeers"
print(a, b, c)
print(a + b + c)   # this is an error
print(a + str(b) + c)

num = 5
print("my num is", num)
s = "my num is" + str(num)
print(s)

x = 1
x_str = str(x)
print("my fav num is", x, ".", "x =", x)
print("my fav num is " + x_str + ". " + "x = " + x_str)

## USER INPUT ##
#Example 1
text = input("Type anything... ")
print(5*text)

#Example 2
num1 = input("Type a number: ")
print(5*num1)
num2 = int(input("Type a number: "))
print(5*num2)

############## YOU TRY IT ###############
# Write a program that:
# * Asks the user for a verb.
# * Prints "I can _ better than you" where you replace _ with the verb.
# * Then prints the verb 5 times in a row separated by spaces.
# For example, if the user enters run, you print:
#     I can run better than you!
#     run run run run run

# your code here
verb = input("Type in a verb: ")
print("I can", verb, "better than you")
print(5*(verb+" ")) # um extra space no final, f-string resolve

#########################################

# #Example 3 - Newton's Method for cube root
# x = int(input('What x to find the cube root of? '))
# g = int(input('What guess to start with? '))

# print('Current estimate cubed = ', g**3)
# next_g = g - ((g**3 - x)/(3*g**2))
# print('Next guess to try = ', next_g)


# ## F-STRINGS ##
# num = 3000
# fraction = 1/3
# print(num*fraction, 'is', fraction*100, '% of', num)
# print(num*fraction, 'is', str(fraction*100) + '% of', num)
# print(f'{num*fraction} is {fraction*100}% of {num}')

# print(f'{num*fraction:,.0f} is {fraction*100:,.2f}% of {num:,}')


# pset_time = 15
# sleep_time = 8
# print(sleep_time > pset_time)
# derive = True
# drink = False
# both = drink and derive
# print(both)


############## YOU TRY IT ###############
# Write a program that:
# * Saves a secret number.
# * Asks the user for a number guess.
# * Prints a bool depending on whether the guess matches the secret.

# your code here
secret = 9
guess = int(input("Pick a number between 1 and 10: "))
print(secret == guess)


#########################################

# ## BRANCHING ##
# #Example 1
# pset_time = 22
# sleep_time = 8
# if (pset_time + sleep_time) > 24:
#     print("impossible!")
# elif (pset_time + sleep_time) >= 24:
#     print("full schedule!")
# else:
#     leftover = abs(24-pset_time-sleep_time)
#     print(leftover,"h of free time!")
# print("end of day")


############## YOU TRY IT ###############
# # Buggy, fix it!
# x = int(input("Enter a number for x: "))
# y = int(input("Enter a different number for y: "))
# if x == y:
#     print(x,"is the same as",y)
# print("These are equal!")

#########################################

# ## NESTED BRANCHING ##
# #Example 1
# x = float(input("Enter a number for x: "))
# y = float(input("Enter a number for y: "))
# if x == y:
#     print("x and y are equal")
#     if y != 0:
#         print("therefore, x / y is", x/y)
# elif x < y:
#     print("x is smaller")
# else:
#     print("y is smaller")
# print("thanks!")


############## YOU TRY IT ###############
# What's printed when y = 2, y = 20, y = 11?
# What if "if x <= y:" becomes "elif x <= y:"

# answer = ''
# x = 11
# y = 2 # try 20 and 11
# if x == y:
#     answer = answer + 'M'
# if x <= y:   # try making this line: elif x <= y:
#     answer = answer + 'i'
# else:
#     answer = answer + 'T'
# print(answer)

#########################################

############## YOU TRY IT ###############
# Write a program that:
# * Saves a secret number.
# * Asks the user for a number guess.
# * Prints whether the guess is too low, too high, or the same as the secret.

# your code here

secret = 19
guess = int(input("Pick a number: "))

if guess == secret:
    print("Lucky guess! Congratulations!")
elif guess > secret:
    print("You guessed higher!")
else:
    print("You guessed lower!")

#########################################
############### AT HOME ###################
#########################################
# Practice 1: What is the value of s1 and s2?
# DIDN'T NOTICE THE _ BEFORE ANA AT FIRST
s1 = "a" + "b"

d = "hi"
e = " ana" # note the space
s2 = d + 2 * e

# Practice 2: What are the substrings of s?
# ANSWER: GOT FIRST TWO WRONG, FORGOT ABOUT END-1, BUT THEN FIGURED IT OUT
s = "ABC d3f ghi"
s[0:3:1] # "ABC ", console returns "ABC", why? EXCLUDING THE END, IT'S ALWAYS END-1
s[0:4] # "ABC d". NOPE, ABC_, EXCLUDING THE END, IT'S ALWAYS END-1
s[8 : len(s) : 3] # "g"
s[2::-1] # "CBA"

# Practice 3: What does this print?
# ANSWER: GOT IT RIGHT. DON'T UNDERSTAND WHY THE STR() IS HERE.
# Note that a += b is the same as a = a + b
answer = ''
x = 11
# try with y = 2 and y = 12
y = 12
if len(str(x)) == len(str(y)):
    if y != 0 and x%2 == 1:
        answer = answer + "x / y is " + str(x/y)
elif x < y:
    answer += "\nx is smaller"  # \n inserts a newline character in the string
else:
    answer += "\ny is smaller"
print(answer) # why not change answer all together, if it starts as an empty string?

# TRY AT HOME!
# What's printed when y = 2, y = 20, y = 11?
# What if "if x <= y:" becomes "elif x <= y:"

answer = ''
x = 11
y = 11 # try 20 and 11
if x == y:
    answer = answer + 'M'
elif x <= y:   # try making this line: elif x <= y:
    answer = answer + 'i'
else:
    answer = answer + 'T'
print(answer)

# y=2 prints T; y=20 prints i (or does it jump to else and print T as well?); y=11 prints M
# ANSWER: first two right, but y=11 returs prints Mi, because second if is <=, not only <  
# changing second if to elif prints only M, why? because it's not processed if the master if is
# i.e., the elif is subordinate to the first it, but the second one isn't 

# Practice 4: Uncomment the code below and:
# What does it print when a = 6 and b = "6" // ANSWER: "int conversion" and "int and str conversion" 
# What does it print when a = "1" and b = 1 // ANSWER: "interesting"
# What does it print when a = 3 and b = 3 // ANSWER: "int conversion" for sure; "interesting" if else is subject to 
# second if, which I think it is
# What does it print when a = "1" and b = "1" // ANSWER: "interesting"

a, b = "1", "1"
if ( a == int(b) ):
    print("int conversion")
if ( a == int(b) ) and ( str(a) == b ):
    print("int and str conversion")
else:
    print("interesting")

#########################################
############### END AT HOME ##########################
#########################################

# finger exercises
""" Assume you are given a variable named `number` (has a numerical value).
Write a piece of Python code that prints out one of the following strings: 
		- `positive` if the variable `number` is positive
		- `negative` if the variable `number` is negative
		- `zero` if the variable `number` is equal to zero """

number = -6

if number > 0:
    print("positive")
elif number < 0:
	print("negative")
else:
    print("zero")