import random

def fun(x):
    return (6*x)**3

def cruza(bpob, n):
    a=[]
    a=bpob
    par=[]
    k=0
    
    for i in range(0,n,2):
        ran=random.randrange(0,len(a[i]))
        while (k<n):
            if k in par:
                k=k+1
                continue
            par.append(k)
            p=random.randrange(k+1,n)
            while p in par:
                p=random.randrange(k+1,n)
            par.append(p)
            k=k+1
            
        for j in range(ran,len(a[i])):
            tmp=a[par[i]][j]
            tmp1=list(a[par[i]])
            tmp2=list(a[par[i+1]])
            tmp1[j]=a[par[i+1]][j]
            tmp2[j]=tmp
            a[par[i]]=''.join(tmp1)
            a[par[i+1]]=''.join(tmp2)
    return a

def poblacion(n,start,stop):
    pob=[]
    bpob=[]
    sumi=0
    suma=0
    for i in range(0,n):
        pob.append(random.randrange(start,stop))
        suma+=fun(pob[i])
        sumi+=pob[i]
        bpob.append(format(pob[i], '{fill}{width}b'.format(width=10, fill=0)))
        
    PS=[]
    VE=[]
    VA=[]
    media=suma/n
    for i in range(0,n):
        PS.append(fun(pob[i])/suma)
        VE.append(fun(pob[i])/media)
        VA.append(round(VE[i]))
        print(pob[i],' ',bpob[i],' ',PS[i],' ',VE[i],' ',VA[i])
    print(sumi/n)
    print('\n')
    return bpob

def maximice(t, n, bpob):
    bsg=[]
    for i in range(0,n):
        bsg.append(bpob[i])
    while(t!=0):
        bsg=cruza(bsg,n)
        sg=[]
        sumi=0
        sgsuma=0
        for i in range(0,n):
            sg.append(int(bsg[i],2))
            sumi+=sg[i]
            sgsuma+=fun(sg[i])
        sgPS=[]
        sgVE=[]
        sgVA=[]
        sgmedia=sgsuma/n
        for i in range(0,n):
            sgPS.append(fun(sg[i])/sgsuma)
            sgVE.append(fun(sg[i])/sgmedia)
            sgVA.append(round(sgVE[i]))
        sp=0
        for i in range(0,n):
            print(sg[i],' ',bsg[i],' ',sgPS[i],' ',sgVE[i],' ',sgVA[i])
        print(sumi/n)
        print('\n')

        t=t-1

n=6
t=10
min=0
max=2**10
bpob=poblacion(n,min,max)
maximice(t, n, bpob)