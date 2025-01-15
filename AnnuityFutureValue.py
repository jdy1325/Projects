P=100
r=0.06/12
n=2*12

numerator = (1+r)**n-1
denominator = r

FV=P*(numerator/denominator)

print("Annuity's Future Value", FV)