# Código TAC generado
nums = [3, 1, 4, 1, 5]
total = 0
i = 0
L1:
  t1 = i < 5
  if t1 goto L2
  goto L3
L2:
  t2 = nums[i]
val = t2
  t3 = val % 2
  t4 = t3 == 0
  if t4 goto L4
  goto L5
L4:
  t5 = total + val
total = t5
L5:
  t6 = i + 1
i = t6
  t7 = total > 10
  if t7 goto L6
  goto L7
L6:
  goto L3
L7:
  goto L1
L3:
msg = 0
  t8 = msg + 0
  print t8
  t9 = call fib, 6
r = t9
  print r
j = 0
L8:
  t10 = j < 5
  if t10 goto L9
  goto L10
L9:
  t11 = j + 1
j = t11
  t12 = j == 3
  if t12 goto L11
  goto L12
L11:
  goto L8
L12:
  print j
  goto L8
L10:
  print 0
  print total