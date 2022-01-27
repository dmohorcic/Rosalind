if __name__ == "__main__":
	with open("PythonVillage/rosalind_ini2.txt", "r") as f:
		data = f.readline().split("\n")[0].split(" ")
	
	print(int(data[0])**2 + int(data[1])**2)