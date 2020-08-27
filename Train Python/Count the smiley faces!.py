def count_smileys(arr):

    correct = 0

    for i in arr:
        if ":)" == i or ":-)" == i or ":~)" == i or ":D" == i or ":-D" == i or ":~D" == i or ";)" == i or ";-)" == i or ";~)" == i or ";D" == i or ";-D" == i or ";~D" == i:
            correct += 1

    return (correct)