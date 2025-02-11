# File Name : analysis_functions.py
# Student Name: Jay Powell
# email: powela9@mail.uc.edu
# Assignment Number: Assignment 04
# Due Date:  2/13/2025
# Course #/Section:  IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Process a list of words, including counting words by prefix and length and identifying the most frequent letter
# Brief Description of what this module does: Functions for word analysis, including counting and letter frequency.
# Citations:
    #https://www.geeksforgeeks.org/python-check-if-string-starts-with-any-element-in-list/
    #Used for the using any() and startswith() function, but we need the total so I replaced any() with sum

    #https://stackoverflow.com/questions/28966495/python-counting-letters-in-string-without-count-function
    #Used a python dictionary to count, had to edit it to apply across all words not just one word. 4th comment down.

    #https://stackoverflow.com/questions/51420726/find-all-words-with-a-given-length-in-python
    #Used list comprehension, the 3rd comment down
# Anything else that's relevant:

def count_total_words(words, prefix):
    """
    Count the total words that start with a particular string
    @param words list: The words to process
    @param prefix string: The prefix to use
    @return the number of words in words that begin with the prefix
    """
    return sum(word.startswith(prefix) for word in words)

def most_frequent_letter(words):
    """
    Find the most frequent letter in a list of words, using case-insensitive logic.
    @param words list: The words to process
    @return list: A 1-element list if there's only one, else a multi-element list if there's a tie.
    """
    # Convert the string to lower case
    lowercase_words = [element.lower() for element in words]
    # Count letters
    dic = {}
    for word in lowercase_words:
        for letter in word:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
    #Find the maximum frequency
    max_freq = max(dic.values())
    #Get all letters
    most_frequent = [letter for letter, count in dic.items() if count == max_freq]
    return most_frequent


def word_count_by_length(words, length):
    """
    Count the number of words that are a specific length
    @param words list: The words to process
    @param length int: The length to test for
    @return int: The number of words that are length characters
    """
    filtered_words = [word for word in words if len(word) == length]
    return len(filtered_words)