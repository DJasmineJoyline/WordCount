import string
name=input('Enter file')
handle=open(name,'r')
counts=dict()
for line in handle:
 line=line.translate(str.maketrans('','',string.punctuation))
 line=line.lower()
 words=line.split()
 for word in words:
  if word not in counts:
   counts[word]=1
  else:
   counts[word]+=1
lst=list()
for key,val in list (counts.items()):
 lst.append((val,key))
lst.sort(reverse=True)
for key,val in lst[:10] :
 print(key,val)
