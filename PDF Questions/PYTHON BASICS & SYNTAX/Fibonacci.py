f=0
fi=1
fn=1
n = int(input("Enter number of terms: "))
for i in range(0,n):
    fi=f
    f=fn
    fn=fi+f
    print(f)
