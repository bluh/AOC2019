fd = open("data/data2.txt", 'r')
lines = ""
while True:
    line = fd.readline()
    lines = lines + line
    if line == '':
        break

input = 0
output = 0

while output != 19690720:
    input += 1
    inA = input % 100
    inB = input // 100
    codes = lines.split(",")
    print("trying ", inA, inB)
    codes[1] = inA
    codes[2] = inB
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
    output = codes[0]

print(codes)
