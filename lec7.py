#####################
## reading
#####################
# finger exercise, p 69: Use the find_root function in Figure 4-3 to print the sum
# of approximations to the square root of 25, the cube root of -8, and the fourth root
# of 16. Use 0.001 as epsilon.
# VAO: my code here
# def find_root (x, power, epsilon):
#     # Find interval containing answer
#     if x < 0 and power % 2 == 0:
#         return None # Negative number has no even-powered roots
#     low = min(-1, x)
#     high = max(1, x)
#     # Use biseciton search
#     ans = (high + low) / 2
#     while abs(ans ** power - x) >= epsilon:
#         if ans ** power < x:
#             low = ans
#         else:
#             high = ans
#         ans = (high + low) / 2
#     return ans
# xs = (25, -8, 16)
# powers = (2, 3, 4)
# e = 0.001
# pwr_index = 0 # hah, this works! maybe there's a better way of doing this, but I'm happy as is
# for x in xs:
#     answer = find_root(x, powers[pwr_index], e)
#     print(f"approximate root of {x} on power {powers[pwr_index]} is {answer}")
#     pwr_index += 1

# finger exercise, p 69: Write a function is_in that accepts two strings as arguments and returns
# 'True' if either string occurs anywhere in the other, and 'False' otherwise. Hint: you might want
# to use the built-in 'str' operator 'in'.
# VAO: my code here
def is_in(str1, str2):
    if str1 in str2 or str2 in str1: # I understand the prompt to be "if the entire string occurs", not only part of it
                                     # i.e., so this works. If it's meant to be partial matches, then it needs a loop
        return True
    else:
        return None
# string1 = str(input("enter the first string: "))
# string2 = str(input("enter the second string: "))
# print(is_in(string1, string2))

# finger exercise, p 69: Write a function to test 'is_in'.
# VAO: my code here
def test_is_in(strs1, strs2):
    for s1 in strs1:
        for s2 in strs2:
            result = is_in(s1, s2)
            if result is None:
                if s1 in s2 or s2 in s1:
                    test = "oops"
                else:
                    test = "good"
            else:
                if s1 in s2 and s2 in s1:
                    test = "good"
                else:
                    test = "oops"
            print(s1, s2, result, test)

string1 = ("abc", "jkl", "ghi")
string2 = ("jkl", "mno", "abc")
test_is_in(string1, string2)

# finger exercise , p 72: Write a function 'mult' that accepts either one or two ints as arguments. If called
# with two arguments, the function prints the product of the two arguments. If called with one argument, it prints
# that argument.
# VAO: my code here
def mult(int1, int2 = None): # I had it as false at first, but then changing it to true doesn't assign any value
    if int2 is not None:
        print(int1 * int2)
    else:
        print(int1)
# now testing it
ints1 = (0, 1, 2, 3, 4, 5)
ints2 = (None, 5, None, 8, None, 17)
for i in ints1:
    for ii in ints2:
        mult(i, ii)

# finger exercise, p. 82: Using the algorithm of Figure 3-6, write a function that satisfies the specification
# def log(x, base, epsilon): "Assumes x and epsilon int or float, base an int, x > 1, epsilon > 0, power >= 1.
# Returns float y such that base **y is within epsilon of x."
# Figure 3-6
# Find lower bound on ans
# x = input("enter integer: ")
# epsilon = 0.01
# lower_bound = 0
# while 2 ** lower_bound < x:
#     lower_bound += 1
# low = lower_bound - 1
# high = lower_bound + 1
# # Perform bisection search
# ans = (high + low) / 2
# while abs(2 ** ans - x) >= epsilon:
#     if 2 ** ans < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low) / 2
# print(ans, "is close to the log base 2 of", x)

# VAO: my code here
def log(x, base, epsilon):
    lower_bound = 0
    while base ** lower_bound < x:
        lower_bound += 1
    low = lower_bound - 1
    high = lower_bound + 1
    ans = (high + low) / 2
    while abs(base ** ans - x) >= epsilon:
        if base ** ans < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    print(ans, "is close to the log base", base, "of", x)
# testing
bases = (2, 3, 5)
xs = (10, 20, 30)
for b in bases:
    for x in xs:
        log(x, b, 0.01)

#####################
## lecture
#####################

# ###########################
# #### EXAMPLE: applying functions to repeat same task many times
# ###########################
# #A very simple example of a function that has one
# #argument and returns one value
# def is_even(i):   
#     """Assumes: i, a positive int
#     Returns True if i is even, otherwise False"""
#     if i%2 == 0:
#         return True
#     else:
#         return False

# # is_even(3) # <- returns False
# # is_even(8) # <- returns True

# # print(is_even(3)) # <- prints False
# # print(is_even(8)) # <- prints True



# ############## YOU TRY IT ###################
# # Write code that satisfies the following specification:
def div_by(n, d):
#     """ n and d are ints > 0
#         Returns True if d divides n evenly and False otherwise 
#     """
#     # your code here
      # VAO: my code
    return n % d == 0

