def f(s):
  return math.sin(s)

def x(s):
  return a+(b-a)/n*s

def c(s,lam,k):
  for j in range(0,k):
    lam=lam*(s-x(j))
  for j in range(k,n+1):
    lam=lam*(s-x(j))
  return lam
  
n=int(input())
a=float(input())
b=float(input())
xx=float(input())
l=[]
for i in range(0,n+1):
  h=1.0
  for j in range(0,i):
    h=h/(x(i)-x(j))
  for j in range(i+1,n+1):
    h=h/(x(i)-x(j)) 
    l.append(h)
L=0.0
for i in range(0,n+1):
  L = L + c(xx, l[i],i) * f( x(i) )
print(L)
