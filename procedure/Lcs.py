def LCString(str1,str2):
    maxl = 0
    matrix = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]
    pos_x, pos_y = None,None
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]+1
                if matrix[i][j] > maxl:
                    maxl = matrix[i][j]
                    pos_x = i
                    pos_y = j
            else:
                matrix[i][j] = 0
    res = []
    print matrix
    while matrix[pos_x][pos_y]:
        res.append(str1[pos_x-1])
        pos_x -= 1
        pos_y -= 1
    print res[::-1]

LCString("abcd","bc")

def LCS(str1,str2):
    maxl = 0
    matrix = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]
    pos_x, pos_y = None,None
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]+1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    res = []
    i,j = 0,0

    while i<len(str1) and j<len(str2):
        if str1[i] == str2[j]:
            res.append(str1[i])
            i+=1
            j+=1
        elif matrix[i+1][j]>matrix[i][j+1]:


