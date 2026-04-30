# Código TAC generado
nota = 85
resultado = 0
  t1 = nota >= 61
  if t1 goto L1
  print 0
resultado = 0
  goto L2
L1:
  print 1
  t2 = nota >= 90
  if t2 goto L3
  t3 = nota >= 80
  if t3 goto L5
resultado = 60
  goto L6
L5:
resultado = 80
L6:
  goto L4
L3:
resultado = 100
L4:
L2:
  print resultado