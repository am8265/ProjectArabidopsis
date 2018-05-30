#!/usr/bin/env python
import re
import sys
pat=re.compile('^@ERR.+')#my header lines start with @ERR..change this for @<3-4letter approproate pattern>
fh1=open(sys.argv[1])
fh2=open(sys.argv[2])
mate1=dict()
mate2=dict()

for line in fh1:
    line=line.strip().strip(' ')
    if pat.search(line)!=None:#i.e there is a match with header starting with @..
        l=len(line)
        k=line[:l-1]
        mate1[k]=''
    else:
        mate1[k]+=line+'\n'
for line in fh2:
    line=line.strip().rstrip('')
    if pat.search(line)!=None:#i.e there is a match                             
        l=len(line)
        k=line[:l-1]
        mate2[k]=''
    else:
        mate2[k]+=line+'\n'
fh1.close()
fh2.close()
fh1=open(sys.argv[3],'w')
fh2=open(sys.argv[4],'w')
for k in mate1.keys():
    if mate2.get(k,0)!=0:#i.e the same mate pair exists!
        fh1.write(k+'1'+'\n'+mate1[k])
        fh2.write(k+'2'+'\n'+mate2[k])
fh1.close()
fh2.close()
