; ModuleID = "compilador_umg_final"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"p" = alloca i32
  %"dist" = alloca i32
  %".2" = mul i32 0, 0
  %".3" = mul i32 0, 0
  %".4" = add i32 %".2", %".3"
  store i32 %".4", i32* %"dist"
  %"etiqueta" = alloca i32
  %"load_dist" = load i32, i32* %"dist"
  %".6" = icmp sgt i32 %"load_dist", 20
  %".7" = select  i1 %".6", i32 0, i32 0
  store i32 %".7", i32* %"etiqueta"
  %"load_etiqueta" = load i32, i32* %"etiqueta"
  %".9" = bitcast [4 x i8]* @"fstr_139539592824096" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %"load_etiqueta")
  %"opcion" = alloca i32
  store i32 2, i32* %"opcion"
  %"load_opcion" = load i32, i32* %"opcion"
  %".12" = bitcast [4 x i8]* @"fstr_139539592827008" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i32 0)
  %".14" = bitcast [4 x i8]* @"fstr_139539592828240" to i8*
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14", i32 0)
  %".16" = bitcast [4 x i8]* @"fstr_139539592829360" to i8*
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".16", i32 0)
  %".18" = icmp sle i32 0, 1
  %"nums" = alloca [5 x i32]
  %"i" = alloca i32
  %"total" = alloca i32
  %"r" = alloca i32
  br i1 %".18", label %"entry.if", label %"entry.endif"
entry.if:
  br label %"entry.endif"
entry.endif:
  %".21" = add i32 0, 0
  %".22" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 0
  store i32 5, i32* %".22"
  %".24" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 1
  store i32 8, i32* %".24"
  %".26" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 2
  store i32 13, i32* %".26"
  %".28" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 3
  store i32 21, i32* %".28"
  %".30" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 4
  store i32 34, i32* %".30"
  store i32 0, i32* %"i"
  store i32 0, i32* %"total"
  br label %"w_cond_139539592891872"
w_cond_139539592891872:
  %"load_i" = load i32, i32* %"i"
  %".35" = icmp slt i32 %"load_i", 5
  br i1 %".35", label %"w_body_139539592891872", label %"w_end_139539592891872"
w_body_139539592891872:
  %"load_i.1" = load i32, i32* %"i"
  %".37" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 %"load_i.1"
  %"arr_load_nums" = load i32, i32* %".37"
  %".38" = srem i32 %"arr_load_nums", 2
  store i32 %".38", i32* %"r"
  %"load_r" = load i32, i32* %"r"
  %".40" = icmp eq i32 %"load_r", 0
  br i1 %".40", label %"w_body_139539592891872.if", label %"w_body_139539592891872.endif"
w_end_139539592891872:
  %".52" = bitcast [4 x i8]* @"fstr_139539592900608" to i8*
  %".53" = call i32 (i8*, ...) @"printf"(i8* %".52", i32 0)
  %"load_total.2" = load i32, i32* %"total"
  %".54" = bitcast [4 x i8]* @"fstr_139539592902288" to i8*
  %".55" = call i32 (i8*, ...) @"printf"(i8* %".54", i32 %"load_total.2")
  ret i32 0
w_body_139539592891872.if:
  %"load_total" = load i32, i32* %"total"
  %"load_i.2" = load i32, i32* %"i"
  %".42" = getelementptr [5 x i32], [5 x i32]* %"nums", i32 0, i32 %"load_i.2"
  %"arr_load_nums.1" = load i32, i32* %".42"
  %".43" = add i32 %"load_total", %"arr_load_nums.1"
  store i32 %".43", i32* %"total"
  br label %"w_body_139539592891872.endif"
w_body_139539592891872.endif:
  %"load_i.3" = load i32, i32* %"i"
  %".46" = add i32 %"load_i.3", 1
  store i32 %".46", i32* %"i"
  %"load_total.1" = load i32, i32* %"total"
  %".48" = icmp sgt i32 %"load_total.1", 50
  br i1 %".48", label %"w_body_139539592891872.endif.if", label %"w_body_139539592891872.endif.endif"
w_body_139539592891872.endif.if:
  br label %"w_body_139539592891872.endif.endif"
w_body_139539592891872.endif.endif:
  br label %"w_cond_139539592891872"
}

@"fstr_139539592824096" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_139539592827008" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_139539592828240" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_139539592829360" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_139539592900608" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_139539592902288" = internal constant [4 x i8] c"%d\0a\00"