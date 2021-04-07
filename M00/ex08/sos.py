import sys

morse_dict = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': '/'
}


def check(p):
    for argm in p:
        for letter in argm:
            if not (letter.isalnum() or letter.isspace()):
                return -1
    return 0




def print_morse(s):
    for i in range(len(s)):
        if s[i].upper() in morse_dict:
            print(morse_dict[s[i].upper()], end='')
        if i != len(s) - 1:
            print(" ", end='')


args = sys.argv[1:]
if check(args) == -1:
    print("ERROR")
    exit()

for arg in args:
    print_morse(arg)
    if arg != args[-1]:
        print(" / ", end='')

print("")