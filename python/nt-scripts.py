import math
def legendre(a,p):
    ans=pow(a,(p-1)//2,p)
    if ans==1: return True
    return False
def ressol(a,p): #Shanks-Tonelli RESSOL from niven's intro to NT, solves x^2=a(mod p)
    """p prime"""
    if not legendre(a,p): return 'No solution'
    if p%4==3:
        sol=pow(a,(p+1)//4,p)
        return [sol,p-sol]
    q,s=p-1,0
    while q%2==0: q,s=q//2,s+1
    z=2
    while legendre(z,p): z+=1
    m,c,t,r=s,pow(z,q,p),pow(a,q,p),pow(a,(q+1)//2,p)
    if t==0: return [0]
    while t!=1:
        i,t1=0,t
        while t1 !=1: t1,i = (t1*t1)%p,i+1
        b=c
        for i in range(m-i-1): b=(b*b)%p #b=c^{2^{m-i-1}}(mod p)
        m,c,t,r=i,(b*b)%p,(((t*b)%p)*b)%p,(r*b)%p
    return [r,p-r]
# for the following 2 scripts u need the  "multiply" function from hpc-scripts.py for proper function
def twosquaresum(p): #solving diophantine eq x^2+y^2=p for primes, criterion is famous, but alg to find nums explicitly is not
    '''works for primes p only'''
    if p%4==3: return 'Impossible'
    l=ressol(p-1,p)
    S=[[0,-1],[1,0]]
    s=min(l[0],l[1])
    k=math.ceil(s*(s/p))
    a,b,c=p,2*s,k
    v=[[1],[0]]
    while (a,b,c) !=(1,0,1):
        if a>c: a,b,c,v =c,-b,a,multiply(S,v)
        m=math.ceil(-b/(2*a))
        b,c=2*a*m+b,(a*m*m)+(b*m)+c
        v=multiply([[1,-m],[0,1]],v)
    return [abs(v[0][0]),abs(v[1][0])]
def x2_xy_y2(p):# solves diophantine eq x^2+xy+y^2=p, prime p
    if p==3: return [1,1]
    if p !=3 and p%3 !=1: return 'Impossible'
    l=ressol(p-3,p)
    s=l[l[1]%2 !=0]
    k=(s*s+3)//(4*p)
    a,b,c=p,s,k
    v,S=[[1],[0]],[[0,-1],[1,0]]
    while (a,b,c) !=(1,1,1):
        if a>c: a,b,c,v =c,-b,a,multiply(S,v)
        if b<0: m=math.floor(-b/(2*a)+0.5)
        else: m=math.ceil(-b/(2*a)-0.5)
        b,c=2*a*m+b,(a*m*m)+(b*m)+c
        v=multiply([[1,-m],[0,1]],v)
    p,q=v[0][0],v[1][0]
    if p*q > 0: return [abs(p),abs(q)]
    elif p+q<0: return [max(p,q),-(p+q)]
    return [-min(p,q),p+q]
