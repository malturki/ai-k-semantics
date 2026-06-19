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
               | "{" "}" [symbol(emptyDictVal)]
               | "{" DictItems "}" [symbol(dictVal)]
               | "{" ValItems "}" [symbol(setVal)]

  syntax ValItems ::= Val "," [symbol(valItemsLast)]
                    | Val "," ValItems [symbol(valItemsCons)]

  syntax DictItems ::= Val ":" Val "," [symbol(dictItemsLast)]
                     | Val ":" Val "," DictItems [symbol(dictItemsCons)]

  syntax IdItems ::= "#id" "(" Id ")" [symbol(idItemsLast)]
                   | "#noIds" [symbol(noIdItems)]
                   | "#ids" "(" Id "," IdItems ")" [symbol(idItemsCons)]

  syntax ArgExps ::= "#noArgs" [symbol(noArgExps)]
                   | "#arg" "(" Exp ")" [symbol(argExp)]
                   | "#args" "(" Exp "," ArgExps ")" [symbol(argExpsCons)]

  syntax DictExps ::= "#noDictItems" [symbol(noDictExps)]
                    | "#dictItem" "(" Exp "," Exp ")" [symbol(dictExpItem)]
                    | "#dictItems" "(" Exp "," Exp "," DictExps ")" [symbol(dictExpsCons)]

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
                | Id "%=" Exp [symbol(augModStmt)]
                | Id "**=" Exp [symbol(augPowStmt)]
                | Id "<<=" Exp [symbol(augLShiftStmt)]
                | Id ">>=" Exp [symbol(augRShiftStmt)]
                | Id "&=" Exp [symbol(augBitAndStmt)]
                | Id "^=" Exp [symbol(augBitXorStmt)]
                | Id "|=" Exp [symbol(augBitOrStmt)]
                | "#floorDivAssign" "(" Id "," Exp ")" [symbol(augFloorDivStmt)]
                | "#assignMany" "(" IdItems ";" Exp ")" [symbol(assignManyStmt), strict(2)]
                | "return" Exp [symbol(returnStmt), strict]
                | "#def" "(" Id "," Id "," Block ")" [symbol(functionDefStmt)]
                | "#defArgs" "(" Id "," IdItems "," Block ")" [symbol(functionDefArgsStmt)]
                | "#if" "(" Exp "," Block "," Block ")" [symbol(ifStmt)]
                | "#while" "(" Exp "," Block ")" [symbol(whileStmt)]
                | "#for" "(" Id "," Exp "," Block ")" [symbol(forStmt)]

  syntax Exp ::= Val
               | Id
               | "(" Exp ")" [bracket]
               | Exp "(" Exp ")" [symbol(callExp)]
               | "#call" "(" Exp "," ArgExps ")" [symbol(callArgsExp)]
               | "#list" "(" ArgExps ")" [symbol(listDisplayExp)]
               | "#tuple" "(" ArgExps ")" [symbol(tupleDisplayExp)]
               | "#dict" "(" DictExps ")" [symbol(dictDisplayExp)]
               | "#set" "(" ArgExps ")" [symbol(setDisplayExp)]
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
               | "#range" "(" Exp ")" [symbol(range1Exp), strict]
               | "#range" "(" Exp "," Exp ")" [symbol(range2Exp), strict]
               > "not" Exp [symbol(notExp), strict]
               > Exp "and" Exp [symbol(andExp), left]
               > Exp "or" Exp [symbol(orExp), left]
               > Exp "if" Exp "else" Exp [symbol(ifExp), right]
               > "lambda" Id ":" Exp [symbol(lambdaExp)]
               | "#lambdaArgs" "(" IdItems "," Exp ")" [symbol(lambdaArgsExp)]
endmodule

