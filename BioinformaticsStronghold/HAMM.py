import os
from pathlib import Path
FILENAME = os.path.join(os.path.dirname(__file__), f"rosalind_{Path(__file__).stem.lower()}.txt")

def hamming(s, t):
	return sum(1 if a != b else 0 for a, b in zip(s, t))

if __name__ == "__main__":
	with open(FILENAME, "r") as f:
		data = [l.split("\n")[0] for l in f.readlines()]
	
	print(hamming(data[0], data[1]))