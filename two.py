a = int(input('enter the number of rows: '))
b = int(input('enter the number of columns: '))
for i in range(0,a):
        if i%2 == 0:
                for j in range(0,b):
                        if j%2 == 0:
                                print('1',end='')
                        else:
                                print('0',end='')
                     
        else:
                for j in range(0,b):
                        if j%2 == 0:
                                print('0',end='')
                        else:
                                print('1',end='')
        print()