module PYTHON
  imports PYTHON-SYNTAX
  imports INT
  imports BOOL
  imports STRING
  imports MAP

  syntax Val ::= closure(Id, Exp) [symbol(closure)]
               | closureArgs(IdItems, Exp) [symbol(closureArgs)]
               | functionVal(Id, Block) [symbol(functionVal)]
               | functionValArgs(IdItems, Block) [symbol(functionValArgs)]
               | rangeVal(Int, Int) [symbol(rangeVal)]
               | argsVal(ArgVals) [symbol(argsVal)]
               | dictArgsVal(DictVals) [symbol(dictArgsVal)]

  syntax KResult ::= Val
  syntax KItem ::= stmtNext(Stmts) [symbol(stmtNext)]
                 | "stmtEnd" [symbol(stmtEnd)]
                 | "stmtNoResult" [symbol(stmtNoResult)]
                 | andThen(Exp) [symbol(andThen)]
                 | orElse(Exp) [symbol(orElse)]
                 | ifThenElse(Exp, Exp) [symbol(ifThenElse)]
                 | callArg(Exp) [symbol(callArg)]
                 | callApply(Val) [symbol(callApply)]
                 | callArgs(ArgExps) [symbol(callArgs)]
                 | evalArgs(ArgExps, ArgVals) [symbol(evalArgs)]
                 | evalArgNext(ArgExps, ArgVals) [symbol(evalArgNext)]
                 | callApplyArgs(Val) [symbol(callApplyArgs)]
                 | "buildList" [symbol(buildList)]
                 | "buildTuple" [symbol(buildTuple)]
                 | "buildSet" [symbol(buildSet)]
                 | evalDict(DictExps, DictVals) [symbol(evalDict)]
                 | evalDictValue(Exp, DictExps, DictVals) [symbol(evalDictValue)]
                 | evalDictNext(DictExps, DictVals, Val) [symbol(evalDictNext)]
                 | "buildDict" [symbol(buildDict)]
                 | restoreEnv(Map) [symbol(restoreEnv)]
                 | ifStmtBranch(Block, Block) [symbol(ifStmtBranch)]
                 | "ifStmtDone" [symbol(ifStmtDone)]
                 | whileStmtBranch(Exp, Block) [symbol(whileStmtBranch)]
                 | whileStmtAgain(Exp, Block) [symbol(whileStmtAgain)]
                 | forIter(Id, Block) [symbol(forIter)]
                 | forItems(Id, ValItems, Block) [symbol(forItems)]
                 | forRange(Id, Int, Int, Block) [symbol(forRange)]
                 | forRangeAgain(Id, Int, Int, Block) [symbol(forRangeAgain)]
                 | "forDone" [symbol(forDone)]
                 | "breakSignal" [symbol(breakSignal)]
                 | "continueSignal" [symbol(continueSignal)]
                 | returnSignal(Val) [symbol(returnSignal)]
                 | functionDone(Map) [symbol(functionDone)]
                 | assignMany(IdItems, Val) [symbol(assignMany)]

  syntax Bool ::= truthy(Val) [function, symbol(truthy)]
                | isIntLike(Val) [function, symbol(isIntLike)]
                | valEq(Val, Val) [function, symbol(valEq)]
                | valsEq(ValItems, ValItems) [function, symbol(valsEq)]
                | sameArity(IdItems, ArgVals) [function, symbol(sameArity)]
                | emptyArgVals(ArgVals) [function, symbol(emptyArgVals)]
                | emptyDictVals(DictVals) [function, symbol(emptyDictVals)]
                | containsVal(Val, ValItems) [function, symbol(containsVal)]
                | containsKey(Val, DictItems) [function, symbol(containsKey)]

  syntax Int ::= intValue(Val) [function, symbol(intValue)]
               | pyFloorDiv(Int, Int) [function, symbol(pyFloorDiv)]
               | pyModulo(Int, Int) [function, symbol(pyModulo)]
  syntax ArgVals ::= "#noArgVals" [symbol(noArgVals)]
                   | argValsCons(Val, ArgVals) [symbol(argValsCons)]
                   | appendArgVal(ArgVals, Val) [function, symbol(appendArgVal)]
  syntax DictVals ::= "#noDictVals" [symbol(noDictVals)]
                    | dictValsCons(Val, Val, DictVals) [symbol(dictValsCons)]
                    | appendDictVal(DictVals, Val, Val) [function, symbol(appendDictVal)]
  syntax Map ::= bindArgs(Map, IdItems, ArgVals) [function, symbol(bindArgs)]
  syntax ValItems ::= argValsToValItems(ArgVals) [function, symbol(argValsToValItems)]
  syntax DictItems ::= dictValsToDictItems(DictVals) [function, symbol(dictValsToDictItems)]
  syntax Val ::= listGet(ValItems, Int) [function, symbol(listGet)]
  syntax Val ::= dictGet(DictItems, Val) [function, symbol(dictGet)]
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
  rule truthy({}) => false
  rule truthy(dictVal(_:DictItems)) => true
  rule truthy(setVal(_:ValItems)) => true
  rule truthy(closure(_:Id, _:Exp)) => true
  rule truthy(closureArgs(_:IdItems, _:Exp)) => true
  rule truthy(functionVal(_:Id, _:Block)) => true
  rule truthy(functionValArgs(_:IdItems, _:Block)) => true
  rule truthy(rangeVal(Start:Int, Stop:Int)) => Start <Int Stop
  rule truthy(argsVal(_:ArgVals)) => true
  rule truthy(dictArgsVal(_:DictVals)) => true

  rule isIntLike(_:Int) => true
  rule isIntLike(_:String) => false
  rule isIntLike(True) => true
  rule isIntLike(False) => true
  rule isIntLike(None) => false
  rule isIntLike([]) => false
  rule isIntLike(listVal(_:ValItems)) => false
  rule isIntLike(()) => false
  rule isIntLike(tupleVal(_:ValItems)) => false
  rule isIntLike({}) => false
  rule isIntLike(dictVal(_:DictItems)) => false
  rule isIntLike(setVal(_:ValItems)) => false
  rule isIntLike(closure(_:Id, _:Exp)) => false
  rule isIntLike(closureArgs(_:IdItems, _:Exp)) => false
  rule isIntLike(functionVal(_:Id, _:Block)) => false
  rule isIntLike(functionValArgs(_:IdItems, _:Block)) => false
  rule isIntLike(rangeVal(_:Int, _:Int)) => false
  rule isIntLike(argsVal(_:ArgVals)) => false
  rule isIntLike(dictArgsVal(_:DictVals)) => false

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

  rule sameArity(#noIds, #noArgVals) => true
  rule sameArity(#noIds, argValsCons(_:Val, _:ArgVals)) => false
  rule sameArity(idItemsLast(_:Id), #noArgVals) => false
  rule sameArity(idItemsLast(_:Id), argValsCons(_:Val, #noArgVals)) => true
  rule sameArity(idItemsLast(_:Id), argValsCons(_:Val, argValsCons(_:Val, _:ArgVals))) => false
  rule sameArity(idItemsCons(_:Id, _:IdItems), #noArgVals) => false
  rule sameArity(idItemsCons(_:Id, IDS:IdItems), argValsCons(_:Val, VS:ArgVals)) => sameArity(IDS, VS)

  rule emptyArgVals(#noArgVals) => true
  rule emptyArgVals(argValsCons(_:Val, _:ArgVals)) => false

  rule emptyDictVals(#noDictVals) => true
  rule emptyDictVals(dictValsCons(_:Val, _:Val, _:DictVals)) => false

  rule appendArgVal(#noArgVals, V:Val) => argValsCons(V, #noArgVals)
  rule appendArgVal(argValsCons(V0:Val, VS:ArgVals), V:Val) =>
    argValsCons(V0, appendArgVal(VS, V))

  rule appendDictVal(#noDictVals, K:Val, V:Val) => dictValsCons(K, V, #noDictVals)
  rule appendDictVal(dictValsCons(K0:Val, V0:Val, DVS:DictVals), K:Val, V:Val) =>
    dictValsCons(K0, V0, appendDictVal(DVS, K, V))

  rule bindArgs(Rho:Map, #noIds, #noArgVals) => Rho
  rule bindArgs(Rho:Map, idItemsLast(X:Id), argValsCons(V:Val, #noArgVals)) => Rho [ X <- V ]
  rule bindArgs(Rho:Map, idItemsCons(X:Id, IDS:IdItems), argValsCons(V:Val, VS:ArgVals)) =>
    bindArgs(Rho [ X <- V ], IDS, VS)

  rule argValsToValItems(argValsCons(V:Val, #noArgVals)) => valItemsLast(V)
  rule argValsToValItems(argValsCons(V:Val, VS:ArgVals)) =>
    valItemsCons(V, argValsToValItems(VS))
    requires notBool emptyArgVals(VS)

  rule dictValsToDictItems(dictValsCons(K:Val, V:Val, #noDictVals)) => dictItemsLast(K, V)
  rule dictValsToDictItems(dictValsCons(K:Val, V:Val, DVS:DictVals)) =>
    dictItemsCons(K, V, dictValsToDictItems(DVS))
    requires notBool emptyDictVals(DVS)

  rule valsEq(valItemsLast(V1:Val), valItemsLast(V2:Val)) => valEq(V1, V2)
  rule valsEq(valItemsCons(V1:Val, VS1:ValItems), valItemsCons(V2:Val, VS2:ValItems)) =>
    valEq(V1, V2) andBool valsEq(VS1, VS2)
  rule valsEq(valItemsLast(_:Val), valItemsCons(_:Val, _:ValItems)) => false
  rule valsEq(valItemsCons(_:Val, _:ValItems), valItemsLast(_:Val)) => false

  rule containsVal(V:Val, valItemsLast(V1:Val)) => valEq(V, V1)
  rule containsVal(V:Val, valItemsCons(V1:Val, VS:ValItems)) =>
    valEq(V, V1) orBool containsVal(V, VS)

  rule containsKey(K:Val, dictItemsLast(K1:Val, _:Val)) => valEq(K, K1)
  rule containsKey(K:Val, dictItemsCons(K1:Val, _:Val, DS:DictItems)) =>
    valEq(K, K1) orBool containsKey(K, DS)

  rule listGet(valItemsLast(V:Val), 0) => V
  rule listGet(valItemsCons(V:Val, _:ValItems), 0) => V
  rule listGet(valItemsCons(_:Val, VS:ValItems), I:Int) => listGet(VS, I -Int 1)
    requires I >Int 0

  rule dictGet(dictItemsLast(K1:Val, V:Val), K:Val) => V
    requires valEq(K, K1)
  rule dictGet(dictItemsCons(K1:Val, V:Val, _:DictItems), K:Val) => V
    requires valEq(K, K1)
  rule dictGet(dictItemsCons(K1:Val, _:Val, DS:DictItems), K:Val) => dictGet(DS, K)
    requires notBool valEq(K, K1)

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
  rule _V:Val in {} => False
  rule V:Val in dictVal(DS:DictItems) => boolValue(containsKey(V, DS))
  rule V:Val in setVal(VS:ValItems) => boolValue(containsVal(V, VS))
  rule _V:Val not in [] => True
  rule V:Val not in listVal(VS:ValItems) => boolValue(notBool containsVal(V, VS))
  rule _V:Val not in () => True
  rule V:Val not in tupleVal(VS:ValItems) => boolValue(notBool containsVal(V, VS))
  rule _V:Val not in {} => True
  rule V:Val not in dictVal(DS:DictItems) => boolValue(notBool containsKey(V, DS))
  rule V:Val not in setVal(VS:ValItems) => boolValue(notBool containsVal(V, VS))
  rule subscriptExp(listVal(VS:ValItems), I:Val) => listGet(VS, intValue(I))
    requires isIntLike(I) andBool intValue(I) >=Int 0
  rule subscriptExp(tupleVal(VS:ValItems), I:Val) => listGet(VS, intValue(I))
    requires isIntLike(I) andBool intValue(I) >=Int 0
  rule subscriptExp(dictVal(DS:DictItems), K:Val) => dictGet(DS, K)
    requires containsKey(K, DS)

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
  rule <k> lambdaArgsExp(IDS:IdItems, Body:Exp) => closureArgs(IDS, Body) ... </k>
  rule <k> callExp(F:Exp, Arg:Exp) => F ~> callArg(Arg) ... </k>
  rule <k> F:Val ~> callArg(Arg:Exp) => Arg ~> callApply(F) ... </k>
  rule <k> A:Val ~> callApply(closure(X:Id, Body:Exp)) => Body ~> restoreEnv(Rho) ... </k>
       <env> Rho => Rho [ X <- A ] </env>
  rule <k> A:Val ~> callApply(functionVal(X:Id, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => Rho [ X <- A ] </env>
  rule <k> A:Val ~> callApply(functionVal(X:Id, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => Rho [ X <- A ] </env>
  rule <k> V:Val ~> restoreEnv(Rho:Map) => V ... </k>
       <env> _ => Rho </env>

  rule <k> callArgsExp(F:Exp, Args:ArgExps) => F ~> callArgs(Args) ... </k>
  rule <k> F:Val ~> callArgs(Args:ArgExps) =>
           evalArgs(Args, #noArgVals) ~> callApplyArgs(F)
       ... </k>
  rule <k> evalArgs(#noArgs, VS:ArgVals) => argsVal(VS) ... </k>
  rule <k> evalArgs(argExp(E:Exp), VS:ArgVals) =>
           E ~> evalArgNext(#noArgs, VS)
       ... </k>
  rule <k> evalArgs(argExpsCons(E:Exp, ES:ArgExps), VS:ArgVals) =>
           E ~> evalArgNext(ES, VS)
       ... </k>
  rule <k> V:Val ~> evalArgNext(ES:ArgExps, VS:ArgVals) =>
           evalArgs(ES, appendArgVal(VS, V))
       ... </k>
  rule <k> argsVal(VS:ArgVals) ~> callApplyArgs(closureArgs(IDS:IdItems, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, VS) </env>
    requires sameArity(IDS, VS)
  rule <k> argsVal(VS:ArgVals) ~> callApplyArgs(functionValArgs(IDS:IdItems, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, VS) </env>
    requires sameArity(IDS, VS)
  rule <k> argsVal(VS:ArgVals) ~> callApplyArgs(functionValArgs(IDS:IdItems, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, VS) </env>
    requires sameArity(IDS, VS)

  rule <k> listDisplayExp(Args:ArgExps) => evalArgs(Args, #noArgVals) ~> buildList ... </k>
  rule <k> argsVal(#noArgVals) ~> buildList => [] ... </k>
  rule <k> argsVal(VS:ArgVals) ~> buildList => listVal(argValsToValItems(VS)) ... </k>
    requires notBool emptyArgVals(VS)

  rule <k> tupleDisplayExp(Args:ArgExps) => evalArgs(Args, #noArgVals) ~> buildTuple ... </k>
  rule <k> argsVal(#noArgVals) ~> buildTuple => () ... </k>
  rule <k> argsVal(VS:ArgVals) ~> buildTuple => tupleVal(argValsToValItems(VS)) ... </k>
    requires notBool emptyArgVals(VS)

  rule <k> setDisplayExp(Args:ArgExps) => evalArgs(Args, #noArgVals) ~> buildSet ... </k>
  rule <k> argsVal(VS:ArgVals) ~> buildSet => setVal(argValsToValItems(VS)) ... </k>
    requires notBool emptyArgVals(VS)

  rule <k> dictDisplayExp(Items:DictExps) => evalDict(Items, #noDictVals) ~> buildDict ... </k>
  rule <k> evalDict(#noDictItems, DVS:DictVals) => dictArgsVal(DVS) ... </k>
  rule <k> evalDict(dictExpItem(K:Exp, V:Exp), DVS:DictVals) =>
           K ~> evalDictValue(V, #noDictItems, DVS)
       ... </k>
  rule <k> evalDict(dictExpsCons(K:Exp, V:Exp, Rest:DictExps), DVS:DictVals) =>
           K ~> evalDictValue(V, Rest, DVS)
       ... </k>
  rule <k> K:Val ~> evalDictValue(V:Exp, Rest:DictExps, DVS:DictVals) =>
           V ~> evalDictNext(Rest, DVS, K)
       ... </k>
  rule <k> V:Val ~> evalDictNext(Rest:DictExps, DVS:DictVals, K:Val) =>
           evalDict(Rest, appendDictVal(DVS, K, V))
       ... </k>
  rule <k> dictArgsVal(#noDictVals) ~> buildDict => ({}):Val ... </k>
  rule <k> dictArgsVal(DVS:DictVals) ~> buildDict => dictVal(dictValsToDictItems(DVS)) ... </k>
    requires notBool emptyDictVals(DVS)

  rule range1Exp(N:Val) => rangeVal(0, intValue(N))
    requires isIntLike(N)
  rule range2Exp(Start:Val, Stop:Val) => rangeVal(intValue(Start), intValue(Stop))
    requires isIntLike(Start) andBool isIntLike(Stop)

  rule <k> assignStmt(X:Id, V:Val) => stmtNoResult ... </k>
       <env> Rho => Rho [ X <- V ] </env>
       <result> _ => .K </result>

  rule <k> augAddStmt(X:Id, E:Exp) => assignStmt(X, X + E) ... </k>
  rule <k> augSubStmt(X:Id, E:Exp) => assignStmt(X, X - E) ... </k>
  rule <k> augMulStmt(X:Id, E:Exp) => assignStmt(X, X * E) ... </k>
  rule <k> augModStmt(X:Id, E:Exp) => assignStmt(X, X % E) ... </k>
  rule <k> augPowStmt(X:Id, E:Exp) => assignStmt(X, X ** E) ... </k>
  rule <k> augLShiftStmt(X:Id, E:Exp) => assignStmt(X, X << E) ... </k>
  rule <k> augRShiftStmt(X:Id, E:Exp) => assignStmt(X, X >> E) ... </k>
  rule <k> augBitAndStmt(X:Id, E:Exp) => assignStmt(X, X & E) ... </k>
  rule <k> augBitXorStmt(X:Id, E:Exp) => assignStmt(X, X ^ E) ... </k>
  rule <k> augBitOrStmt(X:Id, E:Exp) => assignStmt(X, X | E) ... </k>
  rule <k> augFloorDivStmt(X:Id, E:Exp) => assignStmt(X, #floorDiv(X, E)) ... </k>

  rule <k> assignManyStmt(IDS:IdItems, V:Val) => assignMany(IDS, V) ... </k>
  rule <k> assignMany(idItemsLast(X:Id), V:Val) => stmtNoResult ... </k>
       <env> Rho => Rho [ X <- V ] </env>
       <result> _ => .K </result>
  rule <k> assignMany(idItemsCons(X:Id, IDS:IdItems), V:Val) => assignMany(IDS, V) ... </k>
       <env> Rho => Rho [ X <- V ] </env>
       <result> _ => .K </result>

  rule <k> functionDefStmt(F:Id, X:Id, Body:Block) => stmtNoResult ... </k>
       <env> Rho => Rho [ F <- functionVal(X, Body) ] </env>
       <result> _ => .K </result>
  rule <k> functionDefArgsStmt(F:Id, IDS:IdItems, Body:Block) => stmtNoResult ... </k>
       <env> Rho => Rho [ F <- functionValArgs(IDS, Body) ] </env>
       <result> _ => .K </result>

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

  rule <k> forStmt(X:Id, E:Exp, Body:Block) =>
           E ~> forIter(X, Body)
       ... </k>
  rule <k> [] ~> forIter(_:Id, _:Block) => stmtNoResult ... </k>
  rule <k> listVal(VS:ValItems) ~> forIter(X:Id, Body:Block) =>
           forItems(X, VS, Body)
       ... </k>
  rule <k> () ~> forIter(_:Id, _:Block) => stmtNoResult ... </k>
  rule <k> tupleVal(VS:ValItems) ~> forIter(X:Id, Body:Block) =>
           forItems(X, VS, Body)
       ... </k>
  rule <k> rangeVal(Start:Int, Stop:Int) ~> forIter(X:Id, Body:Block) =>
           forRange(X, Start, Stop, Body)
       ... </k>

  rule <k> forItems(X:Id, valItemsCons(V:Val, VS:ValItems), block(SS:Stmts)) =>
           SS ~> forItems(X, VS, block(SS))
       ... </k>
       <env> Rho => Rho [ X <- V ] </env>
  rule <k> forItems(X:Id, valItemsLast(V:Val), block(SS:Stmts)) =>
           SS ~> forDone
       ... </k>
       <env> Rho => Rho [ X <- V ] </env>
  rule <k> forItems(X:Id, valItemsCons(V:Val, VS:ValItems), {}) =>
           forItems(X, VS, {})
       ... </k>
       <env> Rho => Rho [ X <- V ] </env>
  rule <k> forItems(X:Id, valItemsLast(V:Val), {}) =>
           stmtNoResult
       ... </k>
       <env> Rho => Rho [ X <- V ] </env>
  rule <k> forDone => stmtNoResult ... </k>

  rule <k> forRange(X:Id, I:Int, Stop:Int, block(SS:Stmts)) =>
           SS ~> forRangeAgain(X, I +Int 1, Stop, block(SS))
       ... </k>
       <env> Rho => Rho [ X <- I ] </env>
    requires I <Int Stop
  rule <k> forRange(X:Id, I:Int, Stop:Int, {}) =>
           forRange(X, I +Int 1, Stop, {})
       ... </k>
       <env> Rho => Rho [ X <- I ] </env>
    requires I <Int Stop
  rule <k> forRange(_:Id, I:Int, Stop:Int, _:Block) => stmtNoResult ... </k>
    requires I >=Int Stop
  rule <k> forRangeAgain(X:Id, I:Int, Stop:Int, Body:Block) =>
           forRange(X, I, Stop, Body)
       ... </k>

  rule <k> break => breakSignal ... </k>
  rule <k> continue => continueSignal ... </k>
  rule <k> returnStmt(V:Val) => returnSignal(V) ... </k>

  rule <k> breakSignal ~> stmtNext(_:Stmts) => breakSignal ... </k>
  rule <k> continueSignal ~> stmtNext(_:Stmts) => continueSignal ... </k>
  rule <k> returnSignal(V:Val) ~> stmtNext(_:Stmts) => returnSignal(V) ... </k>
  rule <k> breakSignal ~> stmtEnd => breakSignal ... </k>
  rule <k> continueSignal ~> stmtEnd => continueSignal ... </k>
  rule <k> returnSignal(V:Val) ~> stmtEnd => returnSignal(V) ... </k>
  rule <k> breakSignal ~> ifStmtDone => breakSignal ... </k>
  rule <k> continueSignal ~> ifStmtDone => continueSignal ... </k>
  rule <k> returnSignal(V:Val) ~> ifStmtDone => returnSignal(V) ... </k>
  rule <k> breakSignal ~> whileStmtAgain(_:Exp, _:Block) => stmtNoResult ... </k>
  rule <k> continueSignal ~> whileStmtAgain(C:Exp, Body:Block) =>
           whileStmt(C, Body)
       ... </k>
  rule <k> returnSignal(V:Val) ~> whileStmtAgain(_:Exp, _:Block) => returnSignal(V) ... </k>
  rule <k> breakSignal ~> forItems(_:Id, _:ValItems, _:Block) => stmtNoResult ... </k>
  rule <k> breakSignal ~> forDone => stmtNoResult ... </k>
  rule <k> continueSignal ~> forItems(X:Id, VS:ValItems, Body:Block) =>
           forItems(X, VS, Body)
       ... </k>
  rule <k> continueSignal ~> forDone => stmtNoResult ... </k>
  rule <k> returnSignal(V:Val) ~> forItems(_:Id, _:ValItems, _:Block) => returnSignal(V) ... </k>
  rule <k> returnSignal(V:Val) ~> forDone => returnSignal(V) ... </k>
  rule <k> breakSignal ~> forRangeAgain(_:Id, _:Int, _:Int, _:Block) => stmtNoResult ... </k>
  rule <k> continueSignal ~> forRangeAgain(X:Id, I:Int, Stop:Int, Body:Block) =>
           forRange(X, I, Stop, Body)
       ... </k>
  rule <k> returnSignal(V:Val) ~> forRangeAgain(_:Id, _:Int, _:Int, _:Block) => returnSignal(V) ... </k>
  rule <k> returnSignal(V:Val) ~> functionDone(Rho:Map) => V ~> restoreEnv(Rho) ... </k>
  rule <k> functionDone(Rho:Map) => None ~> restoreEnv(Rho) ... </k>

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
