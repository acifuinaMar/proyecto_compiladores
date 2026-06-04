; ModuleID = '<string>'
source_filename = "<string>"
target triple = "x86_64-unknown-linux-gnu"

@fstr_135621817392320 = internal constant [4 x i8] c"%d\0A\00"
@fstr_135621817393328 = internal constant [4 x i8] c"%d\0A\00"
@fstr_135621817394224 = internal constant [4 x i8] c"%d\0A\00"

declare i32 @printf(ptr, ...)

define i32 @main() {
entry:
  %px = alloca i32, align 4
  store i32 0, ptr %px, align 4
  %py = alloca i32, align 4
  store i32 0, ptr %py, align 4
  %dist = alloca i32, align 4
  %load_px = load i32, ptr %px, align 4
  %load_px.1 = load i32, ptr %px, align 4
  %.4 = mul i32 %load_px, %load_px.1
  %load_py = load i32, ptr %py, align 4
  %load_py.1 = load i32, ptr %py, align 4
  %.5 = mul i32 %load_py, %load_py.1
  %.6 = add i32 %.4, %.5
  store i32 %.6, ptr %dist, align 4
  %load_px.2 = load i32, ptr %px, align 4
  %.8 = bitcast ptr @fstr_135621817392320 to ptr
  %.9 = call i32 (ptr, ...) @printf(ptr %.8, i32 %load_px.2)
  %load_py.2 = load i32, ptr %py, align 4
  %.10 = bitcast ptr @fstr_135621817393328 to ptr
  %.11 = call i32 (ptr, ...) @printf(ptr %.10, i32 %load_py.2)
  %load_dist = load i32, ptr %dist, align 4
  %.12 = bitcast ptr @fstr_135621817394224 to ptr
  %.13 = call i32 (ptr, ...) @printf(ptr %.12, i32 %load_dist)
  ret i32 0
}
