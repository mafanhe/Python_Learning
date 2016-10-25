def pow(base, exponent):
	if is_equal(base, 0.0) and exponent < 0:
		raise Exception
	if is_equal(base, 0.0):
		return 0
	result = power_with_unsigned_exponent(base, abs(exponent))
	if exponent <=0:
		result = 1.0/result
	return result


def is_equal(n1, n2):
	if abs(n1-n2) < 0.000000001:
		return True
	return False


def power_with_unsigned_exponent(base, exponent):
	if exponent == 0:
		return 1
	if exponent == 1:
		return base
	result = power_with_unsigned_exponent(base, exponent >> 1)
	result *= result
	if exponent & 1 == 1:
		result *= base
	return result

print pow(1.4, 2)
