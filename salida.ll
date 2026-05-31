; ModuleID = "compilador_umg_final"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"texto" = alloca i32
  store i32 0, i32* %"texto"
  %"x" = alloca i32
  %"load_texto" = load i32, i32* %"texto"
  store i32 %"load_texto", i32* %"x"
  ret i32 0
}
