; ModuleID = "compilador_umg_final"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"nota" = alloca i32
  store i32 85, i32* %"nota"
  %"resultado" = alloca i32
  store i32 0, i32* %"resultado"
  %"load_nota" = load i32, i32* %"nota"
  %".4" = icmp sge i32 %"load_nota", 61
  br i1 %".4", label %"entry.if", label %"entry.else"
entry.if:
  %".6" = bitcast [4 x i8]* @"fstr_136488264528656" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 1)
  %"load_nota.1" = load i32, i32* %"nota"
  %".8" = icmp sge i32 %"load_nota.1", 90
  br i1 %".8", label %"entry.if.if", label %"entry.if.else"
entry.else:
  %".20" = bitcast [4 x i8]* @"fstr_136488112671440" to i8*
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".20", i32 0)
  store i32 0, i32* %"resultado"
  br label %"entry.endif"
entry.endif:
  %"load_resultado" = load i32, i32* %"resultado"
  %".24" = bitcast [4 x i8]* @"fstr_136488112673232" to i8*
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".24", i32 %"load_resultado")
  ret i32 0
entry.if.if:
  store i32 100, i32* %"resultado"
  br label %"entry.if.endif"
entry.if.else:
  %"load_nota.2" = load i32, i32* %"nota"
  %".12" = icmp sge i32 %"load_nota.2", 80
  br i1 %".12", label %"entry.if.else.if", label %"entry.if.else.else"
entry.if.endif:
  br label %"entry.endif"
entry.if.else.if:
  store i32 80, i32* %"resultado"
  br label %"entry.if.else.endif"
entry.if.else.else:
  store i32 60, i32* %"resultado"
  br label %"entry.if.else.endif"
entry.if.else.endif:
  br label %"entry.if.endif"
}

@"fstr_136488264528656" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_136488112671440" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_136488112673232" = internal constant [4 x i8] c"%d\0a\00"