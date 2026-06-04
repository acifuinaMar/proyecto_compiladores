; ModuleID = '<string>'
source_filename = "<string>"
target triple = "x86_64-unknown-linux-gnu"

@fstr_135621817392320 = internal constant [4 x i8] c"%d\0A\00"
@fstr_135621817393328 = internal constant [4 x i8] c"%d\0A\00"
@fstr_135621817394224 = internal constant [4 x i8] c"%d\0A\00"

declare i32 @printf(ptr, ...)

define i32 @main() {
entry:
  %.4 = mul i32 0, 0
  %.5 = mul i32 0, 0
  %.6 = add i32 %.4, %.5
  %.8 = bitcast ptr @fstr_135621817392320 to ptr
  %.9 = call i32 (ptr, ...) @printf(ptr %.8, i32 0)
  %.10 = bitcast ptr @fstr_135621817393328 to ptr
  %.11 = call i32 (ptr, ...) @printf(ptr %.10, i32 0)
  %.12 = bitcast ptr @fstr_135621817394224 to ptr
  %.13 = call i32 (ptr, ...) @printf(ptr %.12, i32 %.6)
  ret i32 0
}
