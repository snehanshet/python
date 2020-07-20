text = "X-DSPAM-Confidence: 0.84756"
atpos=text.find(' ')
#print atpos
sppos=text.find('6',atpos)
#print sppos
host=text[atpos+1:sppos]
hos=float(host)
print(hos)
