; ModuleID = "compilador_umg_final"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"x" = alloca i32
  store i32 2, i32* %"x"
  %"load_x" = load i32, i32* %"x"
  %".3" = bitcast [4 x i8]* @"fstr_126623151215392" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 1)
  %".5" = bitcast [4 x i8]* @"fstr_126623151216736" to i8*
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5", i32 2)
  %".7" = bitcast [4 x i8]* @"fstr_126623151217856" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 999)
  ret i32 0
}

@"fstr_126623151215392" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_126623151216736" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_126623151217856" = internal constant [4 x i8] c"%d\0a\00"