# -*- coding:utf-8 -*-
__author__ = "liang qian"
#author:liangqian at 20220215
import sys
import os
import re
import subprocess
import argparse
import configparser
import datetime
import time
from threading import *
from Bio import SeqIO
from deal_fasta import *
from Callmutation.call_snp_from_fasta import call_snp
from Callmutation.get_indel_from_fasta import call_indel
from Rename.rename_file import rename_fasta,rename_table
from Plot.plot_picture import plot_site_info

def make_dir(inpath):
    if not os.path.exists(inpath):
        os.makedirs(inpath)


class MyThread(Thread):
    def __init__(self,infile,refid,outfile,sem):
        super().__init__()
        self.fa=infile
        self.out=outfile
        self.id=refid
        self.sem=sem
        
    def run(self):
        call_snp(self.fa,self.id,self.out)
        print(self.fa,self.id,self.out)
        time.sleep(1)
        self.sem.release()

class MyThread2(Thread):
    def __init__(self,infile,refid,outdir,sem):
        super().__init__()
        self.fa=infile
        self.out=outdir
        self.id=refid
        self.sem=sem
        
    def run(self):
        call_indel(self.fa,self.id,self.out)
        time.sleep(1)
        self.sem.release()

def get_reverse_pos(string,postion1):
    key,pos=string.split('-')
    cut=postion1.split('-');len1=int(cut[1])-int(cut[0])+1
    repos=int(len1)-int(pos)+1
    string1=key+"-"+str(repos)
    return string1
