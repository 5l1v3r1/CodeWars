def make_readable(seconds):
    hour = 0
    minute = 0


    # Hours
    if seconds // 3600 >= 1:
        hour += seconds // 3600
        seconds -= hour * 3600

    if hour == 0:
        hour = "00"

    elif 0 <= hour <= 9:
        hour = "0{}".format(hour)



    # Minutes
    if seconds // 60 >= 1:
        minute += seconds // 60
        seconds -= minute * 60

    if minute == 0:
        minute = "00"

    elif 0 <= minute <= 9:
        minute = "0{}".format(minute)



    # Seconds

    if 0 <= seconds <= 9:
        seconds = "0{}".format(seconds)


    return ("{}:{}:{}".format(hour, minute, seconds))


make_readable(0)
