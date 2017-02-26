import sys

lines = [l.strip() for l in sys.stdin.readlines()]

"""
Code Challenge: Solve the Overlap Graph Problem (restated below).
     Input: A collection Patterns of k-mers.
     Output: The overlap graph Overlap(Patterns), in the form of an adjacency list. (You may return the edges in any order.)


Sample Input:
ATGCG
GCATG
CATGC
AGGCA
GGCAT

Sample Output:
CATGC -> ATGCG
GCATG -> CATGC
GGCAT -> GCATG
AGGCA -> GGCAT

"""

class Graph(object):
	def __init__(self, lines):
		self.prefix = {}
		self.suffix = {}
		self.lines = lines
		self.graphMatrix = {}
		self.fillPrefixAndSuffix()
		self.fillGraph()

	def fillPrefixAndSuffix(self):
		for l in self.lines:
			cur_prefix = l[:-1]
			cur_suffix = l[1:]
			if cur_suffix in self.suffix:
				self.suffix[cur_suffix].append(l)
			else:
				self.suffix[cur_suffix] = [l]

			if cur_prefix in self.prefix:
				self.prefix[cur_prefix].append(l)
			else:
				self.prefix[cur_prefix] = [l]

	def fillGraph(self):
		for l in self.lines:
			self.graphMatrix[l] = []
			cur_suffix = l[1:]
			if cur_suffix in self.prefix:
				for kmer in self.prefix[cur_suffix]:
					if kmer != l:
						self.graphMatrix[l].append(kmer)

	def printGraph(self):
		#print self.prefix
		#print self.suffix
		#print self.graphMatrix
		#for key in self.graphMatrix:
		#	for kmer in self.graphMatrix[key]:
		#		print key,"->",kmer
		for key in self.graphMatrix:
			print key,"->", ",".join(self.graphMatrix[key])

Graph(lines).printGraph()




