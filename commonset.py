import sys
set_a = sys.argv[1:]
set_b = ['apple', 'banana', 'mango', 'orange']


def list_contains(*args):
    match = []

    # Iterate in the 1st list
    for m in set_a:

        # Iterate in the 2nd list
        for n in set_b:

            # if there is a match
            if m == n:
                match.append(m) and match.append(n)

    print(set(match))


list_contains(sys.argv[1:])



