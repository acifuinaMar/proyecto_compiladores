; ModuleID = "compilador_umg_final"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"nums" = alloca [3 x i32]
  %".2" = getelementptr [3 x i32], [3 x i32]* %"nums", i32 0, i32 0
  store i32 1, i32* %".2"
  %".4" = getelementptr [3 x i32], [3 x i32]* %"nums", i32 0, i32 1
  store i32 2, i32* %".4"
  %".6" = getelementptr [3 x i32], [3 x i32]* %"nums", i32 0, i32 2
  store i32 3, i32* %".6"
  %".8" = getelementptr [3 x i32], [3 x i32]* %"nums", i32 0, i32 1
  store i32 99, i32* %".8"
  %".10" = getelementptr [3 x i32], [3 x i32]* %"nums", i32 0, i32 0
  %"arr_load_nums" = load i32, i32* %".10"
  %".11" = bitcast [4 x i8]* @"fstr_137502800034432" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i32 %"arr_load_nums")
  %".13" = getelementptr [3 x i32], [3 x i32]* %"nums", i32 0, i32 1
  %"arr_load_nums.1" = load i32, i32* %".13"
  %".14" = bitcast [4 x i8]* @"fstr_137502798496160" to i8*
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14", i32 %"arr_load_nums.1")
  %".16" = getelementptr [3 x i32], [3 x i32]* %"nums", i32 0, i32 2
  %"arr_load_nums.2" = load i32, i32* %".16"
  %".17" = bitcast [4 x i8]* @"fstr_137502798497616" to i8*
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".17", i32 %"arr_load_nums.2")
  ret i32 0
}

@"fstr_137502800034432" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_137502798496160" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_137502798497616" = internal constant [4 x i8] c"%d\0a\00"