#!/usr/bin/python -tt

def connected(visited, curr, adjL):
    visited[curr] = True
    s = 1;
    for c in adjL[curr]:
        if(not visited[c]):
            visited[c] = True;
            s += connected(visited,c,adjL)
    return s;

if __name__ == '__main__':
  [n, p] = input().strip().split()
  n, p = int(n), int(p)
  vis = [False for i in range(0,n)]
  neighs = [[] for i in range(0,n)]

  for i in range(0,p):
    [a, b] = input().strip().split()
    a, b = int(a), int(b)
    neighs[a].append(b)
    neighs[b].append(a)

  M1, M2 = (0, 0) 

  for i in range(0,n):
    if(not vis[i]):
      t = connected(vis, i, neighs)
      M1 += t
      M2 += t * t
        
  print((M1 * M1 - M2)//2)

