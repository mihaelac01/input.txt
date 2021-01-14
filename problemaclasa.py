with open("input.txt","r") as f:
    n=f.readline()
a=0
b=0
c=0
d=0
for i in n:
    if ord(i) in range(65,91):
        a+=1
with open("litereA.txt","w") as f:
    f.write(str(a))
for i in n:
    if ord(i) in range(97,123):
        b+=1
with open("litereB.txt","w") as f:
    f.write(str(b))
for i in n:
    if ord(i) in range(49,58):
        c+=1
with open("cifre.txt","w") as f:
    f.write(str(c))
for i in n:
    if ord(i) in range(33,42):
        d+=1
with open("caractere.txt","w") as f:
    f.write(str(d))