from sys import stdin,stdout
#from functools import reduce
#from itertools import combinations
#from itertools import chain, combinations
#import gmpy2
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
def producto_matrices(a, b):
    filas_a = len(a)
    filas_b = len(b)
    columnas_a = len(a[0])
    columnas_b = len(b[0])
    if columnas_a != filas_b:
        return None
    producto = []
    for i in range(filas_b):
        producto.append([])
        for j in range(columnas_b):
            producto[i].append(None)
    for c in range(columnas_b):
        for i in range(filas_a):
            suma = 0
            for j in range(columnas_a):
                suma += a[i][j]*b[j][c]
            producto[i][c] = suma
    return producto
def main():
    a,b=Ri(R())
    vec=[]
    for i in range(a):
        vec.append([int(j) for j in R().strip().split()])
    f=vec
    for i in range(b-1):
        f = producto_matrices(f, vec)
    for k in f:
        print(*k)
if __name__ == '__main__':
        main() 