# T = int(raw_input())
# lines = []
# for i in range(T):
#     lines.append(raw_input())
#
# numbers = []
# bigNumber = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
# for line in lines:
#     numbers = []
#     for i in range(10):
#         hasi = True
#         for j in bigNumber[i]:
#             if j not in line:
#                 hasi = False
#                 break
#         if hasi:
#             if i<8:
#                 numbers.append(i+10-8)
#             else:
#                 numbers.append(i-8)
#
#             for k in bigNumber[i]:
#                 pos = line.find(k)
#                 line = line[0:pos]+line[pos+1:]
#
#     numbers.sort()
#     print "".join([str(i) for i in numbers])




n = int(raw_input())
m = dict()
ss = set()
while len(ss)<n:
    x,y = raw_input().strip().split()

    s = m.get(x,[])
    s.append(y)
    m[x] = s
    ss.add(x)
    ss.add(y)

key = '0'
values = m.get('0')

step = 1
while values:
    key = values[0]
    values = m.get('key')
    step+=1
print step+1