import test, os 
import math

def get_face_indices(side_len, startp, endp):
    if side_len in startp:
        start_face = startp.index(side_len)*2 + 1
    else:
        start_face = startp.index(0)*2

    if side_len in endp:
        end_face = endp.index(side_len)*2 + 1
    else:
        end_face = endp.index(0)*2
    
    return start_face, end_face

def is_opposite(f1, f2):
    if abs(f1-f2) == 1 and min(f1, f2) % 2 == 0:
        return True
    return False

for filename in os.scandir("uloha1\ENG"):
    if filename.is_file() and "_in" in filename.name:
        inp = open(filename, "r").read().split("\n")[:-1]
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
        is_too_close = False
        for i in startp + endp:
            if i in range(1, 20) or i in range(side_len - 19, side_len):
                is_too_close = True
                break
        if is_too_close:
            print("Invalid input")
            continue
        face1, face2 = get_face_indices(side_len, startp, endp)
        if not is_opposite(face1, face2):
            pipedist = abs(startp[0] - endp[0]) + abs(startp[1] - endp[1] ) + abs(startp[2] - endp[2])
            axes = [face1 // 2, face2 //2]
            paxis = [axis for axis in (0, 1, 2) if axis not in axes][0]
            hosedist = math.sqrt((abs(startp[axes[0]] - endp[axes[0]]) + abs(startp[axes[1]] - endp[axes[1]]))**2 + abs(startp[paxis] - endp[paxis])**2)
        else:
            axis = face1 // 2
            mindist = side_len #cant be larger than side len
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
