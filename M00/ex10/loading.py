
import time
import sys

n = 0

def ft_progress(lst):
    for i in lst:
        timee = round(int(i + 1) * 0.01,2)
        percentage = int((i + 1) * 100 / (len(lst)))
        lenght = len(lst)
        ttime = round((lenght * 0.01) - timee,2)

        e = (i + 1) * 20 / lenght 
        s = 20 - e
        e = int(e)
        s = int(s)
        print("ETA: {timee}s [{percentage}%][{tool}>{space}] {i}/{lentgh} | elapsed time {ttime}s".format( timee=timee, percentage=percentage,tool= e * "=" ,space= s * " ",i=i+1,lentgh=lenght,ttime=ttime) , end='\r')
        yield i 
    
 
listy = range(700)
ret = 0

for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)

print()
print(ret)


