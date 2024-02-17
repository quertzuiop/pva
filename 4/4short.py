import os

for f in [f for f in os.listdir("uloha4\ENG")if"_i"in f]:
    i=open("uloha4/ENG/"+f,"r").read().replace("\n"," ").split(" ")[:-1]
    try:i=[int(i)for i in i]
    except:
        print("Invalid input")
        continue
    s=[sum(i[j:k])for j in range(len(i))for k in range(j+2,len(i)+1)]
    m=[[n]*s.count(n)for n in tuple(set(s))if s.count(n)>1]
    r=0
    for i in m:r+=len(i)*(len(i)-1)/2
    print(r)