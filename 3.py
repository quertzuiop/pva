def c(n,b):return[n]if n<b else c(n//b,b)+[n%b]
def s(n,b):
    while c(n,b)!=c(n,b)[::-1]:n+=1
    return n if n<2**64 and 1<b<37 else 0 
for a in open("3.txt","r").read().split("\n"):
    i,o=a.split(":")
    n,b=map(int,i.split())
    print("👌"if str(s(n+1,b))==o else"❌")