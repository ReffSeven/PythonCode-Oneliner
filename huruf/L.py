"""
1------
1------
1------
1------
1------
1------
1111111
"""
n=int(input('Tinggi L : '));print(''.join([''.join([('1' if(x==0) or(i==n-1) else '-') for x in range(n)])+'\n' for i in range(n)]))
