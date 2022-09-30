import os
from pathlib import Path
FILENAME = os.path.join(os.path.dirname(__file__), f"rosalind_{Path(__file__).stem.lower()}.txt")

import requests
from Bio import SeqIO
from io import StringIO

def find_motif(seq):
	results = list()
	start = -4
	i = 0
	while i < len(seq):
		char = seq[i]
		diff = i-start
		if start == -4 and char == "N":
			start = i
		elif diff == 1 and char == "P":
			i = start
			start = -4
		elif diff == 2 and char not in "ST":
			i = start
			start = -4
		elif diff == 3:
			if char != "P":
				results.append(start+1)
			i = start
			start = -4
		i += 1
	return results

def mprt(data):
	results = dict()
	for protein in data:
		response = requests.get(f"http://www.uniprot.org/uniprot/{protein.split('_')[0]}.fasta")
		if response.status_code != 200:
			print(f"Error with protein {protein}")
			continue
		with StringIO(response.text) as f:
			seq = list(SeqIO.parse(f, "fasta"))[0]
		loc = find_motif(str(seq.seq))
		if len(loc) > 0:
			results[protein] = loc
	return results
	
if __name__ == "__main__":
	with open(FILENAME, "r") as f:
		data = [line[:-1] for line in f.readlines()]

	res = mprt(data)
	for key, val in res.items():
		print(key)
		print(" ".join(str(x) for x in val))