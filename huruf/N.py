"""
1-----1
11----1
1-1---1
1--1--1
1---1-1
1----11
1-----1
"""
n=int(input('Tinggi N : '));s=n/2;print(''.join([''.join([('1' if(i==x) or(x==0) or(x==n-1) else '-') for x in range(n)])+'\n' for i in range(n)]))
