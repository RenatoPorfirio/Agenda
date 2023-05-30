def hoare(list, i, j):
    if i >= j:
        return
    p = hoare_sort(list, i, j)
    hoare(list, i, p)
    hoare(list, p+1, j)

def hoare_sort(list, i, j):
    p, x, y = list[i], i-1, j+1
    while True:
        x += 1
        while list[x] < p:
            x += 1
        y -= 1
        while list[y] > p:
            y -= 1
        if x >= y: 
            return y
        list[x], list[y] = list[y], list[x]

