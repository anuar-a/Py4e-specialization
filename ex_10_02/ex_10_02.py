name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle :
    words = line.split()
    if len(line) < 3 or words[0] != 'From' :
        continue
    hours = words[5].split(':')
    counts[hours[0]] = counts.get(hours[0],0) + 1
for k,v in sorted(counts.items()) :
    print(k,v)
