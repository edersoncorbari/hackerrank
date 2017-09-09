#!/usr/bin/python -tt

import sys

def compute_profit(values):
  for i in range(values):
    N = int(input().strip())
    prices = list(map(int, input().strip().split(' ')))
    s, c = (0, 0)
    tmax = prices[N-1]
    if len(prices) <=1:
      print(0)
    else:
      for j in range(N-1, -1, -1):
        if tmax < prices[j]:
          tmax = prices[j]
        elif  prices[j] < tmax:
          s += (tmax - prices[j])
      print(s)

        
if __name__ == "__main__":        
  compute_profit(int(input().strip()))


