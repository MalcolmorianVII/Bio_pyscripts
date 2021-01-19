from Bio import Entrez
from Bio import SeqIO

Entrez.email = "example@gmail.com"
handle = Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id="6273291,6273290,6273289")
for seq_record in SeqIO.parse(handle, "gb"):
    print(seq_record.id, seq_record.description[:100], "....")
    print("Sequence length: ", len(seq_record))

handle.close()
