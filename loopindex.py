import sys
loop_list = sys.argv[1:]


def loops(*args) -> int:
    len1 = []

    for i in range(len(loop_list)):
        len1.append(i)

        x = [x + y for x, y in zip(len1)]

        print(x)
          
    
loops(sys.argv[1:])


