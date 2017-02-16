import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

pattern = lines[0]
k, d = lines[1].split()
k = int(k)
d = int(d)

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


def patternToNum(pat):
	if len(pat) == 1:
		return "ACGT".index(pat)
	
	return "ACGT".index(pat[-1]) + patternToNum(pat[:-1]) * 4


def numToPattern(index, k):
	if k == 1:
		return "ACGT"[index]

	prefix_index = index / 4
	remainder = index % 4
	symbol = "ACGT"[remainder]
	
	return numToPattern(prefix_index, k-1) + symbol

def frequentWordsWithMismatch(text, k, d):
	freq = [0] * (4**k)
	close = [0] * (4**k)
	res = []
	for i in range(len(text) - k+1):
		neib = getNeighbour(text[i:i+k],d)
		for pat in neib:
			index = patternToNum(pat)
			close[index] += 1

	maxCnt = max(close)
	for i, cnt in enumerate(close):
		if cnt == maxCnt:
			res.append(numToPattern(i, k))

	return res

def complement(line):
	result = ""
	for c in reversed(line):
		if c == "A":
			result += "T"
		elif c == "T":
			result += "A"
		elif c == "G":
			result += "C"
		elif c == "C":
			result += "G"

	return result

def frequentWordsWithMismatchAndReverse(text, k, d):
	freq = [0] * (4**k)
	close = [0] * (4**k)
	res = []
	for i in range(len(text) - k+1):
		neib = getNeighbour(text[i:i+k],d)
		for pat in neib:
			index = patternToNum(pat)
			close[index] += 1
		neib = getNeighbour(complement(text[i:i+k]),d)
		for pat in neib:
			index = patternToNum(pat)
			close[index] += 1

	maxCnt = max(close)
	for i, cnt in enumerate(close):
		if cnt == maxCnt:
			res.append(numToPattern(i, k))

	return res

for pat in frequentWordsWithMismatchAndReverse(pattern, k, d):
	print pat ,


