# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, array, target):
        # write code here
        m = len(array)
        n = len(array[0])
        i = m-1
        j = 0
        while i>=0 and j<n:
            if array[i][j]>target:
                i-=1
            elif array[i][j]<target:
                j+=1
            else:
				return True
        return False
s= Solution()
print s.Find([[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]],7)