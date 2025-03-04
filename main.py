tab = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def binarne(x, y):
    l = 0
    p = len(x) - 1
    while l <= p:  # Use <= instead of != to keep checking until the subarray is exhausted
        sr = (p + l) // 2
        if x[sr] == y:
            print(f'{y} in array is at index {sr}')
            return
        elif x[sr] > y:
            p = sr - 1
        else:
            l = sr + 1
    print(f'{y} not found in array')

binarne(tab, 9)
