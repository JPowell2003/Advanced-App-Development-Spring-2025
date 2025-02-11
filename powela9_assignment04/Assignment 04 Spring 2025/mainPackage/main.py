# File Name : main.py
# Student Name: Jay Powell
# email: powela9@mail.uc.edu
# Assignment Number: Assignment 04
# Due Date:  2/13/2025
# Course #/Section:  IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Process a list of words, including counting words by prefix and length and identifying the most frequent letter
# Brief Description of what this module does: Reads words from a english-2 and analyzes them using different functions
# Citations:
# Anything else that's relevant:


from utilities_package.english_utilities import *
from word_analysis.analysis_functions import *


if __name__ == "__main__":
    words = read_words()
    print(len(words), "words read from file")
    
    print("Total words that start with S:", count_total_words(words, "S"))

    mfl = most_frequent_letter(words)
    print("Most frequent letter(s):")
    for l in mfl:
        print(l)

    count = word_count_by_length(words, 10)
    print(count, "words are 10 characters in length")

    # Test case for most_frequent_letter with a tie between multiple letters
    print("Testing most_frequent_letter with a tie:")
    test_words_tie = [
        "aaab", "bbbc", "ccca", "ddda", "bbb", "ccc", "ddd"
    ]
    print("Most frequent letter(s):", most_frequent_letter(test_words_tie))
    
