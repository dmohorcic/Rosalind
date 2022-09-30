import os
from pathlib import Path
FILENAME = os.path.join(os.path.dirname(__file__), f"rosalind_{Path(__file__).stem.lower()}.txt")

from Bio import SeqIO

def grph(data, k):
	edges = dict()
	for tag, dna in data.items():
		edges[tag] = []
		for other_tag in edges:
			if other_tag == tag: continue
			if data[other_tag][:k] == dna[-k:]:
				edges[tag].append(other_tag)
			if dna[:k] == data[other_tag][-k:]:
				edges[other_tag].append(tag)
	return edges

if __name__ == "__main__":
	data = dict()
	sequences = list(SeqIO.parse(open(FILENAME, "r"), 'fasta'))
	for sequence in sequences:
		data[sequence.id] = str(sequence.seq)
	
	res = grph(data, k=3)
	for key, val in res.items():
		for v in val:
			print(f"{key} {v}")