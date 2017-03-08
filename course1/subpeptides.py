import sys

cnt = int(sys.stdin.readlines()[0].strip())


def getCount(cnt):
	return cnt * (cnt - 1)

print getCount(cnt)