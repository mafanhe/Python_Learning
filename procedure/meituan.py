# meituan
class Memory:
    def __init__(self, maxMem):
        self.maxMem = maxMem
        self.memo = [0]*maxMem
        self.nextHandel = 1

    def new(self,size):
        count = 0
        start = 0
        end = 0
        i = 0
        handel = self.nextHandel
        while i<self.maxMem:
            # print count,start,end
            if self.memo[i]!=0:
                start = i
                count = 0
            else:
                count+=1
            end = i
            i += 1
            if count>=size:
                if start>0:
                    start +=1
                for j in range(start, end+1):
                    self.memo[j] = self.nextHandel
                self.nextHandel += 1
                break
        if count<size:
            return "NULL"
        return handel
    def dell(self,handel):
        count = 0
        for i in range(self.maxMem):
            if self.memo[i] == handel:
                count+=1
                self.memo[i] = 0
        if count == 0:
            print 'ILLEGAL_OPERATION'

    def deff(self,index):
        count = 0
        start = 0
        for i in range(self.maxMem):
            if self.memo[i] == 0:
                count+=1
                if count ==0:
                    start = i
            elif count != 0:
                break

            # elif count!=0:
            #     self.deff(i+1)
        for i in range(start, start+count):
            self.memo[i] = self.memo[i+count]
            self.memo[i+count] = 0


T ,MaxMem = raw_input().strip().split(' ')
calcus = []
for i in range(int(T)):
    line = raw_input().strip().split(' ')
    calcus.append(line)
memory = Memory(int(MaxMem))
for calcu in calcus:
    if calcu[0] =='new':
        print memory.new(int(calcu[1]))

    elif calcu[0] == 'del':
        memory.dell(int(calcu[1]))

    elif calcu[0] == 'def':
        memory.deff(0)
    print memory.memo
