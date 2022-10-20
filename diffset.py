import sys


set_a = sys.argv[1:] 
set_b = ['apple', 'banana', 'mango', 'orange']

def difflist(*args):
    temp = []
    for element in set_a:
        if element not in set_b:
            temp.append(element)
            
    print(set(temp))         
        
difflist(sys.argv[1:])
