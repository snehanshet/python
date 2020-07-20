# Use words.txt as the file name
fname = open('words.txt')
for lx in fname:
    ly=lx.rstrip()
    print(ly.upper())
