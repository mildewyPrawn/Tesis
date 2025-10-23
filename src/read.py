import Point as pt

filename = '../examples/new_example.tes'

all_lines = []
max_moves = 0

with open(filename) as file:
    for line in file:
        s = line.strip().split(',')
        max_moves = len(s) if len(s) > max_moves else max_moves
        point_line = []
        for si in s:            
            si = si.strip().split(' ')
            point_line.append(si)
        all_lines.append(point_line)

all_moves = []
for lines in all_lines:
    missing = max_moves - len(lines)
    points = []
    last = lines[-1]
    if missing != 0:
        lines.extend([last] * missing)
    all_moves.append(lines)

print('->>>>>>>>>>>')
print(all_moves)

for moves in all_moves:
    p = pt.Point(moves[0][0], moves[0][1], moves)
    print(p)
    for i in range(0, max_moves+ 4):
        p.update()
        print('After {}-update: {}'.format(i, p))



