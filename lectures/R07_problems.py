# Dictionaries Practice

# Problem 1:
# Write a function that takes as input a dictionary and returns a new dictionary,
# where 5 is added to each value of the original dictionary, assuming all values are integers.
# e.g
# {"item1": 2, "item2": 7, "item3": 20} returns {"item1": 7, "item2": 12, "item3": 25}
def new_dict(input_dict):
    new_d = {}
    for k, v in input_dict.items():
        new_d[k] = v + 5
    return new_d


input_dict = {"item1": 2, "item2": 7, "item3": 20}
print(
    new_dict({"item1": 2, "item2": 7, "item3": 20})
)  # expect {"item1": 7, "item2": 12, "item3": 25}


# Problem 2:
# Write a function to check all values are same in a dictionary.
# Return True if they are all the same, False otherwise
# e.g
# {'item1': 'apple', 'item2': 'apple', 'item3': 'apple'} returns True,
# {'item1': 'apple', 'item2': 'apple', 'item3': 'orange'} return False


def check_same_values(input_dict):
    # VAO: there has to be an easier way?
    temp_v = []
    for k, v in input_dict.items():
        temp_v.append(input_dict[k])
    for i in range(len(temp_v) - 1):
        if temp_v[i] != temp_v[i + 1]:
            return False
    return True


# testing
input_dict = {"item1": "apple", "item2": "apple", "item3": "apple"}
print(check_same_values(input_dict))  # expect True
input_dict = {"item1": "apple", "item2": "apple", "item3": "orange"}
print(check_same_values(input_dict))  # expect False


# Problem 3:
# Convert a dictionary to a list of lists where each sublist is in the
# form [key, value]. Return a sorted version of this list where we sort
# by decreasing values.
# Example input: {'a': 1, 'b': 5, 'c': 10, 'd': 3, 'e': 2}
# Example output: [['c', 10], ['b', 5], ['d', 3], ['e', 2], ['a', 1]]


def dict_to_sorted_list(input_dict):
    # lol = []
    # for k, v in input_dict.items():
    #     lol.append([v, k]) # inverting so I can sort by value first
    # lol.sort(
    #     reverse=True
    # )  # could key work here? specify that you should sort by index 1?
    # inv_lol = lol[:]
    # for i in range(len(inv_lol)):
    #     lol[i] = [inv_lol[i][1], inv_lol[i][0]]
    # return lol
    # VAO: using key, much easier
    lol = []
    for k, v in input_dict.items():
        lol.append([k, v])
    return sorted(
        lol, reverse=True, key=lambda lol: lol[1]
    )  # key looks at each element


# testing
input_dict = {"a": 1, "b": 5, "c": 10, "d": 3, "e": 2}
print(
    dict_to_sorted_list(input_dict)
)  # expect: [['c', 10], ['b', 5], ['d', 3], ['e', 2], ['a', 1]]


# Problem 4:
# Given a list of dictionaries with item names and amounts in the form {'item': 'my_item_name', 'amount': 'my_amount'}
# write function to combine these items into a single dictionary. See example below.
# Example input: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: {'item1': 1150, 'item2': 300}


def combine_dicts(input_dicts):
    consolidated_d = {}
    for d in input_dicts:
        key_value = list(
            d.values()
        )  # fine because part of specification is that I know beforehand the structure of the input_dicts
        if key_value[0] not in consolidated_d:
            consolidated_d[key_value[0]] = key_value[1]
        else:
            consolidated_d[key_value[0]] += key_value[1]
    return consolidated_d


# testing
input_dicts = [
    {"item": "item1", "amount": 400},
    {"item": "item2", "amount": 300},
    {"item": "item1", "amount": 750},
]
print(combine_dicts(input_dicts))  # expect {'item1': 1150, 'item2': 300}
