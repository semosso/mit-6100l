# 6.100A Fall 2022
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name:
# Collaborators:

# Purpose: Check for similarity between two texts by comparing different kinds of word statistics.
# from IPython.testing.plugin.test_ipdoctest import doctest_builtin_underscore
# from wsgiref.types import FileWrapper

import string
import math


### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    # print("Loading file %s" % filename)
    inFile = open(filename, "r")
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()


### Problem 0: Prep Data ###
def text_to_list(input_text):
    """
    Args:
        input_text: string representation of text from file.
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    return [e for e in input_text.split()]


### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):
    """
    Args:
        input_iterable: a string or a list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in input_iterable and the corresponding int
        is the frequency of the letter or word in input_iterable
    Note:
        You can assume that the only kinds of white space in the text documents we provide will be new lines or space(s) between words (i.e. there are no tabs)
    """
    frequency_dict = {}
    for e in input_iterable:
        if e in frequency_dict:
            frequency_dict[e] += 1
        else:
            frequency_dict[e] = 1
    return frequency_dict


### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    """
    Args:
        word: word as a string
    Returns:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word
    """
    return get_frequencies(word)


### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary of letters of word1 or words of text1
        freq_dict2: frequency dictionary of letters of word2 or words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    # VAO: super ugly, but works, so I guess YAY?! revisit at the end
    DIFF = 0
    ALL = 0
    unique_elements = []
    for e in [
        [e1 for e1 in freq_dict1 if e1 not in freq_dict2],
        [e2 for e2 in freq_dict2 if e2 not in freq_dict1],
    ]:
        unique_elements.extend(e)
    common_elements = [e for e in freq_dict1 if e in freq_dict2]

    for e in unique_elements:
        if e in freq_dict1:
            DIFF += freq_dict1[e]
        if e in freq_dict2:
            DIFF += freq_dict2[e]

    for e in common_elements:
        DIFF += abs(freq_dict1[e] - freq_dict2[e])

    for e in freq_dict1:
        ALL += freq_dict1[e]

    for e in freq_dict2:
        ALL += freq_dict2[e]

    return round((1 - (DIFF / ALL)), ndigits=2)


### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary for one text
        freq_dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    merged_dict = {}

    # VAO: loads of aliasing, but should I care? I think I can do it without merged_dict
    for k, v in freq_dict1.items():
        merged_dict[k] = v
    for k, v in freq_dict2.items():
        if k in merged_dict:
            merged_dict[k] += v
        else:
            merged_dict[k] = v
    values_list = [e for e in merged_dict.values()]
    values_list.sort()
    return [
        k for k, v in merged_dict.items() if v == max(values_list)
    ]  # sorted alphabetically?


### Problem 5: Finding TF-IDF ###
def get_tf(file_path):
    """
    Args:
        file_path: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculatd as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_frequencies from earlier
    """
    words_list: list = text_to_list(load_file(file_path))
    frequency: dict = get_frequencies(words_list)
    total_num = 0
    for k in frequency:
        total_num += frequency[k]
    tf_dict = {}  # just to avoid aliasing
    for k in frequency:
        tf_dict[k] = frequency[k] / total_num
    return tf_dict


def get_idf(file_paths):
    """
    Args:
        file_paths: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculated as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()

    """
    # VAO: total number of docs is straightforward
    num_docs = 0
    for e in file_paths:
        num_docs += 1

    # opens each file, stores each string as a list in docs_list
    docs_list = []
    for f in file_paths:  # for file in list of names of files
        docs_list.append(text_to_list(load_file(f)))

    # for each doc in list, if word in doc, add k(word), v(+1) to dict
    ref_dict = {}
    for f in docs_list:
        temp = get_frequencies(f)
        for k in temp:
            if k not in ref_dict:
                ref_dict[k] = 1
            else:
                ref_dict[k] += 1

    # calculate IDF in dict; I could do it together with above, but baby steps
    idf_dict = {}
    for k, v in ref_dict.items():
        idf_dict[k] = math.log10(num_docs / v)

    return idf_dict


def get_tfidf(tf_file_path, idf_file_paths):
    """
    Args:
        tf_file_path: name of file in the form of a string (used to calculate TF)
        idf_file_paths: list of names of files, where each file name is a string
        (used to calculate IDF)
    Returns:
       a sorted list of tuples (in increasing TF-IDF score), where each tuple is
       of the form (word, TF-IDF). In case of words with the same TF-IDF, the
       words should be sorted in increasing alphabetical order.

    * TF-IDF(i) = TF(i) * IDF(i)
    """
    # VAO: initiate TF and IDF dicts
    TF_dict, IDF_dict = get_tf(tf_file_path), get_idf(idf_file_paths)

    # calculate TFIDF and include in dicts
    TFIDF_dict = {}
    for k in TF_dict:
        TFIDF_dict[k] = TF_dict[k] * IDF_dict[k]

    # create list of tuples with word, TFIDF
    unsorted_list_TFIDF = []
    for k, v in TFIDF_dict.items():
        unsorted_list_TFIDF.append((k, v))

    # sorting by TFIDF, low to high
    sorted_by_tuple = sorted(unsorted_list_TFIDF, key=lambda x: x[1])
    return sorted_by_tuple  # I was returning with list_TFIDF.sort() and surprised I got none... rookie


if __name__ == "__main__":
    pass
    ###############################################################
    ## Uncomment the following lines to test your implementation ##
    ###############################################################

    # Tests Problem 0: Prep Data
    test_directory = "tests/student_tests/"
    hello_world, hello_friend = (
        load_file(test_directory + "hello_world.txt"),
        load_file(test_directory + "hello_friends.txt"),
    )
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    print(world)  # should print ['hello', 'world', 'hello']
    print(friend)  # should print ['hello', 'friends']

    ## Tests Problem 1: Get Frequencies
    test_directory = "tests/student_tests/"
    hello_world, hello_friend = (
        load_file(test_directory + "hello_world.txt"),
        load_file(test_directory + "hello_friends.txt"),
    )
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    world_word_freq = get_frequencies(world)
    friend_word_freq = get_frequencies(friend)
    print(world_word_freq)  # should print {'hello': 2, 'world': 1}
    print(friend_word_freq)  # should print {'hello': 1, 'friends': 1}

    ## Tests Problem 2: Get Letter Frequencies
    freq1 = get_letter_frequencies("hello")
    freq2 = get_letter_frequencies("that")
    print(freq1)  #  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    print(freq2)  #  should print {'t': 2, 'h': 1, 'a': 1}

    ## Tests Problem 3: Similarity
    test_directory = "tests/student_tests/"
    hello_world, hello_friend = (
        load_file(test_directory + "hello_world.txt"),
        load_file(test_directory + "hello_friends.txt"),
    )
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    world_word_freq = get_frequencies(world)
    friend_word_freq = get_frequencies(friend)
    word1_freq = get_letter_frequencies("toes")
    word2_freq = get_letter_frequencies("that")
    word3_freq = get_frequencies("nah")
    word_similarity1 = calculate_similarity_score(word1_freq, word1_freq)
    word_similarity2 = calculate_similarity_score(word1_freq, word2_freq)
    word_similarity3 = calculate_similarity_score(word1_freq, word3_freq)
    word_similarity4 = calculate_similarity_score(world_word_freq, friend_word_freq)
    print(word_similarity1)  # should print 1.0
    print(word_similarity2)  # should print 0.25
    print(word_similarity3)  # should print 0.0
    print(word_similarity4)  # should print 0.4

    ## Tests Problem 4: Most Frequent Word(s)
    freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
    most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
    print(most_frequent)  # should print ["hello", "world"]

    ## Tests Problem 5: Find TF-IDF
    tf_text_file = "tests/student_tests/hello_world.txt"
    idf_text_files = [
        "tests/student_tests/hello_world.txt",
        "tests/student_tests/hello_friends.txt",
    ]
    tf = get_tf(tf_text_file)
    idf = get_idf(idf_text_files)
    tf_idf = get_tfidf(tf_text_file, idf_text_files)
    print(tf)  # should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    print(
        idf
    )  # should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    print(tf_idf)  # should print [('hello', 0.0), ('world', 0.10034333188799373)]
