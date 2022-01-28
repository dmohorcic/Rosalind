import os
from pathlib import Path
FILENAME = os.path.join(os.path.dirname(__file__), f"rosalind_{Path(__file__).stem.lower()}.txt")

from Bio.Seq import Seq

if __name__ == "__main__":

	with open(FILENAME, "r") as f:
		s = Seq(f.readline().split("\n")[0])
		t = Seq(f.readline().split("\n")[0])

	start = list()
	idx = s.find(t)
	while idx >= 0:
		start.append(idx)
		idx = s.find(t, start[-1]+1)
	
	for i in start:
		print(i+1, end=" ")
	print("")