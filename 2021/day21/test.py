

def foo(a):
  a[0] = 99






a = [0,1,2,3]
print(a)
foo(a.copy())
print(a)