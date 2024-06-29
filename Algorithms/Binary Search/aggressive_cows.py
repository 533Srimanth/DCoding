def condition(mid, positions, num_cows, left_limit, right_limit):
    return positions[mid] - positions[left_limit] >= aggressive_cows(positions, num_cows - 1, mid, right_limit)


def aggressive_cows(positions, num_cows, left_limit, right_limit):
    if num_cows == 2:
        return positions[right_limit] - positions[left_limit]
    if num_cows > right_limit - left_limit + 1:
        return 0

    left = left_limit + 1
    right = right_limit

    while left < right:
        mid = left + (right - left) // 2
        if condition(mid, positions, num_cows, left_limit, right_limit):
            right = mid
        else:
            left = mid + 1

    return max(positions[left - 1] - positions[left_limit], aggressive_cows(positions, num_cows - 1, left, right_limit))


if __name__ == '__main__':
    print(aggressive_cows([1,2,4,8,9], 3, 0, 4))
    print(aggressive_cows([6,7,9,11,13,15], 4, 0, 5))



