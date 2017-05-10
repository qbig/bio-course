"""
  CyclopeptideSequencing(Spectrum)
        Peptides < -  -  a set containing only the empty peptide
        while Peptides is nonempty
            Peptides < -  -  Expand(Peptides)
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

m = int(lines[0])
n = int(lines[1])
spectrum = [int(l) for l in lines[2].strip().split()]
print "spectrum:", spectrum, len(spectrum)
aminos = lines[3:]
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
    prefixMass = [0] * (l + 1)

    for i in range(1, l + 1):
        for j in range(20):
            if aminoAcid[j] == pep[i - 1]:
                prefixMass[i] = prefixMass[i - 1]  +  aminoAcidMass[j]
    result = [0]

    for i in range(l):
        for j in range(i + 1, l + 1):
            result.append(prefixMass[j] - prefixMass[i])

    linearSpectrumDic[pep] = sorted(result)
    return linearSpectrumDic[pep]

cyclicSpectrumDic = {}


def cyclicSpectrum(pep, aminoAcid, aminoAcidMass):
    if pep in cyclicSpectrumDic:
        return cyclicSpectrumDic[pep]
    
    l = len(pep)
    prefixMass = [0] * (l  +  1)

    for i in range(1, l  +  1):
        for j in range(20):
            if aminoAcid[j] == pep[i  -  1]:
                prefixMass[i] = prefixMass[i  -  1]  +  aminoAcidMass[j]
    result = [0]
    pepMass = prefixMass[ - 1]
    for i in range(l):
        for j in range(i  +  1, l  +  1):
            result.append(prefixMass[j]  -  prefixMass[i])
            if i > 0 and j < l:
                result.append(pepMass  -  (prefixMass[j]  -  prefixMass[i]))
    cyclicSpectrumDic[pep] = sorted(result)
    return cyclicSpectrumDic[pep]


def expand(peps):
    result = []
    for pep in peps:
        result  += [pep  +  amino for amino in aminoAcid]
    return result



def mass(pep):
    return sum([massDic[p] for p in pep])

def consistent(pep, spectrum):
    dic = {}
    for num in spectrum:
        if num in dic:
            dic[num]  += 1
        else:
            dic[num] = 1
    linearSpec = linearSpectrum(pep, aminoAcid, aminoAcidMass)
    for w in linearSpec:
        if w not in dic:
            return False
        dic[w]   += 1
        if dic[w] < 0:
            return False

    return True

def cyclopeptideSequencing(spectrum):
    peptides = [""]
    result = []
    while peptides:
        peptides = expand(peptides)
        peptidesNext = peptides[:]
        for i, pep in enumerate(peptides):
            if mass(pep) == spectrum[ - 1]:
                if cyclicSpectrum(pep, aminoAcid, aminoAcidMass) == spectrum:
                    result.append(pep)
                peptidesNext.remove(pep)
            elif not consistent(pep, spectrum):
                peptidesNext.remove(pep)        
        peptides = peptidesNext[:]
        
    return result


def linearSpectrum(pep, aminoAcid, aminoAcidMass):
    l = len(pep)
    prefixMass = [0] * (l + 1)

    for i in range(1, l + 1):
        for j in range(20):
            if aminoAcid[j] == pep[i - 1]:
                prefixMass[i] = prefixMass[i - 1] + aminoAcidMass[j]

    result = [0]
    for i in range(l):
        for j in range(i + 1, l + 1):
            result.append(prefixMass[j] - prefixMass[i])

    return sorted(result)

def cyclicSpectrum(pep, aminoAcid, aminoAcidMass):
    l = len(pep)
    prefixMass = [0] * (l + 1)

    for i in range(1, l + 1):
        for j in range(20):
            if aminoAcid[j] == pep[i - 1]:
                prefixMass[i] = prefixMass[i - 1]  +  aminoAcidMass[j]

    result = [0]
    pepMass = prefixMass[ - 1]
    for i in range(l):
        for j in range(i + 1, l + 1):
            result.append(prefixMass[j] - prefixMass[i])
            if i > 0 and j < l:
                result.append(pepMass  -  (prefixMass[j] - prefixMass[i]))
    return sorted(result)

def score(pep, spectrum):
    perfectSpecture = cyclicSpectrum(pep, aminoAcid, aminoAcidMass)

    result = 0
    for i in spectrum:
        if i in perfectSpecture:
            result   += 1
            perfectSpecture.remove(i)

    return result

def linearScore(pep, spectrum):
    perfectSpecture = linearSpectrum(pep, aminoAcid, aminoAcidMass)

    result = 0
    for i in spectrum:
        if i in perfectSpecture:
            result   += 1
            perfectSpecture.remove(i)
    return result

def trim(leaderBoard, spectrum, n):
    scores = [(pep, score(pep, spectrum)) for pep in leaderBoard]
    scores = sorted(scores, key=lambda x: -x[1])
    if len(scores) > n:
        while len(scores) > n and scores[n][1] == scores[n-1][1]:
            n += 1
        scores = scores[:n]

    return [item[0] for item in scores]

def leaderBoardcyclopeptideSequencing(spectrum, n):
    spectrum.sort()
    print "extended:", spectrum, len(spectrum)
    leaderBoard = [""]
    leaderPeptide = ""
    while leaderBoard:
        #print leaderBoard
        leaderBoard = expand(leaderBoard)
        peptidesNext = leaderBoard[:]
        for i, pep in enumerate(leaderBoard):
            #print score(pep, spectrum), pep, mass(pep)
            if mass(pep) == spectrum[-1]:
                print score(pep, spectrum), pep, mass(pep), len(leaderBoard)
                if score(pep, spectrum) > score(leaderPeptide, spectrum):
                    leaderPeptide = pep
            elif mass(pep) >  spectrum[-1]:
                peptidesNext.remove(pep)        
        leaderBoard = peptidesNext[:]
        leaderBoard = trim(leaderBoard, spectrum, n)
        #print leaderBoard
    return leaderPeptide

def convolute(spectrum):
    spectrum = [0] + spectrum
    spectrum.sort()
    l = len(spectrum)
    dic = {}
    res = []
    for i in range(l):
        for j in range(i+1, l):
            diff = spectrum[j] - spectrum[i]
            if diff == 0:
                continue
            res.append(diff)
            if diff not in dic:
                dic[diff] = 1
            else:
                dic[diff] += 1
    print "convoluted: ", sorted(res)
    return res

def topM(spectrum, m):
    cnt = {}
    for i in spectrum:
        if i not in cnt:
            cnt[i] = 1
        else:
            cnt[i] += 1
    res = sorted([i for i in cnt.keys() if 57 <= i <=200], key=lambda x: -cnt[x])
    
    resLen = len(res)
    if resLen > m:
        while m < resLen and m-1 > 0 and cnt[res[m]] == cnt[res[m-1]]:
            m += 1
        res = res[:m]
    #return res
    extended = []
    for key in res:
        extended += [key] * cnt[key]
    return extended


print "-".join([str(massDic[p]) for p in leaderBoardcyclopeptideSequencing(spectrum + topM(convolute(spectrum), m), n)])










