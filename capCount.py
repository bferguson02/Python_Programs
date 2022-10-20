import sys


def count_upper_case_letters(str_obj):
    uppers = [i for i, s in enumerate(str_obj) if s.isupper()]

    g = len(uppers)

    y = sum(uppers)

    print(g)
    print(y)


count_upper_case_letters(sys.argv[1])
