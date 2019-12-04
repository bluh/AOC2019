fd = open("data/data1.txt", 'r')
total = 0
while True:
    line = fd.readline()
    if line == '':
        break
    else:
        num = int(line)
        result = num // 3 - 2
        total += result

print("Final result: %(val)s" % {'val': total})