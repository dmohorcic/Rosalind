import os
from pathlib import Path
FILENAME = os.path.join(os.path.dirname(__file__), f"rosalind_{Path(__file__).stem.lower()}.txt")

def iev(data):
	probs = [1, 1, 1, 0.75, 0.5, 0]
	return sum(a*b for a, b in zip(data, probs))*2

if __name__ == "__main__":
	with open(FILENAME, "r") as f:
		data = [int(x) for x in f.readline()[:-1].split(" ")]
	
	print(iev(data))