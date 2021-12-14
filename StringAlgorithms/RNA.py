if __name__ == "__main__":
    with open("StringAlgorithms/rosalind_rna.txt", "r") as f:
        data = f.readline().split("\n")[0]
    print(data.replace("T", "U"))
