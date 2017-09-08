#!/usr/bin/python -tt

q = int(input())

for qq in range(q):
  a = input()
  b = input()
  dic = {}
  result = False

  for i in b:
    if i not in dic:
      dic[i] = 0
    dic[i] += 1

  for i in a:
    if i not in dic:
      if i == i.upper():
        print ('NO')
        result = True
        break
      else:
        if dic[i] > 0:
          dic[i] -= 1
        else:
          print ('NO')
          result = True
          break

  if result:
    continue

  a = a.upper()
  T = ['' for i in range(len(a)+1)]

  for i in range(1, len(a)+1):
    temp = ''
    for j in range(i):
      if len(T[j] + a[i-1]) > len(temp):
        temp = T[j] + a[i-1]
        if temp == b[:len(temp)]:
          T[i] = temp
          if len(temp) == len(b):
            print ('YES')
            result = True
            break
          if result:
            break
      if not result:
        print ('NO')

