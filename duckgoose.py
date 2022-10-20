import sys

duck_goose = sys.argv[1:]

def duck(list):
    l = []
    for i in duck_goose:
        if i == 'duck':
            l.append(i)
    print (l)

duck(sys.argv[1:])