def main():
    config = configparser.ConfigParser()
    binpath= os.path.split(os.path.abspath(__file__))[0]

    parser=argparse.ArgumentParser()
    parser.add_argument('-i','--fasta')
    parser.add_argument('-p','--pos')
    parser.add_argument('-o','--outdir')
    parser.add_argument('-r','--rename')
    args = parser.parse_args()
    fafile=args.fasta
    posfile=args.pos
    outdir=args.outdir
    make_dir(outdir)
    refid="NC_045512.2"
    lineagename=os.path.basename(fafile).split('_')[0]#谱系名称
    postion={}#引物在参考序列上的位置信息
    newpostion={}#引物在参考序列上新的位置信息
    newpos=[]
    fastalist={}
    seqlist1={}#9段引物放在一起
    uniqseq={}
    primerid={}
    ref=''
    primerref={}#基因组引物片段序列
    sumn=0
    filtern=0
    tmpdir=outdir+"/tmp"
    make_dir(tmpdir)
    logfile=open(outdir+"/run.log","w")
    starttime = datetime.datetime.now()
    time1=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logfile.write("[Run log] start at "+time1+"\n")
    logfile.write("[Run log] read align fasta file "+lineagename+"\n")
    if (args.rename):
        logfile.write("[Run log] rename sequences \n")
        idfile=tmpdir+"/tempid"
        os.system('cut -f 1,3,5 %s >%s'%(args.rename,idfile))
        key1=os.path.basename(fafile)
        key2=key1.replace(' ',"_");
        tmpfadir=tmpdir+"/fa"
        make_dir(tmpfadir)
        outfile=tmpfadir+"/"+key2
        rename_fasta(fafile,outfile,idfile)
        fafile=outfile
        logfile.write("[Run log] rename sequences done \n")
    for seq in SeqIO.parse(fafile,'fasta'):
        id=str(seq.description)
        if re.match(refid,str(seq.id)):
            id=str(seq.id)
        else:
            id=str(seq.description).replace(" ","_")
        m=re.search('EPI_ISL_\d+',id)
        if m:
            id=m.group(0)
        fastalist[id]=str(seq.seq)
        sumn=sumn+1
        if id ==refid:
            fastalist[refid]=str(seq.seq)
            logfile.write("[Run log] read postion file\n")
            newposout=open(outdir+"/newpos.txt","w")
            with open (posfile,'r') as handle:
                for line in handle:
                    line=line.strip()
                    cut=line.split('\t')
                    print(cut)
                    new1,new2=deal_pos(str(seq.seq),cut[1],cut[2])
                    new1=int(new1);new2=int(new2)
                    postion[cut[0]]=cut[1]+"-"+cut[2]
                    newpostion[cut[0]]=str(new1)+"-"+str(new2)
                    s1=new1-1;
                    primerref[cut[0]]=str(seq.seq)[s1:new2]
                    print(cut[0],s1,new2,str(seq.seq)[s1:new2])
                    ref=ref+str(seq.seq)[s1:new2]
                    newpos.append(str(s1)+"-"+str(new2))
                    newposout.write(cut[0]+"\t"+cut[1]+"\t"+cut[2]+"\t"+str(new1)+"\t"+str(new2)+"\n")
                    if cut[0] not in primerid:
                        primerid[str(new1)+"-"+str(new2)]=cut[0]
            newposout.close()
            temseq=''
            for pos1 in newpos:
                cut1=pos1.split('-')
                temseq=temseq+str(seq.seq)[int(cut1[0]):int(cut1[1])]
            seqlist1.setdefault(temseq,[]).append(id)
            logfile.write("[Run log] new position done\n")
            logfile.write("[Run log] remove repeat sequences\n")
        else:
            temseq=''
            for pos1 in newpos:
                cut1=pos1.split('-')
                #print(cut1[0],cut1[1])
                temseq=temseq+str(seq.seq)[int(cut1[0]):int(cut1[1])]
            n=temseq.count('n');N=temseq.count('N')
            if n+N<=1:
                seqlist1.setdefault(temseq,[]).append(id)
            else:
                filtern=filtern+1
    logfile.write("[Run log] filter "+str(filtern)+" sequences \n")
    print(sumn,filtern)
    alln=sumn-filtern-1#去掉低质量序列后的条数
    uniqsum={}#每条序列重复出现的次数
    outfasta1=open(outdir+"/"+lineagename+".complete.fasta","w")
    outfasta2=open(outdir+"/"+lineagename+".part.fasta","w")
    newidlist={}
    lenpart=0
    primerpos={}
    print(postion,newpostion)
    for pos1 in newpos:
        cut1=pos1.split('-')
        p1=int(cut1[0])+1;p2=int(cut1[1])
        pos2=str(p1)+"-"+str(p2)
        p_start=1+lenpart
        lenpart=lenpart+p2-p1+1
        p_end=p2-p1+p_start
        primerpos[primerid[pos2]]=str(p_start)+"-"+ str(p_end)
        #print(primerid[pos2],p_start,p_end)
    primerseq={}#9段基因引物的信息
    primerseq2={}
    for i in primerpos.keys():primerseq.setdefault(i,{})
    for i in primerpos.keys():primerseq2.setdefault(i,{})
    for seq in seqlist1.keys():
        num1=len(seqlist1[seq])
        #print(seq+"\t"+str(num1))
        outfasta2.write(">"+seqlist1[seq][0]+"\n"+seq+"\n")
        outfasta1.write(">"+seqlist1[seq][0]+"\n"+fastalist[seqlist1[seq][0]]+"\n")
        newid=seqlist1[seq][0];newid=newid.replace("/",'-');newid=newid.replace("|",'-')
        newidlist[newid]=seqlist1[seq][0]
        uniqsum[seqlist1[seq][0]]=num1 # 代表id对应的序列重复的次数     
        for key in newpostion.keys():
            cut=newpostion[key].split('-')
            p_start0=int(cut[0])-1;p_end0=int(cut[1])
            primerseq[key][seqlist1[seq][0]]=fastalist[seqlist1[seq][0]][p_start0:p_end0]           

    for key in primerseq.keys():
        outtemp=open(tmpdir+"/"+key+".fasta",'w')
        outtemp.write(">"+refid+" "+postion[key]+" "+newpostion[key]+"\n"+primerref[key]+"\n")
        for key2 in  primerseq[key].keys():
            outtemp.write(">"+key2+"\n"+primerseq[key][key2]+"\n")
        outtemp.close()
 
    outfasta1.close()
    outfasta2.close()
    logfile.write("[Run log] remove repeats done \n")
    logfile.write("[Run log] start call snp \n")
    sem=Semaphore(10)#最大线程数
    threads1=[]
    for key in newpostion.keys():
        file1=tmpdir+"/"+key+".fasta"
        out1=tmpdir+"/"+key+".snp.temp"
        sem.acquire()
        thread = MyThread(file1,refid,out1,sem)
        threads1.append(thread)
        thread.start()

    for t in threads1:
        t.join()

    out=open(outdir+"/snp.xls",'w')
    out_snpt=open(outdir+"/snp.plot.xls",'w')
    numsnp=0
    format_snpout={}
    for key in newpostion.keys(): #遍历位点，从相对位置推算原始位置并且计算突变频率
        pos=newpostion[key].split('-')
        print(pos)
        prim=key
        direc='NA'
        if re.search(r'(\w+)(F|R|P)',key):
            prim=re.search(r'(\w+)(F|R|P)',key).group(1)
            direc=re.search(r'(\w+)(F|R|P)',key).group(2)
        with open(tmpdir+"/"+key+".snp.temp",'r') as handle:#引物信息
             for line in handle:
                 line=line.strip()
                 cut=line.split("\t")
                 posn1=int(pos[0])+int(cut[0])-1
                 n=primerref[key].count('-',0,int(cut[0])-1)
                 #print(key+"\t"+str(n))
                 posprint=int(cut[0])-n
                 sample=cut[-1].split(',')
                 num2=0
                 for sam in sample:
                     num2=num2+int(uniqsum[sam])#uniqsum[sam]为序列重复次数
                 rate=round(int(num2)*100/int(alln),4)
                 for sam in sample:
                     numsnp+=1
                     conn=key+"-"+str(posprint)+"|"+cut[1]+"|"+str(rate)+"|"+str(num2)
                     format_snpout.setdefault(sam,{}).setdefault(prim,{}).setdefault(direc,[]).append(conn)
                     out_snpt.write(lineagename+"\t"+sam+"\t"+primerseq[key][sam]+"\t"+key+"-"+str(posprint)+"\t"+cut[1]+"\t"+str(uniqsum[sam])+"\t"+str(rate)+"\t"+str(num2)+"\t"+str(alln)+"\n")
    out_snpt.close()
    print(format_snpout)
    for key in format_snpout.keys():
       for prim in format_snpout[key]:
           a=sorted(format_snpout[key][prim].keys(),reverse=False)
           s=[]
           b=[]
           c=[]
           r=[]
           nn=[]
           b_re=[]
           for direct in a:
               id=prim+direct
               if direct=="NA":
                   id=prim
               s.append(primerseq[id][key])
               con= format_snpout[key][prim][direct]
               for con1 in con:
                   cut=con1.split('|')
                   re_b=get_reverse_pos(cut[0],postion[id])
                   b_re.append(re_b)
                   b.append(cut[0]);c.append(cut[1]);r.append(cut[2]);nn.append(cut[3])
           out.write(lineagename+"\t"+key+"\t"+'\t'.join('%s' %s1 for s1 in s)+"\t"+';'.join('%s'%str(b1) for b1 in b)+"\t"+';'.join('%s'%str(c1) for c1 in c)+"\t"+';'.join('%s'%str(r1) for r1 in r)+"\t"+';'.join('%s'%str(n1) for n1 in nn)+"\t"+str(alln)+"\t"+';'.join('%s'%reb for reb in b_re)+"\n") 
    out.close()           
    logfile.write("[Run log] find %s snp \n" % numsnp)
    logfile.write("[Run log] call snp done\n")
    logfile.write("[Run log] start call indel \n")
    
    threads2=[]
    sem2=Semaphore(10)#最大线程数
    for key in newpostion.keys():
        file1=tmpdir+"/"+key+".fasta"
        outindel=tmpdir+"/"+key
        make_dir(outindel)
        sem2.acquire()
        thread2 = MyThread2(file1,"NC_045512.2",outindel,sem2)
        threads2.append(thread2)
        thread2.start()

    for t in threads2:
        t.join()
    out2=open(outdir+"/indel.xls",'w') #合并indel,遍历位点，推算原始位置,统计突变率
    numindel=0

    for key in newpostion.keys():
        outindel=[]
        rate_indel={}
        pos=newpostion[key].split('-')
        with open(tmpdir+"/"+key+"/indel.xls",'r') as handle:
            for line in handle:
                line=line.strip()
                cut=line.split("\t")
                if re.search('-',cut[2]):
                    s,t=cut[2].split('-')
                    n1=primerref[key].count('-',0,int(s)-1)
                    n2=primerref[key].count('-',0,int(t)-1)
                    sprint=int(s)-n1
                    tprint=int(t)-n2
                    if cut[-1]=="insertion":
                        tprint=sprint+len(cut[4])-1
                    posprint=str(sprint)+"-"+str(tprint)
                    print("posprint",posprint)
                    tempkey=posprint+cut[5]
                    if tempkey not in rate_indel:
                        rate_indel[tempkey]=int(uniqsum[cut[1]])
                    else:
                        rate_indel[tempkey]=rate_indel[tempkey]+int(uniqsum[cut[1]])
                    outindel.append(lineagename+"\t"+cut[1]+"\t"+key+"\t"+posprint+"\t"+cut[3]+"\t"+cut[4]+"\t"+cut[5])
                    numindel+=1
               
                else:
                    posn1=int(pos[0])+int(cut[2])-1
                    n=primerref[key].count('-',0,int(cut[2])-1)
                    posprint=str(int(cut[2])-n)
                    tempkey=posprint+cut[5]
                    if tempkey not in rate_indel:
                        rate_indel[tempkey]=int(uniqsum[cut[1]])
                    else:
                        rate_indel[tempkey]=rate_indel[tempkey]+int(uniqsum[cut[1]])
                    outindel.append(lineagename+"\t"+cut[1]+"\t"+key+"\t"+posprint+"\t"+cut[3]+"\t"+cut[4]+"\t"+cut[5])
                    numindel+=1
            
            for t in outindel:
                cut1=t.split('\t')
                tempkey=cut1[3]+cut1[6]
                rate=round(rate_indel[tempkey]*100/int(alln),4)
                out2.write(t+"\t"+str(rate)+"\t"+str(rate_indel[tempkey])+"\t"+str(alln)+"\n")                
    out2.close()
    logfile.write("[Run log] find %s indel \n" % numindel)    
    logfile.write("[Run log] call indel done \n")
    time2=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    endtime = datetime.datetime.now()
    #print(endtime,starttime)
    t=(endtime - starttime).seconds
    logfile.write("[Run log] elapsed "+ str(t) +" seconds\n")
    logfile.write("[Run log] start plot picture \n")
    plot_site_info(outdir+"/snp.plot.xls",outdir+"/indel.xls",posfile,outdir)
    #snptfile=outdir+'/snp.xls.temp'
    #rename_table(outdir+'/snp.xls',snptfile)
    #indeltfile=outdir+'/indel.xls.temp'
    #rename_table(outdir+'/indel.xls',indeltfile)
    #os.system("mv %s/snp.xls.temp %s/snp.xls"%(outdir,outdir))
    #os.system("mv %s/indel.xls.temp %s/indel.xls"%(outdir,outdir))
    #rename_table(outdir+'/snp.plot.xls',outdir+'/snp.plot.xls2')
    #os.system("mv %s/snp.plot.xls2 %s/snp.plot.xls"%(outdir,outdir))
    outall=open(outdir+"/all_mutation.txt",'w')
    outall.write("谱系\tID\t引物\t位置\t碱基\t突变信息\t突变频率\t序列条数\n")
    with open (outdir+"/snp.plot.xls",'r') as f1:
        for line in f1:
            line=line.strip()
            cut=line.split("\t")
            t1=cut[3].split('-')
            t2=cut[4].split('->')
            s1=postion[t1[0]].split('-')[0]
            newp1=int(s1)+int(t1[1])-1
            outall.write(cut[0]+"\t"+cut[1]+"\t"+t1[0]+"\t"+str(newp1)+"\t"+t2[0]+"\t"+t2[1]+"\t"+cut[6]+"%\t"+cut[8]+"\n")
        
    with open (outdir+"/indel.xls",'r') as f2:   
        for line in f2:
            line=line.strip()
            cut=line.split("\t")
            type=''
            if cut[6]=="deletion":
                type="缺失"
            else:
                type="插入"
            s1=postion[cut[2]].split('-')[0]
            if re.search('-',cut[3]):
                t=cut[3].split('-')
                n1=int(s1)+int(t[0])-1
                n2=int(s1)+int(t[1])-1
                newp1=str(n1)+"-"+str(n2)
            else:
                newp1=int(s1)+int(cut[3])-1
            outall.write(cut[0]+"\t"+cut[1]+"\t"+cut[2]+"\t"+str(newp1)+"\t"+cut[4]+"\t"+cut[5]+"\t"+cut[7]+"%\t"+cut[9]+"\t"+type+"\n")            
    outall.close()         
    logfile.write("[Run log] plot picture done\n")
    time2=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    endtime = datetime.datetime.now()
    t=(endtime - starttime).seconds
    logfile.write("[Run log] done at "+time2+", Used "+str(t)+" seconds"+"\n")
    logfile.close()
    os.system('rm -f %s/snp.plot.xls'%outdir)
    os.system('rm -rf %s/tmp'%outdir)
    #os.system('rm -rf %s'%fafile)
if __name__ == '__main__':
    main()
    
    
