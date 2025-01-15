def DictionaryAvgLoop():
  ages = {"John":21, "Beth":27, "Bill":65, "Joe":40, "Sarah":7, "Jane":16}
  ageSum = 0
  for key in ages:
    ageSum += ages[key]
  ageAvg = ageSum / len(ages)
  print("The average age is", ageAvg)


def DictionaryAddLoop():
  dictionary = {}
  while True:
    name = input("Enter a name: ")
    if not name:
      break
    age = input("Enter an age: ")
    dictionary[name] = age
  for key in sorted(dictionary):
    print(key + ":" + dictionary[key])


def DictionaryCountLoop():
  names = {'John': 21, 'Beth': 32, 'Bill': 70, 'Joe': 40, 'Sarah': 7, 'Jane': 16}
  count = 0
  for key in names.keys():
    if key[0] == 'J':
      count += 1
  for key in names.keys():
    if key[0] == 'B':
      names[key] = names[key] + 5
  print(count)
  print(names)


DictionaryAvgLoop()
DictionaryAddLoop()
DictionaryCountLoop()