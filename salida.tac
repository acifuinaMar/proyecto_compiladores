# Código TAC generado
i = 0
m = 0
i = 1
L1:
  t1 = i <= 10
  if t1 goto L2
  goto L3
L2:
  t2 = i % 2
m = t2
  t3 = m == 0
  if t3 goto L4
  goto L5
L4:
  print i
L5:
  t4 = i + 1
i = t4
  goto L1
L3: