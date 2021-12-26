import itertools
x = ['1','2','3','4','5','6','7','8','9']
arr = [''.join(p) for p in itertools.product(x, repeat=14)]
for s in arr:
  print(s)
