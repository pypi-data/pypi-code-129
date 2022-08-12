import re,os
import sys

def deal_pos(sequence,pos1,pos2):
    sum=sequence.count('-')
    new_pos1=0
    new_pos2=0
    if sum==0:
        new_pos1=pos1
        new_pos2=pos2
    s1=int(pos1)-1
    count1=sequence.count('-',0,s1)
    #print(s1,sum,count1)
    if count1==0:
        new_pos1=pos1
    if count1>0:
        for i in range(1,sum+1):
            s1=int(pos1)-1+i
            n=sequence.count('-',0,s1)
            len1=s1+1
            if len1-n==int(pos1):
                new_pos1=len1
                break
    
    s2=int(pos2)-1
    count2=sequence.count('-',0,s2)
    if count2==0:
        new_pos2=pos2
    if count2>0:
        for i in range(1,sum+1):
            s2=int(pos2)-1+i
            n=sequence.count('-',0,s2)
            len1=s2+1
            if len1-n==int(pos2):
                new_pos2=len1
                break
    print(sum,pos1,pos2,new_pos1,new_pos2)
    return(new_pos1,new_pos2)


def recovery_pos(sequence,pos):
    s1=pos-1
    count1=sequence.count('-',0,s1)
    newpos=pos-count1
    return newpos

#def merge_result(snpfile,indel,outfile):
#    with open (snpfile,'r') as f1:
    
