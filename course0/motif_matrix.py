import math

motifs = [
"TCGGGGGTTTTT",
"CCGGTGACTTAC",
"ACGGGGATTTTC",
"TTGGGGACTTTT",
"AAGGGGACTTCC",
"TTGGGGACTTCC",
"TCGGGGATTCAT",
"TCGGGGATTCCT",
"TAGGGGAACTAC",
"TCGGGTATAACC"
]


motif_len = len(motifs[0])
motifs_count = len(motifs)
cnts = []
scores = []
for i in range(motif_len):
	dic = {}
	for motif in motifs:
		if motif[i] in dic:
			dic[motif[i]] += 1
		else:
			dic[motif[i]] = 1
	cnts.append(dic)

	score = 0
	for key in dic:
		ratio = dic[key] * 1.0/motifs_count
		score += (-ratio*math.log(ratio, 2))
	scores.append(score)

print scores
print sum(scores)