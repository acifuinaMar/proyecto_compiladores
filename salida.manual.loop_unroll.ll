; ModuleID = '<string>'
source_filename = "<string>"
target triple = "x86_64-unknown-linux-gnu"

@fstr_128414830365280 = internal constant [4 x i8] c"%d\0A\00"
@fstr_128414830366848 = internal constant [4 x i8] c"%d\0A\00"

declare i32 @printf(ptr, ...)

define i32 @main() {
entry:
  %p = alloca i32, align 4
  %nums = alloca [3 x i32], align 4
  %.2 = getelementptr [3 x i32], ptr %nums, i32 0, i32 0
  store i32 1, ptr %.2, align 4
  %.4 = getelementptr [3 x i32], ptr %nums, i32 0, i32 1
  store i32 2, ptr %.4, align 4
  %.6 = getelementptr [3 x i32], ptr %nums, i32 0, i32 2
  store i32 3, ptr %.6, align 4
  %.8 = getelementptr [3 x i32], ptr %nums, i32 0, i32 0
  store i32 0, ptr %.8, align 4
  %.10 = getelementptr [3 x i32], ptr %nums, i32 0, i32 1
  store i32 0, ptr %.10, align 4
  %.12 = getelementptr [3 x i32], ptr %nums, i32 0, i32 0
  %arr_load_nums = load i32, ptr %.12, align 4
  %.13 = bitcast ptr @fstr_128414830365280 to ptr
  %.14 = call i32 (ptr, ...) @printf(ptr %.13, i32 %arr_load_nums)
  %.15 = getelementptr [3 x i32], ptr %nums, i32 0, i32 1
  %arr_load_nums.1 = load i32, ptr %.15, align 4
  %.16 = bitcast ptr @fstr_128414830366848 to ptr
  %.17 = call i32 (ptr, ...) @printf(ptr %.16, i32 %arr_load_nums.1)
  ret i32 0
}
