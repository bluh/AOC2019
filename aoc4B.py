#start = 128888 #128392
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
            while d <= 9:
                e = d
                while e <= 9:
                    f = e
                    while f <= 9:

                        if firstRun:
                            a = 1
                            b = 2
                            c = 8
                            d = 8
                            e = 8
                            f = 8
                            firstRun = False
                        
                        test = [a,b,c,d,e,f]

                        hasDouble = False

                        runChar = a
                        runLength = 1

                        for i in range(1, 6):
                            if test[i] == runChar:
                                runLength += 1
                                hasDouble = runLength == 2
                            else:
                                if runLength == 2:
                                    break
                                runChar = test[i]
                                runLength = 1

                        if hasDouble:
                            total += 1

                        f += 1
                    e += 1
                d += 1
            c += 1
        b += 1
    a += 1

print(total)