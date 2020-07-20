#name = input("Enter file:")
fh = open('mbox-short.txt')

master = dict()

for lines in fh:
    if not 'From ' in lines:
        continue
    else:
        recipient = lines.split()
        emails = recipient[1]
        master[emails] = master.get(emails, 0) + 1

bigcount = None
bigword = None

for word,totalcount in master.items():
    if bigcount is None or totalcount > bigcount:
        bigword = word
        bigcount = totalcount

print(bigword, bigcount)
