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
  %".12" = icmp sle i32 0, 1
  %"i" = alloca i32
  %"total" = alloca i32
  %"r" = alloca i32
  %"fib" = alloca i32
  %"base" = alloca i32
  %"extra" = alloca i32
  %"opcion" = alloca i32
  %"marcador" = alloca i32
  br i1 %".12", label %"entry.if", label %"entry.endif"
entry.if:
  br label %"entry.endif"
entry.endif:
  %".15" = add i32 0, 0
  store i32 0, i32* %"i"
  store i32 0, i32* %"total"
  br label %"w_cond_131115412156192"
w_cond_131115412156192:
  %"load_i" = load i32, i32* %"i"
  %".19" = icmp slt i32 %"load_i", 5
  br i1 %".19", label %"w_body_131115412156192", label %"w_end_131115412156192"
w_body_131115412156192:
  %"load_i.1" = load i32, i32* %"i"
  %".21" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 %"load_i.1"
  %"arr_load_nums" = load i32, i32* %".21"
  %".22" = srem i32 %"arr_load_nums", 2
  store i32 %".22", i32* %"r"
  %"load_r" = load i32, i32* %"r"
  %".24" = icmp eq i32 %"load_r", 0
  br i1 %".24", label %"w_body_131115412156192.if", label %"w_body_131115412156192.endif"
w_end_131115412156192:
  store i32 0, i32* %"fib"
  store i32 20, i32* %"base"
  %"load_total.1" = load i32, i32* %"total"
  %".35" = icmp sgt i32 %"load_total.1", 40
  %".36" = select  i1 %".35", i32 8, i32 0
  store i32 %".36", i32* %"extra"
  store i32 2, i32* %"opcion"
  store i32 0, i32* %"marcador"
  %"load_opcion" = load i32, i32* %"opcion"
  store i32 7, i32* %"marcador"
  store i32 7, i32* %"marcador"
  store i32 7, i32* %"marcador"
  %"load_fib" = load i32, i32* %"fib"
  %".43" = bitcast [4 x i8]* @"fstr_131115412241360" to i8*
  %".44" = call i32 (i8*, ...) @"printf"(i8* %".43", i32 %"load_fib")
  %"load_total.2" = load i32, i32* %"total"
  %".45" = bitcast [4 x i8]* @"fstr_131115412242256" to i8*
  %".46" = call i32 (i8*, ...) @"printf"(i8* %".45", i32 %"load_total.2")
  %"load_base" = load i32, i32* %"base"
  %"load_extra" = load i32, i32* %"extra"
  %".47" = add i32 %"load_base", %"load_extra"
  %"load_total.3" = load i32, i32* %"total"
  %".48" = add i32 %".47", %"load_total.3"
  %".49" = bitcast [4 x i8]* @"fstr_131115412341600" to i8*
  %".50" = call i32 (i8*, ...) @"printf"(i8* %".49", i32 %".48")
  %"load_marcador" = load i32, i32* %"marcador"
  %".51" = bitcast [4 x i8]* @"fstr_131115412342944" to i8*
  %".52" = call i32 (i8*, ...) @"printf"(i8* %".51", i32 %"load_marcador")
  ret i32 0
w_body_131115412156192.if:
  %"load_total" = load i32, i32* %"total"
  %"load_i.2" = load i32, i32* %"i"
  %".26" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 %"load_i.2"
  %"arr_load_nums.1" = load i32, i32* %".26"
  %".27" = add i32 %"load_total", %"arr_load_nums.1"
  store i32 %".27", i32* %"total"
  br label %"w_body_131115412156192.endif"
w_body_131115412156192.endif:
  %"load_i.3" = load i32, i32* %"i"
  %".30" = add i32 %"load_i.3", 1
  store i32 %".30", i32* %"i"
  br label %"w_cond_131115412156192"
}

@"fstr_131115412241360" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_131115412242256" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_131115412341600" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_131115412342944" = internal constant [4 x i8] c"%d\0a\00"