requires "domains.md"

module SUM-LOOP-VERIFICATION
  imports INT
  imports BOOL

  configuration
    <sum>
      <k> $PGM:K </k>
      <n> 0 </n>
      <i> 0 </i>
      <total> 0 </total>
    </sum>

  syntax KItem ::= "sumProgram"
                 | "sumInit"
                 | "sumLoop"
                 | "sumDone"

  rule <k> sumProgram => sumInit ~> sumLoop </k>

  rule <k> sumInit => .K </k>
       <i> _ => 1 </i>
       <total> _ => 0 </total>

  rule <k> sumLoop => sumLoop ... </k>
       <n> N </n>
       <i> I => I +Int 1 </i>
       <total> Total => Total +Int I </total>
    requires I <=Int N

  rule <k> sumLoop => sumDone ... </k>
       <n> N </n>
       <i> I </i>
    requires notBool I <=Int N

  syntax Int ::= sumTo(Int) [function, total]
  rule sumTo(0) => 0
  rule sumTo(N:Int) => sumTo(N -Int 1) +Int N
    requires N >Int 0

  syntax Bool ::= sumLoopInv(Int, Int, Int) [function, total]
  rule sumLoopInv(N:Int, I:Int, Total:Int) =>
       1 <=Int I
    andBool I <=Int N +Int 1
    andBool Total ==Int sumTo(I -Int 1)
endmodule
