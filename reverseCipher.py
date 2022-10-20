message =   '.daed era meht fo owt fi ,terces a peek nac eerhT'
translated = ' '
i = len(message) -1
#len(message) is a function call to the len() function, which accepts
#a string argument, like print(), and returns an integer value of how many
#characters are in the string (that is, the length of the string).
while i >= 0:
    translated = translated + message[i]
    i = i -1
print(translated)
