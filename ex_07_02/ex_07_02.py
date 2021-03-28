# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(" ")
    line = line.rstrip()
    value = float(line[pos:])
    total = total + value
    count = count + 1
avg = total/count
print("Average spam confidence:",avg)
