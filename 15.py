import time
r=5
y=2
g=5
while True:
    for i in range(r,0,-1):
        print('Red..Remaining time {} seconds'.format(i))
        time.sleep(1)
    for k in range(y,0,-1):
        print('Yellow..Remaining time {} seconds'.format(k))
        time.sleep(1)
    for l in range(g,0,-1):
        print('Green..Remaining time {} seconds'.format(l))
        time.sleep(1)
