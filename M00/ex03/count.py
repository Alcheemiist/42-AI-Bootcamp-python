def text_analyzer(text):
    lent = len(text) 
    print ("this text fcontain " ,lent, "characters :")
    p = l = u = s = 0  
    for i in text:
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

text_analyzer("Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.")
