m=5
m1=5
map=[]
for i in range(m):
    m2=[]
    if i==0 or i==m-1:
        for j in range(m1):
            m2.append(1)
    else:
        for j in range(m1):
            if j==0 or j==m1-1:
                m2.append(1)
            else:
                m2.append(0)
    map.append(m2)
m3=3
m4=4
map[m3-1][m4-1]=2
