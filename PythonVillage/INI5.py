if __name__ == "__main__":
	with open("PythonVillage/rosalind_ini5.txt", "r") as f:
		i = False
		for l in f:
			if i:
				print(l.split("\n")[0])
			i = not i
