import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

pattern = lines[0]
d = int(lines[1])

def hamming(x, y):
	res = 0
	for i, c in enumerate(x):
		if c != y[i]:
			res += 1
	return res

def proxiEqual(x, y, d):
	return hamming(x, y) <= d

def getNeighbour(text, d):
	if d == 0:
		return [text]

	if len(text) == 1:
		return ["A", "T", "G", "C"]

	neighours = []
	suffix = text[1:]
	suffix_neighours = getNeighbour(suffix, d)
	for t in suffix_neighours:
		if hamming(t, suffix) < d:
			neighours += [x + t for x in ["A", "T", "G", "C"]]
		else:
			neighours.append(text[0] + t) 

	return neighours

print len(getNeighbour(pattern, d))
