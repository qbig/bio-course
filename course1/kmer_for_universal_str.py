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
ATGC -> TGCG
GCAT -> CATG
...

"""

class Graph(object):
	def __init__(self, lines):
		self.lines = lines
		self.graphMatrix = {}
		self.fillGraph()

	def fillGraph(self):
		for l in self.lines:
			prefix = l[:-1]
			suffix = l[1:]
			if prefix in self.graphMatrix:
				self.graphMatrix[prefix].append(suffix)
			else:
				self.graphMatrix[prefix] = [suffix]

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




