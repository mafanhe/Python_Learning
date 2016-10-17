import random

def histogram(t):
    d = dict()
    for i in t:
        d[i] = d.get(i,0)+1
    return d

def choose_from_hist(d):
    t = []
    for i in d:
        t.extend([i]*d.get(i))
    j = random.choice(t)
    return j

t=['a','a','b','c']
hist = histogram(t)
print(hist)
print(choose_from_hist(hist))
