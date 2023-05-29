e=0
i=0
for i in range(6):
    for j in range(6):
        x = j * 1000 - 3600
        y = i * 800 - 2900
        x=abs(x)
        e+=x
        y=abs(y)
        i+=y
print(e)
print(i)