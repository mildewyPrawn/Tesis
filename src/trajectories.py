import Point as pt

filename = "../examples/trajectories.tes"

p1 = pt.Point(6,1, 1, -5) # Is on the line
p2 = pt.Point(7,1, 1, -5) # Is not on the line

print(p1.validate())
print(p2.validate())

pts = []
with open(filename) as file:
    for line in file:
        p = line.rstrip().split()
        if len(p) == 4:
            pts.append(pt.Point(float(p[0]), float(p[1]), float(p[2]), float(p[3])))

print(pts)

for p in pts:
    if not p.validate():
        print("the point {} does not lie on the trajectory".format(p))

for p in pts:
    print('The point before the update: {}'.format(p))
    for i in range(0,3):
        p.update()
        print('The point after the update: {}'.format(p))
    print()
