# Código TAC generado
p = struct Punto
p.x = 3
p.y = 4
  t1 = p.x
  t2 = p.x
  t3 = t1 * t2
  t4 = p.y
  t5 = p.y
  t6 = t4 * t5
  t7 = t3 + t6
dist = t7
  t8 = dist > 20
  if t8 goto L1
  goto L2
L1:
  t9 = 0
  goto L3
L2:
  t9 = 0
L3:
etiqueta = t9
  print etiqueta
opcion = 2
  t10 = opcion == 1
  if t10 goto L5
  t11 = opcion == 2
  if t11 goto L6
  goto L7
L5:
  print 0
  goto L4
L6:
  print 0
  goto L4
L7:
  print 0
L4:

func fibonacci:
  t12 = n <= 1
  if t12 goto L8
  goto L9
L8:
  return n
  goto L10
L9:
L10:
  t13 = n - 1
  t14 = call fibonacci, t13
  t15 = n - 2
  t16 = call fibonacci, t15
  t17 = t14 + t16
  return t17
endfunc fibonacci

nums = [5, 8, 13, 21, 34]
i = 0
total = 0
L11:
  t18 = i < 5
  if t18 goto L12
  goto L13
L12:
  t19 = nums[i]
  t20 = t19 % 2
r = t20
  t21 = r == 0
  if t21 goto L14
  goto L15
L14:
  goto L16
L15:
L16:
  t22 = total > 50
  if t22 goto L17
  goto L18
L17:
  goto L13
  goto L19
L18:
L19:
  goto L11
L13:
  t23 = call fibonacci, 10
  print t23
  print total