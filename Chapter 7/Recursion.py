#factorial

def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
j=fact(4)
print("the factoraial is "+str(j))