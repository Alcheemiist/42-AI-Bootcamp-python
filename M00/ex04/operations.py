import sys 

res = sys.argv[1:]

if (len(res) < 2):
    print("""Usage: python operations.py <number1> <number2>
    Example:
    python operations.py 10 3""")
    exit(0)

elif (len(res) > 2):
    print("""InputError: too many arguments
    Usage: python operations.py <number1> <number2>
    Example:
    python operations.py 10 3""")
    exit(0)

if not res[0].isdigit() or not res[1].isdigit():
    print("""InputError: only numbers
    Usage: python operations.py <number1> <number2>
    Example:
    python operations.py 10 3""")
    exit(0)

x = float(res[0])
y = float(res[1])
operation = x + y
print("Sum:         " + str(int(operation)))
operation = x - y
print("Difference:  " + str(int(operation)))
operation = x  * y
print("Product:     " + str(int(operation)))
if y== 0:
    operation = "ERROR (div by zero)"
else:
    operation = x / y
print("Quotient:    " + str(operation))
if y== 0:
    operation = "ERROR (modulo by zero)"
else:
    operation = int(x % y)
print("Remainder:   " + str(operation))