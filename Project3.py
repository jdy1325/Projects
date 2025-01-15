
s = input('Enter a string: ')

firstCharacter = s[0]
lastCharacter = s[len(s) - 1]
midCharacter = s[1:len(s) - 1]
restString = s[1:]

newS = lastCharacter + midCharacter + firstCharacter

fixedString = restString.replace(firstCharacter, '@')

print("1.)", len(s))
print("2.)", s[::-1])
print("3.)", newS)
print("4.)", firstCharacter + fixedString)