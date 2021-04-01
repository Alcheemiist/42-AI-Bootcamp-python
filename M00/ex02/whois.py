
import sys

if (len(sys.argv) == 2):
    if (sys.argv[1].isdigit()):
        if ((int(sys.argv[1]) % 2) == 1):       
             print("Odd")
        elif ((int(sys.argv[1]) == 0)):
            print("I'm Zero")
        else:
            print("Even")
    else :
        print("ERROR")
else :
    print("ERROR")