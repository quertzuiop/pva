import os
for f in[f for f in os.listdir("uloha4\ENG")if"_i"in f]:
    try:i=[int(i)for i in open("uloha4/ENG/"+f,"r").read().replace("\n"," ").split(" ")[:-1]]
    except:print("Invalid input");continue
    l=len
    s=[sum(i[j:k])for j in range(l(i))for k in range(j+2,l(i)+1)]
    print(sum([l(i)*(l(i)-1)/2for i in[[n]*s.count(n)for n in set(s)]]))