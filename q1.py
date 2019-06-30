
def generator(start, stop):
    start = start.split('-')
    stop = stop.split('-')
    start[0], start[1] = int(start[0]), int(start[1])
    stop[0], stop[1] = int(stop[0]), int(stop[1])
    result = []
    if start[0] != stop[0]:
        for i in range(start[0], stop[0]+1):
            if start[0] == i:
                for j in range(start[1], 1000):
                    if j < 10:
                        result.append("{i}-00{j}".format(i=i, j=j))
                    elif j < 100:
                        result.append("{i}-0{j}".format(i=i, j=j))
                    else:
                        result.append("{i}-{j}".format(i=i, j=j))
            elif int(stop[0]) == i:
                for j in range(0, stop[1]+1):
                    if j < 10:
                        result.append("{i}-00{j}".format(i=i, j=j))
                    elif j < 100:
                        result.append("{i}-0{j}".format(i=i, j=j))
                    else:
                        result.append("{i}-{j}".format(i=i, j=j))
            else:
                for j in range(0, 1000):
                    if j < 10:
                        result.append("{i}-00{j}".format(i=i, j=j))
                    elif j < 100:
                        result.append("{i}-0{j}".format(i=i, j=j))
                    else:
                        result.append("{i}-{j}".format(i=i, j=j))
    return result



generator('79-900', '80-155')