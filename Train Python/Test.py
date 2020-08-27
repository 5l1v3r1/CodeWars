import string

alphabet = [x for x in string.ascii_lowercase]
numbers = [0 for x in range(26)]
dictAlpha = dict(zip(alphabet, numbers))

print(dictAlpha)