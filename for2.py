print ('Hi')
username=input('What is your name?')
print('hello',username)
print('This is you!')
print('@')
x=3
y=3
for counter in range(0,100):
    for counter in range(0,5):
        print('')
    for counter in range(0,y-1):
        for counter in range(0,5):
            print('# ', end='')
        print('')
    for counter in range(0,x-1):
        print('# ', end='')
    print('@ ', end='')
    for counter in range(0,5-x):
        print('# ', end='')
    print('')
    for counter in range(0,5-y):
        for counter in range(0,5):
            print('# ', end='')
        print('')
    where=input('Go where(w/a/s/d)?')
    if where=='w':
        y=y-1
    if where=='a':
        x=x-1
    if where=='s':
        y=y+1
    if where=='d':
        x=x+1
    if x<=0:
        print('Where are you going?')
        x=1
    if x>5:
        print('Where are you going?')
        x=5
    if y<=0:
        print('Where are you going?')
        y=1
    if y>5:
        print('Where are you going?')
        y=5
