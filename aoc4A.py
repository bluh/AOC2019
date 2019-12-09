start = 128888 #128392
end = 599999 #643281

firstRun = True
total = 0

a = 1

initialVals = [1, 2, 8, 8, 8, 8]

def recurse(vals, index, runChar, runLength, hasDouble):
    if index > 6:
        return
    
    #expand
    vals[index] += 1

    if vals[index] > 9:
        return
    
    if vals[index] == runChar:
        runLength += 1
        if runLength == 
        hasDouble = hasDouble or runLength == 2

    for v in range(index, 6):
        vals[v] = vals[index]
    recurse(vals, index + 1, runChar, runLength, hasDouble)



recurse(initialVals, 0, 0, 0, False)

while a <= 5:
    b = a
    runLength = 0
    runChar = 0
    hasDouble = False
    while b <= 9:
        c = b
        if b == runChar:
            runLength += 1
        while c <= 9:
            d = c
            isDouble = b == c and c != a
            while d <= 9:
                e = d
                isDoubleC = isDoubleB or c == d
                while e <= 9:
                    f = e
                    isDoubleD = isDoubleC or d == e
                    while f <= 9:
                        isDoubleE = isDoubleD or e == f

                        if firstRun:
                            a = 1
                            b = 2
                            c = 8
                            d = 8
                            e = 8
                            f = 8
                            firstRun = False
                            isDoubleE = True
                        
                        if isDoubleE:
                            total += 1
                        f += 1
                    e += 1
                d += 1
            c += 1
        b += 1
    a += 1

print(total)