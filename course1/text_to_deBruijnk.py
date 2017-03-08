
import sys

lines = [l.strip() for l in sys.stdin.readlines()]


"""
Code Challenge: Solve the De Bruijn Graph from a String Problem.
     Input: An integer k and a string Text.
     Output: DeBruijnk(Text), in the form of an adjacency list.

Sample Input:
4
AAGATTCTCTAAGA

Sample Output:
AAG -> AGA,AGA
AGA -> GAT
ATT -> TTC
CTA -> TAA
CTC -> TCT
GAT -> ATT	
TAA -> AAG
TCT -> CTA,CTC
TTC -> TCT

"""

class DBGraph(object):
	def __init__(self, lines):
		self.lines = lines
		self.graphMatrix = {}
		self.fillGraph()

	def fillGraph(self):
		for l in self.lines:
			cur_prefix = l[:-1]
			cur_suffix = l[1:]
			if cur_prefix in self.graphMatrix:
				self.graphMatrix[cur_prefix].append(cur_suffix)
			else:
				self.graphMatrix[cur_prefix] = [cur_suffix]

	def printGraph(self):
		#print self.prefix
		#print self.suffix
		#print self.graphMatrix
		for key in self.graphMatrix:
			if len(self.graphMatrix[key]) == 1:
				print key,"->",self.graphMatrix[key][0]
			else:
				print key,"->",",".join(self.graphMatrix[key])
			
				

def strCompose(line, length):
	"""
	Code Challenge: Solve the String Composition Problem.
     Input: An integer k and a string Text.
     Output: Compositionk(Text) (the k-mers can be provided in any order).
	"""
	return [line[i:i+length] for i in range(len(line)-length+1)]

DBGraph(lines).printGraph()
