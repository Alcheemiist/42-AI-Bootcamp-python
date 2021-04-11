s = "Mehdi"
if (len(s) > 42):
    s = s[:41]
print("-" * (42 - len(s))+s,end="")