# Think about big number
# use string/array to show big number,string there


def print_to_max_of_digits(n):
	for i in range(1, 10**n):
		print i


def print_to_max_of_digits2(n):
	if n < 0:
		return
	l = [0]*n
	while not increment(l):
		print_number2(l)


def print_to_max_of_digits3(n, num=''):
	if n <= 0:
		print_number2(num)
		return

	for i in range(0, 10):
		print_to_max_of_digits3(n-1, num+str(i))


def increment(n):
	plus = 1
	for i in range(len(n)-1, -1, -1):
		if n[i] != '9':
			n[i] = str(int(n[i])+1)
			plus = 0
			break
		else:
			n[i] = '0'
	else:
		if plus == 1:
			return True
	return False


def print_number(n):
	result = 0
	for i in n:
		result = result*10+int(i)
	print result


def print_number2(n):
	beginning0 = True
	for i in range(len(n)):
		if beginning0 and n[i]!='0':
			beginning0=False
		if not beginning0:
			print n[i],
	print

# print_to_max_of_digits3(3)


# no concern of negative number
def xgtm1(n, m):
	plus = 0
	index = -1
	if len(n) < len(m):
		n, m = m, n
	for i in range(-1, -len(m)-1, -1):
		if int(n[i])+int(m[i])+plus > 9:
			n[i] = str(int(n[i]) + int(m[i]) + plus - 10)
			plus = 1
		else:
			n[i] = str(int(n[i]) + int(m[i]) + plus)
			plus = 0
		index = i
	print n
	if plus == 1:
		if index == -len(n):
			n.insert(0, '1')
		else:
			for i in range(len(n)+index-1, -1, -1):
				if n[i] != '9':
					n[i] = str(int(n[i]) + 1)
					break
				else:
					n[i] = '0'
					if i == 0:
						n.insert(0, 1)
	print n

xgtm1(['6','6','6'],['9','8','7','6'])



