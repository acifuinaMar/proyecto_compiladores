; ModuleID = '<string>'
source_filename = "<string>"
target triple = "x86_64-unknown-linux-gnu"

@fstr_135621817392320 = internal constant [4 x i8] c"%d\0A\00"
@fstr_135621817393328 = internal constant [4 x i8] c"%d\0A\00"
@fstr_135621817394224 = internal constant [4 x i8] c"%d\0A\00"

declare i32 @printf(ptr, ...)

define i32 @main() {
entry:
  %.9 = call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @fstr_135621817392320, i32 0)
  %.11 = call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @fstr_135621817393328, i32 0)
  %.13 = call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @fstr_135621817394224, i32 0)
  ret i32 0
}
