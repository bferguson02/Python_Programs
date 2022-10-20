import sys

relations = {'Darth Vader': 'father', 'Leia': 'sister', 'Han': 'brother in law',
             'R2D2': 'droid', 'Rey': 'Padawan', 'Tatooine': 'homeworld'}


def luke(x):
    if x == 'Darth Vader':
      print(f"No, I am your {relations['Darth Vader']}")
    else:
      print(f'Luke, I am your {relations[x]}')

luke(sys.argv[1])