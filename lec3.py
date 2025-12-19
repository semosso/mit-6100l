# ##################
# ## reading
# ##################

# finger exercise, p 36: Replace the comment in the following code with a while loop
# num_X = int(input("How many times should I print the letter X? "))
# to_print = ""
# # concatenate X to to_print num_x times
# while len(to_print) < num_X:
#     to_print += "X"
# print (to_print)

# finger exercise, p 36: Write a program that asks the user to input 10 integers, and then prints the largest odd number that was entered.
# If no odd number was entered, it should print a message to that effect.

# first, break example from the book: Find a positive integer that is divisable by both 11 and 12
# x = 1
# while True:
#     if x%11 == 0 and x%12 == 0:
#         break
#     x = x + 1
# print (x, "is divisible by 11 and 12")

# # however, I can do the same w/o break, no? I get that break might be useful in other uses, but I don't get what the difference was here
# x = 1
# while x%11 != 0 or x%12 != 0:
#     x = x + 1
# print (x, "is divisible by 11 and 12")

# # now to the finger exercise
# counter = 0
# num = int(input("enter ten integers, one at a time: "))

# if num % 2 != 0: # tem como colocar dentro do while loop? não sei. fora é bom que cria uma variável de largada e independente da recursão
#     answer = num
# else: answer = "no odd entered"

# while counter < 9:
# 	num = int(input("enter ten integers, one at a time: "))
# 	if num % 2 != 0 and (type(answer) == str or num > answer): # aqui foi só inverter; se a primeira operação processada é a int > str, erro; se a outra, não
# 		answer = num
# 	counter += 1
# print(answer) # se eu quisse dar uma garibada aqui, incluir uma leading sentence, talvez teria mais um if pra checar o que é answer aqui

# finger exercise, p 40: Write a program that prints the sum of the prime numbers greater than 2 and less than 1000. Hint: you probably want to use a for loop that is a primality test
# nested inside a for loop that iterates over the odd integers between 3 and 999.

# ANSWER: similar to variable in loop issue above, what was happening is that the primality tester would run multiple tests (as intended, inside for) to check for it; and if adding the number to the sum was
# simply a result of those testings failing (i.e., % != 0), that happened multiple cases, so sum was always being increased. I tried on my own to fix with "break", but couldn't do it until I saw the
# variable idea on https://www.geeksforgeeks.org/python/python-program-to-check-whether-a-number-is-prime-or-not/ and that worked. I also got the prime testing formula online, from the same website
# since I was using a brute force (AND INCOMPLETE, WHICH I REALIZED ON MY OWN) one earlier - e.g., calling specific divisions vs. 3, 5, 7 (incomplete because other numbers, e.g., 121 - 11*11)

# prime_sum = 0

# for num in range(3, 1000):
#     is_prime = True           
#     for x in range(2, int(num**0.5) + 1):
#         if num % x == 0:
#             is_prime = False
#             break
#     if is_prime == True: prime_sum += num
#     print(num, is_prime, prime_sum)

# print(prime_sum)

# ## lecture
# ##################
# Tou can uncomment each of these examples
# and try running them yourself

# To batch comment/uncomment, select the lines and then
# on Windows hit CTRL+1 or on Mac hit CMD+1
# ##################


# ##################
# EXAMPLE: while loops
# ###################
# where = input("You are in the Lost Forest. Go left or right? ")
# while where == "right":
#     where = input("You are in the Lost Forest. Go left or right? ")
# print("You got out of the Lost Forest! \o/")


###########################################

# Fun Lost Forest code, run it on your own!
# where = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
# while where.lower() == "right":
#    where = input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯\n     ︵ \n    ┻━┻\n****************\n****************\nGo left or right? ")
# print("\nYou got out of the Lost Forest!\n\o/")


###########
## EXAMPLE
###########
# n = int(input('Please enter a non-negative integer: '))
# while n > 0:
#     print('x')
#     n = n-1  # the same as n -= 1


################ YOU TRY IT ###################
## EXAMPLE: infinite loop, be careful!
# To stop it, click the shell and hit CTRL+c or
# the red square at the top of the shell
##############################################
# while True:
#     print("noooooooo")


############### YOU TRY IT ################
# Expand this code to show a sad face when the user entered
# the while loop more than 2 times. Hint: use a counter
##################
# where = input("Go left or right? ")
# counter = 0 # if inside while loop, gets erased/reset by the loop; whether it should be 0 or 1, depends on how the code is written
#             # i.e., think before writing

