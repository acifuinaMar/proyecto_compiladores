; ModuleID = "compilador_umg_final"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"p" = alloca i32
  %"nums" = alloca [3 x i32]
  %".2" = getelementptr [3 x i32], [3 x i32]* %"nums", i32 0, i32 0
  store i32 1, i32* %".2"
  %".4" = getelementptr [3 x i32], [3 x i32]* %"nums", i32 0, i32 1
  store i32 2, i32* %".4"
  %".6" = getelementptr [3 x i32], [3 x i32]* %"nums", i32 0, i32 2
  store i32 3, i32* %".6"
  %".8" = getelementptr [3 x i32], [3 x i32]* %"nums", i32 0, i32 0
  store i32 0, i32* %".8"
  %".10" = getelementptr [3 x i32], [3 x i32]* %"nums", i32 0, i32 1
  store i32 0, i32* %".10"
  %".12" = getelementptr [3 x i32], [3 x i32]* %"nums", i32 0, i32 0
  %"arr_load_nums" = load i32, i32* %".12"
  %".13" = bitcast [4 x i8]* @"fstr_136384263817600" to i8*
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".13", i32 %"arr_load_nums")
  %".15" = getelementptr [3 x i32], [3 x i32]* %"nums", i32 0, i32 1
  %"arr_load_nums.1" = load i32, i32* %".15"
  %".16" = bitcast [4 x i8]* @"fstr_136384263819168" to i8*
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".16", i32 %"arr_load_nums.1")
  ret i32 0
}

@"fstr_136384263817600" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_136384263819168" = internal constant [4 x i8] c"%d\0a\00"