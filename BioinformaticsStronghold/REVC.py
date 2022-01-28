import os
from pathlib import Path
FILENAME = os.path.join(os.path.dirname(__file__), f"rosalind_{Path(__file__).stem.lower()}.txt")

from Bio.Seq import Seq

if __name__ == "__main__":
	with open(FILENAME, "r") as f:
		data = Seq(f.readline().split("\n")[0])
	
	print(data.reverse_complement())