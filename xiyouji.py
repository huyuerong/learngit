#encoding=utf-8
#!/usr/bin/env python
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')

fr=open('3.txt','r')
characters=[]
stat={}
for line in fr:
	line=line.strip()
	if len(line)==0:
		continue
	
	line=unicode(line)
	for x in xrange(0,len(line)):
		if line[x] in {' ','\{','\}',',','.',';','?'}:
			continue
		if not line in characters:
			characters.append(line[x])
		if not stat.has_key(line[x]):
			stat[line[x]]=0
		stat[line[x]] +=1
print len(characters)
fj=open('result.json','w')
fj.write(json.dumps(stat))
fj.close()
stat=sorted(stat.iteritems(),key=lambda d:d[1],reverse=True)
print type(stat),len(stat)
for x in xrange(0,10):
	print characters[x]

for x in xrange(0,10):
	print stat[x][0],stat[x][1]
fw=open('result.csv','w')
for item in stat:
	fw.write(item[0]+','+str(item[1])+'\n')
fw.close()
fr.close()
