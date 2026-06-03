; ModuleID = '<string>'
source_filename = "<string>"
target triple = "x86_64-unknown-linux-gnu"

@fstr_128414830365280 = internal constant [4 x i8] c"%d\0A\00"
@fstr_128414830366848 = internal constant [4 x i8] c"%d\0A\00"

declare i32 @printf(ptr, ...)

define i32 @main() {
entry:
  %.13 = bitcast ptr @fstr_128414830365280 to ptr
  %.14 = call i32 (ptr, ...) @printf(ptr %.13, i32 0)
  %.16 = bitcast ptr @fstr_128414830366848 to ptr
  %.17 = call i32 (ptr, ...) @printf(ptr %.16, i32 0)
  ret i32 0
}
