a=0
b=[]
n=input('give the total fibb no req ')
def fibb(n):
    if int(n)==0 or int(n)==1:
        return n
    else :
        return fibb(int(n)-1)+fibb(int(n)-2)
        

    
print (fibb(n))
