def solution(arr):
    tmp = sorted(arr)
    arr.remove(tmp[0])

    if not arr:
        arr.append(-1)

    return arr


def solution(arr):
    arr.remove(min(arr))
    if not arr:
        arr.append(-1)
    return arr