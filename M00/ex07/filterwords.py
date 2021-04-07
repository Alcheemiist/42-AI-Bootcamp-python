import sys

number = len(sys.argv)

""" ERRORS """

if (number != 3):
    print("ERROR")
    exit()
elif ( ( (sys.argv[1].isdigit()) == True ) or ( (sys.argv[2].isdigit()) == False)):
    print("ERROR")
    exit()

string = list(sys.argv[1].split(" "))
size = int(sys.argv[2])

for i in list(string):
    num = int(len(i))
    if (num <= size):
      string.remove(i)
print(string)
