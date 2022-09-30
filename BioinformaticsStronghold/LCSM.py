import os
from pathlib import Path
FILENAME = os.path.join(os.path.dirname(__file__), f"rosalind_{Path(__file__).stem.lower()}.txt")

from Bio import SeqIO

def is_in_every(subseq, data):
	for seq in data:
		if subseq not in seq:
			return False
	return True

def lcsm(data):
	base_seq = data[0]
	remaining = data[1:]
	start_idx = 0
	end_idx = 2
	longest = ""
	current = base_seq[start_idx:end_idx]
	while end_idx < len(base_seq):
		is_ok = is_in_every(current, remaining)
		if is_ok:
			if len(current) > len(longest):
				longest = current
			end_idx += 1
			current = base_seq[start_idx:end_idx]
		else:
			start_idx += 1
			end_idx = start_idx+2
			current = base_seq[start_idx:end_idx]
	return longest

if __name__ == "__main__":
	data = list()
	sequences = list(SeqIO.parse(open(FILENAME, "r"), 'fasta'))
	for sequence in sequences:
		data.append(str(sequence.seq))
	
	print(lcsm(data))