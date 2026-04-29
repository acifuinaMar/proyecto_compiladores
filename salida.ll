; ModuleID = "programa"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"limite" = alloca i32
  store i32 10, i32* %"limite"
  %"suma" = alloca i32
  store i32 0, i32* %"suma"
  %"i" = alloca i32
  store i32 1, i32* %"i"           ; Empezamos en 1
  br label %"f_cond"

f_cond:
  %curr_i = load i32, i32* %"i"
  %max_l = load i32, i32* %"limite"
  ; sle = Signed Less or Equal (i <= limite)
  %test = icmp sle i32 %curr_i, %max_l 
  br i1 %test, label %"f_body", label %"f_end"

f_body:
  %s_val = load i32, i32* %"suma"
  %i_val = load i32, i32* %"i"
  %new_sum = add i32 %s_val, %i_val
  store i32 %new_sum, i32* %"suma"
  br label %"f_step"

f_step:
  %old_i = load i32, i32* %"i"
  %next_i = add i32 %old_i, 1
  store i32 %next_i, i32* %"i"
  br label %"f_cond"

f_end:
  %res = load i32, i32* %"suma"
  ret i32 %res
}
