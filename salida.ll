; ModuleID = "compilador_umg_final"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %".2" = icmp sgt i32 0, 0
  %".3" = sub i32 0, 0
  %".4" = select  i1 %".2", i32 0, i32 %".3"
  %".5" = bitcast [4 x i8]* @"fstr_130581644049920" to i8*
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5", i32 0)
  ret i32 0
}

@"fstr_130581644049920" = internal constant [4 x i8] c"%d\0a\00"