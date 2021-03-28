import re
handle = open('regex_sum_211057.txt')
total = 0
for line in handle :
    y = re.findall('[0-9]+',line)
    for number in y:
        total = total + int(number)
print(total)
