import sys

lines = sys.stdin.readlines()

pep = lines[0].strip()

aminos = lines[1:]
aminoAcid = [amino.strip().split()[0] for amino in aminos]
aminoAcidMass = [int(amino.strip().split()[1]) for amino in aminos]


def linearSpectrum(pep, aminoAcid, aminoAcidMass):
	l = len(pep)
	prefixMass = [0] * (l+1)

	for i in range(1, l+1):
		for j in range(20):
			if aminoAcid[j] == pep[i-1]:
				prefixMass[i] = prefixMass[i-1] + aminoAcidMass[j]
	result = [0]

	for i in range(l):
		for j in range(i+1, l+1):
			result.append(prefixMass[j]-prefixMass[i])

	return sorted(result)

def cyclicSpectrum(pep, aminoAcid, aminoAcidMass):
	l = len(pep)
	prefixMass = [0] * (l+1)

	for i in range(1, l+1):
		for j in range(20):
			if aminoAcid[j] == pep[i-1]:
				prefixMass[i] = prefixMass[i-1] + aminoAcidMass[j]
	result = [0]
	pepMass = prefixMass[-1]
	for i in range(l):
		for j in range(i+1, l+1):
			result.append(prefixMass[j]-prefixMass[i])
			if i > 0 and j < l:
				result.append(pepMass - (prefixMass[j]-prefixMass[i]))
	return sorted(result)


for l in linearSpectrum(pep, aminoAcid, aminoAcidMass):
	print l,

print

for l in cyclicSpectrum(pep, aminoAcid, aminoAcidMass):
	print l,