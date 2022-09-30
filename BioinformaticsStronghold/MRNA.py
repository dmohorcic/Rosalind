import os
from pathlib import Path
FILENAME = os.path.join(os.path.dirname(__file__), f"rosalind_{Path(__file__).stem.lower()}.txt")

translate = {
	"A": 4, "R": 6, "N": 2, "D": 2, "B": 4, "C": 2, "Q": 2,
	"E": 2, "Z": 4, "G": 4, "H": 2, "I": 3, "L": 6, "K": 2,
	"M": 1, "F": 2, "P": 4, "S": 6, "T": 4, "W": 1, "Y": 2,
	"V": 4
}


def mRNA(seq):
	score = 1
	for c in seq:
		score = (score*translate[c]) % 1000000
	score = (score*3) % 1000000 # for stop codons
	return score


def main():
	with open(FILENAME, "r") as f:
		seq = f.readline().split("\n")[0]
	
	res = mRNA(seq)
	print(res)


if __name__ == "__main__":
	main()