import sys

def count_vowels(text):
    word = set(text.lower()) #rename for easier identification

    count = 0
    for letter in word: #iterate through word
        if letter in "aeiou": #if "letter" is a vowel, increment
            count += 1
    return count 

print(count_vowels(sys.argv[1]))