# # For example: 
print(div_by(10,3))     # print False
print(div_by(195,13))   # returns True

# ##############################################

# # # Using the is_even function later on in the code
# # print("Numbers between 1 and 10: even or odd")

# # for i in range(1,10):
# #     if is_even(i):
# #         print(i, "even")
# #     else:
# #         print(i, "odd")



# ###########################
# ### EXAMPLE: sum of all odd numbers between (including) a and b
# ###########################
# ## with a for loop
# def sum_odd(a, b):
#     sum_of_odds = 0
#     for i in range(a, b+1):
#         if i%2 == 0:
#             sum_of_odds += i
#             print(i, sum_of_odds)
#     return sum_of_odds

# # print(sum_odd(2,4)) 
# # print(sum_odd(2,7)) 

# # # with a while loop
# def sum_odd(a, b):
#     sum_of_odds = 0
#     i = a
#     while i <= b:
#         if i%2 == 1:
#             sum_of_odds += i
#         i += 1
#     return sum_of_odds

# # print(sum_odd(2,4)) 
# # print(sum_odd(2,7)) 


# ############## YOU TRY IT ###################
# # Write code that satisfies the following specification:
# # Hint, use paper and pen for a strategy before coding!
# def is_palindrome(s):
#     """ s is a string
#     Returns True if s is a palindrome and False otherwise
#     """
#     # your code here

# ################################################

# ################################################
# ################ YOU TRY IT AT HOME #####################
# ################################################
# # 1. Write code that satisfies the following specs:
# def keep_consonants(word):
#     """ word is a string of lowercase letters
#         Returns a string containing only the consonants 
#         of word in the order they appear
#     """
#     # your code here

# # For example
# # print(keep_consonants("abcd"))  # prints bcd
# # print(keep_consonants("aaa"))  # prints an empty string
# # print(keep_consonants("babas"))  # prints bbs



# # 2. Write code that satisfies the following specs:
# def first_to_last_diff(s, c):
#     """ s is a string, c is single character string
#         Returns the difference between the index where c first
#         occurs and the index where c last occurs. If c does not 
#         occur in s, returns -1. 
#     """
#     # your code here

# # For example
# # print(first_to_last_diff('aaaa', 'a'))  # prints 3
# # print(first_to_last_diff('abcabcabc', 'b'))  # prints 6
# # print(first_to_last_diff('abcabcabc', 'b'))  # prints -1


# ################################################
# ################################################
# ################################################

# ################################################
# ########## ANSWERS TO YOU TRY IT #######
# ################################################
# # def div_by(n, d):
# #     """ n and d are ints > 0
# #         Returns True if d divides n evenly and False otherwise 
# #     """
# #     # your code here
# #     # one way
# #     if n%d==0:
# #         return True
# #     else:
# #         return False
# #     # another way: 
# #     # return n%d==0
    
# # print(div_by(10,3))    
# # print(div_by(195,13))    


# # def is_palindrome(s):
# #     """ s is a string
# #     Returns True if s is a palindrome and False otherwise
# #     """
# #     # your code here
# #     for i in range(len(s)//2):
# #         if s[i] != s[len(s)-i-1]:
# #             return False
# #     return True        

# # s="2222"
# # print(is_palindrome(s))

# # s="222"
# # print(is_palindrome(s))

# # s="abc"
# # print(is_palindrome(s))


# ################################################
# ########## ANSWERS TO YOU TRY IT AT HOME #######
# ################################################
# def keep_consonants(word):
#     """ word is a string of lowercase letters
#         Returns a string containing only the consonants 
#         of word in the order they appear
#     """
#     vowels = "aeiou"
#     ans = ""
#     for char in word:
#         if char not in vowels:
#             ans += char
#     return ans

# # For example:
# # print(keep_consonants("abcd"))  # prints bcd
# # print(keep_consonants("aaa"))  # prints an empty string
# # print(keep_consonants("babas"))  # prints bbs


# def first_to_last_diff(s, c):
#     """ s is a string, c is single character string
#         Returns the difference between the index where c first
#         occurs and the index where c last occurs. If c does not 
#         occur in s, returns -1. 
#     """
#     if c not in s:
#         return -1
#     # if reach here, c is in s
#     for i in range(len(s)):
#         if s[i]==c:
#             # break here to save i as the first instance of c in s
#             break
#     # loop through s backwards
#     for j in range(len(s)-1,-1,-1):
#         if s[j]==c:
#             # break here to save j as the last instance of c in s
#             break
#     # this return is ok becasue the loops iterated through indices not chars of s
#     return j-i

# # For example
# # print(first_to_last_diff('aaaa', 'a'))  # prints 3
# # print(first_to_last_diff('abcabcabc', 'b'))  # prints 6
# # print(first_to_last_diff('xyz', 'b'))  # prints -1

# ################################################
# ################################################
# ################################################




