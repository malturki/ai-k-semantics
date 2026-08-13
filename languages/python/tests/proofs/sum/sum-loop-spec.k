requires "sum-loop-verification.k"

module SUM-LOOP-SPEC
  imports SUM-LOOP-VERIFICATION

  claim
    <sum>
      <k> sumInit => .K </k>
      <n> N:Int </n>
      <i> _ => 1 </i>
      <total> _ => 0 </total>
    </sum>
    requires N >=Int 0
    ensures sumLoopInv(N, 1, 0)
    [label(sum-init-establishes-invariant)]

  claim
    <sum>
      <k> sumLoop => sumLoop ... </k>
      <n> N:Int </n>
      <i> I:Int => I +Int 1 </i>
      <total> Total:Int => Total +Int I </total>
    </sum>
    requires N >=Int 0
     andBool sumLoopInv(N, I, Total)
     andBool I <=Int N
    ensures sumLoopInv(N, I +Int 1, Total +Int I)
    [label(sum-loop-preserves-invariant)]

  claim
    <sum>
      <k> sumLoop => sumDone ... </k>
      <n> N:Int </n>
      <i> I:Int </i>
      <total> Total:Int </total>
    </sum>
    requires N >=Int 0
     andBool sumLoopInv(N, I, Total)
     andBool notBool I <=Int N
    ensures I ==Int N +Int 1
     andBool Total ==Int sumTo(N)
    [label(sum-loop-exit-implies-postcondition)]
endmodule
