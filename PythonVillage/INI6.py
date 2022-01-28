import os
from pathlib import Path
FILENAME = os.path.join(os.path.dirname(__file__), f"rosalind_{Path(__file__).stem.lower()}.txt")

if __name__ == "__main__":
	with open(FILENAME, "r") as f:
		data = f.readline().split("\n")[0].split(" ")
	
	d = {w: 0 for w in data}
	for w in data:
		d[w] += 1
	
	for k, v in d.items():
		print(f"{k}: {v}")