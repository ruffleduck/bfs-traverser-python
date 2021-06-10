start = 1
finish = 6

connections = {
    1: [2, 3],
    2: [6, 7],
    3: [4, 5],
    4: [],
    5: [],
    6: [],
    7: []
}

nodeData = [[False, None] for _ in range(len(connections))]
nodeData[start - 1][1] = 0

nodeIdxs = [start - 1]
while nodeIdxs != []:
    nodeIdx = nodeIdxs.pop(0)
    
    if nodeData[nodeIdx][0]:
        continue
    
    nodeData[nodeIdx][0] = True
    for i in connections[nodeIdx + 1]:
        current_dist = nodeData[i - 1][1]
        new_dist = nodeData[nodeIdx][1] + 1
        if current_dist == None or new_dist < current_dist:
            nodeData[i - 1][1] = new_dist
        nodeIdxs.append(i - 1)

if not nodeData[finish - 1][0]:
    print('node unreachable')
else:
    print('distance', nodeData[finish - 1][1])
