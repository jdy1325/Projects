def ListSumLoop(numbers):
    sum = 0
    for i in numbers:
        sum += i
    print(sum)


def ListEditLoop(numbers):
    i = 0
    while i < len(numbers):
        print(numbers[i], end="")
        if numbers[i] == 20:
            break
        if numbers[i] == 3:
            numbers[i] = numbers[i] * 5
        i += 1
    print()
    print(numbers)


def ListCheckLoop(numbers):
    key = int(input("Enter an integer to search for in the list: "))
    for i in numbers:
        if i == key:
            break
    if i == key:
        print("FOUND IT!")
    else:
        print("NOT FOUND!")


numbers = [10, 15, 3, 37, 10, 21, 11, 3, 20, 57, 3, 0, 99]
ListSumLoop(numbers)
ListEditLoop(numbers)
ListCheckLoop(numbers)
ListCheckLoop(numbers)