"""
1111111
---1---
---1---
---1---
---1---
---1---
---1---
"""
n=int(input('Tinggi T : '));s=int(n/2);print(''.join([''.join([('1' if(x==s) or(i==0) else '-') for x in range(n)])+'\n' for i in range(n)]))
