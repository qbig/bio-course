"""
  CyclopeptideSequencing(Spectrum)
        Peptides <-- a set containing only the empty peptide
        while Peptides is nonempty
            Peptides <-- Expand(Peptides)
            for each peptide Peptide in Peptides
                if Mass(Peptide) = ParentMass(Spectrum)
                    if Cyclospectrum(Peptide) = Spectrum
                        output Peptide
                    remove Peptide from Peptides
                else if Peptide is not consistent with Spectrum
                    remove Peptide from Peptides
"""

import sys

lines = sys.stdin.readlines()

spectrum = [int(l) for l in lines[0].strip().split()]

aminos = lines[1:]
aminoAcid = [amino.strip().split()[0] for amino in aminos]
aminoAcidMass = [int(amino.strip().split()[1]) for amino in aminos]
massDic = {}
for i in range(20):
    massDic[aminoAcid[i]] = aminoAcidMass[i]

linearSpectrumDic = {}
def linearSpectrum(pep, aminoAcid, aminoAcidMass):
    if pep in linearSpectrumDic:
        return linearSpectrumDic[pep]

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

    linearSpectrumDic[pep] = sorted(result)
    return linearSpectrumDic[pep]

cyclicSpectrumDic = {}
def cyclicSpectrum(pep, aminoAcid, aminoAcidMass):
    if pep in cyclicSpectrumDic:
        return cyclicSpectrumDic[pep]
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
    cyclicSpectrumDic[pep] = sorted(result)
    return cyclicSpectrumDic[pep]


def expand(peps):
    result = []
    for pep in peps:
        result += [pep + amino for amino in aminoAcid]
    #print result
    return result



def mass(pep):
    return sum([massDic[p] for p in pep])

def consistent(pep, spectrum):
    dic = {}
    for num in spectrum:
        if num in dic:
            dic[num] += 1
        else :
            dic[num] = 1
    linearSpec = linearSpectrum(pep, aminoAcid, aminoAcidMass)
    for w in linearSpec:
        if w not in dic:
            return False
        dic[w] -= 1
        if dic[w] < 0:
            return False

    return True

def cyclopeptideSequencing(spectrum):
    peptides = [""]
    result = []
    visied = {}
    while peptides:
        peptides = expand(peptides)
        peptidesNext = peptides[:]
        for i, pep in enumerate(peptides):
            if mass(pep) == spectrum[-1]:
                if cyclicSpectrum(pep, aminoAcid, aminoAcidMass) == spectrum:
                    result.append(pep)
                peptidesNext.remove(pep)
            elif not consistent(pep, spectrum):
                peptidesNext.remove(pep)
        
        peptides = peptidesNext[:]
        
    return result

for l in list(set(["-".join([str(massDic[p]) for p in pep]) for pep in cyclopeptideSequencing(spectrum)])):
    print l,










