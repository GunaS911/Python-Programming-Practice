n = int(input("Enter n in nCr: "))
r = int(input("Enter r in nCr: "))
d = n-r
fn=1
fr=1
fd=1
while n>0:
    fn=fn*n
    n-=1
while r>0:
    fr=fr*r
    r-=1
while d>0:
    fd=fd*d
    d-=1
print("nCr: ",(fn/(fd*fr)))
