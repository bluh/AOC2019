fd = open("data/data1.txt", 'r')
total = 0
while True:
    line = fd.readline()
    if line == '':
        break
    else:
        num = int(line)
        result = num
        numTotal = 0
        while result > 0:
            result = result // 3 - 2
            numTotal += max(result, 0)
        total += numTotal

print("Final result: %(val)s" % {'val': total})