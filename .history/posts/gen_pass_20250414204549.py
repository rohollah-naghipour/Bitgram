import random
import string

def Generate_Password(num):
    password = ''
    r = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,
          a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,
          0,1,2,3,4,5,6,7,8,9,'!','@','$','%','^','&','*','(',')',
           '=','+','{','}','[',']','|','/',':',';','<','>','?','/']
    for n in range(num):
        x = random.randint(0, 94)
        password += string.printable[x]
    return password


print(Generate_Password(10))

d = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,
          a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,
          0,1,2,3,4,5,6,7,8,9,'!','@','$','%','^','&','*','(',')',
           '=','+','{','}','[',']','|','/',':',';','<','>','?','/']
print(d)