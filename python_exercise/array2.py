# -*- coding:utf-8 -*-



def Find(array, target):
    m = len(array)
    n = len(array[0])
    for line in array:
        if line[0]>target or line[-1]<target:
            continue
        else:
            left = 0
            right = len(line)-1
            while left!=right:
                mid = (left+right)/2
                if line[mid]==target:
                    return True
                elif line[mid]<target:
		            left = mid+1
             	else:
                    right = mid-1
    return False


array = [[1,3,5,7,9],
         [2,4,6,8,10]]

print Find(array, 8)