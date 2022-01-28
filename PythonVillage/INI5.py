import os
from pathlib import Path
FILENAME = os.path.join(os.path.dirname(__file__), f"rosalind_{Path(__file__).stem.lower()}.txt")

if __name__ == "__main__":
	with open(FILENAME, "r") as f:
		i = False
		for l in f:
			if i:
				print(l.split("\n")[0])
			i = not i
