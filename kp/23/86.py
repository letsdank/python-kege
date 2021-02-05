#   Copyright 2021 LetsDank (see LICENSE in root folder)

def F(start, end):
    if end < start:
        return 0
    if end == start:
        return 1
    k = F(start, end - 1)
    if end % 2 == 0:
        k += F(start, end // 2)
    if end % 3 == 0:
        k += F(start, end // 3)
    return k
print(F(2, 12) * F(12, 28))
