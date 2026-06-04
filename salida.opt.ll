; ModuleID = '<string>'
source_filename = "<string>"
target triple = "x86_64-unknown-linux-gnu"

@fstr_131115412241360 = internal constant [4 x i8] c"%d\0A\00"
@fstr_131115412242256 = internal constant [4 x i8] c"%d\0A\00"
@fstr_131115412341600 = internal constant [4 x i8] c"%d\0A\00"
@fstr_131115412342944 = internal constant [4 x i8] c"%d\0A\00"

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr nocapture noundef readonly, ...) local_unnamed_addr #0

; Function Attrs: nofree nounwind
define noundef i32 @main() local_unnamed_addr #0 {
entry:
  %.44 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr_131115412241360, i32 0)
  %.46 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr_131115412242256, i32 42)
  %.50 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr_131115412341600, i32 70)
  %.52 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr_131115412342944, i32 7)
  ret i32 0
}

attributes #0 = { nofree nounwind }
