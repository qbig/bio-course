import sys

k = int(sys.stdin.readlines()[0].strip())


def toBinary(num, k):
	if num == 0:
		return "0" * k

	result = ""
	while num != 0:
		result = str(num%2) + result
		num /= 2

	if len(result) < k:
		result = "0" * (k - len(result)) + result

	return result

def kToBinaries(k):
	return [toBinary(i, k) for i in range(2**k)]

for i in kToBinaries(k):
	print i
