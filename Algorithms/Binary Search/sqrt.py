def condition(mid, k):
    return mid**2 > k


def sqrt(k):
    left = 0
    right = k

    while left < right:
        mid = left + (right - left) // 2
        if condition(mid, k):
            right = mid
        else:
            left = mid + 1

    return left - 1


if __name__ == '__main__':
    print(sqrt(9))
    print(sqrt(10))
    print(sqrt(63))
    print(sqrt(67))

