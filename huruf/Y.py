"""
1-----1
-1---1-
--1-1--
---1---
---1---
---1---
---1---
"""
n=int(input('Tinggi Y : '));;s=int(n/2);print(''.join([''.join([('1' if(i==x and i<s+(1 if(n%2==1) else 0)) or(i==n-x-1 and i<s) or((x==s or x==s-(1 if(n%2==0) else 0)) and i>=s) else '-') for x in range(n)])+'\n' for i in range(n)]))
