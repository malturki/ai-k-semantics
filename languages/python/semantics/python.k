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
               | "set" "(" ")" [symbol(emptySetVal)]
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

  syntax CmpOp ::= "#lt" [symbol(cmpLt)]
                 | "#le" [symbol(cmpLe)]
                 | "#gt" [symbol(cmpGt)]
                 | "#ge" [symbol(cmpGe)]
                 | "#eq" [symbol(cmpEq)]
                 | "#ne" [symbol(cmpNe)]
                 | "#is" [symbol(cmpIs)]
                 | "#isNot" [symbol(cmpIsNot)]
                 | "#in" [symbol(cmpIn)]
                 | "#notIn" [symbol(cmpNotIn)]

  syntax CmpChain ::= "#cmpLast" "(" CmpOp "," Exp ")" [symbol(cmpChainLast)]
                    | "#cmpCons" "(" CmpOp "," Exp "," CmpChain ")" [symbol(cmpChainCons)]

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
                | "#unpackAssign" "(" IdItems ";" Exp ")" [symbol(unpackAssignStmt), strict(2)]
                | "#unpackStarAssign" "(" IdItems ";" Id ";" IdItems ";" Exp ")" [symbol(unpackStarAssignStmt), strict(4)]
                | "return" Exp [symbol(returnStmt), strict]
                | "#def" "(" Id "," Id "," Block ")" [symbol(functionDefStmt)]
                | "#defArgs" "(" Id "," IdItems "," Block ")" [symbol(functionDefArgsStmt)]
                | "#if" "(" Exp "," Block "," Block ")" [symbol(ifStmt)]
                | "#while" "(" Exp "," Block ")" [symbol(whileStmt)]
                | "#whileElse" "(" Exp "," Block "," Block ")" [symbol(whileElseStmt)]
                | "#for" "(" Id "," Exp "," Block ")" [symbol(forStmt)]
                | "#forElse" "(" Id "," Exp "," Block "," Block ")" [symbol(forElseStmt)]
                | "#forUnpack" "(" IdItems "," Exp "," Block ")" [symbol(forUnpackStmt)]
                | "#forUnpackElse" "(" IdItems "," Exp "," Block "," Block ")" [symbol(forUnpackElseStmt)]

  syntax Exp ::= Val
               | Id
               | "#namedExpr" "(" Id "," Exp ")" [symbol(namedExprExp), strict(2)]
               | "(" Exp ")" [bracket]
               | Exp "(" Exp ")" [symbol(callExp)]
               | "#call" "(" Exp "," ArgExps ")" [symbol(callArgsExp)]
               | "#list" "(" ArgExps ")" [symbol(listDisplayExp)]
               | "#tuple" "(" ArgExps ")" [symbol(tupleDisplayExp)]
               | "#dict" "(" DictExps ")" [symbol(dictDisplayExp)]
               | "#set" "(" ArgExps ")" [symbol(setDisplayExp)]
               | "#listCtor" "(" ")" [symbol(listCtorExp)]
               | "#listCtor" "(" Exp ")" [symbol(listCtor1Exp), strict]
               | "#tupleCtor" "(" ")" [symbol(tupleCtorExp)]
               | "#tupleCtor" "(" Exp ")" [symbol(tupleCtor1Exp), strict]
               | "#dictCtor" "(" ")" [symbol(dictCtorExp)]
               | "#setCtor" "(" ")" [symbol(setCtorExp)]
               | "#boolCtor" "(" ")" [symbol(boolCtor0Exp)]
               | "#boolCtor" "(" Exp ")" [symbol(boolCtor1Exp), strict]
               | "#all" "(" Exp ")" [symbol(allExp), strict]
               | "#any" "(" Exp ")" [symbol(anyExp), strict]
               | "#sum" "(" Exp ")" [symbol(sum1Exp), strict]
               | "#sum" "(" Exp "," Exp ")" [symbol(sum2Exp), strict]
               | "#min" "(" Exp ")" [symbol(minExp), strict]
               | "#max" "(" Exp ")" [symbol(maxExp), strict]
               | "#intCtor" "(" ")" [symbol(intCtor0Exp)]
               | "#intCtor" "(" Exp ")" [symbol(intCtor1Exp), strict]
               | "#abs" "(" Exp ")" [symbol(absExp), strict]
               | "#divmod" "(" Exp "," Exp ")" [symbol(divmodExp), strict]
               | "#pow" "(" Exp "," Exp ")" [symbol(powBuiltinExp), strict]
               | "#compareChain" "(" Exp "," CmpChain ")" [symbol(compareChainExp)]
               | "#len" "(" Exp ")" [symbol(lenExp), strict]
               | "#floorDiv" "(" Exp "," Exp ")" [symbol(floorDivInternal), strict]
               | "#slice" "(" Exp "," Exp "," Exp ")" [symbol(sliceExp), strict]
               | "#sliceStep" "(" Exp "," Exp "," Exp "," Exp ")" [symbol(sliceStepExp), strict]
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
               | Exp "is" Exp [symbol(identityExp), strict]
               | Exp "is" "not" Exp [symbol(identityNotExp), strict]
               | Exp "in" Exp [symbol(inExp), strict]
               | Exp "not" "in" Exp [symbol(notInExp), strict]
               | Exp "[" Exp "]" [symbol(subscriptExp), strict]
               | "#range" "(" Exp ")" [symbol(range1Exp), strict]
               | "#range" "(" Exp "," Exp ")" [symbol(range2Exp), strict]
               | "#range" "(" Exp "," Exp "," Exp ")" [symbol(range3Exp), strict]
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
               | rangeVal(Int, Int, Int) [symbol(rangeValStep)]
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
                 | compareChain(CmpChain) [symbol(compareChain)]
                 | compareChainLast(CmpOp, Val) [symbol(compareChainLast)]
                 | compareChainNext(CmpOp, Val, CmpChain) [symbol(compareChainNext)]
                 | compareFrom(Val, CmpChain) [symbol(compareFrom)]
                 | restoreEnv(Map) [symbol(restoreEnv)]
                 | ifStmtBranch(Block, Block) [symbol(ifStmtBranch)]
                 | "ifStmtDone" [symbol(ifStmtDone)]
                 | whileStmtBranch(Exp, Block) [symbol(whileStmtBranch)]
                 | whileStmtAgain(Exp, Block) [symbol(whileStmtAgain)]
                 | whileElseStmtBranch(Exp, Block, Block) [symbol(whileElseStmtBranch)]
                 | whileElseStmtAgain(Exp, Block, Block) [symbol(whileElseStmtAgain)]
                 | forIter(Id, Block) [symbol(forIter)]
                 | forItems(Id, ValItems, Block) [symbol(forItems)]
                 | forUnpackIter(IdItems, Block) [symbol(forUnpackIter)]
                 | forUnpackItems(IdItems, ValItems, Block) [symbol(forUnpackItems)]
                 | forRange(Id, Int, Int, Block) [symbol(forRange)]
                 | forRangeAgain(Id, Int, Int, Block) [symbol(forRangeAgain)]
                 | forRangeStep(Id, Int, Int, Int, Block) [symbol(forRangeStep)]
                 | forRangeStepAgain(Id, Int, Int, Int, Block) [symbol(forRangeStepAgain)]
                 | forElseIter(Id, Block, Block) [symbol(forElseIter)]
                 | forElseItems(Id, ValItems, Block, Block) [symbol(forElseItems)]
                 | forElseDone(Block) [symbol(forElseDone)]
                 | forUnpackElseIter(IdItems, Block, Block) [symbol(forUnpackElseIter)]
                 | forUnpackElseItems(IdItems, ValItems, Block, Block) [symbol(forUnpackElseItems)]
                 | forUnpackElseDone(Block) [symbol(forUnpackElseDone)]
                 | forElseRange(Id, Int, Int, Block, Block) [symbol(forElseRange)]
                 | forElseRangeAgain(Id, Int, Int, Block, Block) [symbol(forElseRangeAgain)]
                 | forElseRangeStep(Id, Int, Int, Int, Block, Block) [symbol(forElseRangeStep)]
                 | forElseRangeStepAgain(Id, Int, Int, Int, Block, Block) [symbol(forElseRangeStepAgain)]
                 | runLoopElse(Block) [symbol(runLoopElse)]
                 | "forDone" [symbol(forDone)]
                 | "breakSignal" [symbol(breakSignal)]
                 | "continueSignal" [symbol(continueSignal)]
                 | returnSignal(Val) [symbol(returnSignal)]
                 | functionDone(Map) [symbol(functionDone)]
                 | assignMany(IdItems, Val) [symbol(assignMany)]

  syntax Bool ::= truthy(Val) [function, symbol(truthy)]
                | isIntLike(Val) [function, symbol(isIntLike)]
                | valEq(Val, Val) [function, symbol(valEq)]
                | valIs(Val, Val) [function, symbol(valIs)]
                | cmpHolds(CmpOp, Val, Val) [function, symbol(cmpHolds)]
                | singletonIdentity(Val) [function, symbol(singletonIdentity)]
                | valsEq(ValItems, ValItems) [function, symbol(valsEq)]
                | valItemsLt(ValItems, ValItems) [function, symbol(valItemsLt)]
                | isListSequence(Val) [function, symbol(isListSequence)]
                | isTupleSequence(Val) [function, symbol(isTupleSequence)]
                | seqOrderComparable(Val, Val) [function, symbol(seqOrderComparable)]
                | seqLt(Val, Val) [function, symbol(seqLt)]
                | dictsEq(DictItems, DictItems) [function, symbol(dictsEq)]
                | dictItemsContained(DictItems, DictItems) [function, symbol(dictItemsContained)]
                | containsDictPair(Val, Val, DictItems) [function, symbol(containsDictPair)]
                | setsEq(ValItems, ValItems) [function, symbol(setsEq)]
                | setItemsSubset(ValItems, ValItems) [function, symbol(setItemsSubset)]
                | sameArity(IdItems, ArgVals) [function, symbol(sameArity)]
                | sameIdValArity(IdItems, ValItems) [function, symbol(sameIdValArity)]
                | starUnpackArityOk(IdItems, IdItems, Int) [function, symbol(starUnpackArityOk)]
                | emptyArgVals(ArgVals) [function, symbol(emptyArgVals)]
                | emptyDictVals(DictVals) [function, symbol(emptyDictVals)]
                | containsVal(Val, ValItems) [function, symbol(containsVal)]
                | containsKey(Val, DictItems) [function, symbol(containsKey)]
                | rangeContains(Val, Int, Int) [function, symbol(rangeContains)]
                | rangeContains(Val, Int, Int, Int) [function, symbol(rangeContainsStep)]
                | rangeEq(Int, Int, Int, Int, Int, Int) [function, symbol(rangeEq)]
                | allValItems(ValItems) [function, symbol(allValItems)]
                | anyValItems(ValItems) [function, symbol(anyValItems)]
                | valItemsAllIntLike(ValItems) [function, symbol(valItemsAllIntLike)]
                | rangeAllTruthy(Int, Int, Int) [function, symbol(rangeAllTruthy)]
                | rangeAnyTruthy(Int, Int, Int) [function, symbol(rangeAnyTruthy)]

  syntax Int ::= intValue(Val) [function, symbol(intValue)]
               | pyFloorDiv(Int, Int) [function, symbol(pyFloorDiv)]
               | pyModulo(Int, Int) [function, symbol(pyModulo)]
               | pyLen(Val) [function, symbol(pyLen)]
               | pyRangeLen(Int, Int, Int) [function, symbol(pyRangeLen)]
               | pySliceLower(Val, Int) [function, symbol(pySliceLower)]
               | pySliceUpper(Val, Int) [function, symbol(pySliceUpper)]
               | pySliceIndex(Int, Int) [function, symbol(pySliceIndex)]
               | pySliceLowerNeg(Val, Int) [function, symbol(pySliceLowerNeg)]
               | pySliceUpperNeg(Val, Int) [function, symbol(pySliceUpperNeg)]
               | pySliceIndexNeg(Int, Int) [function, symbol(pySliceIndexNeg)]
               | valItemsLen(ValItems) [function, symbol(valItemsLen)]
               | idItemsLen(IdItems) [function, symbol(idItemsLen)]
               | dictItemsLen(DictItems) [function, symbol(dictItemsLen)]
               | rangeGet(Int, Int, Int, Int) [function, symbol(rangeGet)]
               | sumValItems(ValItems) [function, symbol(sumValItems)]
               | rangeSum(Int, Int, Int) [function, symbol(rangeSum)]
               | minValItems(ValItems) [function, symbol(minValItems)]
               | maxValItems(ValItems) [function, symbol(maxValItems)]
               | rangeMin(Int, Int, Int) [function, symbol(rangeMin)]
               | rangeMax(Int, Int, Int) [function, symbol(rangeMax)]
  syntax String ::= repeatString(String, Int) [function, symbol(repeatString)]
                  | sliceString(String, Int, Int) [function, symbol(sliceString)]
                  | sliceStepString(String, Int, Int, Int) [function, symbol(sliceStepString)]
  syntax ArgVals ::= "#noArgVals" [symbol(noArgVals)]
                   | argValsCons(Val, ArgVals) [symbol(argValsCons)]
                   | appendArgVal(ArgVals, Val) [function, symbol(appendArgVal)]
  syntax DictVals ::= "#noDictVals" [symbol(noDictVals)]
                    | dictValsCons(Val, Val, DictVals) [symbol(dictValsCons)]
                    | appendDictVal(DictVals, Val, Val) [function, symbol(appendDictVal)]
  syntax Map ::= bindArgs(Map, IdItems, ArgVals) [function, symbol(bindArgs)]
  syntax Map ::= bindVals(Map, IdItems, ValItems) [function, symbol(bindVals)]
  syntax Map ::= bindPrefixVals(Map, IdItems, ValItems) [function, symbol(bindPrefixVals)]
  syntax Map ::= bindSuffixVals(Map, IdItems, ValItems, Int) [function, symbol(bindSuffixVals)]
  syntax Map ::= bindOneVal(Map, Id, Val) [function, symbol(bindOneVal)]
  syntax Map ::= bindStarUnpack(Map, IdItems, Id, IdItems, ValItems) [function, symbol(bindStarUnpack)]
  syntax ValItems ::= argValsToValItems(ArgVals) [function, symbol(argValsToValItems)]
  syntax ValItems ::= argValsToSetItems(ArgVals) [function, symbol(argValsToSetItems)]
  syntax ValItems ::= stringToValItems(String, Int, Int) [function, symbol(stringToValItems)]
  syntax ValItems ::= dictKeysToValItems(DictItems) [function, symbol(dictKeysToValItems)]
  syntax ValItems ::= rangeToValItems(Int, Int, Int, Int, Int) [function, symbol(rangeToValItems)]
  syntax ValItems ::= dropValItems(ValItems, Int) [function, symbol(dropValItems)]
  syntax ValItems ::= concatValItems(ValItems, ValItems) [function, symbol(concatValItems)]
  syntax ValItems ::= repeatValItems(ValItems, Int) [function, symbol(repeatValItems)]
  syntax ValItems ::= sliceValItems(ValItems, Int, Int) [function, symbol(sliceValItems)]
  syntax ValItems ::= sliceStepValItems(ValItems, Int, Int, Int) [function, symbol(sliceStepValItems)]
  syntax DictItems ::= dictValsToDictItems(DictVals) [function, symbol(dictValsToDictItems)]
  syntax Val ::= listSlice(ValItems, Int, Int) [function, symbol(listSlice)]
               | tupleSlice(ValItems, Int, Int) [function, symbol(tupleSlice)]
               | listSliceStep(ValItems, Int, Int, Int) [function, symbol(listSliceStep)]
               | tupleSliceStep(ValItems, Int, Int, Int) [function, symbol(tupleSliceStep)]
               | listGet(ValItems, Int) [function, symbol(listGet)]
               | rangeSlice(Int, Int, Int, Int, Int) [function, symbol(rangeSlice)]
               | rangeSliceStep(Int, Int, Int, Int, Int, Int) [function, symbol(rangeSliceStep)]
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
  rule truthy(set()) => false
  rule truthy(setVal(_:ValItems)) => true
  rule truthy(closure(_:Id, _:Exp)) => true
  rule truthy(closureArgs(_:IdItems, _:Exp)) => true
  rule truthy(functionVal(_:Id, _:Block)) => true
  rule truthy(functionValArgs(_:IdItems, _:Block)) => true
  rule truthy(rangeVal(Start:Int, Stop:Int)) => Start <Int Stop
  rule truthy(rangeVal(Start:Int, Stop:Int, Step:Int)) => pyRangeLen(Start, Stop, Step) >Int 0
    requires Step =/=Int 0
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
  rule isIntLike(set()) => false
  rule isIntLike(setVal(_:ValItems)) => false
  rule isIntLike(closure(_:Id, _:Exp)) => false
  rule isIntLike(closureArgs(_:IdItems, _:Exp)) => false
  rule isIntLike(functionVal(_:Id, _:Block)) => false
  rule isIntLike(functionValArgs(_:IdItems, _:Block)) => false
  rule isIntLike(rangeVal(_:Int, _:Int)) => false
  rule isIntLike(rangeVal(_:Int, _:Int, _:Int)) => false
  rule isIntLike(argsVal(_:ArgVals)) => false
  rule isIntLike(dictArgsVal(_:DictVals)) => false

  rule singletonIdentity(True) => true
  rule singletonIdentity(False) => true
  rule singletonIdentity(None) => true
  rule singletonIdentity(_:Int) => false
  rule singletonIdentity(_:String) => false
  rule singletonIdentity([]) => false
  rule singletonIdentity(listVal(_:ValItems)) => false
  rule singletonIdentity(()) => false
  rule singletonIdentity(tupleVal(_:ValItems)) => false
  rule singletonIdentity({}) => false
  rule singletonIdentity(dictVal(_:DictItems)) => false
  rule singletonIdentity(set()) => false
  rule singletonIdentity(setVal(_:ValItems)) => false
  rule singletonIdentity(closure(_:Id, _:Exp)) => false
  rule singletonIdentity(closureArgs(_:IdItems, _:Exp)) => false
  rule singletonIdentity(functionVal(_:Id, _:Block)) => false
  rule singletonIdentity(functionValArgs(_:IdItems, _:Block)) => false
  rule singletonIdentity(rangeVal(_:Int, _:Int)) => false
  rule singletonIdentity(rangeVal(_:Int, _:Int, _:Int)) => false
  rule singletonIdentity(argsVal(_:ArgVals)) => false
  rule singletonIdentity(dictArgsVal(_:DictVals)) => false

  rule intValue(I:Int) => I
  rule intValue(True) => 1
  rule intValue(False) => 0

  rule pyLen(S:String) => lengthString(S)
  rule pyLen([]) => 0
  rule pyLen(listVal(VS:ValItems)) => valItemsLen(VS)
  rule pyLen(()) => 0
  rule pyLen(tupleVal(VS:ValItems)) => valItemsLen(VS)
  rule pyLen({}) => 0
  rule pyLen(dictVal(DS:DictItems)) => dictItemsLen(DS)
  rule pyLen(set()) => 0
  rule pyLen(setVal(VS:ValItems)) => valItemsLen(VS)
  rule pyLen(rangeVal(Start:Int, Stop:Int)) => Stop -Int Start
    requires Start <Int Stop
  rule pyLen(rangeVal(Start:Int, Stop:Int)) => 0
    requires Start >=Int Stop
  rule pyLen(rangeVal(Start:Int, Stop:Int, Step:Int)) => pyRangeLen(Start, Stop, Step)
    requires Step =/=Int 0

  rule pyRangeLen(Start:Int, Stop:Int, Step:Int) => ((Stop -Int Start -Int 1) /Int Step) +Int 1
    requires Step >Int 0 andBool Start <Int Stop
  rule pyRangeLen(Start:Int, Stop:Int, Step:Int) => ((Start -Int Stop -Int 1) /Int (0 -Int Step)) +Int 1
    requires Step <Int 0 andBool Start >Int Stop
  rule pyRangeLen(Start:Int, Stop:Int, Step:Int) => 0
    requires (Step >Int 0 andBool Start >=Int Stop)
      orBool (Step <Int 0 andBool Start <=Int Stop)

  rule rangeContains(V:Val, _Start:Int, _Stop:Int) => false
    requires notBool isIntLike(V)
  rule rangeContains(V:Val, Start:Int, Stop:Int) =>
    intValue(V) >=Int Start andBool intValue(V) <Int Stop
    requires isIntLike(V)
  rule rangeContains(V:Val, _Start:Int, _Stop:Int, Step:Int) => false
    requires notBool isIntLike(V) andBool Step =/=Int 0
  rule rangeContains(V:Val, Start:Int, Stop:Int, Step:Int) =>
    intValue(V) >=Int Start
      andBool intValue(V) <Int Stop
      andBool ((intValue(V) -Int Start) %Int Step ==Int 0)
    requires isIntLike(V) andBool Step >Int 0
  rule rangeContains(V:Val, Start:Int, Stop:Int, Step:Int) =>
    intValue(V) <=Int Start
      andBool intValue(V) >Int Stop
      andBool ((Start -Int intValue(V)) %Int (0 -Int Step) ==Int 0)
    requires isIntLike(V) andBool Step <Int 0

  rule rangeEq(Start1:Int, Stop1:Int, Step1:Int, Start2:Int, Stop2:Int, Step2:Int) =>
    pyRangeLen(Start1, Stop1, Step1) ==Int pyRangeLen(Start2, Stop2, Step2)
      andBool (pyRangeLen(Start1, Stop1, Step1) ==Int 0
        orBool (Start1 ==Int Start2
          andBool (pyRangeLen(Start1, Stop1, Step1) ==Int 1 orBool Step1 ==Int Step2)))
    requires Step1 =/=Int 0 andBool Step2 =/=Int 0

  rule rangeGet(Start:Int, _Stop:Int, Step:Int, Index:Int) => Start +Int (Step *Int Index)
    requires Step =/=Int 0
  rule rangeSlice(Start:Int, Stop:Int, Step:Int, Lower:Int, Upper:Int) =>
    rangeVal(rangeGet(Start, Stop, Step, Lower), rangeGet(Start, Stop, Step, Upper), Step)
    requires Step =/=Int 0
  rule rangeSliceStep(Start:Int, Stop:Int, Step:Int, Lower:Int, Upper:Int, SliceStep:Int) =>
    rangeVal(rangeGet(Start, Stop, Step, Lower), rangeGet(Start, Stop, Step, Upper), Step *Int SliceStep)
    requires Step =/=Int 0 andBool SliceStep =/=Int 0

  rule pySliceLower(None, _:Int) => 0
  rule pySliceLower(True, Len:Int) => pySliceIndex(1, Len)
  rule pySliceLower(False, Len:Int) => pySliceIndex(0, Len)
  rule pySliceLower(I:Int, Len:Int) => pySliceIndex(I, Len)

  rule pySliceUpper(None, Len:Int) => Len
  rule pySliceUpper(True, Len:Int) => pySliceIndex(1, Len)
  rule pySliceUpper(False, Len:Int) => pySliceIndex(0, Len)
  rule pySliceUpper(I:Int, Len:Int) => pySliceIndex(I, Len)

  rule pySliceIndex(I:Int, Len:Int) => 0
    requires I <Int 0 -Int Len
  rule pySliceIndex(I:Int, Len:Int) => Len +Int I
    requires I <Int 0 andBool I >=Int 0 -Int Len
  rule pySliceIndex(I:Int, Len:Int) => Len
    requires I >Int Len
  rule pySliceIndex(I:Int, Len:Int) => I
    requires I >=Int 0 andBool I <=Int Len

  rule pySliceLowerNeg(None, Len:Int) => Len -Int 1
  rule pySliceLowerNeg(True, Len:Int) => pySliceIndexNeg(1, Len)
  rule pySliceLowerNeg(False, Len:Int) => pySliceIndexNeg(0, Len)
  rule pySliceLowerNeg(I:Int, Len:Int) => pySliceIndexNeg(I, Len)

  rule pySliceUpperNeg(None, _:Int) => -1
  rule pySliceUpperNeg(True, Len:Int) => pySliceIndexNeg(1, Len)
  rule pySliceUpperNeg(False, Len:Int) => pySliceIndexNeg(0, Len)
  rule pySliceUpperNeg(I:Int, Len:Int) => pySliceIndexNeg(I, Len)

  rule pySliceIndexNeg(I:Int, Len:Int) => -1
    requires I <Int 0 -Int Len
  rule pySliceIndexNeg(I:Int, Len:Int) => Len +Int I
    requires I <Int 0 andBool I >=Int 0 -Int Len
  rule pySliceIndexNeg(I:Int, Len:Int) => Len -Int 1
    requires I >=Int Len
  rule pySliceIndexNeg(I:Int, Len:Int) => I
    requires I >=Int 0 andBool I <Int Len

  rule valItemsLen(valItemsLast(_:Val)) => 1
  rule valItemsLen(valItemsCons(_:Val, VS:ValItems)) => 1 +Int valItemsLen(VS)

  rule idItemsLen(#noIds) => 0
  rule idItemsLen(idItemsLast(_:Id)) => 1
  rule idItemsLen(idItemsCons(_:Id, IDS:IdItems)) => 1 +Int idItemsLen(IDS)

  rule dictItemsLen(dictItemsLast(_:Val, _:Val)) => 1
  rule dictItemsLen(dictItemsCons(_:Val, _:Val, DS:DictItems)) => 1 +Int dictItemsLen(DS)

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
  rule valEq({}, {}) => true
  rule valEq({}, dictVal(_:DictItems)) => false
  rule valEq(dictVal(_:DictItems), {}) => false
  rule valEq(dictVal(DS1:DictItems), dictVal(DS2:DictItems)) => dictsEq(DS1, DS2)
  rule valEq(set(), set()) => true
  rule valEq(set(), setVal(_:ValItems)) => false
  rule valEq(setVal(_:ValItems), set()) => false
  rule valEq(setVal(VS1:ValItems), setVal(VS2:ValItems)) => setsEq(VS1, VS2)
  rule valEq(rangeVal(Start1:Int, Stop1:Int), rangeVal(Start2:Int, Stop2:Int)) =>
    rangeEq(Start1, Stop1, 1, Start2, Stop2, 1)
  rule valEq(rangeVal(Start1:Int, Stop1:Int), rangeVal(Start2:Int, Stop2:Int, Step2:Int)) =>
    rangeEq(Start1, Stop1, 1, Start2, Stop2, Step2)
  rule valEq(rangeVal(Start1:Int, Stop1:Int, Step1:Int), rangeVal(Start2:Int, Stop2:Int)) =>
    rangeEq(Start1, Stop1, Step1, Start2, Stop2, 1)
  rule valEq(rangeVal(Start1:Int, Stop1:Int, Step1:Int), rangeVal(Start2:Int, Stop2:Int, Step2:Int)) =>
    rangeEq(Start1, Stop1, Step1, Start2, Stop2, Step2)
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

  rule valIs(V1:Val, V2:Val) => valEq(V1, V2)
    requires singletonIdentity(V1) andBool singletonIdentity(V2)
  rule valIs(V1:Val, V2:Val) => false
    requires singletonIdentity(V1) andBool notBool singletonIdentity(V2)
  rule valIs(V1:Val, V2:Val) => false
    requires notBool singletonIdentity(V1) andBool singletonIdentity(V2)

  rule cmpHolds(#lt, V1:Val, V2:Val) => intValue(V1) <Int intValue(V2)
    requires isIntLike(V1) andBool isIntLike(V2)
  rule cmpHolds(#lt, S1:String, S2:String) => S1 <String S2
  rule cmpHolds(#lt, V1:Val, V2:Val) => seqLt(V1, V2)
    requires seqOrderComparable(V1, V2)
  rule cmpHolds(#lt, setVal(VS1:ValItems), setVal(VS2:ValItems)) =>
    setItemsSubset(VS1, VS2) andBool notBool setsEq(VS1, VS2)
  rule cmpHolds(#lt, set(), set()) => false
  rule cmpHolds(#lt, set(), setVal(_:ValItems)) => true
  rule cmpHolds(#lt, setVal(_:ValItems), set()) => false
  rule cmpHolds(#le, V1:Val, V2:Val) => intValue(V1) <=Int intValue(V2)
    requires isIntLike(V1) andBool isIntLike(V2)
  rule cmpHolds(#le, S1:String, S2:String) => S1 <=String S2
  rule cmpHolds(#le, V1:Val, V2:Val) => seqLt(V1, V2) orBool valEq(V1, V2)
    requires seqOrderComparable(V1, V2)
  rule cmpHolds(#le, setVal(VS1:ValItems), setVal(VS2:ValItems)) =>
    setItemsSubset(VS1, VS2)
  rule cmpHolds(#le, set(), set()) => true
  rule cmpHolds(#le, set(), setVal(_:ValItems)) => true
  rule cmpHolds(#le, setVal(_:ValItems), set()) => false
  rule cmpHolds(#gt, V1:Val, V2:Val) => intValue(V1) >Int intValue(V2)
    requires isIntLike(V1) andBool isIntLike(V2)
  rule cmpHolds(#gt, S1:String, S2:String) => S1 >String S2
  rule cmpHolds(#gt, V1:Val, V2:Val) => seqLt(V2, V1)
    requires seqOrderComparable(V1, V2)
  rule cmpHolds(#gt, setVal(VS1:ValItems), setVal(VS2:ValItems)) =>
    setItemsSubset(VS2, VS1) andBool notBool setsEq(VS1, VS2)
  rule cmpHolds(#gt, set(), set()) => false
  rule cmpHolds(#gt, set(), setVal(_:ValItems)) => false
  rule cmpHolds(#gt, setVal(_:ValItems), set()) => true
  rule cmpHolds(#ge, V1:Val, V2:Val) => intValue(V1) >=Int intValue(V2)
    requires isIntLike(V1) andBool isIntLike(V2)
  rule cmpHolds(#ge, S1:String, S2:String) => S1 >=String S2
  rule cmpHolds(#ge, V1:Val, V2:Val) => seqLt(V2, V1) orBool valEq(V1, V2)
    requires seqOrderComparable(V1, V2)
  rule cmpHolds(#ge, setVal(VS1:ValItems), setVal(VS2:ValItems)) =>
    setItemsSubset(VS2, VS1)
  rule cmpHolds(#ge, set(), set()) => true
  rule cmpHolds(#ge, set(), setVal(_:ValItems)) => false
  rule cmpHolds(#ge, setVal(_:ValItems), set()) => true
  rule cmpHolds(#eq, V1:Val, V2:Val) => valEq(V1, V2)
  rule cmpHolds(#ne, V1:Val, V2:Val) => notBool valEq(V1, V2)
  rule cmpHolds(#is, V1:Val, V2:Val) => valIs(V1, V2)
  rule cmpHolds(#isNot, V1:Val, V2:Val) => notBool valIs(V1, V2)
  rule cmpHolds(#in, Needle:String, Haystack:String) => findString(Haystack, Needle, 0) >=Int 0
  rule cmpHolds(#in, _V:Val, []) => false
  rule cmpHolds(#in, V:Val, listVal(VS:ValItems)) => containsVal(V, VS)
  rule cmpHolds(#in, _V:Val, ()) => false
  rule cmpHolds(#in, V:Val, tupleVal(VS:ValItems)) => containsVal(V, VS)
  rule cmpHolds(#in, _V:Val, {}) => false
  rule cmpHolds(#in, V:Val, dictVal(DS:DictItems)) => containsKey(V, DS)
  rule cmpHolds(#in, _V:Val, set()) => false
  rule cmpHolds(#in, V:Val, setVal(VS:ValItems)) => containsVal(V, VS)
  rule cmpHolds(#in, V:Val, rangeVal(Start:Int, Stop:Int)) => rangeContains(V, Start, Stop)
  rule cmpHolds(#in, V:Val, rangeVal(Start:Int, Stop:Int, Step:Int)) => rangeContains(V, Start, Stop, Step)
  rule cmpHolds(#notIn, V1:Val, V2:Val) => notBool cmpHolds(#in, V1, V2)

  rule sameArity(#noIds, #noArgVals) => true
  rule sameArity(#noIds, argValsCons(_:Val, _:ArgVals)) => false
  rule sameArity(idItemsLast(_:Id), #noArgVals) => false
  rule sameArity(idItemsLast(_:Id), argValsCons(_:Val, #noArgVals)) => true
  rule sameArity(idItemsLast(_:Id), argValsCons(_:Val, argValsCons(_:Val, _:ArgVals))) => false
  rule sameArity(idItemsCons(_:Id, _:IdItems), #noArgVals) => false
  rule sameArity(idItemsCons(_:Id, IDS:IdItems), argValsCons(_:Val, VS:ArgVals)) => sameArity(IDS, VS)

  rule sameIdValArity(idItemsLast(_:Id), valItemsLast(_:Val)) => true
  rule sameIdValArity(idItemsLast(_:Id), valItemsCons(_:Val, _:ValItems)) => false
  rule sameIdValArity(idItemsCons(_:Id, _:IdItems), valItemsLast(_:Val)) => false
  rule sameIdValArity(idItemsCons(_:Id, IDS:IdItems), valItemsCons(_:Val, VS:ValItems)) =>
    sameIdValArity(IDS, VS)

  rule starUnpackArityOk(Prefix:IdItems, Suffix:IdItems, Len:Int) =>
    idItemsLen(Prefix) +Int idItemsLen(Suffix) <=Int Len

  rule emptyArgVals(#noArgVals) => true
  rule emptyArgVals(argValsCons(_:Val, _:ArgVals)) => false

  rule emptyDictVals(#noDictVals) => true
  rule emptyDictVals(dictValsCons(_:Val, _:Val, _:DictVals)) => false

  rule appendArgVal(#noArgVals, V:Val) => argValsCons(V, #noArgVals)
  rule appendArgVal(argValsCons(V0:Val, VS:ArgVals), V:Val) =>
    argValsCons(V0, appendArgVal(VS, V))

  rule appendDictVal(#noDictVals, K:Val, V:Val) => dictValsCons(K, V, #noDictVals)
  rule appendDictVal(dictValsCons(K0:Val, _:Val, DVS:DictVals), K:Val, V:Val) =>
    dictValsCons(K0, V, DVS)
    requires valEq(K, K0)
  rule appendDictVal(dictValsCons(K0:Val, V0:Val, DVS:DictVals), K:Val, V:Val) =>
    dictValsCons(K0, V0, appendDictVal(DVS, K, V))
    requires notBool valEq(K, K0)

  rule bindArgs(Rho:Map, #noIds, #noArgVals) => Rho
  rule bindArgs(Rho:Map, idItemsLast(X:Id), argValsCons(V:Val, #noArgVals)) => Rho [ X <- V ]
  rule bindArgs(Rho:Map, idItemsCons(X:Id, IDS:IdItems), argValsCons(V:Val, VS:ArgVals)) =>
    bindArgs(Rho [ X <- V ], IDS, VS)

  rule bindVals(Rho:Map, idItemsLast(X:Id), valItemsLast(V:Val)) => Rho [ X <- V ]
  rule bindVals(Rho:Map, idItemsCons(X:Id, IDS:IdItems), valItemsCons(V:Val, VS:ValItems)) =>
    bindVals(Rho [ X <- V ], IDS, VS)

  rule bindPrefixVals(Rho:Map, #noIds, _:ValItems) => Rho
  rule bindPrefixVals(Rho:Map, idItemsLast(X:Id), valItemsLast(V:Val)) => Rho [ X <- V ]
  rule bindPrefixVals(Rho:Map, idItemsLast(X:Id), valItemsCons(V:Val, _:ValItems)) => Rho [ X <- V ]
  rule bindPrefixVals(Rho:Map, idItemsCons(X:Id, IDS:IdItems), valItemsCons(V:Val, VS:ValItems)) =>
    bindPrefixVals(Rho [ X <- V ], IDS, VS)

  rule bindSuffixVals(Rho:Map, #noIds, _:ValItems, _:Int) => Rho
  rule bindSuffixVals(Rho:Map, IDS:IdItems, VS:ValItems, Len:Int) =>
    bindVals(Rho, IDS, dropValItems(VS, Len -Int idItemsLen(IDS)))
    requires idItemsLen(IDS) >Int 0

  rule bindOneVal(Rho:Map, X:Id, V:Val) => Rho [ X <- V ]

  rule bindStarUnpack(Rho:Map, Prefix:IdItems, Star:Id, Suffix:IdItems, VS:ValItems) =>
    bindSuffixVals(
      bindOneVal(
        bindPrefixVals(Rho, Prefix, VS),
        Star,
        listSlice(VS, idItemsLen(Prefix), valItemsLen(VS) -Int idItemsLen(Suffix))),
      Suffix,
      VS,
      valItemsLen(VS))

  rule argValsToValItems(argValsCons(V:Val, #noArgVals)) => valItemsLast(V)
  rule argValsToValItems(argValsCons(V:Val, VS:ArgVals)) =>
    valItemsCons(V, argValsToValItems(VS))
    requires notBool emptyArgVals(VS)

  rule argValsToSetItems(argValsCons(V:Val, #noArgVals)) => valItemsLast(V)
  rule argValsToSetItems(argValsCons(V:Val, VS:ArgVals)) => argValsToSetItems(VS)
    requires notBool emptyArgVals(VS)
      andBool containsVal(V, argValsToSetItems(VS))
  rule argValsToSetItems(argValsCons(V:Val, VS:ArgVals)) =>
    valItemsCons(V, argValsToSetItems(VS))
    requires notBool emptyArgVals(VS)
      andBool notBool containsVal(V, argValsToSetItems(VS))

  rule stringToValItems(S:String, I:Int, Len:Int) =>
    valItemsLast(substrString(S, I, I +Int 1))
    requires I +Int 1 >=Int Len
  rule stringToValItems(S:String, I:Int, Len:Int) =>
    valItemsCons(substrString(S, I, I +Int 1), stringToValItems(S, I +Int 1, Len))
    requires I +Int 1 <Int Len

  rule dictKeysToValItems(dictItemsLast(K:Val, _:Val)) => valItemsLast(K)
  rule dictKeysToValItems(dictItemsCons(K:Val, _:Val, DS:DictItems)) =>
    valItemsCons(K, dictKeysToValItems(DS))

  rule rangeToValItems(Start:Int, Stop:Int, Step:Int, I:Int, Len:Int) =>
    valItemsLast(rangeGet(Start, Stop, Step, I))
    requires Step =/=Int 0 andBool I +Int 1 >=Int Len
  rule rangeToValItems(Start:Int, Stop:Int, Step:Int, I:Int, Len:Int) =>
    valItemsCons(rangeGet(Start, Stop, Step, I), rangeToValItems(Start, Stop, Step, I +Int 1, Len))
    requires Step =/=Int 0 andBool I +Int 1 <Int Len

  rule allValItems(valItemsLast(V:Val)) => truthy(V)
  rule allValItems(valItemsCons(V:Val, VS:ValItems)) => truthy(V) andBool allValItems(VS)
  rule anyValItems(valItemsLast(V:Val)) => truthy(V)
  rule anyValItems(valItemsCons(V:Val, VS:ValItems)) => truthy(V) orBool anyValItems(VS)
  rule valItemsAllIntLike(valItemsLast(V:Val)) => isIntLike(V)
  rule valItemsAllIntLike(valItemsCons(V:Val, VS:ValItems)) =>
    isIntLike(V) andBool valItemsAllIntLike(VS)

  rule rangeAllTruthy(Start:Int, Stop:Int, Step:Int) => notBool rangeContains(0, Start, Stop, Step)
    requires Step =/=Int 0
  rule rangeAnyTruthy(Start:Int, Stop:Int, Step:Int) => false
    requires Step =/=Int 0 andBool pyRangeLen(Start, Stop, Step) ==Int 0
  rule rangeAnyTruthy(Start:Int, Stop:Int, Step:Int) => false
    requires Step =/=Int 0
      andBool pyRangeLen(Start, Stop, Step) ==Int 1
      andBool rangeGet(Start, Stop, Step, 0) ==Int 0
  rule rangeAnyTruthy(Start:Int, Stop:Int, Step:Int) => true
    requires Step =/=Int 0
      andBool pyRangeLen(Start, Stop, Step) ==Int 1
      andBool rangeGet(Start, Stop, Step, 0) =/=Int 0
  rule rangeAnyTruthy(Start:Int, Stop:Int, Step:Int) => true
    requires Step =/=Int 0 andBool pyRangeLen(Start, Stop, Step) >Int 1
  rule sumValItems(valItemsLast(V:Val)) => intValue(V)
    requires isIntLike(V)
  rule sumValItems(valItemsCons(V:Val, VS:ValItems)) => intValue(V) +Int sumValItems(VS)
    requires isIntLike(V) andBool valItemsAllIntLike(VS)
  rule rangeSum(Start:Int, Stop:Int, Step:Int) =>
    (pyRangeLen(Start, Stop, Step) *Int ((2 *Int Start) +Int ((pyRangeLen(Start, Stop, Step) -Int 1) *Int Step))) /Int 2
    requires Step =/=Int 0
  rule minValItems(valItemsLast(V:Val)) => intValue(V)
    requires isIntLike(V)
  rule minValItems(valItemsCons(V:Val, VS:ValItems)) => intValue(V)
    requires isIntLike(V)
      andBool valItemsAllIntLike(VS)
      andBool intValue(V) <=Int minValItems(VS)
  rule minValItems(valItemsCons(V:Val, VS:ValItems)) => minValItems(VS)
    requires isIntLike(V)
      andBool valItemsAllIntLike(VS)
      andBool intValue(V) >Int minValItems(VS)
  rule maxValItems(valItemsLast(V:Val)) => intValue(V)
    requires isIntLike(V)
  rule maxValItems(valItemsCons(V:Val, VS:ValItems)) => intValue(V)
    requires isIntLike(V)
      andBool valItemsAllIntLike(VS)
      andBool intValue(V) >=Int maxValItems(VS)
  rule maxValItems(valItemsCons(V:Val, VS:ValItems)) => maxValItems(VS)
    requires isIntLike(V)
      andBool valItemsAllIntLike(VS)
      andBool intValue(V) <Int maxValItems(VS)
  rule rangeMin(Start:Int, Stop:Int, Step:Int) => Start
    requires Step >Int 0 andBool pyRangeLen(Start, Stop, Step) >Int 0
  rule rangeMin(Start:Int, Stop:Int, Step:Int) =>
    rangeGet(Start, Stop, Step, pyRangeLen(Start, Stop, Step) -Int 1)
    requires Step <Int 0 andBool pyRangeLen(Start, Stop, Step) >Int 0
  rule rangeMax(Start:Int, Stop:Int, Step:Int) =>
    rangeGet(Start, Stop, Step, pyRangeLen(Start, Stop, Step) -Int 1)
    requires Step >Int 0 andBool pyRangeLen(Start, Stop, Step) >Int 0
  rule rangeMax(Start:Int, Stop:Int, Step:Int) => Start
    requires Step <Int 0 andBool pyRangeLen(Start, Stop, Step) >Int 0

  rule concatValItems(valItemsLast(V:Val), VS:ValItems) => valItemsCons(V, VS)
  rule concatValItems(valItemsCons(V:Val, VS1:ValItems), VS2:ValItems) =>
    valItemsCons(V, concatValItems(VS1, VS2))

  rule repeatString(_:String, N:Int) => "" requires N <=Int 0
  rule repeatString(S:String, 1) => S
  rule repeatString(S:String, N:Int) => S +String repeatString(S, N -Int 1)
    requires N >Int 1

  rule repeatValItems(VS:ValItems, 1) => VS
  rule repeatValItems(VS:ValItems, N:Int) => concatValItems(VS, repeatValItems(VS, N -Int 1))
    requires N >Int 1

  rule dropValItems(VS:ValItems, 0) => VS
  rule dropValItems(valItemsCons(_:Val, VS:ValItems), N:Int) => dropValItems(VS, N -Int 1)
    requires N >Int 0

  rule sliceString(_:String, Start:Int, Stop:Int) => "" requires Start >=Int Stop
  rule sliceString(S:String, Start:Int, Stop:Int) => substrString(S, Start, Stop)
    requires Start <Int Stop

  rule sliceStepString(_:String, Start:Int, Stop:Int, Step:Int) => ""
    requires Start >=Int Stop andBool Step >Int 0
  rule sliceStepString(S:String, Start:Int, Stop:Int, Step:Int) =>
    substrString(S, Start, Start +Int 1) +String sliceStepString(S, Start +Int Step, Stop, Step)
    requires Start <Int Stop andBool Step >Int 0
  rule sliceStepString(_:String, Start:Int, Stop:Int, Step:Int) => ""
    requires Start <=Int Stop andBool Step <Int 0
  rule sliceStepString(S:String, Start:Int, Stop:Int, Step:Int) =>
    substrString(S, Start, Start +Int 1) +String sliceStepString(S, Start +Int Step, Stop, Step)
    requires Start >Int Stop andBool Step <Int 0

  rule listSlice(_:ValItems, Start:Int, Stop:Int) => [] requires Start >=Int Stop
  rule listSlice(VS:ValItems, Start:Int, Stop:Int) => listVal(sliceValItems(VS, Start, Stop))
    requires Start <Int Stop

  rule tupleSlice(_:ValItems, Start:Int, Stop:Int) => () requires Start >=Int Stop
  rule tupleSlice(VS:ValItems, Start:Int, Stop:Int) => tupleVal(sliceValItems(VS, Start, Stop))
    requires Start <Int Stop

  rule listSliceStep(_:ValItems, Start:Int, Stop:Int, Step:Int) => []
    requires Start >=Int Stop andBool Step >Int 0
  rule listSliceStep(VS:ValItems, Start:Int, Stop:Int, Step:Int) =>
    listVal(sliceStepValItems(VS, Start, Stop, Step))
    requires Start <Int Stop andBool Step >Int 0
  rule listSliceStep(_:ValItems, Start:Int, Stop:Int, Step:Int) => []
    requires Start <=Int Stop andBool Step <Int 0
  rule listSliceStep(VS:ValItems, Start:Int, Stop:Int, Step:Int) =>
    listVal(sliceStepValItems(VS, Start, Stop, Step))
    requires Start >Int Stop andBool Step <Int 0

  rule tupleSliceStep(_:ValItems, Start:Int, Stop:Int, Step:Int) => ()
    requires Start >=Int Stop andBool Step >Int 0
  rule tupleSliceStep(VS:ValItems, Start:Int, Stop:Int, Step:Int) =>
    tupleVal(sliceStepValItems(VS, Start, Stop, Step))
    requires Start <Int Stop andBool Step >Int 0
  rule tupleSliceStep(_:ValItems, Start:Int, Stop:Int, Step:Int) => ()
    requires Start <=Int Stop andBool Step <Int 0
  rule tupleSliceStep(VS:ValItems, Start:Int, Stop:Int, Step:Int) =>
    tupleVal(sliceStepValItems(VS, Start, Stop, Step))
    requires Start >Int Stop andBool Step <Int 0

  rule sliceValItems(valItemsLast(V:Val), 0, Stop:Int) => valItemsLast(V)
    requires Stop >Int 0
  rule sliceValItems(valItemsCons(V:Val, _:ValItems), 0, 1) => valItemsLast(V)
  rule sliceValItems(valItemsCons(V:Val, VS:ValItems), 0, Stop:Int) =>
    valItemsCons(V, sliceValItems(VS, 0, Stop -Int 1))
    requires Stop >Int 1
  rule sliceValItems(valItemsCons(_:Val, VS:ValItems), Start:Int, Stop:Int) =>
    sliceValItems(VS, Start -Int 1, Stop -Int 1)
    requires Start >Int 0

  rule sliceStepValItems(VS:ValItems, Start:Int, Stop:Int, Step:Int) =>
    valItemsLast(listGet(VS, Start))
    requires Start <Int Stop andBool Start +Int Step >=Int Stop
  rule sliceStepValItems(VS:ValItems, Start:Int, Stop:Int, Step:Int) =>
    valItemsCons(listGet(VS, Start), sliceStepValItems(VS, Start +Int Step, Stop, Step))
    requires Start <Int Stop andBool Start +Int Step <Int Stop
  rule sliceStepValItems(VS:ValItems, Start:Int, Stop:Int, Step:Int) =>
    valItemsLast(listGet(VS, Start))
    requires Start >Int Stop andBool Start +Int Step <=Int Stop
  rule sliceStepValItems(VS:ValItems, Start:Int, Stop:Int, Step:Int) =>
    valItemsCons(listGet(VS, Start), sliceStepValItems(VS, Start +Int Step, Stop, Step))
    requires Start >Int Stop andBool Start +Int Step >Int Stop

  rule dictValsToDictItems(dictValsCons(K:Val, V:Val, #noDictVals)) => dictItemsLast(K, V)
  rule dictValsToDictItems(dictValsCons(K:Val, V:Val, DVS:DictVals)) =>
    dictItemsCons(K, V, dictValsToDictItems(DVS))
    requires notBool emptyDictVals(DVS)

  rule valsEq(valItemsLast(V1:Val), valItemsLast(V2:Val)) => valEq(V1, V2)
  rule valsEq(valItemsCons(V1:Val, VS1:ValItems), valItemsCons(V2:Val, VS2:ValItems)) =>
    valEq(V1, V2) andBool valsEq(VS1, VS2)
  rule valsEq(valItemsLast(_:Val), valItemsCons(_:Val, _:ValItems)) => false
  rule valsEq(valItemsCons(_:Val, _:ValItems), valItemsLast(_:Val)) => false

  rule valItemsLt(valItemsLast(V1:Val), valItemsLast(V2:Val)) => cmpHolds(#lt, V1, V2)
    requires notBool valEq(V1, V2)
  rule valItemsLt(valItemsLast(V1:Val), valItemsLast(V2:Val)) => false
    requires valEq(V1, V2)
  rule valItemsLt(valItemsLast(V1:Val), valItemsCons(V2:Val, _:ValItems)) => true
    requires valEq(V1, V2)
  rule valItemsLt(valItemsLast(V1:Val), valItemsCons(V2:Val, _:ValItems)) => cmpHolds(#lt, V1, V2)
    requires notBool valEq(V1, V2)
  rule valItemsLt(valItemsCons(V1:Val, _:ValItems), valItemsLast(V2:Val)) => false
    requires valEq(V1, V2)
  rule valItemsLt(valItemsCons(V1:Val, _:ValItems), valItemsLast(V2:Val)) => cmpHolds(#lt, V1, V2)
    requires notBool valEq(V1, V2)
  rule valItemsLt(valItemsCons(V1:Val, VS1:ValItems), valItemsCons(V2:Val, VS2:ValItems)) =>
    valItemsLt(VS1, VS2)
    requires valEq(V1, V2)
  rule valItemsLt(valItemsCons(V1:Val, _:ValItems), valItemsCons(V2:Val, _:ValItems)) =>
    cmpHolds(#lt, V1, V2)
    requires notBool valEq(V1, V2)

  rule isListSequence([]) => true
  rule isListSequence(listVal(_:ValItems)) => true
  rule isListSequence(()) => false
  rule isListSequence(tupleVal(_:ValItems)) => false
  rule isListSequence(_:Int) => false
  rule isListSequence(_:String) => false
  rule isListSequence(True) => false
  rule isListSequence(False) => false
  rule isListSequence(None) => false
  rule isListSequence({}) => false
  rule isListSequence(dictVal(_:DictItems)) => false
  rule isListSequence(set()) => false
  rule isListSequence(setVal(_:ValItems)) => false
  rule isListSequence(closure(_:Id, _:Exp)) => false
  rule isListSequence(closureArgs(_:IdItems, _:Exp)) => false
  rule isListSequence(functionVal(_:Id, _:Block)) => false
  rule isListSequence(functionValArgs(_:IdItems, _:Block)) => false
  rule isListSequence(rangeVal(_:Int, _:Int)) => false
  rule isListSequence(rangeVal(_:Int, _:Int, _:Int)) => false
  rule isListSequence(argsVal(_:ArgVals)) => false
  rule isListSequence(dictArgsVal(_:DictVals)) => false

  rule isTupleSequence([]) => false
  rule isTupleSequence(listVal(_:ValItems)) => false
  rule isTupleSequence(()) => true
  rule isTupleSequence(tupleVal(_:ValItems)) => true
  rule isTupleSequence(_:Int) => false
  rule isTupleSequence(_:String) => false
  rule isTupleSequence(True) => false
  rule isTupleSequence(False) => false
  rule isTupleSequence(None) => false
  rule isTupleSequence({}) => false
  rule isTupleSequence(dictVal(_:DictItems)) => false
  rule isTupleSequence(set()) => false
  rule isTupleSequence(setVal(_:ValItems)) => false
  rule isTupleSequence(closure(_:Id, _:Exp)) => false
  rule isTupleSequence(closureArgs(_:IdItems, _:Exp)) => false
  rule isTupleSequence(functionVal(_:Id, _:Block)) => false
  rule isTupleSequence(functionValArgs(_:IdItems, _:Block)) => false
  rule isTupleSequence(rangeVal(_:Int, _:Int)) => false
  rule isTupleSequence(rangeVal(_:Int, _:Int, _:Int)) => false
  rule isTupleSequence(argsVal(_:ArgVals)) => false
  rule isTupleSequence(dictArgsVal(_:DictVals)) => false

  rule seqOrderComparable(V1:Val, V2:Val) =>
    (isListSequence(V1) andBool isListSequence(V2))
      orBool (isTupleSequence(V1) andBool isTupleSequence(V2))

  rule seqLt([], []) => false
  rule seqLt([], listVal(_:ValItems)) => true
  rule seqLt(listVal(_:ValItems), []) => false
  rule seqLt(listVal(VS1:ValItems), listVal(VS2:ValItems)) => valItemsLt(VS1, VS2)
  rule seqLt((), ()) => false
  rule seqLt((), tupleVal(_:ValItems)) => true
  rule seqLt(tupleVal(_:ValItems), ()) => false
  rule seqLt(tupleVal(VS1:ValItems), tupleVal(VS2:ValItems)) => valItemsLt(VS1, VS2)

  rule dictsEq(DS1:DictItems, DS2:DictItems) =>
    dictItemsLen(DS1) ==Int dictItemsLen(DS2)
      andBool dictItemsContained(DS1, DS2)
      andBool dictItemsContained(DS2, DS1)

  rule dictItemsContained(dictItemsLast(K:Val, V:Val), DS:DictItems) => containsDictPair(K, V, DS)
  rule dictItemsContained(dictItemsCons(K:Val, V:Val, DS1:DictItems), DS2:DictItems) =>
    containsDictPair(K, V, DS2) andBool dictItemsContained(DS1, DS2)

  rule containsDictPair(K:Val, V:Val, dictItemsLast(K1:Val, V1:Val)) =>
    valEq(K, K1) andBool valEq(V, V1)
  rule containsDictPair(K:Val, V:Val, dictItemsCons(K1:Val, V1:Val, DS:DictItems)) =>
    (valEq(K, K1) andBool valEq(V, V1)) orBool containsDictPair(K, V, DS)

  rule setsEq(VS1:ValItems, VS2:ValItems) =>
    setItemsSubset(VS1, VS2) andBool setItemsSubset(VS2, VS1)

  rule setItemsSubset(valItemsLast(V:Val), VS:ValItems) => containsVal(V, VS)
  rule setItemsSubset(valItemsCons(V:Val, VS1:ValItems), VS2:ValItems) =>
    containsVal(V, VS2) andBool setItemsSubset(VS1, VS2)

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

  rule <k> namedExprExp(X:Id, V:Val) => V ... </k>
       <env> Rho => Rho [ X <- V ] </env>

  rule + V:Val => intValue(V) requires isIntLike(V)
  rule - V:Val => 0 -Int intValue(V) requires isIntLike(V)
  rule ~ V:Val => ~Int intValue(V) requires isIntLike(V)

  rule V1:Val + V2:Val => intValue(V1) +Int intValue(V2)
    requires isIntLike(V1) andBool isIntLike(V2)
  rule V1:Val - V2:Val => intValue(V1) -Int intValue(V2)
    requires isIntLike(V1) andBool isIntLike(V2)
  rule V1:Val * V2:Val => intValue(V1) *Int intValue(V2)
    requires isIntLike(V1) andBool isIntLike(V2)
  rule S:String * V:Val => repeatString(S, intValue(V))
    requires isIntLike(V)
  rule V:Val * S:String => repeatString(S, intValue(V))
    requires isIntLike(V)
  rule [] * V:Val => []
    requires isIntLike(V)
  rule V:Val * [] => []
    requires isIntLike(V)
  rule listVal(_:ValItems) * V:Val => []
    requires isIntLike(V) andBool intValue(V) <=Int 0
  rule V:Val * listVal(_:ValItems) => []
    requires isIntLike(V) andBool intValue(V) <=Int 0
  rule listVal(VS:ValItems) * V:Val => listVal(repeatValItems(VS, intValue(V)))
    requires isIntLike(V) andBool intValue(V) >Int 0
  rule V:Val * listVal(VS:ValItems) => listVal(repeatValItems(VS, intValue(V)))
    requires isIntLike(V) andBool intValue(V) >Int 0
  rule () * V:Val => ()
    requires isIntLike(V)
  rule V:Val * () => ()
    requires isIntLike(V)
  rule tupleVal(_:ValItems) * V:Val => ()
    requires isIntLike(V) andBool intValue(V) <=Int 0
  rule V:Val * tupleVal(_:ValItems) => ()
    requires isIntLike(V) andBool intValue(V) <=Int 0
  rule tupleVal(VS:ValItems) * V:Val => tupleVal(repeatValItems(VS, intValue(V)))
    requires isIntLike(V) andBool intValue(V) >Int 0
  rule V:Val * tupleVal(VS:ValItems) => tupleVal(repeatValItems(VS, intValue(V)))
    requires isIntLike(V) andBool intValue(V) >Int 0
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
  rule [] + [] => []
  rule [] + listVal(VS:ValItems) => listVal(VS)
  rule listVal(VS:ValItems) + [] => listVal(VS)
  rule listVal(VS1:ValItems) + listVal(VS2:ValItems) => listVal(concatValItems(VS1, VS2))
  rule () + () => ()
  rule () + tupleVal(VS:ValItems) => tupleVal(VS)
  rule tupleVal(VS:ValItems) + () => tupleVal(VS)
  rule tupleVal(VS1:ValItems) + tupleVal(VS2:ValItems) => tupleVal(concatValItems(VS1, VS2))
  rule lenExp(V:Val) => pyLen(V)
  rule sliceExp(S:String, Lower:Val, Upper:Val) =>
    sliceString(S, pySliceLower(Lower, lengthString(S)), pySliceUpper(Upper, lengthString(S)))
  rule sliceExp([], _Lower:Val, _Upper:Val) => []
  rule sliceExp(listVal(VS:ValItems), Lower:Val, Upper:Val) =>
    listSlice(VS, pySliceLower(Lower, valItemsLen(VS)), pySliceUpper(Upper, valItemsLen(VS)))
  rule sliceExp((), _Lower:Val, _Upper:Val) => ()
  rule sliceExp(tupleVal(VS:ValItems), Lower:Val, Upper:Val) =>
    tupleSlice(VS, pySliceLower(Lower, valItemsLen(VS)), pySliceUpper(Upper, valItemsLen(VS)))
  rule sliceExp(rangeVal(Start:Int, Stop:Int), Lower:Val, Upper:Val) =>
    rangeSlice(Start, Stop, 1, pySliceLower(Lower, pyRangeLen(Start, Stop, 1)), pySliceUpper(Upper, pyRangeLen(Start, Stop, 1)))
  rule sliceExp(rangeVal(Start:Int, Stop:Int, Step:Int), Lower:Val, Upper:Val) =>
    rangeSlice(Start, Stop, Step, pySliceLower(Lower, pyRangeLen(Start, Stop, Step)), pySliceUpper(Upper, pyRangeLen(Start, Stop, Step)))
    requires Step =/=Int 0
  rule sliceStepExp(S:String, Lower:Val, Upper:Val, Step:Val) =>
    sliceStepString(S, pySliceLower(Lower, lengthString(S)), pySliceUpper(Upper, lengthString(S)), intValue(Step))
    requires isIntLike(Step) andBool intValue(Step) >Int 0
  rule sliceStepExp(S:String, Lower:Val, Upper:Val, Step:Val) =>
    sliceStepString(S, pySliceLowerNeg(Lower, lengthString(S)), pySliceUpperNeg(Upper, lengthString(S)), intValue(Step))
    requires isIntLike(Step) andBool intValue(Step) <Int 0
  rule sliceStepExp([], _Lower:Val, _Upper:Val, Step:Val) => []
    requires isIntLike(Step) andBool intValue(Step) =/=Int 0
  rule sliceStepExp(listVal(VS:ValItems), Lower:Val, Upper:Val, Step:Val) =>
    listSliceStep(VS, pySliceLower(Lower, valItemsLen(VS)), pySliceUpper(Upper, valItemsLen(VS)), intValue(Step))
    requires isIntLike(Step) andBool intValue(Step) >Int 0
  rule sliceStepExp(listVal(VS:ValItems), Lower:Val, Upper:Val, Step:Val) =>
    listSliceStep(VS, pySliceLowerNeg(Lower, valItemsLen(VS)), pySliceUpperNeg(Upper, valItemsLen(VS)), intValue(Step))
    requires isIntLike(Step) andBool intValue(Step) <Int 0
  rule sliceStepExp((), _Lower:Val, _Upper:Val, Step:Val) => ()
    requires isIntLike(Step) andBool intValue(Step) =/=Int 0
  rule sliceStepExp(tupleVal(VS:ValItems), Lower:Val, Upper:Val, Step:Val) =>
    tupleSliceStep(VS, pySliceLower(Lower, valItemsLen(VS)), pySliceUpper(Upper, valItemsLen(VS)), intValue(Step))
    requires isIntLike(Step) andBool intValue(Step) >Int 0
  rule sliceStepExp(tupleVal(VS:ValItems), Lower:Val, Upper:Val, Step:Val) =>
    tupleSliceStep(VS, pySliceLowerNeg(Lower, valItemsLen(VS)), pySliceUpperNeg(Upper, valItemsLen(VS)), intValue(Step))
    requires isIntLike(Step) andBool intValue(Step) <Int 0
  rule sliceStepExp(rangeVal(Start:Int, Stop:Int), Lower:Val, Upper:Val, Step:Val) =>
    rangeSliceStep(Start, Stop, 1, pySliceLower(Lower, pyRangeLen(Start, Stop, 1)), pySliceUpper(Upper, pyRangeLen(Start, Stop, 1)), intValue(Step))
    requires isIntLike(Step) andBool intValue(Step) >Int 0
  rule sliceStepExp(rangeVal(Start:Int, Stop:Int), Lower:Val, Upper:Val, Step:Val) =>
    rangeSliceStep(Start, Stop, 1, pySliceLowerNeg(Lower, pyRangeLen(Start, Stop, 1)), pySliceUpperNeg(Upper, pyRangeLen(Start, Stop, 1)), intValue(Step))
    requires isIntLike(Step) andBool intValue(Step) <Int 0
  rule sliceStepExp(rangeVal(Start:Int, Stop:Int, RangeStep:Int), Lower:Val, Upper:Val, Step:Val) =>
    rangeSliceStep(Start, Stop, RangeStep, pySliceLower(Lower, pyRangeLen(Start, Stop, RangeStep)), pySliceUpper(Upper, pyRangeLen(Start, Stop, RangeStep)), intValue(Step))
    requires RangeStep =/=Int 0 andBool isIntLike(Step) andBool intValue(Step) >Int 0
  rule sliceStepExp(rangeVal(Start:Int, Stop:Int, RangeStep:Int), Lower:Val, Upper:Val, Step:Val) =>
    rangeSliceStep(Start, Stop, RangeStep, pySliceLowerNeg(Lower, pyRangeLen(Start, Stop, RangeStep)), pySliceUpperNeg(Upper, pyRangeLen(Start, Stop, RangeStep)), intValue(Step))
    requires RangeStep =/=Int 0 andBool isIntLike(Step) andBool intValue(Step) <Int 0

  rule V1:Val < V2:Val => boolValue(intValue(V1) <Int intValue(V2))
    requires isIntLike(V1) andBool isIntLike(V2)
  rule S1:String < S2:String => boolValue(S1 <String S2)
  rule V1:Val < V2:Val => boolValue(cmpHolds(#lt, V1, V2))
    requires seqOrderComparable(V1, V2)
  rule setVal(VS1:ValItems) < setVal(VS2:ValItems) =>
    boolValue(cmpHolds(#lt, setVal(VS1), setVal(VS2)))
  rule set() < set() => False
  rule set() < setVal(_:ValItems) => True
  rule setVal(_:ValItems) < set() => False
  rule V1:Val <= V2:Val => boolValue(intValue(V1) <=Int intValue(V2))
    requires isIntLike(V1) andBool isIntLike(V2)
  rule S1:String <= S2:String => boolValue(S1 <=String S2)
  rule V1:Val <= V2:Val => boolValue(cmpHolds(#le, V1, V2))
    requires seqOrderComparable(V1, V2)
  rule setVal(VS1:ValItems) <= setVal(VS2:ValItems) =>
    boolValue(cmpHolds(#le, setVal(VS1), setVal(VS2)))
  rule set() <= set() => True
  rule set() <= setVal(_:ValItems) => True
  rule setVal(_:ValItems) <= set() => False
  rule V1:Val > V2:Val => boolValue(intValue(V1) >Int intValue(V2))
    requires isIntLike(V1) andBool isIntLike(V2)
  rule S1:String > S2:String => boolValue(S1 >String S2)
  rule V1:Val > V2:Val => boolValue(cmpHolds(#gt, V1, V2))
    requires seqOrderComparable(V1, V2)
  rule setVal(VS1:ValItems) > setVal(VS2:ValItems) =>
    boolValue(cmpHolds(#gt, setVal(VS1), setVal(VS2)))
  rule set() > set() => False
  rule set() > setVal(_:ValItems) => False
  rule setVal(_:ValItems) > set() => True
  rule V1:Val >= V2:Val => boolValue(intValue(V1) >=Int intValue(V2))
    requires isIntLike(V1) andBool isIntLike(V2)
  rule S1:String >= S2:String => boolValue(S1 >=String S2)
  rule V1:Val >= V2:Val => boolValue(cmpHolds(#ge, V1, V2))
    requires seqOrderComparable(V1, V2)
  rule setVal(VS1:ValItems) >= setVal(VS2:ValItems) =>
    boolValue(cmpHolds(#ge, setVal(VS1), setVal(VS2)))
  rule set() >= set() => True
  rule set() >= setVal(_:ValItems) => False
  rule setVal(_:ValItems) >= set() => True
  rule V1:Val == V2:Val => boolValue(valEq(V1, V2))
  rule V1:Val != V2:Val => boolValue(notBool valEq(V1, V2))
  rule V1:Val is V2:Val => boolValue(valIs(V1, V2))
  rule V1:Val is not V2:Val => boolValue(notBool valIs(V1, V2))
  rule <k> compareChainExp(Left:Exp, Chain:CmpChain) =>
           Left ~> compareChain(Chain)
       ... </k>
  rule <k> L:Val ~> compareChain(cmpChainLast(Op:CmpOp, Right:Exp)) =>
           Right ~> compareChainLast(Op, L)
       ... </k>
  rule <k> R:Val ~> compareChainLast(Op:CmpOp, L:Val) =>
           boolValue(cmpHolds(Op, L, R))
       ... </k>
  rule <k> L:Val ~> compareChain(cmpChainCons(Op:CmpOp, Right:Exp, Rest:CmpChain)) =>
           Right ~> compareChainNext(Op, L, Rest)
       ... </k>
  rule <k> R:Val ~> compareChainNext(Op:CmpOp, L:Val, Rest:CmpChain) =>
           compareFrom(R, Rest)
       ... </k>
    requires cmpHolds(Op, L, R)
  rule <k> R:Val ~> compareChainNext(Op:CmpOp, L:Val, _:CmpChain) =>
           False
       ... </k>
    requires notBool cmpHolds(Op, L, R)
  rule <k> compareFrom(L:Val, Chain:CmpChain) =>
           L ~> compareChain(Chain)
       ... </k>
  rule Needle:String in Haystack:String => boolValue(findString(Haystack, Needle, 0) >=Int 0)
  rule _V:Val in [] => False
  rule V:Val in listVal(VS:ValItems) => boolValue(containsVal(V, VS))
  rule _V:Val in () => False
  rule V:Val in tupleVal(VS:ValItems) => boolValue(containsVal(V, VS))
  rule _V:Val in {} => False
  rule V:Val in dictVal(DS:DictItems) => boolValue(containsKey(V, DS))
  rule _V:Val in set() => False
  rule V:Val in setVal(VS:ValItems) => boolValue(containsVal(V, VS))
  rule V:Val in rangeVal(Start:Int, Stop:Int) => boolValue(rangeContains(V, Start, Stop))
  rule V:Val in rangeVal(Start:Int, Stop:Int, Step:Int) => boolValue(rangeContains(V, Start, Stop, Step))
  rule Needle:String not in Haystack:String => boolValue(findString(Haystack, Needle, 0) <Int 0)
  rule _V:Val not in [] => True
  rule V:Val not in listVal(VS:ValItems) => boolValue(notBool containsVal(V, VS))
  rule _V:Val not in () => True
  rule V:Val not in tupleVal(VS:ValItems) => boolValue(notBool containsVal(V, VS))
  rule _V:Val not in {} => True
  rule V:Val not in dictVal(DS:DictItems) => boolValue(notBool containsKey(V, DS))
  rule _V:Val not in set() => True
  rule V:Val not in setVal(VS:ValItems) => boolValue(notBool containsVal(V, VS))
  rule V:Val not in rangeVal(Start:Int, Stop:Int) => boolValue(notBool rangeContains(V, Start, Stop))
  rule V:Val not in rangeVal(Start:Int, Stop:Int, Step:Int) => boolValue(notBool rangeContains(V, Start, Stop, Step))
  rule subscriptExp(S:String, I:Val) => substrString(S, intValue(I), intValue(I) +Int 1)
    requires isIntLike(I) andBool intValue(I) >=Int 0 andBool intValue(I) <Int lengthString(S)
  rule subscriptExp(S:String, I:Val) =>
    substrString(S, lengthString(S) +Int intValue(I), lengthString(S) +Int intValue(I) +Int 1)
    requires isIntLike(I)
     andBool intValue(I) <Int 0
     andBool lengthString(S) +Int intValue(I) >=Int 0
  rule subscriptExp(rangeVal(Start:Int, Stop:Int), I:Val) =>
    rangeGet(Start, Stop, 1, intValue(I))
    requires isIntLike(I)
     andBool intValue(I) >=Int 0
     andBool intValue(I) <Int pyRangeLen(Start, Stop, 1)
  rule subscriptExp(rangeVal(Start:Int, Stop:Int), I:Val) =>
    rangeGet(Start, Stop, 1, pyRangeLen(Start, Stop, 1) +Int intValue(I))
    requires isIntLike(I)
     andBool intValue(I) <Int 0
     andBool pyRangeLen(Start, Stop, 1) +Int intValue(I) >=Int 0
  rule subscriptExp(rangeVal(Start:Int, Stop:Int, Step:Int), I:Val) =>
    rangeGet(Start, Stop, Step, intValue(I))
    requires isIntLike(I)
     andBool Step =/=Int 0
     andBool intValue(I) >=Int 0
     andBool intValue(I) <Int pyRangeLen(Start, Stop, Step)
  rule subscriptExp(rangeVal(Start:Int, Stop:Int, Step:Int), I:Val) =>
    rangeGet(Start, Stop, Step, pyRangeLen(Start, Stop, Step) +Int intValue(I))
    requires isIntLike(I)
     andBool Step =/=Int 0
     andBool intValue(I) <Int 0
     andBool pyRangeLen(Start, Stop, Step) +Int intValue(I) >=Int 0
  rule subscriptExp(listVal(VS:ValItems), I:Val) => listGet(VS, intValue(I))
    requires isIntLike(I) andBool intValue(I) >=Int 0
  rule subscriptExp(listVal(VS:ValItems), I:Val) => listGet(VS, valItemsLen(VS) +Int intValue(I))
    requires isIntLike(I)
     andBool intValue(I) <Int 0
     andBool valItemsLen(VS) +Int intValue(I) >=Int 0
  rule subscriptExp(tupleVal(VS:ValItems), I:Val) => listGet(VS, intValue(I))
    requires isIntLike(I) andBool intValue(I) >=Int 0
  rule subscriptExp(tupleVal(VS:ValItems), I:Val) => listGet(VS, valItemsLen(VS) +Int intValue(I))
    requires isIntLike(I)
     andBool intValue(I) <Int 0
     andBool valItemsLen(VS) +Int intValue(I) >=Int 0
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
  rule <k> argsVal(#noArgVals) ~> buildSet => set() ... </k>
  rule <k> argsVal(VS:ArgVals) ~> buildSet => setVal(argValsToSetItems(VS)) ... </k>
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

  rule #listCtor() => []
  rule #tupleCtor() => ()
  rule #dictCtor() => ({}):Val
  rule #setCtor() => set()
  rule #listCtor([]) => []
  rule #listCtor(listVal(VS:ValItems)) => listVal(VS)
  rule #listCtor(()) => []
  rule #listCtor(tupleVal(VS:ValItems)) => listVal(VS)
  rule #listCtor(S:String) => []
    requires lengthString(S) ==Int 0
  rule #listCtor(S:String) => listVal(stringToValItems(S, 0, lengthString(S)))
    requires lengthString(S) >Int 0
  rule #listCtor(({}):Val) => []
  rule #listCtor(dictVal(DS:DictItems)) => listVal(dictKeysToValItems(DS))
  rule #listCtor(rangeVal(Start:Int, Stop:Int)) => []
    requires pyRangeLen(Start, Stop, 1) ==Int 0
  rule #listCtor(rangeVal(Start:Int, Stop:Int)) =>
    listVal(rangeToValItems(Start, Stop, 1, 0, pyRangeLen(Start, Stop, 1)))
    requires pyRangeLen(Start, Stop, 1) >Int 0
  rule #listCtor(rangeVal(Start:Int, Stop:Int, Step:Int)) => []
    requires Step =/=Int 0 andBool pyRangeLen(Start, Stop, Step) ==Int 0
  rule #listCtor(rangeVal(Start:Int, Stop:Int, Step:Int)) =>
    listVal(rangeToValItems(Start, Stop, Step, 0, pyRangeLen(Start, Stop, Step)))
    requires Step =/=Int 0 andBool pyRangeLen(Start, Stop, Step) >Int 0
  rule #tupleCtor([]) => ()
  rule #tupleCtor(listVal(VS:ValItems)) => tupleVal(VS)
  rule #tupleCtor(()) => ()
  rule #tupleCtor(tupleVal(VS:ValItems)) => tupleVal(VS)
  rule #tupleCtor(S:String) => ()
    requires lengthString(S) ==Int 0
  rule #tupleCtor(S:String) => tupleVal(stringToValItems(S, 0, lengthString(S)))
    requires lengthString(S) >Int 0
  rule #tupleCtor(({}):Val) => ()
  rule #tupleCtor(dictVal(DS:DictItems)) => tupleVal(dictKeysToValItems(DS))
  rule #tupleCtor(rangeVal(Start:Int, Stop:Int)) => ()
    requires pyRangeLen(Start, Stop, 1) ==Int 0
  rule #tupleCtor(rangeVal(Start:Int, Stop:Int)) =>
    tupleVal(rangeToValItems(Start, Stop, 1, 0, pyRangeLen(Start, Stop, 1)))
    requires pyRangeLen(Start, Stop, 1) >Int 0
  rule #tupleCtor(rangeVal(Start:Int, Stop:Int, Step:Int)) => ()
    requires Step =/=Int 0 andBool pyRangeLen(Start, Stop, Step) ==Int 0
  rule #tupleCtor(rangeVal(Start:Int, Stop:Int, Step:Int)) =>
    tupleVal(rangeToValItems(Start, Stop, Step, 0, pyRangeLen(Start, Stop, Step)))
    requires Step =/=Int 0 andBool pyRangeLen(Start, Stop, Step) >Int 0
  rule #boolCtor() => False
  rule #boolCtor(V:Val) => boolValue(truthy(V))
  rule #all([]) => True
  rule #all(listVal(VS:ValItems)) => boolValue(allValItems(VS))
  rule #all(()) => True
  rule #all(tupleVal(VS:ValItems)) => boolValue(allValItems(VS))
  rule #all(_:String) => True
  rule #all(({}):Val) => True
  rule #all(dictVal(DS:DictItems)) => boolValue(allValItems(dictKeysToValItems(DS)))
  rule #all(set()) => True
  rule #all(setVal(VS:ValItems)) => boolValue(allValItems(VS))
  rule #all(rangeVal(Start:Int, Stop:Int)) => boolValue(rangeAllTruthy(Start, Stop, 1))
  rule #all(rangeVal(Start:Int, Stop:Int, Step:Int)) => boolValue(rangeAllTruthy(Start, Stop, Step))
    requires Step =/=Int 0
  rule #any([]) => False
  rule #any(listVal(VS:ValItems)) => boolValue(anyValItems(VS))
  rule #any(()) => False
  rule #any(tupleVal(VS:ValItems)) => boolValue(anyValItems(VS))
  rule #any(S:String) => boolValue(lengthString(S) >Int 0)
  rule #any(({}):Val) => False
  rule #any(dictVal(DS:DictItems)) => boolValue(anyValItems(dictKeysToValItems(DS)))
  rule #any(set()) => False
  rule #any(setVal(VS:ValItems)) => boolValue(anyValItems(VS))
  rule #any(rangeVal(Start:Int, Stop:Int)) => boolValue(rangeAnyTruthy(Start, Stop, 1))
  rule #any(rangeVal(Start:Int, Stop:Int, Step:Int)) => boolValue(rangeAnyTruthy(Start, Stop, Step))
    requires Step =/=Int 0
  rule #sum([]) => 0
  rule #sum(listVal(VS:ValItems)) => sumValItems(VS)
    requires valItemsAllIntLike(VS)
  rule #sum(()) => 0
  rule #sum(tupleVal(VS:ValItems)) => sumValItems(VS)
    requires valItemsAllIntLike(VS)
  rule #sum(({}):Val) => 0
  rule #sum(dictVal(DS:DictItems)) => sumValItems(dictKeysToValItems(DS))
    requires valItemsAllIntLike(dictKeysToValItems(DS))
  rule #sum(set()) => 0
  rule #sum(setVal(VS:ValItems)) => sumValItems(VS)
    requires valItemsAllIntLike(VS)
  rule #sum(rangeVal(Start:Int, Stop:Int)) => rangeSum(Start, Stop, 1)
  rule #sum(rangeVal(Start:Int, Stop:Int, Step:Int)) => rangeSum(Start, Stop, Step)
    requires Step =/=Int 0
  rule #sum([], Seed:Val) => Seed
    requires isIntLike(Seed)
  rule #sum(listVal(VS:ValItems), Seed:Val) => intValue(Seed) +Int sumValItems(VS)
    requires isIntLike(Seed) andBool valItemsAllIntLike(VS)
  rule #sum((), Seed:Val) => Seed
    requires isIntLike(Seed)
  rule #sum(tupleVal(VS:ValItems), Seed:Val) => intValue(Seed) +Int sumValItems(VS)
    requires isIntLike(Seed) andBool valItemsAllIntLike(VS)
  rule #sum(({}):Val, Seed:Val) => Seed
    requires isIntLike(Seed)
  rule #sum(dictVal(DS:DictItems), Seed:Val) => intValue(Seed) +Int sumValItems(dictKeysToValItems(DS))
    requires isIntLike(Seed) andBool valItemsAllIntLike(dictKeysToValItems(DS))
  rule #sum(set(), Seed:Val) => Seed
    requires isIntLike(Seed)
  rule #sum(setVal(VS:ValItems), Seed:Val) => intValue(Seed) +Int sumValItems(VS)
    requires isIntLike(Seed) andBool valItemsAllIntLike(VS)
  rule #sum(rangeVal(Start:Int, Stop:Int), Seed:Val) => Seed
    requires isIntLike(Seed) andBool pyRangeLen(Start, Stop, 1) ==Int 0
  rule #sum(rangeVal(Start:Int, Stop:Int), Seed:Val) => intValue(Seed) +Int rangeSum(Start, Stop, 1)
    requires isIntLike(Seed) andBool pyRangeLen(Start, Stop, 1) >Int 0
  rule #sum(rangeVal(Start:Int, Stop:Int, Step:Int), Seed:Val) => Seed
    requires isIntLike(Seed) andBool Step =/=Int 0 andBool pyRangeLen(Start, Stop, Step) ==Int 0
  rule #sum(rangeVal(Start:Int, Stop:Int, Step:Int), Seed:Val) => intValue(Seed) +Int rangeSum(Start, Stop, Step)
    requires isIntLike(Seed) andBool Step =/=Int 0 andBool pyRangeLen(Start, Stop, Step) >Int 0
  rule #min(listVal(VS:ValItems)) => minValItems(VS)
    requires valItemsAllIntLike(VS)
  rule #min(tupleVal(VS:ValItems)) => minValItems(VS)
    requires valItemsAllIntLike(VS)
  rule #min(dictVal(DS:DictItems)) => minValItems(dictKeysToValItems(DS))
    requires valItemsAllIntLike(dictKeysToValItems(DS))
  rule #min(setVal(VS:ValItems)) => minValItems(VS)
    requires valItemsAllIntLike(VS)
  rule #min(rangeVal(Start:Int, Stop:Int)) => rangeMin(Start, Stop, 1)
    requires pyRangeLen(Start, Stop, 1) >Int 0
  rule #min(rangeVal(Start:Int, Stop:Int, Step:Int)) => rangeMin(Start, Stop, Step)
    requires Step =/=Int 0 andBool pyRangeLen(Start, Stop, Step) >Int 0
  rule #max(listVal(VS:ValItems)) => maxValItems(VS)
    requires valItemsAllIntLike(VS)
  rule #max(tupleVal(VS:ValItems)) => maxValItems(VS)
    requires valItemsAllIntLike(VS)
  rule #max(dictVal(DS:DictItems)) => maxValItems(dictKeysToValItems(DS))
    requires valItemsAllIntLike(dictKeysToValItems(DS))
  rule #max(setVal(VS:ValItems)) => maxValItems(VS)
    requires valItemsAllIntLike(VS)
  rule #max(rangeVal(Start:Int, Stop:Int)) => rangeMax(Start, Stop, 1)
    requires pyRangeLen(Start, Stop, 1) >Int 0
  rule #max(rangeVal(Start:Int, Stop:Int, Step:Int)) => rangeMax(Start, Stop, Step)
    requires Step =/=Int 0 andBool pyRangeLen(Start, Stop, Step) >Int 0
  rule #intCtor() => 0
  rule #intCtor(V:Val) => intValue(V)
    requires isIntLike(V)
  rule #abs(V:Val) => 0 -Int intValue(V)
    requires isIntLike(V) andBool intValue(V) <Int 0
  rule #abs(V:Val) => intValue(V)
    requires isIntLike(V) andBool intValue(V) >=Int 0
  rule #divmod(V1:Val, V2:Val) =>
    tupleVal(valItemsCons(pyFloorDiv(intValue(V1), intValue(V2)), valItemsLast(pyModulo(intValue(V1), intValue(V2)))))
    requires isIntLike(V1) andBool isIntLike(V2) andBool intValue(V2) =/=Int 0
  rule #pow(V1:Val, V2:Val) => intValue(V1) ^Int intValue(V2)
    requires isIntLike(V1) andBool isIntLike(V2) andBool intValue(V2) >=Int 0

  rule range1Exp(N:Val) => rangeVal(0, intValue(N))
    requires isIntLike(N)
  rule range2Exp(Start:Val, Stop:Val) => rangeVal(intValue(Start), intValue(Stop))
    requires isIntLike(Start) andBool isIntLike(Stop)
  rule range3Exp(Start:Val, Stop:Val, Step:Val) => rangeVal(intValue(Start), intValue(Stop), intValue(Step))
    requires isIntLike(Start) andBool isIntLike(Stop) andBool isIntLike(Step) andBool intValue(Step) =/=Int 0

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

  rule <k> unpackAssignStmt(IDS:IdItems, listVal(VS:ValItems)) => stmtNoResult ... </k>
       <env> Rho => bindVals(Rho, IDS, VS) </env>
       <result> _ => .K </result>
    requires sameIdValArity(IDS, VS)
  rule <k> unpackAssignStmt(IDS:IdItems, tupleVal(VS:ValItems)) => stmtNoResult ... </k>
       <env> Rho => bindVals(Rho, IDS, VS) </env>
       <result> _ => .K </result>
    requires sameIdValArity(IDS, VS)

  rule <k> unpackStarAssignStmt(Prefix:IdItems, Star:Id, Suffix:IdItems, listVal(VS:ValItems)) => stmtNoResult ... </k>
       <env> Rho => bindStarUnpack(Rho, Prefix, Star, Suffix, VS) </env>
       <result> _ => .K </result>
    requires starUnpackArityOk(Prefix, Suffix, valItemsLen(VS))
  rule <k> unpackStarAssignStmt(Prefix:IdItems, Star:Id, Suffix:IdItems, tupleVal(VS:ValItems)) => stmtNoResult ... </k>
       <env> Rho => bindStarUnpack(Rho, Prefix, Star, Suffix, VS) </env>
       <result> _ => .K </result>
    requires starUnpackArityOk(Prefix, Suffix, valItemsLen(VS))
  rule <k> unpackStarAssignStmt(Prefix:IdItems, Star:Id, Suffix:IdItems, []) => stmtNoResult ... </k>
       <env> Rho => Rho [ Star <- [] ] </env>
       <result> _ => .K </result>
    requires idItemsLen(Prefix) +Int idItemsLen(Suffix) ==Int 0
  rule <k> unpackStarAssignStmt(Prefix:IdItems, Star:Id, Suffix:IdItems, ()) => stmtNoResult ... </k>
       <env> Rho => Rho [ Star <- [] ] </env>
       <result> _ => .K </result>
    requires idItemsLen(Prefix) +Int idItemsLen(Suffix) ==Int 0

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

  rule <k> whileElseStmt(C:Exp, Body:Block, Else:Block) =>
           C ~> whileElseStmtBranch(C, Body, Else)
       ... </k>
  rule <k> V:Val ~> whileElseStmtBranch(C:Exp, block(SS:Stmts), Else:Block) =>
           SS ~> whileElseStmtAgain(C, block(SS), Else)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> whileElseStmtBranch(C:Exp, {}, Else:Block) =>
           whileElseStmt(C, {}, Else)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> whileElseStmtBranch(_:Exp, _:Block, Else:Block) =>
           runLoopElse(Else)
       ... </k>
    requires notBool truthy(V)
  rule <k> whileElseStmtAgain(C:Exp, Body:Block, Else:Block) =>
           whileElseStmt(C, Body, Else)
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
  rule <k> S:String ~> forIter(_:Id, _:Block) => stmtNoResult ... </k>
    requires lengthString(S) ==Int 0
  rule <k> S:String ~> forIter(X:Id, Body:Block) =>
           forItems(X, stringToValItems(S, 0, lengthString(S)), Body)
       ... </k>
    requires lengthString(S) >Int 0
  rule <k> rangeVal(Start:Int, Stop:Int) ~> forIter(X:Id, Body:Block) =>
           forRange(X, Start, Stop, Body)
       ... </k>
  rule <k> rangeVal(Start:Int, Stop:Int, Step:Int) ~> forIter(X:Id, Body:Block) =>
           forRangeStep(X, Start, Stop, Step, Body)
       ... </k>
    requires Step =/=Int 0
  rule <k> ({}):Val ~> forIter(_:Id, _:Block) => stmtNoResult ... </k>
  rule <k> dictVal(DS:DictItems) ~> forIter(X:Id, Body:Block) =>
           forItems(X, dictKeysToValItems(DS), Body)
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

  rule <k> forUnpackStmt(IDS:IdItems, E:Exp, Body:Block) =>
           E ~> forUnpackIter(IDS, Body)
       ... </k>
  rule <k> [] ~> forUnpackIter(_:IdItems, _:Block) => stmtNoResult ... </k>
  rule <k> listVal(VS:ValItems) ~> forUnpackIter(IDS:IdItems, Body:Block) =>
           forUnpackItems(IDS, VS, Body)
       ... </k>
  rule <k> () ~> forUnpackIter(_:IdItems, _:Block) => stmtNoResult ... </k>
  rule <k> tupleVal(VS:ValItems) ~> forUnpackIter(IDS:IdItems, Body:Block) =>
           forUnpackItems(IDS, VS, Body)
       ... </k>

  rule <k> forUnpackItems(IDS:IdItems, valItemsCons(listVal(VS:ValItems), Rest:ValItems), block(SS:Stmts)) =>
           SS ~> forUnpackItems(IDS, Rest, block(SS))
       ... </k>
       <env> Rho => bindVals(Rho, IDS, VS) </env>
    requires sameIdValArity(IDS, VS)
  rule <k> forUnpackItems(IDS:IdItems, valItemsCons(tupleVal(VS:ValItems), Rest:ValItems), block(SS:Stmts)) =>
           SS ~> forUnpackItems(IDS, Rest, block(SS))
       ... </k>
       <env> Rho => bindVals(Rho, IDS, VS) </env>
    requires sameIdValArity(IDS, VS)
  rule <k> forUnpackItems(IDS:IdItems, valItemsLast(listVal(VS:ValItems)), block(SS:Stmts)) =>
           SS ~> forDone
       ... </k>
       <env> Rho => bindVals(Rho, IDS, VS) </env>
    requires sameIdValArity(IDS, VS)
  rule <k> forUnpackItems(IDS:IdItems, valItemsLast(tupleVal(VS:ValItems)), block(SS:Stmts)) =>
           SS ~> forDone
       ... </k>
       <env> Rho => bindVals(Rho, IDS, VS) </env>
    requires sameIdValArity(IDS, VS)
  rule <k> forUnpackItems(IDS:IdItems, valItemsCons(listVal(VS:ValItems), Rest:ValItems), {}) =>
           forUnpackItems(IDS, Rest, {})
       ... </k>
       <env> Rho => bindVals(Rho, IDS, VS) </env>
    requires sameIdValArity(IDS, VS)
  rule <k> forUnpackItems(IDS:IdItems, valItemsCons(tupleVal(VS:ValItems), Rest:ValItems), {}) =>
           forUnpackItems(IDS, Rest, {})
       ... </k>
       <env> Rho => bindVals(Rho, IDS, VS) </env>
    requires sameIdValArity(IDS, VS)
  rule <k> forUnpackItems(IDS:IdItems, valItemsLast(listVal(VS:ValItems)), {}) =>
           stmtNoResult
       ... </k>
       <env> Rho => bindVals(Rho, IDS, VS) </env>
    requires sameIdValArity(IDS, VS)
  rule <k> forUnpackItems(IDS:IdItems, valItemsLast(tupleVal(VS:ValItems)), {}) =>
           stmtNoResult
       ... </k>
       <env> Rho => bindVals(Rho, IDS, VS) </env>
    requires sameIdValArity(IDS, VS)

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

  rule <k> forRangeStep(X:Id, I:Int, Stop:Int, Step:Int, block(SS:Stmts)) =>
           SS ~> forRangeStepAgain(X, I +Int Step, Stop, Step, block(SS))
       ... </k>
       <env> Rho => Rho [ X <- I ] </env>
    requires (Step >Int 0 andBool I <Int Stop)
      orBool (Step <Int 0 andBool I >Int Stop)
  rule <k> forRangeStep(X:Id, I:Int, Stop:Int, Step:Int, {}) =>
           forRangeStep(X, I +Int Step, Stop, Step, {})
       ... </k>
       <env> Rho => Rho [ X <- I ] </env>
    requires (Step >Int 0 andBool I <Int Stop)
      orBool (Step <Int 0 andBool I >Int Stop)
  rule <k> forRangeStep(_:Id, I:Int, Stop:Int, Step:Int, _:Block) => stmtNoResult ... </k>
    requires (Step >Int 0 andBool I >=Int Stop)
      orBool (Step <Int 0 andBool I <=Int Stop)
  rule <k> forRangeStepAgain(X:Id, I:Int, Stop:Int, Step:Int, Body:Block) =>
           forRangeStep(X, I, Stop, Step, Body)
       ... </k>

  rule <k> forElseStmt(X:Id, E:Exp, Body:Block, Else:Block) =>
           E ~> forElseIter(X, Body, Else)
       ... </k>
  rule <k> [] ~> forElseIter(_:Id, _:Block, Else:Block) => runLoopElse(Else) ... </k>
  rule <k> listVal(VS:ValItems) ~> forElseIter(X:Id, Body:Block, Else:Block) =>
           forElseItems(X, VS, Body, Else)
       ... </k>
  rule <k> () ~> forElseIter(_:Id, _:Block, Else:Block) => runLoopElse(Else) ... </k>
  rule <k> tupleVal(VS:ValItems) ~> forElseIter(X:Id, Body:Block, Else:Block) =>
           forElseItems(X, VS, Body, Else)
       ... </k>
  rule <k> S:String ~> forElseIter(_:Id, _:Block, Else:Block) => runLoopElse(Else) ... </k>
    requires lengthString(S) ==Int 0
  rule <k> S:String ~> forElseIter(X:Id, Body:Block, Else:Block) =>
           forElseItems(X, stringToValItems(S, 0, lengthString(S)), Body, Else)
       ... </k>
    requires lengthString(S) >Int 0
  rule <k> rangeVal(Start:Int, Stop:Int) ~> forElseIter(X:Id, Body:Block, Else:Block) =>
           forElseRange(X, Start, Stop, Body, Else)
       ... </k>
  rule <k> rangeVal(Start:Int, Stop:Int, Step:Int) ~> forElseIter(X:Id, Body:Block, Else:Block) =>
           forElseRangeStep(X, Start, Stop, Step, Body, Else)
       ... </k>
    requires Step =/=Int 0
  rule <k> ({}):Val ~> forElseIter(_:Id, _:Block, Else:Block) => runLoopElse(Else) ... </k>
  rule <k> dictVal(DS:DictItems) ~> forElseIter(X:Id, Body:Block, Else:Block) =>
           forElseItems(X, dictKeysToValItems(DS), Body, Else)
       ... </k>

  rule <k> forElseItems(X:Id, valItemsCons(V:Val, VS:ValItems), block(SS:Stmts), Else:Block) =>
           SS ~> forElseItems(X, VS, block(SS), Else)
       ... </k>
       <env> Rho => Rho [ X <- V ] </env>
  rule <k> forElseItems(X:Id, valItemsLast(V:Val), block(SS:Stmts), Else:Block) =>
           SS ~> forElseDone(Else)
       ... </k>
       <env> Rho => Rho [ X <- V ] </env>
  rule <k> forElseItems(X:Id, valItemsCons(V:Val, VS:ValItems), {}, Else:Block) =>
           forElseItems(X, VS, {}, Else)
       ... </k>
       <env> Rho => Rho [ X <- V ] </env>
  rule <k> forElseItems(X:Id, valItemsLast(V:Val), {}, Else:Block) =>
           runLoopElse(Else)
       ... </k>
       <env> Rho => Rho [ X <- V ] </env>
  rule <k> forElseDone(Else:Block) => runLoopElse(Else) ... </k>

  rule <k> forUnpackElseStmt(IDS:IdItems, E:Exp, Body:Block, Else:Block) =>
           E ~> forUnpackElseIter(IDS, Body, Else)
       ... </k>
  rule <k> [] ~> forUnpackElseIter(_:IdItems, _:Block, Else:Block) => runLoopElse(Else) ... </k>
  rule <k> listVal(VS:ValItems) ~> forUnpackElseIter(IDS:IdItems, Body:Block, Else:Block) =>
           forUnpackElseItems(IDS, VS, Body, Else)
       ... </k>
  rule <k> () ~> forUnpackElseIter(_:IdItems, _:Block, Else:Block) => runLoopElse(Else) ... </k>
  rule <k> tupleVal(VS:ValItems) ~> forUnpackElseIter(IDS:IdItems, Body:Block, Else:Block) =>
           forUnpackElseItems(IDS, VS, Body, Else)
       ... </k>

  rule <k> forUnpackElseItems(IDS:IdItems, valItemsCons(listVal(VS:ValItems), Rest:ValItems), block(SS:Stmts), Else:Block) =>
           SS ~> forUnpackElseItems(IDS, Rest, block(SS), Else)
       ... </k>
       <env> Rho => bindVals(Rho, IDS, VS) </env>
    requires sameIdValArity(IDS, VS)
  rule <k> forUnpackElseItems(IDS:IdItems, valItemsCons(tupleVal(VS:ValItems), Rest:ValItems), block(SS:Stmts), Else:Block) =>
           SS ~> forUnpackElseItems(IDS, Rest, block(SS), Else)
       ... </k>
       <env> Rho => bindVals(Rho, IDS, VS) </env>
    requires sameIdValArity(IDS, VS)
  rule <k> forUnpackElseItems(IDS:IdItems, valItemsLast(listVal(VS:ValItems)), block(SS:Stmts), Else:Block) =>
           SS ~> forUnpackElseDone(Else)
       ... </k>
       <env> Rho => bindVals(Rho, IDS, VS) </env>
    requires sameIdValArity(IDS, VS)
  rule <k> forUnpackElseItems(IDS:IdItems, valItemsLast(tupleVal(VS:ValItems)), block(SS:Stmts), Else:Block) =>
           SS ~> forUnpackElseDone(Else)
       ... </k>
       <env> Rho => bindVals(Rho, IDS, VS) </env>
    requires sameIdValArity(IDS, VS)
  rule <k> forUnpackElseItems(IDS:IdItems, valItemsCons(listVal(VS:ValItems), Rest:ValItems), {}, Else:Block) =>
           forUnpackElseItems(IDS, Rest, {}, Else)
       ... </k>
       <env> Rho => bindVals(Rho, IDS, VS) </env>
    requires sameIdValArity(IDS, VS)
  rule <k> forUnpackElseItems(IDS:IdItems, valItemsCons(tupleVal(VS:ValItems), Rest:ValItems), {}, Else:Block) =>
           forUnpackElseItems(IDS, Rest, {}, Else)
       ... </k>
       <env> Rho => bindVals(Rho, IDS, VS) </env>
    requires sameIdValArity(IDS, VS)
  rule <k> forUnpackElseItems(IDS:IdItems, valItemsLast(listVal(VS:ValItems)), {}, Else:Block) =>
           runLoopElse(Else)
       ... </k>
       <env> Rho => bindVals(Rho, IDS, VS) </env>
    requires sameIdValArity(IDS, VS)
  rule <k> forUnpackElseItems(IDS:IdItems, valItemsLast(tupleVal(VS:ValItems)), {}, Else:Block) =>
           runLoopElse(Else)
       ... </k>
       <env> Rho => bindVals(Rho, IDS, VS) </env>
    requires sameIdValArity(IDS, VS)
  rule <k> forUnpackElseDone(Else:Block) => runLoopElse(Else) ... </k>

  rule <k> forElseRange(X:Id, I:Int, Stop:Int, block(SS:Stmts), Else:Block) =>
           SS ~> forElseRangeAgain(X, I +Int 1, Stop, block(SS), Else)
       ... </k>
       <env> Rho => Rho [ X <- I ] </env>
    requires I <Int Stop
  rule <k> forElseRange(X:Id, I:Int, Stop:Int, {}, Else:Block) =>
           forElseRange(X, I +Int 1, Stop, {}, Else)
       ... </k>
       <env> Rho => Rho [ X <- I ] </env>
    requires I <Int Stop
  rule <k> forElseRange(_:Id, I:Int, Stop:Int, _:Block, Else:Block) => runLoopElse(Else) ... </k>
    requires I >=Int Stop
  rule <k> forElseRangeAgain(X:Id, I:Int, Stop:Int, Body:Block, Else:Block) =>
           forElseRange(X, I, Stop, Body, Else)
       ... </k>

  rule <k> forElseRangeStep(X:Id, I:Int, Stop:Int, Step:Int, block(SS:Stmts), Else:Block) =>
           SS ~> forElseRangeStepAgain(X, I +Int Step, Stop, Step, block(SS), Else)
       ... </k>
       <env> Rho => Rho [ X <- I ] </env>
    requires (Step >Int 0 andBool I <Int Stop)
      orBool (Step <Int 0 andBool I >Int Stop)
  rule <k> forElseRangeStep(X:Id, I:Int, Stop:Int, Step:Int, {}, Else:Block) =>
           forElseRangeStep(X, I +Int Step, Stop, Step, {}, Else)
       ... </k>
       <env> Rho => Rho [ X <- I ] </env>
    requires (Step >Int 0 andBool I <Int Stop)
      orBool (Step <Int 0 andBool I >Int Stop)
  rule <k> forElseRangeStep(_:Id, I:Int, Stop:Int, Step:Int, _:Block, Else:Block) => runLoopElse(Else) ... </k>
    requires (Step >Int 0 andBool I >=Int Stop)
      orBool (Step <Int 0 andBool I <=Int Stop)
  rule <k> forElseRangeStepAgain(X:Id, I:Int, Stop:Int, Step:Int, Body:Block, Else:Block) =>
           forElseRangeStep(X, I, Stop, Step, Body, Else)
       ... </k>

  rule <k> runLoopElse(block(SS:Stmts)) => SS ~> ifStmtDone ... </k>
  rule <k> runLoopElse({}) => stmtNoResult ... </k>

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
  rule <k> breakSignal ~> whileElseStmtAgain(_:Exp, _:Block, _:Block) => stmtNoResult ... </k>
  rule <k> continueSignal ~> whileElseStmtAgain(C:Exp, Body:Block, Else:Block) =>
           whileElseStmt(C, Body, Else)
       ... </k>
  rule <k> returnSignal(V:Val) ~> whileElseStmtAgain(_:Exp, _:Block, _:Block) => returnSignal(V) ... </k>
  rule <k> breakSignal ~> forItems(_:Id, _:ValItems, _:Block) => stmtNoResult ... </k>
  rule <k> breakSignal ~> forDone => stmtNoResult ... </k>
  rule <k> continueSignal ~> forItems(X:Id, VS:ValItems, Body:Block) =>
           forItems(X, VS, Body)
       ... </k>
  rule <k> continueSignal ~> forDone => stmtNoResult ... </k>
  rule <k> returnSignal(V:Val) ~> forItems(_:Id, _:ValItems, _:Block) => returnSignal(V) ... </k>
  rule <k> returnSignal(V:Val) ~> forDone => returnSignal(V) ... </k>
  rule <k> breakSignal ~> forUnpackItems(_:IdItems, _:ValItems, _:Block) => stmtNoResult ... </k>
  rule <k> continueSignal ~> forUnpackItems(IDS:IdItems, VS:ValItems, Body:Block) =>
           forUnpackItems(IDS, VS, Body)
       ... </k>
  rule <k> returnSignal(V:Val) ~> forUnpackItems(_:IdItems, _:ValItems, _:Block) => returnSignal(V) ... </k>
  rule <k> breakSignal ~> forRangeAgain(_:Id, _:Int, _:Int, _:Block) => stmtNoResult ... </k>
  rule <k> continueSignal ~> forRangeAgain(X:Id, I:Int, Stop:Int, Body:Block) =>
           forRange(X, I, Stop, Body)
       ... </k>
  rule <k> returnSignal(V:Val) ~> forRangeAgain(_:Id, _:Int, _:Int, _:Block) => returnSignal(V) ... </k>
  rule <k> breakSignal ~> forRangeStepAgain(_:Id, _:Int, _:Int, _:Int, _:Block) => stmtNoResult ... </k>
  rule <k> continueSignal ~> forRangeStepAgain(X:Id, I:Int, Stop:Int, Step:Int, Body:Block) =>
           forRangeStep(X, I, Stop, Step, Body)
       ... </k>
  rule <k> returnSignal(V:Val) ~> forRangeStepAgain(_:Id, _:Int, _:Int, _:Int, _:Block) => returnSignal(V) ... </k>
  rule <k> breakSignal ~> forElseItems(_:Id, _:ValItems, _:Block, _:Block) => stmtNoResult ... </k>
  rule <k> breakSignal ~> forElseDone(_:Block) => stmtNoResult ... </k>
  rule <k> continueSignal ~> forElseItems(X:Id, VS:ValItems, Body:Block, Else:Block) =>
           forElseItems(X, VS, Body, Else)
       ... </k>
  rule <k> continueSignal ~> forElseDone(Else:Block) => runLoopElse(Else) ... </k>
  rule <k> returnSignal(V:Val) ~> forElseItems(_:Id, _:ValItems, _:Block, _:Block) => returnSignal(V) ... </k>
  rule <k> returnSignal(V:Val) ~> forElseDone(_:Block) => returnSignal(V) ... </k>
  rule <k> breakSignal ~> forUnpackElseItems(_:IdItems, _:ValItems, _:Block, _:Block) => stmtNoResult ... </k>
  rule <k> breakSignal ~> forUnpackElseDone(_:Block) => stmtNoResult ... </k>
  rule <k> continueSignal ~> forUnpackElseItems(IDS:IdItems, VS:ValItems, Body:Block, Else:Block) =>
           forUnpackElseItems(IDS, VS, Body, Else)
       ... </k>
  rule <k> continueSignal ~> forUnpackElseDone(Else:Block) => runLoopElse(Else) ... </k>
  rule <k> returnSignal(V:Val) ~> forUnpackElseItems(_:IdItems, _:ValItems, _:Block, _:Block) => returnSignal(V) ... </k>
  rule <k> returnSignal(V:Val) ~> forUnpackElseDone(_:Block) => returnSignal(V) ... </k>
  rule <k> breakSignal ~> forElseRangeAgain(_:Id, _:Int, _:Int, _:Block, _:Block) => stmtNoResult ... </k>
  rule <k> continueSignal ~> forElseRangeAgain(X:Id, I:Int, Stop:Int, Body:Block, Else:Block) =>
           forElseRange(X, I, Stop, Body, Else)
       ... </k>
  rule <k> returnSignal(V:Val) ~> forElseRangeAgain(_:Id, _:Int, _:Int, _:Block, _:Block) => returnSignal(V) ... </k>
  rule <k> breakSignal ~> forElseRangeStepAgain(_:Id, _:Int, _:Int, _:Int, _:Block, _:Block) => stmtNoResult ... </k>
  rule <k> continueSignal ~> forElseRangeStepAgain(X:Id, I:Int, Stop:Int, Step:Int, Body:Block, Else:Block) =>
           forElseRangeStep(X, I, Stop, Step, Body, Else)
       ... </k>
  rule <k> returnSignal(V:Val) ~> forElseRangeStepAgain(_:Id, _:Int, _:Int, _:Int, _:Block, _:Block) => returnSignal(V) ... </k>
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
