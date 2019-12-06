import numpy as np

def load_input():
    with open('input.txt', 'r') as fl:
        lines = fl.readlines()
    return lines

def process_lines(lines):
    return [ln.split(',') for ln in lines]

path_dict = {'R': np.array([1, 0]),
             'L': np.array([-1, 0]),
             'U': np.array([0, 1]),
             'D': np.array([0, -1])}

def input_line_to_coords(input_line, start=None):
    '''Transforms list of strings describing path to coordinate system'''
    if start is None:
        start = np.array([0,0])
    coord_list = [start.copy()]
    for inp in input_line:
        start += path_dict[inp[0]] * int(inp[1:])
        coord_list.append(start.copy())
    return np.array(coord_list)

#wann intersected etwas nicht?
#wenn start und end > start und end oder < start und end

#intersected wenn
#x1_1 - x2_1 < 0
#x1_2 - x2_1 > 0
#&&
#y1_1 - y2_1 > 0
#y1_1 - y2_2 < 0

test_cases = [[
'R8,U5,L5,D3',
'U7,R6,D4,L4', 6, 30],
        ['R75,D30,R83,U83,L12,D49,R71,U7,L72',
'U62,R66,U55,R34,D71,R55,D58,R83',159, 610],
['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7', 135, 410]]

def contains(line, many_lines):
    return np.sign(line[None] - many_lines).sum(axis=-1)==0

def identify_intersections(coords1, coords2):
    '''Returns intersection points'''
    from skimage.util import view_as_windows
    return [np.logical_and(
        contains(x_line, view_as_windows(coords2[:, 0], 2)),
        contains(y_line, view_as_windows(coords2[:, 1], 2)))
    for x_line, y_line in zip(view_as_windows(coords1[:, 0], 2),
                              view_as_windows(coords1[:, 1], 2))]

def simple_approx(lines):
    path_dicts = [dict(), dict()]
    counter_dicts = [dict(), dict()]
    for line_i, line in enumerate(lines):
        start = np.array([0,0])
        counter = 0
        for  inp in line:
            for i in range(1, int(inp[1:])+1):
                tmp = start + path_dict[inp[0]] * i
                path_dicts[line_i][tuple(tmp)] = 1
                counter_dicts[line_i][tuple(tmp)] = i + counter
            start += path_dict[inp[0]] * int(inp[1:])
            counter += int(inp[1:])
    intersections = list(set(path_dicts[0].keys()) & set(path_dicts[1].keys()))
    steps = [counter_dicts[0][inters] + counter_dicts[1][inters]
            for inters in intersections]
    return np.array([list(tup) for tup in intersections]), steps

def shortest_intersection(intersections):
    return np.min(np.abs(intersections).sum(axis=-1))

if __name__=='__main__':
    for case in test_cases:
        intersections, steps = simple_approx(process_lines(case[:2]))
        assert case[-2] == shortest_intersection(intersections)
        assert case[-1] == min(steps)
    lines = load_input()
    intersections, steps = simple_approx(process_lines(lines))
    print(shortest_intersection(intersections))
    print(min(steps))
