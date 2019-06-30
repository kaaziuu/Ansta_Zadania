def lost_num(arr , n):
    result = []
    for i in range(1, n+1):
        if not i in arr:
            result.append(i)
    return result


print(lost_num([2,3,7,4,9], 10))