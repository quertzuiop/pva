import os, re
for f in[f for f in os.listdir("uloha5\ENG")if"_i"in f]:
    file = open("uloha5/ENG/" + f, "r").read()
    try:
        inp = re.findall(r"(-?[0-9.]+),(-?[0-9.]+): (\w+)", file)
        inp = [[float(i[0]), float(i[1]), i[2]] for i in inp]
    except:
        print("Invalid input")
        continue
    if len(inp) != file.count("\n"):
        print("Invalid input")
        continue
    distances=[]
    planes = []
    for i in range(len(inp)):
        for j in range(i+1, len(inp)):
            planes.append([inp[i][2], inp[j][2]])
            distances += (abs(inp[i][0] - inp[j][0])**2 + abs(inp[i][1] - inp[j][1])**2)**0.5,
    indices = [i for i, dist in enumerate(distances) if dist == min(distances)]
    print(distances.count(min(distances)))
    for i in indices: print(planes[i])