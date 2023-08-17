# Question 1: Reverse a string

def reverse_string(input_string):
    return input_string[::-1]


# Example usage:
input_str = "Hello, World!"
print(reverse_string(input_str))
# Output: "!dlroW ,olleH"

# Question 2: Check for Palindrome


def is_palindrome(input_string):
    return input_string == input_string[::-1]


# Example usage:
input_str = "racecar"
print(is_palindrome(input_str))
# Output: True


# Question 3: Find the maximum element in a list
def find_max_element(lst):
    return max(lst)


# Example usage:
numbers = [5, 10, 2, 30, 15]
print(find_max_element(numbers))
# Output: 30


# Question 5: Check if two strings are anagrams
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)


# Example usage:
word1 = "listen"
word2 = "silent"
print(are_anagrams(word1, word2))
# Output: True


# Question 4: Find the first non-repeated character in a string
def first_non_repeated_char(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1

    for char in input_string:
        if char_count[char] == 1:
            return char
    return None


# Example usage:
input_str = "programming"
print(first_non_repeated_char(input_str))
# Output: "p"
