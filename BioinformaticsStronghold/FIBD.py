import os
from pathlib import Path
FILENAME = os.path.join(os.path.dirname(__file__), f"rosalind_{Path(__file__).stem.lower()}.txt")

def fibd(n, m):
	rabbits = [0 for _ in range(m)] # how many rabbit pairs specific age we have
	rabbits[0] = 1
	for _ in range(1, n):
		new_rabbits = sum(rabbits[1:])
		rabbits = [new_rabbits] + rabbits[:-1]
	return rabbits

if __name__ == "__main__":
	with open(FILENAME, "r") as f:
		data = [int(x) for x in f.readline().split("\n")[0].split(" ")]
	
	res = fibd(*data)
	print(res)
	print(sum(res))