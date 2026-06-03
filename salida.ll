; ModuleID = "compilador_umg_final"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"nums" = alloca [5 x i32]
  %".2" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 0
  store i32 5, i32* %".2"
  %".4" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 1
  store i32 8, i32* %".4"
  %".6" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 2
  store i32 13, i32* %".6"
  %".8" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 3
  store i32 21, i32* %".8"
  %".10" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 4
  store i32 34, i32* %".10"
  %".12" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 0
  store i32 10, i32* %".12"
  %".14" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 1
  store i32 20, i32* %".14"
  %".16" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 0
  %"arr_load_nums" = load i32, i32* %".16"
  %".17" = bitcast [4 x i8]* @"fstr_138132748163952" to i8*
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".17", i32 %"arr_load_nums")
  %".19" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 1
  %"arr_load_nums.1" = load i32, i32* %".19"
  %".20" = bitcast [4 x i8]* @"fstr_138132748165632" to i8*
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".20", i32 %"arr_load_nums.1")
  ret i32 0
}

@"fstr_138132748163952" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_138132748165632" = internal constant [4 x i8] c"%d\0a\00"