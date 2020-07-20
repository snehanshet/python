#import re
#hand=open('actual data.txt')
#numlist=list()
#for line in hand:
#    line=line.rstrip()
#    stuff=re.findall('([0-9]+#)',line)
#    if len(stuff)!=1:continue
#    num=int(stuff[0])
#    numlist.append(num)
#print('sum:',sum(numlist))

import re

hand = open("sample data.txt")
x=list()
for line in hand:
     y = re.findall('[0-9]+',line)
     x = x+y

sum=0
for z in x:
    sum = sum + int(z)

print(sum)
  
