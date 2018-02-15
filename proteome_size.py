#This is from biopython tutorial not modified
from Bio.SeqIO.FastaIO import SimpleFastaParser #Load fasta parser from biopython
count=0 #Start counting as 0
total=0
with open(raw_input("Enter the fasta file:"),'rU') as fasta:       #Load the fasta file
 for t,s in SimpleFastaParser(fasta): #parse sequence and update within loop
  count+=1
  total+=len(s)
print("%i records with proteome size %i" %(count,total)) #Print the number of sequences and AAs
