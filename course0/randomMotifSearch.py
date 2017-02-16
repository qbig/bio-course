import sys # you must import "sys" to read from STDIN
import random as rd
lines = sys.stdin.read().splitlines() # read in the input from STDIN

k, t = [int(i) for i in lines[0].split()]
DNAs = lines[1:]

def hamming(x, y):
	res = 0
	for i, c in enumerate(x):
		if c != y[i]:
			res += 1
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


def findAll(DNAs, profile, k):
	return [findMotif(dna, k, profile) for dna in DNAs]

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

def randomKmer(dna, k):
	random_index = rd.randint(0, len(dna)-k)
	return dna[random_index:random_index+k]

def randomMotifs(DNAs, k):
	return [randomKmer(dna, k) for dna in DNAs]

def randomMotifSearch(DNAs, k, t):
	motifs = randomMotifs(DNAs, k)
	bestMotifs = motifs
	while True:
		profile = createProfileMatrixWithLap(motifs)
		motifs = findAll(DNAs, profile, k)
		if diffAll(motifs,k ) < diffAll(bestMotifs,k):
			bestMotifs = motifs
		else:
			return bestMotifs

def randomMotifSearchR(DNAs, k, t):
	
	motifs = ["TGA",
				"GTT",
				"GAA",
				"TGT"]
	bestMotifs = motifs
	for i in range(1):
		profile = createProfileMatrixWithLap(motifs)
		motifs = findAll(DNAs, profile, k)
		if diffAll(motifs,k ) < diffAll(bestMotifs,k):
			bestMotifs = motifs
		
	return bestMotifs

for motif in randomMotifSearchR(DNAs, k, t):
	print motif

# bestMotifs = randomMotifSearch(DNAs, k, t)
# for motifs in [randomMotifSearch(DNAs, k, t) for i in range(1000)]:
# 		if diffAll(motifs,k ) < diffAll(bestMotifs,k):
# 			bestMotifs = motifs
# 			print diffAll(motifs,k )
		
# for motif in bestMotifs:
# 	print motif
