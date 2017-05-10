import sys

lines = sys.stdin.readlines()

spectrum = [int(i) for i in lines[0].strip().split()]
spectrum.sort()

def convolute(spectrum):
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
	return res

def topM(spectrum, m):
    cnt = {}
    for i in spectrum:
        if i not in cnt:
            cnt[i] = 1
        else:
            cnt[i] += 1
    print cnt
    res = sorted([i for i in cnt.keys() if 57 <= i <=200], key=lambda x: -cnt[x])
    
    l = len(res)
    if l > m:
        while m < l and m-1 > 0 and cnt[res[m]] == cnt[res[m-1]]:
            m += 1
        res = res[:m]
    extended = []
    for key in res:
        extended += [(key, cnt[key])] * cnt[key]
    return extended
    #return res

for i in sorted(topM(convolute(spectrum), 20), key=lambda x: x[1]):
	print i
