import sys 

def get_input():
    txt = ""
    print("text to analyze")
    for line in sys.stdin:
        txt += line
    return txt


def text_analyzer(*text):

    """
      ------------------------------------------------------------
    | This function counts the number of upper characters,        |
    | lower characters, punctuation and spaces in a given text.   |
      ------------------------------------------------------------
    """
    if (len(text) > 1):
        print("ERROR")
        exit()
    elif len(text) == 0:
        txt = get_input()
    else :
        txt = text[0]

    lent = len(txt) 
    print ("this text contain " ,lent, "characters :")
    p = l = u = s = 0  
    for i in txt:
        if str(i) == ('.') or str(i) == (',') or str(i) == ('?') or str(i) == ('!') or str(i) == (',') or str(i) == ("'") or str(i) == ("-") :
           p += 1 
        elif str(i).isupper():
            u += 1
        elif str(i).islower():
            l += 1
        elif str(i).isspace():
            s += 1
    print ("- pon = ", p)
    print ("- UPPER = ", u)
    print ("- lower = ", l)
    print ("- space = ", s)
    print(" p + u + l + s =", u + p + l + s)


text_analyzer()