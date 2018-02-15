from Bio.SeqIO.FastaIO import SimpleFastaParser
count=0
total=0
with open(raw_input("Enter the fasta file:"),'rU') as fasta:
 for t,s in SimpleFastaParser(fasta):
  count+=1
  total+=len(s)
print("%i records with proteome size %i" %(count,total))
