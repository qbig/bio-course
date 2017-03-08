import sys

lines = sys.stdin.readlines()
amino = lines[0].strip()

lines = [l.strip() for l in lines[1:]]

weight = {}
for l in lines:
	a, w = l.strip().split()
	weight[a] = int(w)


def getSub(fromIndex, size, arr, l):
	if fromIndex + size - 1 < l:
		return arr[fromIndex: fromIndex+size]
	else:
		return arr[fromIndex:] + arr[:size - (l-fromIndex)]

def getSums(amino):
	result = [0, sum([weight[c] for c in amino])] + [weight[c] for c in amino]
	l = len(amino)
	for i in range(l):
		for j in range(2, l):
			result.append(sum([weight[c] for c in getSub(i, j, amino, l)]))

	return result


for i in  getSums(amino):
	print i,

