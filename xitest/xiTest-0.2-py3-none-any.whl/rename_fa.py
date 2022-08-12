import os,sys,re
from Bio import SeqIO

def rename_fasta(infile,outfile,idfile):
    hash={}
    with open(idfile,'r') as handle:
        for line in handle:
            line=line.strip()
            cut=line.split('\t')
            cut[0]="New|"+cut[0]
            hash[cut[0]]=cut[0]+"|"+cut[1]+"|"+cut[2]
    out=open(outfile,'w')
    for seq in SeqIO.parse(infile,'fasta'):
        id=str(seq.id)
        if seq.id in hash.keys():
            id=hash[str(seq.id)]
        out.write(">"+id+"\n"+str(seq.seq).upper()+"\n")

    out.close()

