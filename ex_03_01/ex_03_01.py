hrs = input("Enter Hours:")
rate = input("Enter Rate:")
if float(hrs) <= 40:
    pay = float(hrs) * float(rate)
else:
    pay = 40*float(rate)+(float(hrs)-40)*float(rate)*1.5
print(pay)
