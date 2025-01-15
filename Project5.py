subjects = ["Calculus", "English", "Algebra", "Biology", "Chemistry"]

print("************************")
print("*         MENU         *")
print("************************")
print("* S - Sort             *")
print("* C - Count            *")
print("* L - Last Index       *")
print("* P - Pop              *")
print("************************")
print("* X - Exit             *")
print("************************")
print("Enter your choice: ")


choice = input()


if choice=='S' or choice=='s':
	print("BEFORE SORT: ",end="")
	print(subjects)
	print("AFTER SORT: ",end="")
	print(sorted(subjects))


elif choice=='C' or choice=='c':
	print("The list has {} subjects.".format(len(subjects)))


elif choice=='L' or choice=='l':
    print("The last index in the list is {}".format(len(subjects)-1))


elif choice=='P' or choice=='p':
	print("BEFORE POP: ",end="")
	print(subjects)
	print("AFTER POP: ",end="")
	subjects.pop()
	print(subjects)


elif choice=='X' or choice=='x':
	print("Goodbye!")


else:
	print("You entered an invalid menu selection!")


print("End of Project #5")