from math import factorial
from typing import List


def getRow(rowIndex: int) -> List[int]:
    line = [1]

    for k in range(rowIndex):
        line.append(int(line[k] * (rowIndex - k) / (k + 1)))
    return line
