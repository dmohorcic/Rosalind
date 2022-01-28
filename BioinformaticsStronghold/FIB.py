import os
from pathlib import Path
FILENAME = os.path.join(os.path.dirname(__file__), f"rosalind_{Path(__file__).stem.lower()}.txt")

def fib(n, k):
	a, b = 1, 1
	for i in range(2, n):
		a, b = b, a*k+b
	return b

if __name__ == "__main__":
	with open(FILENAME, "r") as f:
		data = [int(x) for x in f.readline().split("\n")[0].split(" ")]
	
	print(fib(data[0], data[1]))