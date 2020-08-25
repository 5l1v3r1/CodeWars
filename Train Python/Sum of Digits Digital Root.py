def digital_root(n):
    theSum = 0

    for i in range(len(str(n))):
        theSum += int(str(n)[i])

    if len(str(theSum)) == 1:
        print(theSum)
    else:
        while len(str(theSum)) != 1:
            replacementSum = 0
            for i in range(len(str(theSum))):
                replacementSum += int(str(theSum)[i])
            theSum = replacementSum

    return (theSum)