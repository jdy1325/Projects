def StringSumLoop(quote):
    sum = 0
    for i in quote:
        sum += ord(i)
    print(sum)


def StringSpaceLoop(quote):
    count = 0
    i = 0
    while i < len(quote):
        if quote[i] == ' ':
            count += 1
        i += 1
    print(count)


def StringWordsLoop(quote):
    count = 1
    for i in range(len(quote) - 1):
        if quote[i] == ' ' and quote[i + 1] != ' ':
            count += 1
    print(count)


quote = "Anyone who has never made a mistake has never tried anything new."
StringSumLoop(quote)
StringSpaceLoop(quote)
StringWordsLoop(quote)

