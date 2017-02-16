import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

dna = lines[0]
k = int(lines[1])
profile = lines[2:]

profile = {

    'A': [float(i) for i in profile[0].split()],
    'C': [float(i) for i in profile[1].split()],
    'G': [float(i) for i in profile[2].split()],
    'T': [float(i) for i in profile[3].split()]
}

def profileScore(kmer):
	score = 1
	for i, c in enumerate(kmer):
		score *= profile[c][i]
	return score

def findMotif(dna, k):
	score = -1
	res = ""
	for i in range(len(dna)-k+1):
		pat = dna[i:i+k]
		if profileScore(pat) > score:
			score = profileScore(pat)
			res = pat

	return res

print findMotif(dna, k)