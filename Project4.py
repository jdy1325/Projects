weight=int(input("Please enter your weight in pounds :"))

if (weight>=0 and weight<50):
	print("Eat more")

elif(weight>=50 and weight<100):
	print("I hope you are short")

elif(weight>=100 and weight<200):
	print("Quite Average")

elif(weight>=200 and weight<300):
	print("I hope you are tall")

elif(weight>=300 and weight<500):
	print("Into sumo?")

else:
	print("You liar")