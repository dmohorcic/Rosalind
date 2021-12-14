if __name__ == "__main__":
    with open("StringAlgorithms/rosalind_dna.txt", "r") as f:
        data = f.readline().split("\n")[0]
    print(data.count("A"), data.count("C"), data.count("G"), data.count("T"))