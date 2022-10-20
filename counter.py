import sys

strlist = {}

def lcount(string):
    for i in string.lower():
        if i in strlist.keys():
            strlist[i] += 1
        else:
            strlist[i] = 1
    print (strlist)

lcount(sys.argv[1])
