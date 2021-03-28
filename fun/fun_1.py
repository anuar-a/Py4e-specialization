import re
print('Hello Aknur! This program is made for fun')
print('')
handle = open('chat.txt',encoding="utf8")
counts = dict()
for line in handle :
    y = re.findall('\S+',line)
    for word in y:
        #print(word)
        counts[word] = counts.get(word,0) + 1
tmp = list()
for k,v in sorted(counts.items()) :
    tmp.append((v,k))
tmp = sorted(tmp, reverse=True)
for k,v in tmp[0:30] :
    print('"'+v+'"','встречалось',k,'раз')
