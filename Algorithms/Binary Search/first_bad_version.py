
def is_bad_version(n):
    return n >= 534


def condition(k):
    return is_bad_version(k)


def first_bad_version():
    left = 1
    right = 2**32 - 1

    while left < right:
        mid = left + (right - left)//2
        if condition(mid):
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == '__main__':
    print(first_bad_version())


