import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

pattern = lines[0]
line = lines[1]
d = int(lines[2])

def hamming(x, y):
	res = 0
	for i, c in enumerate(x):
		if c != y[i]:
			res += 1
	return res

def proxiEqual(x, y, d):
	return hamming(x, y) <= d

res = []
len_pat = len(pattern)
for i in range(len(line) - len(pattern)+1):
	if proxiEqual(pattern, line[i:i+len_pat], d):
		res.append(i)

print len(res)