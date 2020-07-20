fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if line.startswith('This '):
        continue
    words=line.split()
    print(words[3])
