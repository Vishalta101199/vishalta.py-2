import string
from xml.dom.expatbuilder import theDOMImplementation


Python Program to calculate total number of vowels and count of each individual vowels
def count_vowels(text):
    vowels = 'AEIOU'
    count_total = 0
    count_individual = {vowel: 0 for vowel in vowels}
    
    for char in text:
        if char.upper() in vowels:
            count_total += 1
            count_individual[char.upper()] += 1
            
    return count_total, count_individual

input_text = "Guvi Geeks Network Private Limited"
total_vowels, individual_counts = count_vowels(input_text)

print("Total number of vowels:", total_vowels)
print("Count of each individual vowel:")
for vowel, count in individual_counts.items():
    print(vowel, ":", count)

    Create a pyramid of numbers from 1 to 20
    rows = 5
number = 1
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
    for j in range(1, i + 1):
        print(number, end=" ")
        number += 1
    print()

    Program that takes takes a string and returns a new string
    def remove_vowels(input_str):
    vowels = "aeiouAEIOU"
    return "".join(char for char in input_str if char not in vowels)
input_str = input("Enter a string: ")
result = remove_vowels(input_str)
print("String with vowels removed:", result)

Python program that takes a string and returns true if it is palindrome 
def is_palindrome(input_str):
    # Convert the input string to lowercase and remove spaces
    input_str = input_str.lower().replace(" ", "")
    # Check if the string is equal to its reverse
    return input_str == input_str[::-1]

input_str = input("Enter a string: ")
result = is_palindrome(input_str)
print("Is palindrome:", result)

Program that takes two strings and returns the longest common substring between them
def longest_common_substring(str1, str2):
    # Initialize a 2D table to store lengths of longest common suffixes
    m = len(str1)
    n = len(str2)
    table = [[0] * (n + 1) for _ in range(m + 1)]

    # Variables to store the length of the longest common substring
    max_length = 0
    end_index = 0

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > max_length:
                    max_length = table[i][j]
                    end_index = i
            else:
                table[i][j] = 0

    # The longest common substring is from end_index - max_length to end_index in str1
    return str1[end_index - max_length:end_index]

# Example usage:
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

result = longest_common_substring(str1, str2)
print("Longest common substring:", result)

Program that takes a string and returns the most frequent character in it
def most_frequent_character(input_str):
    char_frequency = {}
    
    # Count the frequency of each character in the string
    for char in input_str:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    
    # Find the character with the maximum frequency
    max_frequency = 0
    most_frequent_char = None
    for char, frequency in char_frequency.items():
        if frequency > max_frequency:
            max_frequency = frequency
            most_frequent_char = char
    
    return most_frequent_char

input_str = input("Enter a string: ")
result = most_frequent_character(input_str)

if result:
    print("Most frequent character:", result)
else:
    print("The string is empty.")

Program that takes two strings and returns the longest common substring between two substrings
def longest_common_substring(str1, str2):
    # Initialize a matrix to store lengths of longest common suffixes
    m = len(str1)
    n = len(str2)
    # Initialize a variable to store the length of the longest common substring
    max_length = 0
    # Initialize a variable to store the ending index of the longest common substring
    end_index = 0
    # Initialize a matrix to store the lengths of longest common suffixes
    lcs_matrix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                lcs_matrix[i][j] = lcs_matrix[i - 1][j - 1] + 1
                if lcs_matrix[i][j] > max_length:
                    max_length = lcs_matrix[i][j]
                    end_index = i
            else:
                lcs_matrix[i][j] = 0

    # The longest common substring is from end_index - max_length to end_index
    return str1[end_index - max_length:end_index]

# Example usage:
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

result = longest_common_substring(str1, str2)
print("Longest common substring:", result)

program that takes string and returns true if it is an anagram of another string
def is_anagram(str1, str2):
    # Convert both strings to lowercase and remove spaces
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    
    # If the lengths of the strings are different, they cannot be anagrams
    if len(str1) != len(str2):
        return False
    
    # Sort the characters in both strings and compare them
    return sorted(str1) == sorted(str2)

# Example usage:
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

result = is_anagram(str1, str2)
print("Are the strings anagrams:", result)

program that takes string and returns the number of words in it
def count_words(input_str):
    # Split the string into words based on whitespace
    words = input_str.split()
    # Return the number of words
    return len(words)

input_str = input("Enter a string: ")
word_count = count_words(input_str)
print("Number of words:", word_count)
