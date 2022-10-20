import sys


def short(str_obj):
    shortest = min((str_obj).split(), key=len)
    shortestU = shortest.upper()

    print ("The shortest word is", shortestU)

short(sys.argv[1])

   


    
