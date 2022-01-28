import os
from pathlib import Path
FILENAME = os.path.join(os.path.dirname(__file__), f"rosalind_{Path(__file__).stem.lower()}.txt")

if __name__ == "__main__":
	
	with open(FILENAME, "r") as f:
		data = [int(x) for x in f.readline().split("\n")[0].split(" ")]
		k, m, n = data[0], data[1], data[2]
	
	s = k+m+n
	p = 2*(k*m+k*n+0.5*m*n+k*(k-1)/2+0.75*m*(m-1)/2)/(s*(s-1))
	print(p)