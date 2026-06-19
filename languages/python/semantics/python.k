requires "domains.md"

module PYTHON-SYNTAX
  imports INT-SYNTAX
  imports ID-SYNTAX
  imports STRING-SYNTAX

  syntax Val ::= Int
               | String
               | "True" [symbol(pyTrue)]
               | "False" [symbol(pyFalse)]
               | "None" [symbol(pyNone)]
               | "[" "]" [symbol(emptyListVal)]
               | "[" ValItems "]" [symbol(listVal)]
               | "(" ")" [symbol(emptyTupleVal)]
               | "(" ValItems ")" [symbol(tupleVal)]

  syntax ValItems ::= Val "," [symbol(valItemsLast)]
                    | Val "," ValItems [symbol(valItemsCons)]

  syntax Stmts ::= Stmt ";" Stmts [symbol(stmtsCons)]
                 | Stmt ";" [symbol(stmtsLast)]

  syntax Block ::= "{" "}" [symbol(emptyBlock)]
                 | "{" Stmts "}" [symbol(block)]

  syntax Stmt ::= Exp
                | "pass" [symbol(passStmt)]
                | "break" [symbol(breakStmt)]
                | "continue" [symbol(continueStmt)]
                | "assert" Exp [symbol(assertStmt), strict]
                | "global" Id [symbol(globalStmt)]
                | "del" Id [symbol(delNameStmt)]
                | Id "=" Exp [symbol(assignStmt), strict(2)]
                | Id "+=" Exp [symbol(augAddStmt)]
                | Id "-=" Exp [symbol(augSubStmt)]
                | Id "*=" Exp [symbol(augMulStmt)]
                | "#if" "(" Exp "," Block "," Block ")" [symbol(ifStmt)]
                | "#while" "(" Exp "," Block ")" [symbol(whileStmt)]

  syntax Exp ::= Val
               | Id
               | "(" Exp ")" [bracket]
               | Exp "(" Exp ")" [symbol(callExp)]
               | "#floorDiv" "(" Exp "," Exp ")" [symbol(floorDivInternal), strict]
               | "+" Exp [symbol(posExp), strict]
               | "-" Exp [symbol(negExp), strict]
               | "~" Exp [symbol(invertExp), strict]
               > Exp "**" Exp [symbol(powExp), right, strict]
               > Exp "*" Exp [symbol(mulExp), left, strict]
               | Exp "//" Exp [symbol(floorDivExp), left, strict]
               | Exp "%" Exp [symbol(modExp), left, strict]
               > Exp "+" Exp [symbol(addExp), left, strict]
               | Exp "-" Exp [symbol(subExp), left, strict]
               > Exp "<<" Exp [symbol(lshiftExp), left, strict]
               | Exp ">>" Exp [symbol(rshiftExp), left, strict]
               > Exp "&" Exp [symbol(bitAndExp), left, strict]
               > Exp "^" Exp [symbol(bitXorExp), left, strict]
               > Exp "|" Exp [symbol(bitOrExp), left, strict]
               > Exp "<" Exp [symbol(ltExp), strict]
               | Exp "<=" Exp [symbol(leExp), strict]
               | Exp ">" Exp [symbol(gtExp), strict]
               | Exp ">=" Exp [symbol(geExp), strict]
               | Exp "==" Exp [symbol(eqExp), strict]
               | Exp "!=" Exp [symbol(neExp), strict]
               | Exp "in" Exp [symbol(inExp), strict]
               | Exp "not" "in" Exp [symbol(notInExp), strict]
               | Exp "[" Exp "]" [symbol(subscriptExp), strict]
               > "not" Exp [symbol(notExp), strict]
               > Exp "and" Exp [symbol(andExp), left]
               > Exp "or" Exp [symbol(orExp), left]
               > Exp "if" Exp "else" Exp [symbol(ifExp), right]
               > "lambda" Id ":" Exp [symbol(lambdaExp)]
endmodule

