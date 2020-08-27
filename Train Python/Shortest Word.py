def find_short(s):
    # your code here
    words = []
    words = s.split(" ")
    l = len(words[0])
    for i in range(len(words)):
        if len(words[i]) < l:
            l = len(words[i])
    return l

find_short("i want to travel the world writing code one day")