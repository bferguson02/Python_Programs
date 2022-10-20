import sys

my_ints = sys.argv[1:]
my_ints = list(map(int, my_ints))

def comp(*my_ints):

    #my_ints = list(map(int, my_ints))

    for num in my_ints:
        #my_ints = list(map(int, my_ints))
        if num % 3 == 0:
            my_ints.remove(num)
            my_ints.append(num * 10)

            new = my_ints
            print(new)


comp(sys.argv[1:])
