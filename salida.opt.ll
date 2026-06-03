; ModuleID = '<string>'
source_filename = "<string>"
target triple = "x86_64-unknown-linux-gnu"

@fstr_139539592824096 = internal constant [4 x i8] c"%d\0A\00"
@fstr_139539592827008 = internal constant [4 x i8] c"%d\0A\00"
@fstr_139539592828240 = internal constant [4 x i8] c"%d\0A\00"
@fstr_139539592829360 = internal constant [4 x i8] c"%d\0A\00"
@fstr_139539592900608 = internal constant [4 x i8] c"%d\0A\00"
@fstr_139539592902288 = internal constant [4 x i8] c"%d\0A\00"

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr nocapture noundef readonly, ...) local_unnamed_addr #0

; Function Attrs: nofree nounwind
define noundef i32 @main() local_unnamed_addr #0 {
entry:
  %.10 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr_139539592824096, i32 0)
  %.13 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr_139539592827008, i32 0)
  %.15 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr_139539592828240, i32 0)
  %.17 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr_139539592829360, i32 0)
  %.53 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr_139539592900608, i32 0)
  %.55 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fstr_139539592902288, i32 42)
  ret i32 0
}

attributes #0 = { nofree nounwind }
