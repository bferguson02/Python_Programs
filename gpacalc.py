import sys

def get_grade(grade_list):
    grade_dict = {'A': 4.0, 'A-': 3.66, 'B+': 3.33, 'B': 3.0, 'B-': 2.66, 'C+': 2.33,
                  'C': 2.0, 'C-': 1.66, 'D+': 1.33, 'D': 1.00, 'D-': .66, 'F': 0.00,
                  'a': 4.0, 'a-': 3.66, 'b+': 3.33, 'b': 3.0, 'b-': 2.66, 'c+': 2.33,
                  'c': 2.0, 'c-': 1.66, 'd+': 1.33, 'd': 1.00, 'd-': .66, 'f': 0.00}
    grade= sum([grade_dict[i] for i in grade_list])/(len(grade_list))
    print(f"My GPA is {grade:.2f}")

get_grade(sys.argv[1:])


