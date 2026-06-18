requires "domains.md"

module PYTHON-SYNTAX
  imports INT-SYNTAX
  imports ID-SYNTAX

  syntax Stmts ::= Stmt ";" Stmts [symbol(stmtsCons)]
                 | Stmt ";" [symbol(stmtsLast)]

  syntax Stmt ::= Exp
                | Id "=" Exp [symbol(assignStmt), strict(2)]

  syntax Exp ::= Int
               | Id
               | "(" Exp ")" [bracket]
               > Exp "*" Exp [symbol(mulExp), left, strict]
               > Exp "+" Exp [symbol(addExp), left, strict]
               | Exp "-" Exp [symbol(subExp), left, strict]
endmodule

module PYTHON
  imports PYTHON-SYNTAX
  imports INT
  imports MAP

  syntax KResult ::= Int
  syntax KItem ::= stmtNext(Stmts) [symbol(stmtNext)]
                 | "stmtEnd" [symbol(stmtEnd)]
                 | "stmtNoResult" [symbol(stmtNoResult)]

  configuration
    <python>
      <k> $PGM:Stmts </k>
      <env> .Map </env>
      <result> .K </result>
    </python>

  rule <k> stmtsCons(S:Stmt, SS:Stmts) => S ~> stmtNext(SS) ... </k>
  rule <k> stmtsLast(S:Stmt) => S ~> stmtEnd ... </k>

  rule <k> I:Int ~> stmtNext(SS:Stmts) => SS ... </k>
       <result> _ => I </result>

  rule <k> I:Int ~> stmtEnd => .K ... </k>
       <result> _ => I </result>

  rule <k> X:Id => I ... </k>
       <env> ... X |-> I:Int ... </env>

  rule I1:Int + I2:Int => I1 +Int I2
  rule I1:Int - I2:Int => I1 -Int I2
  rule I1:Int * I2:Int => I1 *Int I2

  rule <k> assignStmt(X:Id, I:Int) => stmtNoResult ... </k>
       <env> Rho => Rho [ X <- I ] </env>
       <result> _ => .K </result>

  rule <k> stmtNoResult ~> stmtNext(SS:Stmts) => SS ... </k>
  rule <k> stmtNoResult ~> stmtEnd => .K ... </k>
endmodule
