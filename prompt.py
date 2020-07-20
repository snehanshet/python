#fname=input("enter the filename: ")
fhand=open('mbox-short.txt')
count=0
for line in fhand:
    if line.startswith('X-DSPAM'):
        count=count+1
        line=line.rstrip()
        print(line)
print('there were',count,'subject lines in',fhand)
