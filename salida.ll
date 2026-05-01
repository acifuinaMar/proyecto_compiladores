; ModuleID = "compilador_umg_final"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"i" = alloca i32
  %"m" = alloca i32
  store i32 1, i32* %"i"
  br label %"f_cond_138017060303856"
f_cond_138017060303856:
  %"load_i" = load i32, i32* %"i"
  %".4" = icmp sle i32 %"load_i", 10
  br i1 %".4", label %"f_body_138017060303856", label %"f_end_138017060303856"
f_body_138017060303856:
  %"load_i.1" = load i32, i32* %"i"
  %".6" = srem i32 %"load_i.1", 2
  store i32 %".6", i32* %"m"
  %"load_m" = load i32, i32* %"m"
  %".8" = icmp eq i32 %"load_m", 0
  br i1 %".8", label %"f_body_138017060303856.if", label %"f_body_138017060303856.endif"
f_inc_138017060303856:
  %"load_i.3" = load i32, i32* %"i"
  %".14" = add i32 %"load_i.3", 1
  store i32 %".14", i32* %"i"
  br label %"f_cond_138017060303856"
f_end_138017060303856:
  ret i32 0
f_body_138017060303856.if:
  %"load_i.2" = load i32, i32* %"i"
  %".10" = bitcast [4 x i8]* @"fstr_138017060298480" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i32 %"load_i.2")
  br label %"f_body_138017060303856.endif"
f_body_138017060303856.endif:
  br label %"f_inc_138017060303856"
}

@"fstr_138017060298480" = internal constant [4 x i8] c"%d\0a\00"