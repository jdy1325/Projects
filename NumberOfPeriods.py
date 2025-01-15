
import math

FV=4000
r=0.06/12
P=100

numerator = FV * r
denominator = P

n = math.log(1 + numerator/denominator)/math.log(1+r)

print("Number of Periods = ",n)