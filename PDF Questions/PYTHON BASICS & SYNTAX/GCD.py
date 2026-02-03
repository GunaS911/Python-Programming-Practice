n=int(input("Enter the first number:"))
ni=int(input("Enter the second number:"))
ln=[]
lni=[]
hcf=0
for i in range(1,n+1):
    if n%i==0:
        ln.append(i)
for i in range(1,ni+1):
    if ni%i==0:
        lni.append(i)
for i in range(0,len(ln)):
    for j in range(0,len(lni)):
        if ln[i] == lni[j]:
            hcf = lni[j]
print("The hcf is",hcf)
