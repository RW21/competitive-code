from pprint import pprint
from typing import List


def generate(numRows: int) -> List[List[int]]:
    if numRows == 0:
        return []

    triangle = [[1]]

    for i in range(numRows):
        if i != 0:
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(triangle[i - 1][j] + triangle[i - 1][j - 1])
            triangle.append(row)
    return triangle

print(generate(50))