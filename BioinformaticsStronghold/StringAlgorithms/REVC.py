from Bio.Seq import Seq

if __name__ == "__main__":
    with open("BioinformaticsStronghold/StringAlgorithms/rosalind_revc.txt", "r") as f:
        data = Seq(f.readline().split("\n")[0])
    
    print(data.reverse_complement())