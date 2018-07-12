# Method 1
def almostIncreasingSequence_1(sequence):
    deleted = False
    last = prev = min(sequence) - 1
    for elm in sequence:
        if elm <= last:
            if deleted:
                return False
            else:
                deleted = True
            if elm > prev:
                last = elm
        else:
            prev, last = last, elm
    return True


# method 2
def almostIncreasingSequence_2(sequence):
    count = 0
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]: count += 1
        if len(sequence) > i + 2 and sequence[i] >= sequence[i + 2]: count += 1
    return count < 3


# method 3
def almostIncreasingSequence(s):
    return 3 > sum((i >= j) + (i >= k) for i, j, k in zip(s, s[1:], s[2:] + [9999999]))
