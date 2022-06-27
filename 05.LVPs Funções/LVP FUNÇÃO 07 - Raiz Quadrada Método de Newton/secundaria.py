def f_quadp(a1):
  v = (a1//2)+1
  for l in range(1,v+1):
    if (a1 > l**2):
      d = a1 - l**2
    else:
      d = l**2-a1
    if (l == 1):
      difer = d
      q = l
    elif (d < difer):
      difer = d
      q = l
  return q

def f_quad(a1):
  quadperf =  f_quadp(a1)
  quad = (a1+(quadperf**2))/(2*quadperf)
  return quad
