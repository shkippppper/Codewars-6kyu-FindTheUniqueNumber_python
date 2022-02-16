def find_uniq(arr):
    n = 0
    a = arr[0]
    b = arr[1]
    c = arr[2]
    if a == b:
        for x in range(len(arr)):
            if arr[x] != a:
                n = arr[x]
                break
    elif a !=b and a!=c:
        n = a
    else:
        n = b
    return n

find_uniq([ 0, 0, 0.55, 0, 0 ])