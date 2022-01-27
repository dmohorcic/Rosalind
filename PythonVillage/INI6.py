if __name__ == "__main__":
	with open("PythonVillage/rosalind_ini6.txt", "r") as f:
		data = f.readline().split("\n")[0].split(" ")
	
	d = {w: 0 for w in data}
	for w in data:
		d[w] += 1
	
	for k, v in d.items():
		print(f"{k}: {v}")