# Código TAC generado

func abs:
  t1 = n > 0
  if t1 goto L1
  goto L2
L1:
  t2 = n
  goto L3
L2:
  t3 = 0 - n
  t2 = t3
L3:
  return t2
endfunc abs

  t4 = -7
  t5 = call abs, t4
  print t5