t = (0, 4, 132.42222, 100000000, 123455.67555)

day = str(t[0]).zfill(2)
ex = str(t[1]).zfill(2)
arround = round(t[2], 2)
exepo0 = format(t[3], ".2e")
exepo1 = format(t[4], ".2e")

print("day_{day}, ex_{ex} : {arround}, {exepo0}, {exepo1}".format(day=day, ex=ex, arround=arround, exepo0=exepo0, exepo1=exepo1))