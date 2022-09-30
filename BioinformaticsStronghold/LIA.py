import os
from pathlib import Path
FILENAME = os.path.join(os.path.dirname(__file__), f"rosalind_{Path(__file__).stem.lower()}.txt")

import math

def binom_test(n, N):
	return math.comb(N, n) * 0.25**n * 0.75**(N-n)

def lia(k, n):
	prob = 0
	for i in range(n, 2**k+1):
		prob += binom_test(i, 2**k)
	return prob
	
if __name__ == "__main__":
	with open(FILENAME, "r") as f:
		data = [int(x) for x in f.readline()[:-1].split(" ")]
	
	res = lia(*data)
	print(res)
	print(round(res, 3))