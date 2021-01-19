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
print(F(2, 13) * F(13, 44) - F(2, 13) * F(13, 29) * F(29, 44))