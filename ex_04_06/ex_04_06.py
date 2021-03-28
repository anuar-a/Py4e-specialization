hrs = input("Enter Hours:")
rate = input("Enter Rate:")
fhrs = float(hrs)
frate = float(rate)

def computepay(h,r):
    if float(hrs) <= 40:
        pay = h * r
    else:
        pay = 40*r + (h-40)*r*1.5
    return pay
p = computepay(fhrs,frate)
print(p)
