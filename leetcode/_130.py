from typing import List


def plusOne(digits: List[int]) -> List[int]:
    digits[len(digits) - 1] += 1
    curr = len(digits) - 1

    while digits[curr] == 10:
        digits[curr] = 0

        if curr == 0:
            digits.insert(0, 1)
            break
        curr -= 1

        digits[curr] += 1

    return digits


print(plusOne([1, 9, 9]))
