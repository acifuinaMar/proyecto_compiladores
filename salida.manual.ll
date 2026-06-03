; ModuleID = '<string>'
source_filename = "<string>"
target triple = "x86_64-unknown-linux-gnu"

@fstr_128414830365280 = internal constant [4 x i8] c"%d\0A\00"
@fstr_128414830366848 = internal constant [4 x i8] c"%d\0A\00"

declare i32 @printf(ptr, ...)

define i32 @main() {
entry:
  %.14 = call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @fstr_128414830365280, i32 0)
  %.17 = call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @fstr_128414830366848, i32 0)
  ret i32 0
}
