import sys

lines = sys.stdin.readlines()

# sink at (n, m)
n, m = [int(i) for i in lines[0].strip().split()] 
lines = lines[1:]


"""
4 4
1 0 2 4 3 # matrix down
4 6 5 2 1
4 4 5 2 1
5 6 8 5 3
-
3 2 4 0 # matrix right
3 2 4 2
0 7 3 3
3 3 0 2
1 3 2 2
"""

matrix_down = [
	[int(i) for i in line.strip().split(" ")] for line in lines[:n]
]

matrix_right = [
	[int(i) for i in line.strip().split(" ")] for line in lines[n+1:] # skip the `-`
]


def tour(matrix_down, matrix_right, n, m):
	score = [[0] * (m+1) for i in range(n+1)]

	# init first row
	for j in range(1, m+1):
		score[0][j] = score[0][j-1] + matrix_right[0][j-1]
	# init first col
	for i in range(1, n+1):
		score[i][0] = score[i-1][0] + matrix_down[i-1][0]

	for i in range(1, n+1):
		for j in range(1, m+1):
			score[i][j] = max(score[i-1][j] + matrix_down[i-1][j], score[i][j-1] + matrix_right[i][j-1])

	return score[n][m]

print(tour(matrix_down, matrix_right, n, m))

