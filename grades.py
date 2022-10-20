import sys

grades = {'Biology':80, 'Physics':88, 'Chemistry':98, 'Math':89, 'English':79, 'Music':67, 'History':68, 'Art':53, 'Economics':95, 'Psychology':88}

def g (x):
  y = {}
  for key, value in grades.items():
    if key != x:
      y[key] = value
  mean = sum(y.values()) / len(y)
  mean1 = round(mean, 2)
  print(mean1)

g(sys.argv[1])

