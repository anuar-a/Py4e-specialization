text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('0.8475');
result = text[pos:]
fresult = float(result)
print(fresult)
