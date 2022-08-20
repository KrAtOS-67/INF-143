from sys import stdin,stdout
from functools import reduce
#from itertools import combinations
#from itertools import chain, combinations
import gmpy2
#import math
# from multiset import * 
# from math import ceil
# import math
#from collections import deque
# from heapq import heappush,heappop
Pi = lambda x: stdout.write(str(x) + '\n')
Ps = lambda x: stdout.write(str(x))
R = lambda:stdin.readline()
Ri = lambda x:map(int,x.split())
Rs = lambda x:map(str,x.split())
Rf = lambda x:map(float,x.split())
char = lambda x,y:ord(x) - ord(y) 
gcd = lambda a,b: a if b==0 else gcd(b, a%b) 
lcm = lambda a,b: a * b // gcd(a, b)
#ejer = lambda a,i,vocales: stdout.write(f"Case #{i+1}: {a} is ruled by Alice.\n") if a[len(a)-1] in vocales else stdout.write(f"Case #{i+1}: {a} is ruled by Bob.\n")
Matriz = lambda n,m:[[0 for i in range(m)]for i in range(n)]
MaxN = int(1e5) + 10
mod = int(1e9) + 7
fx,fy = [0,0,-1,1],[1,-1,0,0] #matriz dere izq arri abaj    
def main():
    for _ in range(int(R())):
        n=int(R())
        n=n+1
        vec=[int(i) for i in R().strip().split()]
        k=reduce(lambda x, y: x*y, vec)
        Pi("EL producto es numero cuadrado") if(gmpy2.is_square(k)) else Pi("El producto no es numero cuadrado")
if __name__ == '__main__':
        main()