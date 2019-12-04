fd = open("data/data2.txt", 'r')
lines = ""
while True:
    line = fd.readline()
    lines = lines + line
    if line == '':
        break

codes = lines.split(",")

codes[1] = 12
codes[2] = 2

index = 0
operating = True
while operating:
    code = codes[index]
    if code == "1":
        dataA = int(codes[int(codes[index + 1])])
        dataB = int(codes[int(codes[index + 2])])
        codes[int(codes[index + 3])] = dataA + dataB
    elif code == "2":
        dataA = int(codes[int(codes[index + 1])])
        dataB = int(codes[int(codes[index + 2])])
        codes[int(codes[index + 3])] = dataA * dataB
    elif code == "99":
        operating = False
    else:
        raise "ERROR ON OPCODE " + code
    index += 4

print(codes)
