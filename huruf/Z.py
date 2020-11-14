"""
1111111
-----1-
----1--
---1---
--1----
-1-----
1111111
"""
n=int(input('Tinggi Z : '));s=n/2;print(''.join([''.join([('1' if(i==n-x-1) or(i==0) or(i==n-1) else '-') for x in range(n)])+'\n' for i in range(n)]))
