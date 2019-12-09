class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def dist(self):
        return abs(self.x) + abs(self.y)

class Line:
    def __init__(self, line, x, y, dir, length):
        self.line = line
        self.length = length
        self.dir = dir
        if dir == 'U':
            self.x = x
            self.end_x = x
            self.y = y
            self.end_y = self.y + length
        elif dir == 'D':
            self.x = x
            self.end_x = x
            self.y = y - length
            self.end_y = y
        elif dir == 'R':
            self.x = x
            self.end_x = x + length
            self.y = y
            self.end_y = y
        elif dir == 'L':
            self.x = x - length
            self.end_x = x
            self.y = y
            self.end_y = y

    def intersects(self, other):
        if self.line == other.line:
            return None
        if (self.dir == 'U' or self.dir == 'D') and (other.dir == 'R' or other.dir == 'L'):
            if other.y >= self.y and other.y <= self.end_y and self.x >= other.x and self.x <= other.end_x:
                return Point(self.x, other.y)
        elif (self.dir == 'L' or self.dir == 'R') and (other.dir == 'U' or other.dir == 'D'):
            if other.x >= self.x and other.x <= self.end_x and self.y >= other.y and self.y <= other.end_y:
                return Point(other.x, self.y)
        return None

fd = open("data/data3.txt", 'r')
inputLine = 0

shortestLen = -1

lines = []
intersections = []

while True:
    line = fd.readline()
    if line == "":
        break
    inputLine += 1
    vals = line.split(",")
    x,y = 0,0
    for v in vals:
        dir = v[0]
        len = int(v[1:])
        #print("new line at ",x,y," going ",dir," w len ", len)
        newLine = Line(inputLine, x, y, dir, len)
        if dir == 'U':
            y += len
        elif dir == 'D':
            y -= len
        elif dir == 'R':
            x += len
        elif dir == 'L':
            x -= len
        for l in lines:
            inter = l.intersects(newLine)
            if(inter != None and (inter.dist() < shortestLen or shortestLen == -1) and not (inter.x == x and inter.y == 0)):
                shortestPoint = inter
                shortestLen = inter.dist()
        lines.append(newLine)


print(shortestPoint)
print(shortestLen)