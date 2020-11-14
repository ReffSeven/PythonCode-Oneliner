"""
1 - - - - - 1 
1 1 - - - 1 1 
1 - 1 - 1 - 1 
1 - - 1 - - 1 
1 - - - - - 1 
1 - - - - - 1 
1 - - - - - 1 
"""
n=int(input('Tinggi M : '));s=int(n/2);print(''.join([''.join([('1 ' if(i==x and i<s+1) or(i==n-x-1 and i<s) or(x==0) or(x==n-1) else '- ') for x in range(n)])+'\n' for i in range(n)]))
