#sougou
while 1:
    string = raw_input()
    print string
    for i in range(len(string)+1,0,-1):
        str = string[0:i]
        sb = str[::-1]
        n = 0
        print str, sb
        for j in range(len(str)):
            if str[j] == sb[j]:
                n += 1
        if n == len(str):
            print len(str)
            break
