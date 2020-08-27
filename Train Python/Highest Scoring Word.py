def high(x):
    words = x.split(" ")
    amount = []


    for i in range(len(words)):
        sum = 0

        for j in range(len(words[i])):
            sum += ord(words[i][j])

        amount.append(sum)

    longestWordIndex = amount.index(max(amount))
    return (words[longestWordIndex])

high('what time are we climbing up the volcano')