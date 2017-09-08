#!/usr/bin/python -tt

def compute_profit(values, prof):
  buy = [1] * len(values)
  prof, m = (0, 0)

  for i in reversed(range(len(values))):
    ai = values[i]
    if m <= ai:
      buy[i] = 0
      m = ai
    prof += m-ai
    
  if prof:
    return (prof)
  return (prof, buy)

if __name__ == "__main__":
  print compute_profit([5, 3, 2, 2, 0], True)
  print compute_profit([1,2,100], True)    
  print compute_profit([1, 3, 1, 2], True)

