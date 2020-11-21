"""
1 2 3 4 5 6 7
2 3 4 5 6 7 6
3 4 5 6 7 6 5
4 5 6 7 6 5 4
5 6 7 6 5 4 3
6 7 6 5 4 3 2
7 6 5 4 3 2 1
"""
N = 7;print('\n'.join([' '.join([str(x+y) if((x+y)<=N) else(str(N-((N-(x+y))*-1))) for x in range(1,N+1)]) for y in range(N)]))
