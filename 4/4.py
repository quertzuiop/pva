import os

for filename in [file for file in os.listdir("uloha4\ENG") if "_i" in file]:
    inp = open("uloha4/ENG/" + filename, "r").read().replace("\n", " ").split(" ")[:-1]
    try: inp = [int(i) for i in inp]
    except:
        print("Invalid input")
        continue
    sums = []
    for i in range(len(inp)):
        for j in range(i + 2, len(inp) + 1):
            sums.append(sum(inp[i:j]))
    sumset = tuple(set(sums))
    multiples = [[num]*sums.count(num) for num in sumset if sums.count(num) > 1]
    res = 0
    for i in multiples:
        res += len(i)* (len(i) - 1) // 2
    print(res)
    