module PYTHON
  imports PYTHON-SYNTAX
  imports INT
  imports BOOL
  imports STRING
  imports MAP

  syntax Val ::= closure(Id, Exp) [symbol(closure)]

  syntax KResult ::= Val
  syntax KItem ::= stmtNext(Stmts) [symbol(stmtNext)]
                 | "stmtEnd" [symbol(stmtEnd)]
                 | "stmtNoResult" [symbol(stmtNoResult)]
                 | andThen(Exp) [symbol(andThen)]
                 | orElse(Exp) [symbol(orElse)]
                 | ifThenElse(Exp, Exp) [symbol(ifThenElse)]
                 | callArg(Exp) [symbol(callArg)]
                 | callApply(Val) [symbol(callApply)]
                 | restoreEnv(Map) [symbol(restoreEnv)]
                 | ifStmtBranch(Block, Block) [symbol(ifStmtBranch)]
                 | "ifStmtDone" [symbol(ifStmtDone)]
                 | whileStmtBranch(Exp, Block) [symbol(whileStmtBranch)]
                 | whileStmtAgain(Exp, Block) [symbol(whileStmtAgain)]
                 | "breakSignal" [symbol(breakSignal)]
                 | "continueSignal" [symbol(continueSignal)]

  syntax Bool ::= truthy(Val) [function, symbol(truthy)]
                | isIntLike(Val) [function, symbol(isIntLike)]
                | valEq(Val, Val) [function, symbol(valEq)]
                | valsEq(ValItems, ValItems) [function, symbol(valsEq)]
                | containsVal(Val, ValItems) [function, symbol(containsVal)]

  syntax Int ::= intValue(Val) [function, symbol(intValue)]
               | pyFloorDiv(Int, Int) [function, symbol(pyFloorDiv)]
               | pyModulo(Int, Int) [function, symbol(pyModulo)]
  syntax Val ::= listGet(ValItems, Int) [function, symbol(listGet)]
  syntax Val ::= boolValue(Bool) [function, symbol(boolValue)]

  rule truthy(0) => false
  rule truthy(I:Int) => true requires I =/=Int 0
  rule truthy(S:String) => lengthString(S) =/=Int 0
  rule truthy(True) => true
  rule truthy(False) => false
  rule truthy(None) => false
  rule truthy([]) => false
  rule truthy(listVal(_:ValItems)) => true
  rule truthy(()) => false
  rule truthy(tupleVal(_:ValItems)) => true
  rule truthy(closure(_:Id, _:Exp)) => true

  rule isIntLike(_:Int) => true
  rule isIntLike(_:String) => false
  rule isIntLike(True) => true
  rule isIntLike(False) => true
  rule isIntLike(None) => false
  rule isIntLike([]) => false
  rule isIntLike(listVal(_:ValItems)) => false
  rule isIntLike(()) => false
  rule isIntLike(tupleVal(_:ValItems)) => false
  rule isIntLike(closure(_:Id, _:Exp)) => false

  rule intValue(I:Int) => I
  rule intValue(True) => 1
  rule intValue(False) => 0

  rule pyFloorDiv(I1:Int, I2:Int) => (I1 /Int I2) -Int 1
    requires I2 =/=Int 0
     andBool I1 %Int I2 =/=Int 0
     andBool ((I1 <Int 0 andBool I2 >Int 0) orBool (I1 >Int 0 andBool I2 <Int 0))
  rule pyFloorDiv(I1:Int, I2:Int) => I1 /Int I2
    requires I2 =/=Int 0
     andBool (I1 %Int I2 ==Int 0
       orBool notBool ((I1 <Int 0 andBool I2 >Int 0) orBool (I1 >Int 0 andBool I2 <Int 0)))

  rule pyModulo(I1:Int, I2:Int) => I1 -Int (I2 *Int pyFloorDiv(I1, I2))
    requires I2 =/=Int 0

  rule boolValue(true) => True
  rule boolValue(false) => False

  rule valEq(I1:Int, I2:Int) => I1 ==Int I2
  rule valEq(S1:String, S2:String) => S1 ==String S2
  rule valEq(_:String, _:Int) => false
  rule valEq(_:Int, _:String) => false
  rule valEq([], []) => true
  rule valEq([], listVal(_:ValItems)) => false
  rule valEq(listVal(_:ValItems), []) => false
  rule valEq(listVal(VS1:ValItems), listVal(VS2:ValItems)) => valsEq(VS1, VS2)
  rule valEq((), ()) => true
  rule valEq((), tupleVal(_:ValItems)) => false
  rule valEq(tupleVal(_:ValItems), ()) => false
  rule valEq(tupleVal(VS1:ValItems), tupleVal(VS2:ValItems)) => valsEq(VS1, VS2)
  rule valEq((), []) => false
  rule valEq([], ()) => false
  rule valEq((), listVal(_:ValItems)) => false
  rule valEq(listVal(_:ValItems), ()) => false
  rule valEq(tupleVal(_:ValItems), []) => false
  rule valEq([], tupleVal(_:ValItems)) => false
  rule valEq(tupleVal(_:ValItems), listVal(_:ValItems)) => false
  rule valEq(listVal(_:ValItems), tupleVal(_:ValItems)) => false
  rule valEq(_:String, []) => false
  rule valEq([], _:String) => false
  rule valEq(_:Int, []) => false
  rule valEq([], _:Int) => false
  rule valEq(_:String, ()) => false
  rule valEq((), _:String) => false
  rule valEq(_:Int, ()) => false
  rule valEq((), _:Int) => false
  rule valEq(_:String, tupleVal(_:ValItems)) => false
  rule valEq(tupleVal(_:ValItems), _:String) => false
  rule valEq(_:Int, tupleVal(_:ValItems)) => false
  rule valEq(tupleVal(_:ValItems), _:Int) => false
  rule valEq(_:String, listVal(_:ValItems)) => false
  rule valEq(listVal(_:ValItems), _:String) => false
  rule valEq(_:Int, listVal(_:ValItems)) => false
  rule valEq(listVal(_:ValItems), _:Int) => false
  rule valEq(True, []) => false
  rule valEq(False, []) => false
  rule valEq([], True) => false
  rule valEq([], False) => false
  rule valEq(True, listVal(_:ValItems)) => false
  rule valEq(False, listVal(_:ValItems)) => false
  rule valEq(listVal(_:ValItems), True) => false
  rule valEq(listVal(_:ValItems), False) => false
  rule valEq(True, ()) => false
  rule valEq(False, ()) => false
  rule valEq((), True) => false
  rule valEq((), False) => false
  rule valEq(True, tupleVal(_:ValItems)) => false
  rule valEq(False, tupleVal(_:ValItems)) => false
  rule valEq(tupleVal(_:ValItems), True) => false
  rule valEq(tupleVal(_:ValItems), False) => false
  rule valEq(None, []) => false
  rule valEq([], None) => false
  rule valEq(None, listVal(_:ValItems)) => false
  rule valEq(listVal(_:ValItems), None) => false
  rule valEq(None, ()) => false
  rule valEq((), None) => false
  rule valEq(None, tupleVal(_:ValItems)) => false
  rule valEq(tupleVal(_:ValItems), None) => false
  rule valEq(closure(_:Id, _:Exp), _:Int) => false
  rule valEq(_:Int, closure(_:Id, _:Exp)) => false
  rule valEq(closure(_:Id, _:Exp), _:String) => false
  rule valEq(_:String, closure(_:Id, _:Exp)) => false
  rule valEq(closure(_:Id, _:Exp), True) => false
  rule valEq(closure(_:Id, _:Exp), False) => false
  rule valEq(True, closure(_:Id, _:Exp)) => false
  rule valEq(False, closure(_:Id, _:Exp)) => false
  rule valEq(closure(_:Id, _:Exp), None) => false
  rule valEq(None, closure(_:Id, _:Exp)) => false
  rule valEq(closure(_:Id, _:Exp), []) => false
  rule valEq([], closure(_:Id, _:Exp)) => false
  rule valEq(closure(_:Id, _:Exp), listVal(_:ValItems)) => false
  rule valEq(listVal(_:ValItems), closure(_:Id, _:Exp)) => false
  rule valEq(closure(_:Id, _:Exp), ()) => false
  rule valEq((), closure(_:Id, _:Exp)) => false
  rule valEq(closure(_:Id, _:Exp), tupleVal(_:ValItems)) => false
  rule valEq(tupleVal(_:ValItems), closure(_:Id, _:Exp)) => false
  rule valEq(_:String, True) => false
  rule valEq(_:String, False) => false
  rule valEq(_:String, None) => false
  rule valEq(True, _:String) => false
  rule valEq(False, _:String) => false
  rule valEq(None, _:String) => false
  rule valEq(True, I:Int) => 1 ==Int I
  rule valEq(False, I:Int) => 0 ==Int I
  rule valEq(I:Int, True) => I ==Int 1
  rule valEq(I:Int, False) => I ==Int 0
  rule valEq(True, True) => true
  rule valEq(True, False) => false
  rule valEq(False, True) => false
  rule valEq(False, False) => true
  rule valEq(None, None) => true
  rule valEq(None, _:Int) => false
  rule valEq(_:Int, None) => false
  rule valEq(None, True) => false
  rule valEq(None, False) => false
  rule valEq(True, None) => false
  rule valEq(False, None) => false

  rule valsEq(valItemsLast(V1:Val), valItemsLast(V2:Val)) => valEq(V1, V2)
  rule valsEq(valItemsCons(V1:Val, VS1:ValItems), valItemsCons(V2:Val, VS2:ValItems)) =>
    valEq(V1, V2) andBool valsEq(VS1, VS2)
  rule valsEq(valItemsLast(_:Val), valItemsCons(_:Val, _:ValItems)) => false
  rule valsEq(valItemsCons(_:Val, _:ValItems), valItemsLast(_:Val)) => false

  rule containsVal(V:Val, valItemsLast(V1:Val)) => valEq(V, V1)
  rule containsVal(V:Val, valItemsCons(V1:Val, VS:ValItems)) =>
    valEq(V, V1) orBool containsVal(V, VS)

  rule listGet(valItemsLast(V:Val), 0) => V
  rule listGet(valItemsCons(V:Val, _:ValItems), 0) => V
  rule listGet(valItemsCons(_:Val, VS:ValItems), I:Int) => listGet(VS, I -Int 1)
    requires I >Int 0

  configuration
    <python>
      <k> $PGM:Stmts </k>
      <env> .Map </env>
      <result> .K </result>
    </python>

  rule <k> stmtsCons(S:Stmt, SS:Stmts) => S ~> stmtNext(SS) ... </k>
  rule <k> stmtsLast(S:Stmt) => S ~> stmtEnd ... </k>

  rule <k> V:Val ~> stmtNext(SS:Stmts) => SS ... </k>
       <result> _ => V </result>

  rule <k> V:Val ~> stmtEnd => .K ... </k>
       <result> _ => V </result>

  rule <k> X:Id => V ... </k>
       <env> ... X |-> V:Val ... </env>

  rule + V:Val => intValue(V) requires isIntLike(V)
  rule - V:Val => 0 -Int intValue(V) requires isIntLike(V)
  rule ~ V:Val => ~Int intValue(V) requires isIntLike(V)

  rule V1:Val + V2:Val => intValue(V1) +Int intValue(V2)
    requires isIntLike(V1) andBool isIntLike(V2)
  rule V1:Val - V2:Val => intValue(V1) -Int intValue(V2)
    requires isIntLike(V1) andBool isIntLike(V2)
  rule V1:Val * V2:Val => intValue(V1) *Int intValue(V2)
    requires isIntLike(V1) andBool isIntLike(V2)
  rule V1:Val ** V2:Val => intValue(V1) ^Int intValue(V2)
    requires isIntLike(V1) andBool isIntLike(V2) andBool intValue(V2) >=Int 0
  rule floorDivExp(V1:Val, V2:Val) => pyFloorDiv(intValue(V1), intValue(V2))
    requires isIntLike(V1) andBool isIntLike(V2) andBool intValue(V2) =/=Int 0
  rule floorDivInternal(V1:Val, V2:Val) => pyFloorDiv(intValue(V1), intValue(V2))
    requires isIntLike(V1) andBool isIntLike(V2) andBool intValue(V2) =/=Int 0
  rule V1:Val % V2:Val => pyModulo(intValue(V1), intValue(V2))
    requires isIntLike(V1) andBool isIntLike(V2) andBool intValue(V2) =/=Int 0
  rule V1:Val << V2:Val => intValue(V1) <<Int intValue(V2)
    requires isIntLike(V1) andBool isIntLike(V2) andBool intValue(V2) >=Int 0
  rule V1:Val >> V2:Val => intValue(V1) >>Int intValue(V2)
    requires isIntLike(V1) andBool isIntLike(V2) andBool intValue(V2) >=Int 0
  rule V1:Val & V2:Val => intValue(V1) &Int intValue(V2)
    requires isIntLike(V1) andBool isIntLike(V2)
  rule V1:Val ^ V2:Val => intValue(V1) xorInt intValue(V2)
    requires isIntLike(V1) andBool isIntLike(V2)
  rule V1:Val | V2:Val => intValue(V1) |Int intValue(V2)
    requires isIntLike(V1) andBool isIntLike(V2)
  rule S1:String + S2:String => S1 +String S2

  rule V1:Val < V2:Val => boolValue(intValue(V1) <Int intValue(V2))
    requires isIntLike(V1) andBool isIntLike(V2)
  rule V1:Val <= V2:Val => boolValue(intValue(V1) <=Int intValue(V2))
    requires isIntLike(V1) andBool isIntLike(V2)
  rule V1:Val > V2:Val => boolValue(intValue(V1) >Int intValue(V2))
    requires isIntLike(V1) andBool isIntLike(V2)
  rule V1:Val >= V2:Val => boolValue(intValue(V1) >=Int intValue(V2))
    requires isIntLike(V1) andBool isIntLike(V2)
  rule V1:Val == V2:Val => boolValue(valEq(V1, V2))
  rule V1:Val != V2:Val => boolValue(notBool valEq(V1, V2))
  rule _V:Val in [] => False
  rule V:Val in listVal(VS:ValItems) => boolValue(containsVal(V, VS))
  rule _V:Val in () => False
  rule V:Val in tupleVal(VS:ValItems) => boolValue(containsVal(V, VS))
  rule _V:Val not in [] => True
  rule V:Val not in listVal(VS:ValItems) => boolValue(notBool containsVal(V, VS))
  rule _V:Val not in () => True
  rule V:Val not in tupleVal(VS:ValItems) => boolValue(notBool containsVal(V, VS))
  rule subscriptExp(listVal(VS:ValItems), I:Val) => listGet(VS, intValue(I))
    requires isIntLike(I) andBool intValue(I) >=Int 0
  rule subscriptExp(tupleVal(VS:ValItems), I:Val) => listGet(VS, intValue(I))
    requires isIntLike(I) andBool intValue(I) >=Int 0

  rule not V:Val => boolValue(notBool truthy(V))

  rule <k> E1:Exp and E2:Exp => E1 ~> andThen(E2) ... </k>
  rule <k> V:Val ~> andThen(E:Exp) => E ... </k>
    requires truthy(V)
  rule <k> V:Val ~> andThen(_:Exp) => V ... </k>
    requires notBool truthy(V)

  rule <k> E1:Exp or E2:Exp => E1 ~> orElse(E2) ... </k>
  rule <k> V:Val ~> orElse(_:Exp) => V ... </k>
    requires truthy(V)
  rule <k> V:Val ~> orElse(E:Exp) => E ... </k>
    requires notBool truthy(V)

  rule <k> E1:Exp if C:Exp else E2:Exp => C ~> ifThenElse(E1, E2) ... </k>
  rule <k> V:Val ~> ifThenElse(E1:Exp, _:Exp) => E1 ... </k>
    requires truthy(V)
  rule <k> V:Val ~> ifThenElse(_:Exp, E2:Exp) => E2 ... </k>
    requires notBool truthy(V)

  rule <k> lambdaExp(X:Id, Body:Exp) => closure(X, Body) ... </k>
  rule <k> callExp(F:Exp, Arg:Exp) => F ~> callArg(Arg) ... </k>
  rule <k> F:Val ~> callArg(Arg:Exp) => Arg ~> callApply(F) ... </k>
  rule <k> A:Val ~> callApply(closure(X:Id, Body:Exp)) => Body ~> restoreEnv(Rho) ... </k>
       <env> Rho => Rho [ X <- A ] </env>
  rule <k> V:Val ~> restoreEnv(Rho:Map) => V ... </k>
       <env> _ => Rho </env>

  rule <k> assignStmt(X:Id, V:Val) => stmtNoResult ... </k>
       <env> Rho => Rho [ X <- V ] </env>
       <result> _ => .K </result>

  rule <k> augAddStmt(X:Id, E:Exp) => assignStmt(X, X + E) ... </k>
  rule <k> augSubStmt(X:Id, E:Exp) => assignStmt(X, X - E) ... </k>
  rule <k> augMulStmt(X:Id, E:Exp) => assignStmt(X, X * E) ... </k>

  rule <k> ifStmt(C:Exp, Then:Block, Else:Block) =>
           C ~> ifStmtBranch(Then, Else)
       ... </k>
  rule <k> V:Val ~> ifStmtBranch(block(SS:Stmts), _:Block) =>
           SS ~> ifStmtDone
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> ifStmtBranch({}, _:Block) =>
           stmtNoResult
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> ifStmtBranch(_:Block, block(SS:Stmts)) =>
           SS ~> ifStmtDone
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> ifStmtBranch(_:Block, {}) =>
           stmtNoResult
       ... </k>
    requires notBool truthy(V)
  rule <k> ifStmtDone => stmtNoResult ... </k>

  rule <k> whileStmt(C:Exp, Body:Block) =>
           C ~> whileStmtBranch(C, Body)
       ... </k>
  rule <k> V:Val ~> whileStmtBranch(C:Exp, block(SS:Stmts)) =>
           SS ~> whileStmtAgain(C, block(SS))
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> whileStmtBranch(C:Exp, {}) =>
           whileStmt(C, {})
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> whileStmtBranch(_:Exp, _:Block) =>
           stmtNoResult
       ... </k>
    requires notBool truthy(V)
  rule <k> whileStmtAgain(C:Exp, Body:Block) =>
           whileStmt(C, Body)
       ... </k>

  rule <k> break => breakSignal ... </k>
  rule <k> continue => continueSignal ... </k>

  rule <k> breakSignal ~> stmtNext(_:Stmts) => breakSignal ... </k>
  rule <k> continueSignal ~> stmtNext(_:Stmts) => continueSignal ... </k>
  rule <k> breakSignal ~> stmtEnd => breakSignal ... </k>
  rule <k> continueSignal ~> stmtEnd => continueSignal ... </k>
  rule <k> breakSignal ~> ifStmtDone => breakSignal ... </k>
  rule <k> continueSignal ~> ifStmtDone => continueSignal ... </k>
  rule <k> breakSignal ~> whileStmtAgain(_:Exp, _:Block) => stmtNoResult ... </k>
  rule <k> continueSignal ~> whileStmtAgain(C:Exp, Body:Block) =>
           whileStmt(C, Body)
       ... </k>

  rule <k> delNameStmt(X:Id) => stmtNoResult ... </k>
       <env> Rho => Rho [ X <- undef ] </env>
       <result> _ => .K </result>

  rule <k> pass => stmtNoResult ... </k>
  rule <k> assertStmt(V:Val) => stmtNoResult ... </k>
    requires truthy(V)
  rule <k> globalStmt(_:Id) => stmtNoResult ... </k>

  rule <k> stmtNoResult ~> stmtNext(SS:Stmts) => SS ... </k>
  rule <k> stmtNoResult ~> stmtEnd => .K ... </k>
endmodule
