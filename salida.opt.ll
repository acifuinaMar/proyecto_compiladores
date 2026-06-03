; ModuleID = '<string>'
source_filename = "<string>"
target triple = "x86_64-unknown-linux-gnu"

@fstr_138132748163952 = internal constant [4 x i8] c"%d\0A\00"
@fstr_138132748165632 = internal constant [4 x i8] c"%d\0A\00"

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr nocapture noundef readonly, ...) local_unnamed_addr #0

; Function Attrs: nofree nounwind
define noundef i32 @main() local_unnamed_addr #0 {
entry:
  %.18 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr_138132748163952, i32 10)
  %.21 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr_138132748165632, i32 20)
  ret i32 0
}

attributes #0 = { nofree nounwind }
