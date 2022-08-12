#-*- conding: UTF-8 -*-
#author: liangqian at 20220303

import sys
import os,re
import svgwrite


def deal_pos(posfile):
    hash1={}
    with open (posfile,'r') as handle:
        for line in handle:
            line=line.strip()
            cut=line.split('\t')
            hash1[cut[0]]=cut[1]
    return hash1
    
def caculate_site(infile1,infile2,outdir,posfile):
    n1=0
    n2=0
    all00={}
    all0={}
    all1={}
    num1=0
    num2=0
    head=''
    make_dir(outdir)
    poscon=deal_pos(posfile)
    with open (infile1,'r') as handle:#背景文件
        for line in handle:
            n1=n1+1
            line=line.strip()
            cut=line.split('\t')
            key1=cut[0]+"\t"+cut[2]
            if n1==1:
                head=line
                continue
            if re.search('-',cut[3]):
                t=cut[3].split('-')
                if int(t[0])<30:
                    t1=int(poscon[cut[2]])+int(t[0])-1
                    t2=int(poscon[cut[2]])+int(t[1])-1
                    cut[3]=str(t1)+"-"+str(t2)
                    print(cut[3])
            else:
                #print(cut[3])
                if int(cut[3])<30:
                    cut[3]=str(int(poscon[cut[2]])+int(cut[3])-1)
                #print(cut[3])
            key=cut[2]+"|"+cut[3]+"|"+cut[4]+"|"+cut[5]
            #print(cut)
            con=cut[6]+"|"+str(cut[7])+"|"+cut[1]
            if cut[-1]=="插入" or cut[-1] =="缺失":
                con=con+"|"+cut[-1] 
            if n1 >1:
                num1=cut[7]
                all00.setdefault(key1,{})[key]=con
                all0.setdefault(key1,{})[key]=con
    name1=os.path.basename(infile2)
    #print(all0)
    out1=open(outdir+"/"+name1+".new.txt",'w')
    out1.write(head+"\n")
    with open (infile2,'r') as handle:#新文件
        for line in handle:
            n2=n2+1
            line=line.strip()
            cut=line.split('\t')
            key1=cut[0]+"\t"+cut[2]
            if n2==1:
                continue
            if re.search('-',cut[3]):
                t=cut[3].split('-')
                if int(t[0])<30:
                    t1=int(poscon[cut[2]])+int(t[0])-1
                    t2=int(poscon[cut[2]])+int(t[1])-1
                    cut[3]=str(t1)+"-"+str(t2)
            else:
                if int(cut[3])<30:
                    cut[3]=str(int(poscon[cut[2]])+int(cut[3])-1)
            
            key=cut[2]+"|"+cut[3]+"|"+cut[4]+"|"+cut[5]

            if n2 >1:
                rate=float(cut[6].replace('%',''))/100
                #print(cut[7])
                num2=cut[7]
                sumall=int(num1)+int(num2)
                con=''
                if key1 in all00.keys() and key in all00[key1].keys():
                    con1=all00[key1][key].split('|')
                    rate1=float(con1[0].replace('%',''))/100
                    rate_new=round((rate1*int(con1[1])+rate*int(cut[7]))*100/sumall,4)
                    con=str(rate_new)+"%"+"|"+str(sumall)+"|"+cut[1]
                else:
                    rate_new=round((rate*int(cut[7]))*100/sumall,4)
                    con=str(rate_new)+"%"+"|"+str(sumall)+"|"+cut[1]
                    
                if cut[-1]=="插入" or cut[-1] =="缺失":
                    con=con+"|"+cut[-1]     
                all1.setdefault(key1,{})[key]=con
                all0.setdefault(key1,{})[key]=con
                cut[6]=str(rate_new)+"%";cut[7]=sumall
                tt='\t'.join('%s'%d for d in cut)
                out1.write(tt+"\n")
                            
    out1.close()
    
    name2=os.path.basename(infile1)
    out2=open(outdir+"/"+name2+".allnew.txt",'w')
    out2.write(head+"\n")
    #print(all1)
    for key1 in all0.keys():
        for key2 in all0[key1]:
            cut1=key1.split("\t")
            #print(key1)
            if key1 in all1.keys() and key2 in all1[key1]:
                cut2=key2.replace("|","\t")
                cut3=all0[key1][key2].split('|')
                cut4=all1[key1][key2].split('|')
                #print(cut1,cut[3],cut2)
                if cut3[-1] =="插入" or cut3[-1] =="缺失":
                    out2.write(cut1[0]+"\t"+cut3[2]+"\t"+cut2+"\t"+cut3[0]+"\t"+cut3[1]+"\t"+cut3[-1]+"\n")
                else:
                    out2.write(cut1[0]+"\t"+cut3[2]+"\t"+cut2+"\t"+cut3[0]+"\t"+cut3[1]+"\n")
            
            
            else:
                cut2=key2.replace("|","\t")
                cut3=all0[key1][key2].split('|')
                sumn=int(cut3[1])+int(num2)
                rate=(float(cut3[0].replace('%',''))*int(cut3[1])/100)*100/sumn
                rate=round(rate,4)
                
                if cut3[-1] =="插入" or cut3[-1] =="缺失":
                    out2.write(cut1[0]+"\t"+cut3[2]+"\t"+cut2+"\t"+str(rate)+"%\t"+str(sumn)+"\t"+cut3[-1]+"\n")
                else:
                    out2.write(cut1[0]+"\t"+cut3[2]+"\t"+cut2+"\t"+str(rate)+"%\t"+str(sumn)+"\n")
                    
    out2.close()
    plotfile=outdir+"/"+name1+".new.txt"
    return plotfile

