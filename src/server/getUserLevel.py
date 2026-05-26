MAXLV1 = 300
MAXLV2 = 500
MAXLV3 = 850
MAXLV4 = 1150
MAXLV5 = 1500
MAXLV6 = 2000
MAXLV7 = 2400
MAXLV8 = 2850


def getUserLevel(points: int):
    if points < MAXLV1:
        level = 1
    elif points < MAXLV2:
        level = 2
    elif points < MAXLV3:
        level = 3
    elif points < MAXLV4:
        level = 4
    elif points < MAXLV5:
        level = 5
    elif points < MAXLV6:
        level = 6
    elif points < MAXLV7:
        level = 7
    elif points < MAXLV8:
        level = 8
    else:
        level = 9
    return level