# while where == "right":
#     counter += 1
#     where = input("Go left or right? ")
#     if counter >= 2: print(":(")
# print("You got out!")


#############
## EXAMPLE: counter
#############

## With while loop
# n = 0
# while n < 5:
#     print(n)
#     n = n+1

## With for loop
# for n in range(5):
#    print(n)

###########
## EXAMPLE: factorial
###########

## With while loops
# x = 6
# i = 1
# factorial = 1
# while i <= x:
#     factorial *= i
#     i += 1
# print(f'{x} factorial is {factorial}')

## With for loops
# factorial = 1
# for i in range(1, x+1, 1):
#     factorial *= i
# print(f'{x} factorial is {factorial}')


################ YOU TRY IT ################
# for i in range(1,4,1):
#     print(i)
# for j in range(1,4,2):
#     print(j*2)
# for me in range(4,0,-1):
#     print("$"*me)


###########################################

###############
## EXAMPLE: sum
###############

# mysum = 0
# for i in range(10):
#    mysum += i
# print(mysum)

######

# mysum = 0
# for i in range(7, 10):
#    mysum += i
# print(mysum)

######

# mysum = 0
# for i in range(5, 11, 2):
#    mysum += i
#    if mysum == 5:
#        break
#        mysum += 1
# print(mysum)

################ YOU TRY IT ################
# Fix this code to use variables start and end in the
# range, to get the total sum between and including those values.

# mysum = 0
# start = 3
# end = 5
# for i in range(start, end + 1): # end + 1 fixes it
#     mysum += i
# print(mysum)

###########################################


#########################################################
##################### AT HOME ###########################
#########################################################

# Finger Exercise:
# Assume you are given a positive integer variable named `N`.
# Write a piece of Python code that prints `hello world` on separate lines, `N` times.
# You can use either a `while` loop or a `for` loop.

N = 2
counter = 0

while counter < N:
    print("Hello world\n")
    counter += 1

for x in range(N):
    print("Hello world\n")

# Practice 1:
# Declare a variable x that stores an int > 0. Print all ints, one on each
# line, between 1 (inclusive) and x (inclusive) that are divisible by 5.
# For ex. if x = 15, it prints 5, 10, and 15.
# For ex. if x = 14, it prints 5 and 10.

# x = 22

# for num in range(1, x + 1):
#     if num % 5 == 0: print(f"{num}\n")

# Practice 2:
# Declare a variable n that stores an int. Print the sum of all digits
# in n. Hint: you can get a digit at a time looking at the remainder
# when you divide n by 10.
# For ex. If x = 1234, print 10

# n = 999999
# digit_sum = 0

# for x in str(n): # interessante a solução usando module e floor div de 10, mas muito mais fácil assim
#     digit_sum += int(x)
# print(digit_sum)

#########################################################
##################### END AT HOME ###########################
#########################################################


#########################################################
##################### ANSWERS AT HOME ###########################
#########################################################

# Practice 1:
# Declare a variable x that stores an int > 0. Print all ints, one on each
# line, between 1 (inclusive) and x (inclusive) that are divisible by 5.
# For ex. if x = 15, it prints 5, 10, and 15. If x = 14, it prints 5 and 10.

# x = 15
# for i in range(1,x+1):
#     if i%5 == 0:
#         print(i)


# Practice 2:
# Declare a variable n that stores an int. Print the sum of all digits
# in n. Hint: you can get a digit at a time looking at the remainder
# when you divide n by 10.
# For ex. If x = 1234, print 10
# n = 1234
# total = 0
# while True:
#     r = n%10
#     total += r
#     n = n//10
#     if n == 0:
#         break
# print(total)

#########################################################
##################### END ANSWERS AT HOME ###########################
#########################################################


#########################################
############### ANSWERS TO LECTURE ##########################
#########################################
# You Try It 1:
# Expand this code to show a sad face when the user entered
# the while loop more than 2 times. Hint: use a counter
###################
# where = input("Go left or right? ")
# counter = 0
# while where == "right":
#     counter = counter + 1
#     if counter > 2:
#         print(":(")
#     where = input("Go left or right? ")
# print("You got out!")


# Your Try It 2:
# Fix this code to use variables start and end in the
# range, to get the total sum between and including those values.

# mysum = 0
# start = 1
# end = 3
# for i in range(start, end+1):
#     mysum += i
# print(mysum)

#########################################
############### END ANSWERS TO LECTURE ##########################
#########################################
