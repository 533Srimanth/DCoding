def condition(mid, arr, m):
    curr = 0
    index = 0
    parts = 0
    while index < len(arr):
        if arr[index] > mid:
            return False
        if curr + arr[index] > mid:
            parts += 1
            curr = 0
        else:
            curr += arr[index]
            index += 1

    if curr > 0:
        parts += 1

    return parts <= m


def split_array_largest_sum(arr, m):
    left = sum(arr) // m
    right = sum(arr)

    while left < right:
        mid = left + (right - left) // 2

        if condition(mid, arr, m):
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == '__main__':
    print(split_array_largest_sum([7,2,5,10,8], 2))
    print(split_array_largest_sum([1,2,3,4,5], 2))
