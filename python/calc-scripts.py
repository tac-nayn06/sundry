# scripts used during ap bc >.<
import math as m

## integral functions :creiy:
def f1(x): return x*x-4 #change this to your discretion, to be referenced in 'fakeintegral' functions;
def derivative(r,n):
    '''1/n = horizontal length of secant segment'''
    return n*(f1(r+1/n)-f1(r))
def lowfakeintegral(a,b,n): # "left" riemann sum
    '''a,b are endpts, n is number of sections'''
    ans,intervalsize=0,(b-a)/n
    for i in range(n):
        ans+=f1(a+i*intervalsize)
    return ans*intervalsize
def highfakeintegral(a,b,n): # "right" riemann sum
    '''a,b are endpts, n is number of sections'''
    ans,intervalsize=0,(b-a)/n
    for i in range(n):
        ans+=f1(a+(i+1)*intervalsize)
    return ans*intervalsize
def trapezoid(a,b,n): # basic trapezoid integral approx
    ans,intervalsize=0,(b-a)/n
    for i in range(n):
        ans+=f1(a+i*intervalsize)+f1(a+(i+1)*intervalsize)
    return ans*intervalsize/2
def simpson(a,b,n): # simpson's integral approx method
    '''n MUST be even for simpson to work!'''
    ans,intervalsize=f1(a)-f1(b),(b-a)/n
    for i in range(n//2):
        ans+=4*f1(a+(2*i+1)*intervalsize) + 2*f1(a+(2*i+2)*intervalsize)
    return ans*intervalsize/3

# newton zero-calculating algorithm
def newton(g,m):
    '''m iterations'''
    N=10**15
    guess=g
    for i in range(m):
        line= [derivative(guess,N),guess*derivative(guess,N)-f1(guess)] # tangent line: y=l[0]*x-l[1]
        guess=line[1]/line[0]
    return guess

# Euler diff eq sol approx algorithm
def f2(x,y): return m.e**(x*y)
def euler(x,y,n,step):
    x0,y0=x,y
    for i in range(n):
        y0+=f2(x0,y0)*step
        x0+=step
    return y0
# more scripts coming soon >:)
