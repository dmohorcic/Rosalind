import os
from pathlib import Path
FILENAME = os.path.join(os.path.dirname(__file__), f"rosalind_{Path(__file__).stem.lower()}.txt")

if __name__ == "__main__":
	with open(FILENAME, "r") as f:
		data = [int(x) for x in f.readline().split("\n")[0].split(" ")]

	s = sum([x for x in range(data[0], data[1]+1) if x % 2 == 1])
	print(s)