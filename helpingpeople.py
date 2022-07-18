n = input()
b=int(n[0])+int(n[1])
c=int(n[3])+int(n[4])
d=int(n[4])+int(n[5])
f=int(n[7])+int(n[8])
X=n[2]
if(X=="A" or X=="E" or X=="I" or X=="O" or X=="U" or X=="Y"):
    print("invalid")
elif(b%2!=0 or c%2!=0 or d%2!=0 or f%2!=0 ):
    print("invalid")
else:
    print("valid")