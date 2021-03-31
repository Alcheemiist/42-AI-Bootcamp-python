def step_back(x):
  return x[::-1]

import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
r = len(sys.argv)

mytxt = step_back(str)
print(mytxt)