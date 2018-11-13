x = 123456789
numchar = ['0','1','2','3','4','5','6','7','8','9']
stat = '0'
count = 1

for i in range(1000000000):
    x += 1
    curchar = str(x)
    if len(curchar)<10:
        curchar = '0'+curchar

    if numchar == sorted(list(curchar)):
        count += 1

    
        
        
