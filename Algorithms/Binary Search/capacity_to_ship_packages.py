def condition(mid, weights, d):
    index = 0
    curr_weight = 0
    days = 0
    while index < len(weights):
        if curr_weight + weights[index] > mid:
            days += 1
            curr_weight = 0
        else:
            curr_weight += weights[index]
            index += 1

    if curr_weight > 0:
        days += 1

    return days <= d


def capacity(weights, d):
    left = weights[-1]
    right = sum(weights)

    while left < right:
        mid = left + (right - left) // 2

        if condition(mid, weights, d):
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == '__main__':
    print(capacity([1,2,3,4,5,6,7,8,9,10], 5))
    print(capacity([1,2,3,4,5,6,7,8,9,10], 1))
    print(capacity([1,2,3,4,5,6,7,8,9,10], 15))

