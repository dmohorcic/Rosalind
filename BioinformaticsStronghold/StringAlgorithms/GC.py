from Bio import SeqIO

if __name__ == "__main__":
	with open("BioinformaticsStronghold/StringAlgorithms/rosalind_gc.txt", "r") as f:
		data = [rec for rec in SeqIO.parse(f, "fasta")]

	d = {d.name: (d.seq.count("C")+d.seq.count("G"))/len(d.seq) for d in data}
	m_val = max([v for v in d.values()])
	m_name = [k for k, v in d.items() if v == m_val][0]
	print(f"{m_name}\n{m_val*100}")