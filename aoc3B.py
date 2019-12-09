class Point:
    def __init__(self, x, y, dist1, dist2):
        self.x = x
        self.y = y
        self.dist1 = dist1
        self.dist2 = dist2

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def dist(self):
        return self.dist1 + self.dist2

class Line:
    def __init__(self, line, x, y, dist, dir, length):
        self.line = line
        self.length = length
        self.dist = dist
        self.dir = dir
        self.og_x = x
        self.og_y = y
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
                return Point(self.x, other.y, self.dist + abs(self.og_y - other.y), other.dist + abs(other.og_x - self.x))
        elif (self.dir == 'L' or self.dir == 'R') and (other.dir == 'U' or other.dir == 'D'):
            if other.x >= self.x and other.x <= self.end_x and self.y >= other.y and self.y <= other.end_y:
                return Point(other.x, self.y, self.dist + abs(self.og_x - other.x), other.dist + abs(other.og_y - self.y))
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
    length = 0
    x,y = 0,0
    for v in vals:
        dir = v[0]
        len = int(v[1:])
        newLine = Line(inputLine, x, y, length, dir, len)
        length += len
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