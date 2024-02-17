import test, os , math
def get_face_indices(side_len, startp, endp):
    if side_len in startp: start_face = startp.index(side_len)*2 + 1
    else: start_face = startp.index(0)*2
    if side_len in endp: end_face = endp.index(side_len)*2 + 1
    else: end_face = endp.index(0)*2
    return start_face, end_face
for filename in os.listdir("uloha1\ENG"):
    if "_in" in filename:
        inp = open("uloha1/ENG/"+filename, "r").read().split("\n")[:-1]
        if len(inp) != 3: 
            print("Invalid Input")
            continue
        side_len, startp, endp = inp
        side_len = int(side_len)
        try:
            startp = [int(x) for x in startp.split(" ")]
            endp = [int(x) for x in endp.split(" ")]
        except: 
            print("Invalid Input")
            continue
        close_points = 0
        if sum((0<i<20 or side_len-20<i<side_len) for i in startp + endp)>1:
            print("Invalid input")
            continue
        if side_len in startp: face1 = startp.index(side_len)*2 + 1
        else: face1 = startp.index(0)*2
        if side_len in endp: face2 = endp.index(side_len)*2 + 1
        else: face2 = endp.index(0)*2
        if not (face1 != face2 and face1//2 == face2//2):
            pipedist=sum([abs(startp[i]-endp[i]) for i in range(3)])
            axes = sorted([face1 // 2, face2 //2])
            paxis = axes[0]*2-axes[1] #✨✨✨
            hosedist = math.sqrt((abs(startp[axes[0]] - endp[axes[0]]) + abs(startp[axes[1]] - endp[axes[1]]))**2 + abs(startp[paxis] - endp[paxis])**2)
        else:
            axis = face1 // 2
            mindist = side_len
            minhosedist = 2 * side_len
            startp_face_coords = startp[0:axis] + startp[axis+1:]
            endp_face_coords = endp[0:axis] + endp[axis+1:]
            for relaxis in 0, 1:
                for direction in 0, 1:
                    d1 = abs(side_len * direction - startp_face_coords[relaxis])
                    d2 = abs(side_len * direction - endp_face_coords[relaxis])
                    if d1 + d2 + abs(startp_face_coords[relaxis - 1] - endp_face_coords[relaxis - 1]) < mindist:
                        mindist = d1 + d2 + abs(startp_face_coords[relaxis - 1] - endp_face_coords[relaxis - 1])
                    hosedist = math.sqrt((d1 + d2 + side_len)**2 + abs(startp_face_coords[relaxis - 1] - endp_face_coords[relaxis - 1]) **2)
                    minhosedist = min(hosedist, minhosedist)
            pipedist = mindist + side_len
            hosedist = minhosedist
        print(pipedist, hosedist)