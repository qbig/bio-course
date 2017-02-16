import sys # you must import "sys" to read from STDIN
import random as rd
lines = sys.stdin.read().splitlines() # read in the input from STDIN

k, t, N = [int(i) for i in lines[0].split()]
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


def diffAll(motifs, k):
	#print motifs, k
	kmer = getConsensus(motifs)
	return sum([hamming(kmer, motif) for motif in motifs])


def randomDistribute(arr):
	total = sum(arr)
	res = rd.uniform(0, total)
	cur = 0 
	for i, d in enumerate(arr):
		if cur <= res < cur + d:
			return i
		cur += d

def profileRandMotif(dna, profile, k):
	return [profileScore(dna[i:i+k], profile) for i in range(len(dna)-k+1)]

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

def gibRandomMotifSearch(DNAs, k, t, N):
	motifs = randomMotifs(DNAs, k)
	l = len(DNAs)
	bestMotifs = motifs
	for i in range(N):
		index = rd.randint(0, l-1)
		profile = createProfileMatrixWithLap([mot for j, mot in  enumerate(motifs) if j != index])
		new_mot = randomDistribute(profileRandMotif(DNAs[index], profile, k))
		motifs[index] = DNAs[index][new_mot:new_mot+k]
		if diffAll(motifs,k ) < diffAll(bestMotifs,k):
			bestMotifs = motifs
		
	return bestMotifs
		
bestMotifs = gibRandomMotifSearch(DNAs, k, t, N)
for motifs in [gibRandomMotifSearch(DNAs, k, t, N) for i in range(20)]:
		if diffAll(motifs,k ) < diffAll(bestMotifs,k):
			bestMotifs = motifs
			print diffAll(motifs,k )
		
for motif in bestMotifs:
	print motif
