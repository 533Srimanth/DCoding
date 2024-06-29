def condition(mid, arr, k):
    return arr[mid] >= k


def insert_search_position(arr, k):
    n = len(arr)

    if arr[0] > k:
        return 0
    if arr[-1] < k:
        return n - 1

    left = 0
    right = n - 1

    while left < right:
        mid = left + (right - left) // 2
        if condition(mid, arr, k):
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == '__main__':
    print(insert_search_position([1,3,5,6], 5))
    print(insert_search_position([1,3,5,6], 2))
    print(insert_search_position([1,3,5,6], 0))
    print(insert_search_position([1,3,5,6], 8))

