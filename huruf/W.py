"""
1-----1
1-----1
1-----1
1--1--1
1-1-1-1
11---11
1-----1
"""
n=int(input('Tinggi W : '));s=int(n/2);print(''.join([''.join([('1' if(i==x and i>s-(1 if(n%2==0) else 0)) or(i==n-x-1 and i>s-1) or(x==0) or(x==n-1) else '-') for x in range(n)])+'\n' for i in range(n)]))
