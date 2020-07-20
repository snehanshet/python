data='from snehanshet1999@gmail.com sat 25 jun 2008'
atpos=data.find(' ')
print atpos
sppos=data.find('1',atpos)
print sppos
host=data[atpos+1:sppos]
print host
