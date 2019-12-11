class Orbit:
    def __init__(self, name, orbiting):
        self.name = name
        self.orbiting = orbiting
        self.distance = -1

    def __str__(self):
        if self.orbiting is None:
            return "Object " + self.name + " (0)"
        else:
            return "Object " + self.name + " (" + str(self.distance) + ")" 

orbits = {}

fd = open("data/data6.txt")

total = 0

while True:
    line = fd.readline()
    if line == "":
        break
    vals = line.split(")")
    orbit1 = vals[0]
    orbit2 = vals[1].strip()
    if orbit1 not in orbits:
        orbits[orbit1] = Orbit(orbit1, None)
    if orbit2 not in orbits:
        orbits[orbit2] = Orbit(orbit2, orbits[orbit1])
    else:
        orbits[orbit2].orbiting = orbits[orbit1]

def recurse(item, mode):
    if mode == "SAN":
        #print("Checking", item.name)
        if item.orbiting is not None:
            item.orbiting.distance = item.distance + 1
            recurse(item.orbiting, mode)
        #print(item.name,"has distance", item.distance)
    if mode == "YOU":
        #print("Checking", item.name)
        if item.orbiting is not None:
            if item.orbiting.distance > 0:
                print("Found a connection at ",item.orbiting,item.orbiting.distance)
                print(item.distance + item.orbiting.distance + 1)
                return
            else:
                item.orbiting.distance = item.distance + 1
                recurse(item.orbiting, mode)
        #print(item.name,"has distance", item.distance)

recurse(orbits["SAN"],"SAN")

recurse(orbits["YOU"],"YOU")