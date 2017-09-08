#!/usr/bin/python -tt

import sys
from heapq import *

def read(fn):
  return tuple(fn(i) for i in sys.stdin.readline().split(' '))

def load_graph(N, M):
  graph = [dict() for i in range(0, N)]

  for i in range(0, M):
    (x, y, r) = read(int)
    x -= 1
    y -= 1

    r = r if y not in graph[x] else min(r, graph[x][y])
    graph[x][y] = r
    graph[y][x] = r

  return graph

def dijkstras(graph, source):
  q = []
  heappush(q, (0, source))

  distances = [-1] * len(graph)
  distances[source] = 0

  while len(q) > 0:
    (distance, vertice) = heappop(q)
        
    if distances[vertice] > 0:
      continue
    distances[vertice] = distance

    for n in graph[vertice]:
      if distances[n] > -1:
        continue
      cost = distance + graph[vertice][n]
      heappush(q, (cost, n))

  return distances

def test():
  (N, M) = read(int)
  graph = load_graph(N, M)

  S = read(int)[0] - 1
  distances = dijkstras(graph, S)

  for i in range(0, N):
    if i != S:
      end = ' ' if i < N - 1 else '\n'
      print(distances[i], end=end)
    
def main():
  T = read(int)[0]
  for i in range(0, T):
    test()

if __name__ == '__main__':
  main()

