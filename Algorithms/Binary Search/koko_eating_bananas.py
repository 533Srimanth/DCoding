import math


def condition(mid, piles, H):
    hours = 0
    for pile in piles:
        hours += math.ceil(pile / mid)

    return hours <= H


def koko_eating_bananas(piles, H):
    left = 1
    right = max(piles)

    while left < right:
        mid = left + (right - left) // 2
        if condition(mid, piles, H):
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == '__main__':
    print(koko_eating_bananas([3,6,7,11], 8))
    print(koko_eating_bananas([30,11,23,4,20], 5))
    print(koko_eating_bananas([30,11,23,4,20], 6))

