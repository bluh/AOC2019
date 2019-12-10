fd = open("data/data5.txt", 'r')
lines = ""
while True:
    line = fd.readline()
    lines = lines + line
    if line == '':
        break

codes = lines.split(",")


def read(index, mode):
    if mode == '1':
        return codes[int(index)]
    elif mode == '0':
        return codes[int(codes[index])]

def write(index, data):
    codes[int(codes[index])] = data


index = 0
operating = True
while operating:
    code = codes[index].rjust(5,'0')
    op = code[-2:]
    parm1 = code[-3:-2]
    parm2 = code[-4:-3]
    parm3 = code[-5:-4]

    if op == "01":
        dataA = int(read(index + 1, parm1))
        dataB = int(read(index + 2, parm2))
        write(index + 3, str(dataA + dataB))
        index += 4
    elif op == "02":
        dataA = int(read(index + 1, parm1))
        dataB = int(read(index + 2, parm2))
        write(index + 3, str(dataA * dataB))
        index += 4
    elif op == "03":
        print("Input:")
        write(index + 1, input())
        index += 2
    elif op == "04":
        print(read(index + 1, parm1))
        index += 2
    elif op == "05":
        if read(index + 1, parm1) != "0":
            index = int(read(index + 2, parm2))
        else:
            index += 3
    elif op == "06":
        if read(index + 1, parm1) == "0":
            index = int(read(index + 2, parm2))
        else:
            index += 3
    elif op == "07":
        dataA = int(read(index + 1, parm1))
        dataB = int(read(index + 2, parm2))
        if dataA < dataB:
            write(index + 3, "1")
        else:
            write(index + 3, "0")
        index += 4
    elif op == "08":
        dataA = int(read(index + 1, parm1))
        dataB = int(read(index + 2, parm2))
        if dataA == dataB:
            write(index + 3, "1")
        else:
            write(index + 3, "0")
        index += 4
    elif op == "99":
        operating = False
    else:
        raise "ERROR ON OPCODE " + code
