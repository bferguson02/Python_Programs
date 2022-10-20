import sys

def pal(s):

    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            print("It's not a palindrome!")
            return
        else:
            left += 1
            right -= 1
            print("It's a palindrome!")
            return


pal(sys.argv[1])
