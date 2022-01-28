import os
from pathlib import Path
FILENAME = os.path.join(os.path.dirname(__file__), f"rosalind_{Path(__file__).stem.lower()}.txt")

import numpy as np
from Bio import SeqIO

ROW = {"A": 0, "C": 1, "G": 2, "T": 3}
CHAR = {0: "A", 1: "C", 2: "G", 3:"T"}

if __name__ == "__main__":
	with open(FILENAME, "r") as f:
		data = [rec for rec in SeqIO.parse(f, "fasta")]

	profile_mtx = np.zeros((4, len(data[0].seq)), dtype=int)

	for rec in data:
		for i, c in enumerate(rec.seq):
			profile_mtx[ROW[c], i] += 1
	
	concensus_idx = list(profile_mtx.argmax(axis=0))
	print("".join(CHAR[i] for i in concensus_idx))
	for key, val in ROW.items():
		print(f"{key}: {' '.join(str(x) for x in list(profile_mtx[val,:]))}")