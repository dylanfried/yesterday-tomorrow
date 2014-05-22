def shift(l, n):
    return l[n:] + l[:n]

def get_intervals(sequence):
    to_return = []
    for i in range(len(sequence)-1):
        to_return.append(sequence[i+1]-sequence[i])
    return to_return
