i = 1
ans=0
while True:
    temp = ((-1)**(i+1))/(2*i-1)
    ans+=temp
    if(i%100 == 1):
        print("%d\t\t\t%.4f" %(i, 4*ans))
    i = i+1
    if(round(i, 3)==3.141 or i>1000):
        break
    
