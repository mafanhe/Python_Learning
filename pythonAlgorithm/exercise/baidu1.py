def func(list):
	i = 0
	j = len(list)-1
	while i<j:
		while list[i]%2!=0 and i<j:
			i+=1
		while list[j]%2==0 and i<j:
			j-=1

		list[i],list[j] = list[j],list[i]
	print list

func([1,3,5,7,9,2])