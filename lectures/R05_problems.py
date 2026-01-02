# # Problem 1: Given a list of numbers. Write a function to turn every item of
# # a list into its square.
# from weakref import ref


# def square_list(my_list):
#     # VAO: my code
#     for i in range(len(my_list)):
#         my_list[i] = my_list[i] ** 2
#     return my_list  # this is needed because of how the tests are structured
#     # i.e., the function is not modifying an existing list, but returning it squared


# # test
# print(square_list([1, 2, 3, 4]))
# print(square_list([10, 12, 13]))


# # Problem 2: Write a Python program to concatenate element-wise
# # three given lists of same length
# # Original lists:
# list1 = ["0", "1", "2", "3", "4"]
# list2 = ["red", "green", "black", "blue", "white"]
# list3 = ["100", "200", "300", "400", "500"]
# # Expected output : ['0red100', '1green200', '2black300', '3blue400', '4white500']


# def concatenate_lists(list_a, list_b, list_c):
#     # VAO: my code
#     list_abc = []
#     for i in range(
#         len(list_a)
#     ):  # if one of the assumptions is same length, this is fine
#         list_abc.append(list_a[i] + list_b[i] + list_c[i])
#     return list_abc


# # test
# print(concatenate_lists(list1, list2, list3))


# Problem 3: Write a function to shift a given list to the right or left
# direction by a specified amount. Direction, rotation amount, and a
# list of integers should be inputs to the function.
# e.g.
# Input list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Rotate the input list in left direction by 2:
# [3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
# Rotate the input list in Right direction by 4:
# [7, 8, 9, 10, 1, 2, 3, 4, 5, 6]


# edit this to be "right" or "left"
def rotate_list(input_list, direction, shift):
    # VAO: my code and comments
    # rotation amount can be index modifier; direction can be +/-
    # I kept trying to mutate the list and messing up the iterable I need
    # solution suggests slicing based on index
    shift = shift % len(input_list)  # discarding the excess rotation
    if direction == "left":
        r_list = input_list[shift:] + input_list[:shift]
        return r_list
    elif direction == "right":
        r_list = input_list[-shift:] + input_list[:-4]
        return r_list


# test
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
direction = "right"
print(
    rotate_list(input_list, direction, 14),
    rotate_list(input_list, direction="left", shift=4),
)  # even with defined variable above, this works
