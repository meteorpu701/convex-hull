def orientation(a,b,c):
    val = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2
        
def jarvis(Pli):
    index = 0
    result = []
    for i in range(len(Pli)):
        if Pli[i][0]< Pli[index][0]:
            index = i
    current = index
    while(True):
        result.append(Pli[current])
        endpoint = (index + 1) % len(Pli)
        for j in range(len(Pli)):
            if (endpoint == current) or orientation(Pli[current], Pli[j], Pli[endpoint]) == 2:
                endpoint = j
        current = endpoint
        if current == index:
            break
    return result

points = [(-7,8), (-4,6), (2,6), (6,4), (8,6), (7,-2), (4,-6), (8,-7),(0,0), (3,- 2),(6,-10),(0,6),(-9,-5),(-8,-2),(-8,0),(-10,3),(-2,2),(-10,4)]
print(jarvis(points))
