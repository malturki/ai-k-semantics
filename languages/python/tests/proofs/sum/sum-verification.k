requires "../../../semantics/python.k"
requires "domains.md"

module PYTHON-SUM-SPEC-SYNTAX
  imports PYTHON-SYNTAX
endmodule

module PYTHON-SUM-VERIFICATION
  imports PYTHON
  imports INT
  imports MAP-SYMBOLIC

  syntax Int ::= sumTo(Int) [function, total]
  rule sumTo(N:Int) => (N *Int (N +Int 1)) /Int 2

  syntax Bool ::= sumLoopInv(Int, Int, Int) [function, total]
  rule sumLoopInv(N:Int, I:Int, Total:Int) =>
       1 <=Int I
    andBool I <=Int N +Int 1
    andBool Total ==Int ((I -Int 1) *Int I) /Int 2

  syntax Exp ::= "sumCond" [function, symbol(sumCond)]
  rule sumCond => #token("i", "Id") <= #token("n", "Id")

  syntax Stmts ::= "sumBodyStmts" [function, symbol(sumBodyStmts)]
  rule sumBodyStmts =>
    stmtsCons(#token("total", "Id") = #token("total", "Id") + #token("i", "Id"),
    stmtsLast(#token("i", "Id") = #token("i", "Id") + 1))

  syntax Block ::= "sumBody" [function, symbol(sumBody)]
  rule sumBody => block(sumBodyStmts)

  syntax Stmts ::= "sumProgram" [function, symbol(sumProgram)]
  rule sumProgram =>
    stmtsCons(#token("total", "Id") = 0,
    stmtsCons(#token("i", "Id") = 1,
    stmtsCons(#while(sumCond, sumBody),
    stmtsLast(#token("total", "Id")))))
endmodule
