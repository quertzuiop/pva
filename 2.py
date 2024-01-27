import os, math, time
for filename in os.listdir("uloha2\ENG"):
    if "_in" in filename:
        inp = open("uloha2/ENG/"+filename, "r").read().split("\n")[:-1]
        try: points = [tuple([float(c) for c in p.split(" ")]) for p in inp]
        except: 
            print("Invalid input")
            continue
        d1 = math.sqrt((points[0][0]-points[1][0])**2 + (points[0][1]-points[1][1])**2)
        d2 = math.sqrt((points[1][0]-points[2][0])**2 + (points[1][1]-points[2][1])**2)
        d3 = math.sqrt((points[2][0]-points[0][0])**2 + (points[2][1]-points[0][1])**2)
        sort = sorted([d1, d2, d3])
        if sort[0] + sort[1] == sort[2]:
            print("There exists a line connecting all three points.")
            if len(set(points)) == 3: 
                print(f"Point {'ABC'[points.index((sorted(list(zip(*points))[0])[1], sorted(list(zip(*points))[1])[1]))]} is in the middle.")
            else:
                print("Some points are identical.")
        else: 
            print("No line connects all points.")