def plot_site_info(plotfile,posfile,outdir):
    positon={}
    color={}
    lines={}
    lens={}
    lens2={}
    outdir1=outdir+"/svg"
    outdir2=outdir+"/png"
    make_dir(outdir1)
    make_dir(outdir2)
    newpos={}
    offset={}
    with open (plotfile,'r') as handle:#先赋值
        for line in handle:
            line=line.strip()
            cut=line.split('\t')
            key=cut[1]
            lens2.setdefault(key,{})
            newpos.setdefault(key,{})
            offset.setdefault(key,{})
    with open (posfile,'r') as handle:
        for line in handle:
            line=line.strip()
            cut=line.split('\t')
            lens[cut[0]]=int(cut[2])-int(cut[1])+1
            #print(cut[0],lens[cut[0]])
            positon[cut[0]]=int(cut[1])
            for key in lens2.keys():
                lens2[key][cut[0]]=int(cut[2])-int(cut[1])+1
                newpos[key].setdefault(cut[0],{})
                offset[key][cut[0]]=0
            if cut[0].endswith('F'):
                color[cut[0]]="red"
            if cut[0].endswith('P'):
                color[cut[0]]="green"
            if cut[0].endswith('R'):
                color[cut[0]]="blue"
    out1=open(outdir+"/plot.txt",'w')
    
    nn=0
    with open (plotfile,'r') as handle:#转变坐标轴
        for line in handle:
            nn=nn+1
            if nn >1:
                line=line.strip()
                cut=line.split('\t')
                del(cut[0])#谱系名称
                if re.search('-',cut[2]):
                    s,t=cut[2].split('-')
                    n1=int(s)-positon[cut[1]]+1;n2=int(t)-positon[cut[1]]+1
                    cut[2]=str(int(n1))+"-"+str(int(n2))
                else:
                    cut[2]=int(cut[2])-positon[cut[1]]+1
                #print(cut[2])
                tt='\t'.join('%s'%d for d in cut)
                out1.write(tt+"\n")
    out1.close()
    
    plotfile=outdir+"/plot.txt"
    
    #print(newpos)
    with open (plotfile,'r') as handle:
        for line in handle:
            line=line.strip()
            cut=line.split('\t')
            key=cut[1]
            con=''           
            if cut[-1]=="插入":
                lens2[cut[0]][cut[1]]+=len(cut[4])
                maxp=0
                if re.search('-',cut[2]):
                    s,t=cut[2].split('-')
                    print(s,t)
                    n1=int(s);n2=int(t)
                    maxp=n1-1
                    for n in range(n1,n2+1):
                         pos=int(n);i=int(n)-n1
                         base=cut[4][i]
                         if offset[cut[0]][key]>0:
                              pos=pos+offset[cut[0]][key]
                         con=str(pos)+"|"+cut[-3]+"|"+base+"|ins"
                         lines.setdefault(cut[0],{}).setdefault(key,[]).append(con) 
                else:
                    pos=int(cut[2])
                    maxp=pos-1
                    if offset[cut[0]][key]>0:
                        pos=pos+offset[cut[0]][key]
                    con=str(pos)+"|"+cut[-3]+"|"+cut[4]+"|ins"
                    lines.setdefault(cut[0],{}).setdefault(key,[]).append(con)
                offset[cut[0]][key]+=len(cut[4])
                #print(cut[0],maxp)
                for i in range(0,maxp):
                    if i not in newpos[cut[0]][key]:
                        #print(i,maxp)
                        newpos[cut[0]][key][i]=i
                for i in range(maxp,lens[key]):
                    #print("***",i,i+offset[cut[0]][key],maxp,lens[key])
                    newpos[cut[0]][key][i]=i+offset[cut[0]][key]               
            elif cut[-1]=="缺失":
                if re.search('-',cut[2]):
                    s,t=cut[2].split('-')
                    n1=int(s);n2=int(t)
                    for n in range(n1,n2+1):
                        pos=int(n);i=int(n)-n1
                        base=cut[4][i]
                        if offset[cut[0]][key]>0:
                            pos=pos+offset[cut[0]][key]
                        con=str(pos)+"|"+cut[-3]+"|"+base+"|del"
                        lines.setdefault(cut[0],{}).setdefault(key,[]).append(con)
                       
                else:
                    pos=int(cut[2])
                    if offset[cut[0]][key]>0:
                        pos=pos+offset[cut[0]][key]
                    con=str(pos)+"|"+cut[-3]+"|"+cut[4]+"|del"
                    lines.setdefault(cut[0],{}).setdefault(key,[]).append(con)
    #print(newpos)
    newpos2={}
    #print(lines)
    for key1 in lines.keys():
        for key2 in lines[key1].keys():
            tt='\t'.join(lines[key1][key2])
            if re.search('ins',tt):
                newpos2.setdefault(key1,{}).setdefault(key2,{})
                for k,v in newpos[key1][key2].items():
                    #print(k,v,"!!!")
                    newpos2[key1][key2][v]=k
    #print("********************")
    #print(newpos2)
    

    #print(lines)                   
    #snp
    with open (plotfile,'r') as handle:
        for line in handle:
            line=line.strip()
            cut=line.split('\t')
            key=cut[1]
            pos=cut[2]
            if cut[-1] !="插入" and cut[-1] !="缺失":
                s=cut[3];t=cut[4];
                if cut[0] in newpos2 and key in newpos2[cut[0]]:
                    newpos1=newpos[cut[0]][key][int(pos)-1]+1
                    con=str(newpos1)+"|"+s+"|"+t+"|"+str(cut[-2])+"|snp"
                else:
                    con=pos+"|"+s+"|"+t+"|"+str(cut[-2])+"|snp"
                lines.setdefault(cut[0],{}).setdefault(key,[]).append(con)
    #print(lines)
    os.system('rm -rf %s/plot.txt'%outdir)
    threads=[]   
    for sam in lines.keys():
        for key in lines[sam]:
            outkey=sam.replace("/",'-');outkey=outkey.replace("|",'-');
            id=sam
            edgeTop,edgeBottom,edgeLeft,edgeRight = (40,40,100,80);
            H=90
            scale_y=H/2
            scale_x=70
            W=scale_x*lens2[sam][key]
            width=W+edgeLeft+edgeRight
            height=H+edgeTop+edgeBottom
            dwg = svgwrite.Drawing(outdir1+"/%s.%s.svg"% (id,key),size=(width,height))
            pngname=id+"."+key
            dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))#添加白色背景
            #print(lens[key],scale_x,scale_y)
            y1=edgeTop+10;x1=edgeLeft-45;
            dwg.add(dwg.text("ID", insert=(x1,y1),fill="black",style="font-size:14px;font-weight:bold"))
            y2=edgeTop+scale_y;x1=edgeLeft-75;
            dwg.add(dwg.text("Mutation rate", insert=(x1,y2),fill="black",style="font-size:14px;font-weight:bold"))
            y3=edgeTop+scale_y*2;x1=edgeLeft-90
            dwg.add(dwg.text(id, insert=(x1,y3),fill="black",style="font-size:14px;font-weight:bold"))
            for i in range(lens2[sam][key]):
                if sam not in newpos2:
                    posn=int(positon[key])+i
                elif sam in newpos2 and key not in newpos2[sam]:
                    posn=int(positon[key])+i
                else:
                    if i in newpos2[sam][key]:
                        posn=int(positon[key])+int(newpos2[sam][key][i])
                    else:
                        posn=''
                #print(i,posn)
                y1=edgeTop+10;x1=edgeLeft+scale_x*(i+1)
                dwg.add(dwg.text(posn, insert=(x1,y1),fill="black",style="font-size:13px;font-weight:bold"))
            for j in range(len(lines[sam][key])):
                con=lines[sam][key][j]
                cut=con.split('|')
                x=edgeLeft+scale_x*int(cut[0])-5;y=edgeTop+scale_y
                text2=''
                if cut[-1] == 'snp':
                    text1=str(cut[-2])
                    if sam in newpos2 and key in newpos2[sam]:
                        pp=int(newpos2[sam][key][int(cut[0])-1])
                        text2=cut[1]+str(positon[key]+pp)+cut[2]
                    else:
                        text2=cut[1]+str(positon[key]+int(cut[0])-1)+cut[2]
                    dwg.add(dwg.text(text1, insert=(x,y),fill="black",style="font-size:13px;font-weight:bold"))
                else:
                    text1=str(cut[1])
                    dwg.add(dwg.text(text1, insert=(x,y),fill="black",style="font-size:13px;font-weight:bold"))
                    x=edgeLeft+scale_x*int(cut[0])+15
                    text2=cut[2]
                y2=edgeTop+scale_y*2
                #print(text2)
                dwg.add(dwg.text(text2, insert=(x,y2),fill="black",style="font-size:13px;font-weight:bold"))
            x1=edgeLeft+scale_x-10;y1=edgeTop+scale_y*1+20;x2=edgeLeft+scale_x*lens2[sam][key]+scale_x-10;
            y2=H+edgeTop+10;
            #print(y1,y2)
            dwg.add(dwg.path(d='M{0},{1} L{2},{3} L{4},{5} L{6},{7} L{8},{9}Z'.format(x1,y1,x1,y2,x2,y2,x2,y1,x1,y1), stroke=color[key],fill="none",stroke_width=2))

            dwg.save()
            os.system("inkscape -z -e {0}/{1}.png {2}/{3}.svg".format(outdir2,pngname,outdir1,pngname))

    

def make_dir(inpath):
    if not os.path.exists(inpath):
        os.makedirs(inpath)

if __name__ == '__main__':    
    plotfile=caculate_site(sys.argv[1],sys.argv[2],sys.argv[4],sys.argv[3])
    plot_site_info(plotfile,sys.argv[3],sys.argv[4])
