#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.




fname = open('mbox-short.txt')
count=0
total=0
string="X-DSPAM-Confidence:"
for line in fname:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else:
        count=count+1
        num=float(line[len(string)+1:])
        total=total+num

print("Average spam confidence:",float(total/count))
