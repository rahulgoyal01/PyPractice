x,y,z,n = [int(input()) for i in range(4)]

list = [[a,b,c]
        for a in range(x+1)
        for b in range(y+1)
        for c in range(z+1)
        if a+b+c != n]
print(list)

#def list_comp(x, y, z , n):
