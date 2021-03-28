name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle :
    words = line.split()
    if len(line) < 3 or words[0] != 'From' :
        continue
    counts[words[1]] = counts.get(words[1],0) + 1
bigname = None
bigcount = None
for name,count in counts.items() :
    if bigname is None or count > bigcount :
        bigname = name
        bigcount = count
print(bigname,bigcount)
