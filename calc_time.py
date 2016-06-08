import time

t = time.time()
print t
day = t//(60*60*24)
hour = (t%(60*60*24))//(60*24)
mine = ((t%(60*60*24))%(60*24))//60
sec = ((t%(60*60*24))%(60*24))%60
print day,hour,mine,sec