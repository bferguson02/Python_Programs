import sys

fam = {'Brandy' : 'Mom',
       'Cohen' : 'Son'}

def relation():
    print(sys.argv[1], 'is the', fam[sys.argv[1]])


relation()
