class Orbit:
    def __init__(self, name, orbiting):
        self.name = name
        self.orbiting = orbiting
        self.orbits = -1

    def __str__(self):
        if self.orbiting is None:
            return "Object " + self.name + " (0)"
        else:
            return "Object " + self.name + " (" + str(self.orbits) + ")" 

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

def recurse(item):
    if item.orbits > -1:
        return item.orbits
    else:
        if item.orbiting is None:
            item.orbits = 0
        elif item.orbiting.orbits > -1:
            item.orbits = item.orbiting.orbits + 1
        else:
            item.orbits = recurse(item.orbiting) + 1
        return item.orbits

for k,v in orbits.items():
    if v.orbits == -1:
        v.orbits = recurse(v)
    total += v.orbits
    print("value", k, "has", v.orbits, "orbits and is around",v.orbiting)

print(total)