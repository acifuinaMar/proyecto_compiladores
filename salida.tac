# Código TAC generado
x = 2
  t1 = x == 1
  if t1 goto L2
  t2 = x == 2
  if t2 goto L3
  goto L4
L2:
  print 1
  goto L1
L3:
  print 2
  goto L1
L4:
  print 999
L1: