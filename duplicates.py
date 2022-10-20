import sys

duplicated_words = sys.argv[1:]

def words(string):
    nodups = []
    for i in duplicated_words:
        if i not in nodups:
            nodups.append(i)
    nodups.sort(reverse=True)
    print(nodups)

words(sys.argv[1:])
            