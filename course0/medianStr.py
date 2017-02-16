import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

k = int(lines[0])
DNAs = lines[1:]

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

def findMinDiff(dna, kmer, k):
	diff = 9999999
	for i in range(len(dna)-k + 1):
		pat = dna[i:i+k]
		new_diff = hamming(kmer, pat)
		if new_diff < diff:
			diff = new_diff

	return  diff

def diffAll(DNAs, kmer, k):
	return sum([findMinDiff(dna, kmer, k) for dna in DNAs])

def getMediaStr(DNAs, k):
	diff = 999999
	out = ""
	for kmer in getNeighbour("A"*k, k):
		cur_diff = diffAll(DNAs, kmer, k)
		if cur_diff < diff:
			diff = cur_diff
			out = kmer

	return out

print getMediaStr(DNAs, k)

