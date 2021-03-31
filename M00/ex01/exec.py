def step_back(x):
  return x[::-1]

import sys
sent_str = ""
for i in sys.argv[1:]:
    sent_str += str(i) + " "

print(step_back(sent_str.strip()))