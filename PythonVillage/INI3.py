import os
from pathlib import Path
FILENAME = os.path.join(os.path.dirname(__file__), f"rosalind_{Path(__file__).stem.lower()}.txt")

if __name__ == "__main__":
	with open(FILENAME, "r") as f:
		string = f.readline().split("\n")[0]
		splits = [int(x) for x in f.readline().split("\n")[0].split(" ")]
	
	print(string[splits[0]:splits[1]+1]+" "+string[splits[2]:splits[3]+1])