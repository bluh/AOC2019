start = 128888 #128392
end = 599999 #643281

firstRun = True
total = 0

a = 1

while a <= 5:
    b = a
    while b <= 9:
        c = b
        while c <= 9:
            d = c
            isDoubleB = b == c and c != a
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