#!/usr/bin/python -tt

a, b, n = input().split()
arr = [0 for i in range(20)]

arr[0] = int(a)
arr[1] = int(b)
n = int(n)

for i in range(2,n):
  arr[i] = arr[i-1] ** 2 + arr[i-2]

print (arr[n-1])

