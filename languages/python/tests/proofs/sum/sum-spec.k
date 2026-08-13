module PYTHON-SUM-SPEC
  imports PYTHON-SUM-VERIFICATION

  claim
    <python>
      <k> sumProgram => .K </k>
      <env> #token("n", "Id") |-> N:Int => #token("n", "Id") |-> N
                                              #token("total", "Id") |-> sumTo(N)
                                              #token("i", "Id") |-> N +Int 1 </env>
      <iterators> .Map </iterators>
      <objectAttrs> .Map </objectAttrs>
      <nextIterator> 0 </nextIterator>
      <nextObject> 0 </nextObject>
      <activeException> noException </activeException>
      <result> _ => sumTo(N) </result>
    </python>
    requires N >=Int 0
    ensures true
    [label(sum-program-correct)]

  claim
    <python>
      <k> sumBodyStmts ~> whileStmtAgain(sumCond, sumBody)
        => #while(sumCond, sumBody)
        ... </k>
      <env> #token("n", "Id") |-> N:Int
             #token("i", "Id") |-> I:Int
             #token("total", "Id") |-> Total:Int
          => #token("n", "Id") |-> N
             #token("i", "Id") |-> I +Int 1
             #token("total", "Id") |-> Total +Int I </env>
      <result> _ => .K </result>
      ...
    </python>
    requires N >=Int 0
     andBool sumLoopInv(N, I, Total)
     andBool I <=Int N
    ensures sumLoopInv(N, I +Int 1, Total +Int I)
    [label(sum-loop-preserves-invariant)]

  claim
    <python>
      <k> False ~> whileStmtBranch(sumCond, sumBody)
        => .K ... </k>
      <env> #token("n", "Id") |-> N:Int
             #token("i", "Id") |-> I:Int
             #token("total", "Id") |-> Total:Int </env>
      <result> _ => Total </result>
      ...
    </python>
    requires N >=Int 0
     andBool sumLoopInv(N, I, Total)
     andBool notBool I <=Int N
    ensures Total ==Int sumTo(N)
    [label(sum-loop-exit-postcondition)]
endmodule
