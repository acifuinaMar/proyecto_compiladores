# Código TAC generado
nums = [5, 8, 13, 21, 34]

func fibonacci:
  t1 = n <= 1
  if t1 goto L1
  goto L2
L1:
  return n
  goto L3
L2:
L3:
  t2 = n - 1
  t3 = call fibonacci, t2
  t4 = n - 2
  t5 = call fibonacci, t4
  t6 = t3 + t5
  return t6
endfunc fibonacci

i = 0
total = 0
L4:
  t7 = i < 5
  if t7 goto L5
  goto L6
L5:
  t8 = nums[i]
  t9 = t8 % 2
r = t9
  t10 = r == 0
  if t10 goto L7
  goto L8
L7:
  goto L9
L8:
L9:
  goto L4
L6:
  t11 = call fibonacci, 0
fib = t11
  t12 = cast_int 20
base = t12
  t13 = total > 40
  if t13 goto L10
  goto L11
L10:
  t14 = 8
  goto L12
L11:
  t14 = 0
L12:
extra = t14
opcion = 2
marcador = 0
  t15 = opcion == 1
  if t15 goto L14
  t16 = opcion == 2
  if t16 goto L15
  goto L16
L14:
  goto L13
L15:
  goto L13
L16:
L13:
  print fib
  print total
  t17 = base + extra
  t18 = t17 + total
  print t18
  print marcador