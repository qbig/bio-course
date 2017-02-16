import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

k, t = [int(i) for i in lines[0].split()]
DNAs = lines[1:]

def hamming(x, y):
	res = 0
	for i, c in enumerate(x):
		if c != y[i]:
			res += 1
	return res


def profileScore(kmer, profile):
	score = 1
	for i, c in enumerate(kmer):
		score *= profile[c][i]
	return score

def findMotif(dna, k, profile):
	score = -1
	res = ""
	for i in range(len(dna)-k+1):
		pat = dna[i:i+k]
		if profileScore(pat, profile) > score:
			score = profileScore(pat, profile)
			res = pat

	return res

def getConsensus(motifs):
	l = len(motifs[0])
	cnt = len(motifs)
	profile = {
	    'A': [0.0]*l,
	    'C': [0.0]*l,
	    'G': [0.0]*l,
	    'T': [0.0]*l
	}
	for motif in motifs:
		for i, c in enumerate(motif):
			profile[c][i] += 1
	res = ""
	for i in range(l):
		if  profile['A'][i] >= profile['T'][i] and \
			profile['A'][i] >= profile['G'][i] and \
			profile['A'][i] >= profile['C'][i]:
			res+= 'A'
		elif profile['T'][i] >= profile['A'][i] and \
			profile['T'][i] >= profile['G'][i] and \
			profile['T'][i] >= profile['C'][i]:
			res+= 'T'
		elif profile['G'][i] >= profile['A'][i] and \
			profile['G'][i] >= profile['T'][i] and \
			profile['G'][i] >= profile['C'][i]:
			res+= 'G'
		else:
			res+= 'C'

	return res

def diffAll(motifs, k):
	kmer = getConsensus(motifs)
	return sum([hamming(kmer, motif) for motif in motifs])


def createProfileMatrix(motifs):
	l = len(motifs[0])
	cnt = len(motifs)
	profile = {
	    'A': [0.0]*l,
	    'C': [0.0]*l,
	    'G': [0.0]*l,
	    'T': [0.0]*l
	}
	for motif in motifs:
		for i, c in enumerate(motif):
			profile[c][i] += 1
	for i in range(l):
		profile['A'][i]/=cnt
		profile['T'][i]/=cnt
		profile['G'][i]/=cnt
		profile['C'][i]/=cnt

	return profile

def createProfileMatrixWithLap(motifs):
	l = len(motifs[0])
	cnt = len(motifs)+4
	profile = {
	    'A': [1.0]*l,
	    'C': [1.0]*l,
	    'G': [1.0]*l,
	    'T': [1.0]*l
	}
	for motif in motifs:
		for i, c in enumerate(motif):
			profile[c][i] += 1
	for i in range(l):
		profile['A'][i]/=cnt
		profile['T'][i]/=cnt
		profile['G'][i]/=cnt
		profile['C'][i]/=cnt

	return profile

def greedyMotifSearch(DNAs, k, t):
	bestMotifs = [dna[:k] for dna in DNAs]

	baseStrand = DNAs[0]
	otherStrands = DNAs[1:]
	for i in range(len(baseStrand)-k+1):
		pat = baseStrand[i:i+k]
		motifs = [pat]
		for strand in otherStrands:
			profileMatrix = createProfileMatrixWithLap(motifs)
			nextMotif = findMotif(strand, k, profileMatrix)
			motifs.append(nextMotif)
		if diffAll(motifs,k ) < diffAll(bestMotifs,k):
			bestMotifs = motifs

	return bestMotifs

for motif in greedyMotifSearch(DNAs, k, t):
	print motif
