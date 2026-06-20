requires "domains.md"

module PYTHON-SYNTAX
  imports INT-SYNTAX
  imports ID-SYNTAX
  imports STRING-SYNTAX
  imports FLOAT-SYNTAX

  syntax Val ::= Int
               | Float
               | String
               | "True" [symbol(pyTrue)]
               | "False" [symbol(pyFalse)]
               | "None" [symbol(pyNone)]
               | "Ellipsis" [symbol(pyEllipsis)]
               | "[" "]" [symbol(emptyListVal)]
               | "[" ValItems "]" [symbol(listVal)]
               | "(" ")" [symbol(emptyTupleVal)]
               | "(" ValItems ")" [symbol(tupleVal)]
               | "{" "}" [symbol(emptyDictVal)]
               | "{" DictItems "}" [symbol(dictVal)]
               | "set" "(" ")" [symbol(emptySetVal)]
               | "{" ValItems "}" [symbol(setVal)]
               | "#kwDefaultMissing" [symbol(kwDefaultMissing)]

  syntax ValItems ::= Val "," [symbol(valItemsLast)]
                    | Val "," ValItems [symbol(valItemsCons)]

  syntax DictItems ::= Val ":" Val "," [symbol(dictItemsLast)]
                     | Val ":" Val "," DictItems [symbol(dictItemsCons)]

  syntax IdItems ::= "#id" "(" Id ")" [symbol(idItemsLast)]
                   | "#noIds" [symbol(noIdItems)]
                   | "#ids" "(" Id "," IdItems ")" [symbol(idItemsCons)]

  syntax Target ::= "#targetName" "(" Id ")" [symbol(targetName)]
                  | "#targetSeq" "(" Targets ")" [symbol(targetSeq)]

  syntax Targets ::= "#targetLast" "(" Target ")" [symbol(targetsLast)]
                   | "#targetCons" "(" Target "," Targets ")" [symbol(targetsCons)]

  syntax ArgExps ::= "#noArgs" [symbol(noArgExps)]
                   | "#arg" "(" Exp ")" [symbol(argExp)]
                   | "#args" "(" Exp "," ArgExps ")" [symbol(argExpsCons)]
                   | "#starArg" "(" Exp ")" [symbol(starArgExp)]
                   | "#starArgs" "(" Exp "," ArgExps ")" [symbol(starArgExpsCons)]

  syntax KwArgExps ::= "#noKwArgs" [symbol(noKwArgExps)]
                     | "#kwArg" "(" Id "," Exp ")" [symbol(kwArgExp)]
                     | "#kwArgs" "(" Id "," Exp "," KwArgExps ")" [symbol(kwArgExpsCons)]
                     | "#kwStarArg" "(" Exp ")" [symbol(kwStarArgExp)]
                     | "#kwStarArgs" "(" Exp "," KwArgExps ")" [symbol(kwStarArgExpsCons)]

  syntax DictExps ::= "#noDictItems" [symbol(noDictExps)]
                    | "#dictItem" "(" Exp "," Exp ")" [symbol(dictExpItem)]
                    | "#dictItems" "(" Exp "," Exp "," DictExps ")" [symbol(dictExpsCons)]
                    | "#dictStarItem" "(" Exp ")" [symbol(dictStarExpItem)]
                    | "#dictStarItems" "(" Exp "," DictExps ")" [symbol(dictStarExpsCons)]

  syntax CompFilters ::= "#filter" "(" Exp ")" [symbol(compFilterLast)]
                       | "#filters" "(" Exp "," CompFilters ")" [symbol(compFiltersCons)]

  syntax MaybeCompFilters ::= "#noFilters" [symbol(noCompFilters)]
                            | CompFilters

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
                | "#assertMsg" "(" Exp "," Exp ")" [symbol(assertMsgStmt), strict(1)]
                | "global" Id [symbol(globalStmt)]
                | "#globalMany" "(" IdItems ")" [symbol(globalManyStmt)]
                | "del" Id [symbol(delNameStmt)]
                | "#delMany" "(" IdItems ")" [symbol(delManyStmt)]
                | Id "=" Exp [symbol(assignStmt), strict(2)]
                | Id "+=" Exp [symbol(augAddStmt)]
                | Id "-=" Exp [symbol(augSubStmt)]
                | Id "*=" Exp [symbol(augMulStmt)]
                | Id "/=" Exp [symbol(augTrueDivStmt)]
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
                | "#unpackTargetAssign" "(" Targets ";" Exp ")" [symbol(unpackTargetAssignStmt), strict(2)]
                | "return" [symbol(returnNoneStmt)]
                | "return" Exp [symbol(returnStmt), strict]
                | "#def" "(" Id "," Id "," Block ")" [symbol(functionDefStmt)]
                | "#defArgs" "(" Id "," IdItems "," Block ")" [symbol(functionDefArgsStmt)]
                | "#defDefaults" "(" Id "," IdItems "," ArgExps "," Block ")" [symbol(functionDefDefaultsStmt)]
                | "#defVarArgs" "(" Id "," IdItems "," Id "," Block ")" [symbol(functionDefVarArgsStmt)]
                | "#defVarArgsDefaults" "(" Id "," IdItems "," ArgExps "," Id "," Block ")" [symbol(functionDefVarArgsDefaultsStmt)]
                | "#defKwArgs" "(" Id "," IdItems "," Id "," Block ")" [symbol(functionDefKwArgsStmt)]
                | "#defPosOnly" "(" Id "," IdItems "," IdItems "," Block ")" [symbol(functionDefPosOnlyStmt)]
                | "#defKwOnly" "(" Id "," IdItems "," Block ")" [symbol(functionDefKwOnlyStmt)]
                | "#defKwDefaults" "(" Id "," IdItems "," ArgExps "," Block ")" [symbol(functionDefKwDefaultsStmt)]
                | "#defPosKwOnly" "(" Id "," IdItems "," IdItems "," Block ")" [symbol(functionDefPosKwOnlyStmt)]
                | "#defPosKwDefaults" "(" Id "," IdItems "," ArgExps "," IdItems "," ArgExps "," Block ")" [symbol(functionDefPosKwDefaultsStmt)]
                | "#if" "(" Exp "," Block "," Block ")" [symbol(ifStmt)]
                | "#while" "(" Exp "," Block ")" [symbol(whileStmt)]
                | "#whileElse" "(" Exp "," Block "," Block ")" [symbol(whileElseStmt)]
                | "#for" "(" Id "," Exp "," Block ")" [symbol(forStmt)]
                | "#forElse" "(" Id "," Exp "," Block "," Block ")" [symbol(forElseStmt)]
                | "#forUnpack" "(" IdItems "," Exp "," Block ")" [symbol(forUnpackStmt)]
                | "#forUnpackElse" "(" IdItems "," Exp "," Block "," Block ")" [symbol(forUnpackElseStmt)]
                | "#forTargetUnpack" "(" Targets "," Exp "," Block ")" [symbol(forTargetUnpackStmt)]
                | "#forTargetUnpackElse" "(" Targets "," Exp "," Block "," Block ")" [symbol(forTargetUnpackElseStmt)]
                | "#forStarUnpack" "(" IdItems "," Id "," IdItems "," Exp "," Block ")" [symbol(forStarUnpackStmt)]
                | "#forStarUnpackElse" "(" IdItems "," Id "," IdItems "," Exp "," Block "," Block ")" [symbol(forStarUnpackElseStmt)]

  syntax Exp ::= Val
               | Id
               | "#debug" [symbol(debugExp)]
               | "#namedExpr" "(" Id "," Exp ")" [symbol(namedExprExp), strict(2)]
               | "(" Exp ")" [bracket]
               | Exp "(" Exp ")" [symbol(callExp)]
               | "#call" "(" Exp "," ArgExps ")" [symbol(callArgsExp)]
               | "#callKw" "(" Exp "," KwArgExps ")" [symbol(callKwArgsExp)]
               | "#callMixed" "(" Exp "," ArgExps "," KwArgExps ")" [symbol(callMixedArgsExp)]
               | "#attr" "(" Exp "," Id ")" [symbol(attrExp), strict(1)]
               | "#list" "(" ArgExps ")" [symbol(listDisplayExp)]
               | "#tuple" "(" ArgExps ")" [symbol(tupleDisplayExp)]
               | "#dict" "(" DictExps ")" [symbol(dictDisplayExp)]
               | "#set" "(" ArgExps ")" [symbol(setDisplayExp)]
               | "#listComp" "(" Exp "," Id "," Exp ")" [symbol(listCompExp), strict(1)]
               | "#listCompIf" "(" Exp "," Id "," Exp "," Exp ")" [symbol(listCompIfExp), strict(1)]
               | "#listCompIfs" "(" Exp "," Id "," CompFilters "," Exp ")" [symbol(listCompIfsExp), strict(1)]
               | "#listCompFor" "(" Exp "," Id "," Exp "," Id "," Exp ")" [symbol(listCompForExp), strict(1)]
               | "#listCompForIfs" "(" Exp "," Id "," MaybeCompFilters "," Exp "," Id "," MaybeCompFilters "," Exp ")" [symbol(listCompForIfsExp), strict(1)]
               | "#listCompForFor" "(" Exp "," Id "," Exp "," Id "," Exp "," Id "," Exp ")" [symbol(listCompForForExp), strict(1)]
               | "#listCompForForIfs" "(" Exp "," Id "," MaybeCompFilters "," Exp "," Id "," MaybeCompFilters "," Exp "," Id "," MaybeCompFilters "," Exp ")" [symbol(listCompForForIfsExp), strict(1)]
               | "#dictComp" "(" Exp "," Id "," Exp "," Exp ")" [symbol(dictCompExp), strict(1)]
               | "#dictCompIf" "(" Exp "," Id "," Exp "," Exp "," Exp ")" [symbol(dictCompIfExp), strict(1)]
               | "#dictCompIfs" "(" Exp "," Id "," CompFilters "," Exp "," Exp ")" [symbol(dictCompIfsExp), strict(1)]
               | "#dictCompFor" "(" Exp "," Id "," Exp "," Id "," Exp "," Exp ")" [symbol(dictCompForExp), strict(1)]
               | "#dictCompForIfs" "(" Exp "," Id "," MaybeCompFilters "," Exp "," Id "," MaybeCompFilters "," Exp "," Exp ")" [symbol(dictCompForIfsExp), strict(1)]
               | "#dictCompForFor" "(" Exp "," Id "," Exp "," Id "," Exp "," Id "," Exp "," Exp ")" [symbol(dictCompForForExp), strict(1)]
               | "#dictCompForForIfs" "(" Exp "," Id "," MaybeCompFilters "," Exp "," Id "," MaybeCompFilters "," Exp "," Id "," MaybeCompFilters "," Exp "," Exp ")" [symbol(dictCompForForIfsExp), strict(1)]
               | "#setComp" "(" Exp "," Id "," Exp ")" [symbol(setCompExp), strict(1)]
               | "#setCompIf" "(" Exp "," Id "," Exp "," Exp ")" [symbol(setCompIfExp), strict(1)]
               | "#setCompIfs" "(" Exp "," Id "," CompFilters "," Exp ")" [symbol(setCompIfsExp), strict(1)]
               | "#setCompFor" "(" Exp "," Id "," Exp "," Id "," Exp ")" [symbol(setCompForExp), strict(1)]
               | "#setCompForIfs" "(" Exp "," Id "," MaybeCompFilters "," Exp "," Id "," MaybeCompFilters "," Exp ")" [symbol(setCompForIfsExp), strict(1)]
               | "#setCompForFor" "(" Exp "," Id "," Exp "," Id "," Exp "," Id "," Exp ")" [symbol(setCompForForExp), strict(1)]
               | "#setCompForForIfs" "(" Exp "," Id "," MaybeCompFilters "," Exp "," Id "," MaybeCompFilters "," Exp "," Id "," MaybeCompFilters "," Exp ")" [symbol(setCompForForIfsExp), strict(1)]
               | "#listCtor" "(" ")" [symbol(listCtorExp)]
               | "#listCtor" "(" Exp ")" [symbol(listCtor1Exp), strict]
               | "#tupleCtor" "(" ")" [symbol(tupleCtorExp)]
               | "#tupleCtor" "(" Exp ")" [symbol(tupleCtor1Exp), strict]
               | "#dictCtor" "(" ")" [symbol(dictCtorExp)]
               | "#dictCtor" "(" Exp ")" [symbol(dictCtor1Exp), strict]
               | "#dictCtorKw" "(" KwArgExps ")" [symbol(dictCtorKwExp)]
               | "#dictCtorMixed" "(" Exp "," KwArgExps ")" [symbol(dictCtorMixedExp), strict(1)]
               | "#setCtor" "(" ")" [symbol(setCtorExp)]
               | "#setCtor" "(" Exp ")" [symbol(setCtor1Exp), strict]
               | "#boolCtor" "(" ")" [symbol(boolCtor0Exp)]
               | "#boolCtor" "(" Exp ")" [symbol(boolCtor1Exp), strict]
               | "#all" "(" Exp ")" [symbol(allExp), strict]
               | "#any" "(" Exp ")" [symbol(anyExp), strict]
               | "#sum" "(" Exp ")" [symbol(sum1Exp), strict]
               | "#sum" "(" Exp "," Exp ")" [symbol(sum2Exp), strict]
               | "#min" "(" Exp ")" [symbol(minExp), strict]
               | "#max" "(" Exp ")" [symbol(maxExp), strict]
               | "#minArgs" "(" ArgExps ")" [symbol(minArgsExp)]
               | "#maxArgs" "(" ArgExps ")" [symbol(maxArgsExp)]
               | "#sliceCtor" "(" Exp ")" [symbol(sliceCtor1Exp), strict]
               | "#sliceCtor" "(" Exp "," Exp ")" [symbol(sliceCtor2Exp), strict]
               | "#sliceCtor" "(" Exp "," Exp "," Exp ")" [symbol(sliceCtor3Exp), strict]
               | "#intCtor" "(" ")" [symbol(intCtor0Exp)]
               | "#intCtor" "(" Exp ")" [symbol(intCtor1Exp), strict]
               | "#floatCtor" "(" ")" [symbol(floatCtor0Exp)]
               | "#floatCtor" "(" Exp ")" [symbol(floatCtor1Exp), strict]
               | "#abs" "(" Exp ")" [symbol(absExp), strict]
               | "#divmod" "(" Exp "," Exp ")" [symbol(divmodExp), strict]
               | "#pow" "(" Exp "," Exp ")" [symbol(powBuiltinExp), strict]
               | "#pow" "(" Exp "," Exp "," Exp ")" [symbol(powModBuiltinExp), strict]
               | "#compareChain" "(" Exp "," CmpChain ")" [symbol(compareChainExp)]
               | "#len" "(" Exp ")" [symbol(lenExp), strict]
               | "#floorDiv" "(" Exp "," Exp ")" [symbol(floorDivInternal), strict]
               | "#trueDiv" "(" Exp "," Exp ")" [symbol(trueDivInternal), strict]
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
               | "#lambdaDefaults" "(" IdItems "," ArgExps "," Exp ")" [symbol(lambdaDefaultsExp)]
               | "#lambdaVarArgs" "(" IdItems "," Id "," Exp ")" [symbol(lambdaVarArgsExp)]
               | "#lambdaVarArgsDefaults" "(" IdItems "," ArgExps "," Id "," Exp ")" [symbol(lambdaVarArgsDefaultsExp)]
               | "#lambdaKwArgs" "(" IdItems "," Id "," Exp ")" [symbol(lambdaKwArgsExp)]
               | "#lambdaPosOnly" "(" IdItems "," IdItems "," Exp ")" [symbol(lambdaPosOnlyExp)]
               | "#lambdaKwOnly" "(" IdItems "," Exp ")" [symbol(lambdaKwOnlyExp)]
               | "#lambdaKwDefaults" "(" IdItems "," ArgExps "," Exp ")" [symbol(lambdaKwDefaultsExp)]
               | "#lambdaPosKwOnly" "(" IdItems "," IdItems "," Exp ")" [symbol(lambdaPosKwOnlyExp)]
               | "#lambdaPosKwDefaults" "(" IdItems "," ArgExps "," IdItems "," ArgExps "," Exp ")" [symbol(lambdaPosKwDefaultsExp)]
endmodule

module PYTHON
  imports PYTHON-SYNTAX
  imports INT
  imports BOOL
  imports STRING
  imports ID
  imports FLOAT
  imports MAP

  syntax Val ::= closure(Id, Exp) [symbol(closure)]
               | closureArgs(IdItems, Exp) [symbol(closureArgs)]
               | closureDefaults(IdItems, ArgVals, Exp) [symbol(closureDefaults)]
               | closureVarArgs(IdItems, Id, Exp) [symbol(closureVarArgs)]
               | closureVarArgsDefaults(IdItems, ArgVals, Id, Exp) [symbol(closureVarArgsDefaults)]
               | closureKwArgs(IdItems, Id, Exp) [symbol(closureKwArgs)]
               | closurePosOnly(IdItems, IdItems, Exp) [symbol(closurePosOnly)]
               | closureKwOnly(IdItems, Exp) [symbol(closureKwOnly)]
               | closureKwDefaults(IdItems, ArgVals, Exp) [symbol(closureKwDefaults)]
               | closurePosKwOnly(IdItems, IdItems, Exp) [symbol(closurePosKwOnly)]
               | closurePosKwDefaults(IdItems, ArgVals, IdItems, ArgVals, Exp) [symbol(closurePosKwDefaults)]
               | functionVal(Id, Block) [symbol(functionVal)]
               | functionValArgs(IdItems, Block) [symbol(functionValArgs)]
               | functionValDefaults(IdItems, ArgVals, Block) [symbol(functionValDefaults)]
               | functionValVarArgs(IdItems, Id, Block) [symbol(functionValVarArgs)]
               | functionValVarArgsDefaults(IdItems, ArgVals, Id, Block) [symbol(functionValVarArgsDefaults)]
               | functionValKwArgs(IdItems, Id, Block) [symbol(functionValKwArgs)]
               | functionValPosOnly(IdItems, IdItems, Block) [symbol(functionValPosOnly)]
               | functionValKwOnly(IdItems, Block) [symbol(functionValKwOnly)]
               | functionValKwDefaults(IdItems, ArgVals, Block) [symbol(functionValKwDefaults)]
               | functionValPosKwOnly(IdItems, IdItems, Block) [symbol(functionValPosKwOnly)]
               | functionValPosKwDefaults(IdItems, ArgVals, IdItems, ArgVals, Block) [symbol(functionValPosKwDefaults)]
               | rangeVal(Int, Int) [symbol(rangeVal)]
               | rangeVal(Int, Int, Int) [symbol(rangeValStep)]
               | sliceVal(Val, Val, Val) [symbol(sliceVal)]
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
                 | evalStarArgNext(ArgExps, ArgVals) [symbol(evalStarArgNext)]
                 | callApplyArgs(Val) [symbol(callApplyArgs)]
                 | callKwArgs(KwArgExps) [symbol(callKwArgs)]
                 | evalKwArgs(KwArgExps, KwArgVals) [symbol(evalKwArgs)]
                 | evalKwArgNext(Id, KwArgExps, KwArgVals) [symbol(evalKwArgNext)]
                 | evalKwStarArgNext(KwArgExps, KwArgVals) [symbol(evalKwStarArgNext)]
                 | callApplyKwArgs(Val) [symbol(callApplyKwArgs)]
                 | kwArgsVal(KwArgVals) [symbol(kwArgsVal)]
                 | callMixedArgs(ArgExps, KwArgExps) [symbol(callMixedArgs)]
                 | evalMixedKwArgs(KwArgExps, Val) [symbol(evalMixedKwArgs)]
                 | callApplyMixedArgs(Val, ArgVals) [symbol(callApplyMixedArgs)]
                 | bindLambdaDefaults(IdItems, Exp) [symbol(bindLambdaDefaults)]
                 | bindLambdaVarArgsDefaults(IdItems, Id, Exp) [symbol(bindLambdaVarArgsDefaults)]
                 | bindLambdaKwDefaults(IdItems, Exp) [symbol(bindLambdaKwDefaults)]
                 | bindLambdaPosKwDefaults(IdItems, ArgExps, IdItems, Exp) [symbol(bindLambdaPosKwDefaults)]
                 | bindLambdaPosKwDefaultVals(IdItems, ArgVals, IdItems, Exp) [symbol(bindLambdaPosKwDefaultVals)]
                 | "buildList" [symbol(buildList)]
                 | listCompIter(Id, Exp, ArgVals, ArgVals, Map) [symbol(listCompIter)]
                 | listCompNext(Id, Exp, ArgVals, ArgVals, Map) [symbol(listCompNext)]
                 | listCompIfIter(Id, Exp, Exp, ArgVals, ArgVals, Map) [symbol(listCompIfIter)]
                 | listCompIfFilter(Id, Exp, Exp, ArgVals, ArgVals, Map) [symbol(listCompIfFilter)]
                 | listCompIfNext(Id, Exp, Exp, ArgVals, ArgVals, Map) [symbol(listCompIfNext)]
                 | listCompIfsIter(Id, CompFilters, Exp, ArgVals, ArgVals, Map) [symbol(listCompIfsIter)]
                 | listCompIfsFilter(Id, CompFilters, CompFilters, Exp, ArgVals, ArgVals, Map) [symbol(listCompIfsFilter)]
                 | listCompIfsFilterNext(Id, CompFilters, CompFilters, Exp, ArgVals, ArgVals, Map) [symbol(listCompIfsFilterNext)]
                 | listCompIfsFilterLast(Id, CompFilters, Exp, ArgVals, ArgVals, Map) [symbol(listCompIfsFilterLast)]
                 | listCompIfsNext(Id, CompFilters, Exp, ArgVals, ArgVals, Map) [symbol(listCompIfsNext)]
                 | listCompForIter(Id, Exp, Id, Exp, ArgVals, ArgVals, Map) [symbol(listCompForIter)]
                 | listCompForInner(Id, Exp, Id, Exp, ArgVals, ArgVals, Map) [symbol(listCompForInner)]
                 | listCompForInnerIter(Id, Exp, Id, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(listCompForInnerIter)]
                 | listCompForNext(Id, Exp, Id, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(listCompForNext)]
                 | listCompForIfsIter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, Map) [symbol(listCompForIfsIter)]
                 | listCompForIfsOuterFilter(Id, MaybeCompFilters, CompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, Map) [symbol(listCompForIfsOuterFilter)]
                 | listCompForIfsOuterFilterNext(Id, MaybeCompFilters, CompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, Map) [symbol(listCompForIfsOuterFilterNext)]
                 | listCompForIfsOuterFilterLast(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, Map) [symbol(listCompForIfsOuterFilterLast)]
                 | listCompForIfsInner(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, Map) [symbol(listCompForIfsInner)]
                 | listCompForIfsInnerIter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(listCompForIfsInnerIter)]
                 | listCompForIfsInnerFilter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, CompFilters, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(listCompForIfsInnerFilter)]
                 | listCompForIfsInnerFilterNext(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, CompFilters, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(listCompForIfsInnerFilterNext)]
                 | listCompForIfsInnerFilterLast(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(listCompForIfsInnerFilterLast)]
                 | listCompForIfsNext(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(listCompForIfsNext)]
                 | listCompForForIter(Id, Exp, Id, Exp, Id, Exp, ArgVals, ArgVals, Map) [symbol(listCompForForIter)]
                 | listCompForForMiddle(Id, Exp, Id, Exp, Id, Exp, ArgVals, ArgVals, Map) [symbol(listCompForForMiddle)]
                 | listCompForForMiddleIter(Id, Exp, Id, Exp, Id, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(listCompForForMiddleIter)]
                 | listCompForForInner(Id, Exp, Id, Exp, Id, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(listCompForForInner)]
                 | listCompForForInnerIter(Id, Exp, Id, Exp, Id, Exp, ArgVals, ArgVals, ArgVals, ArgVals, Map) [symbol(listCompForForInnerIter)]
                 | listCompForForNext(Id, Exp, Id, Exp, Id, Exp, ArgVals, ArgVals, ArgVals, ArgVals, Map) [symbol(listCompForForNext)]
                 | listCompForForIfsIter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, Map) [symbol(listCompForForIfsIter)]
                 | listCompForForIfsOuterFilter(Id, MaybeCompFilters, CompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, Map) [symbol(listCompForForIfsOuterFilter)]
                 | listCompForForIfsOuterFilterNext(Id, MaybeCompFilters, CompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, Map) [symbol(listCompForForIfsOuterFilterNext)]
                 | listCompForForIfsOuterFilterLast(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, Map) [symbol(listCompForForIfsOuterFilterLast)]
                 | listCompForForIfsMiddle(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, Map) [symbol(listCompForForIfsMiddle)]
                 | listCompForForIfsMiddleIter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(listCompForForIfsMiddleIter)]
                 | listCompForForIfsMiddleFilter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, CompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(listCompForForIfsMiddleFilter)]
                 | listCompForForIfsMiddleFilterNext(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, CompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(listCompForForIfsMiddleFilterNext)]
                 | listCompForForIfsMiddleFilterLast(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(listCompForForIfsMiddleFilterLast)]
                 | listCompForForIfsInner(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(listCompForForIfsInner)]
                 | listCompForForIfsInnerIter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, ArgVals, ArgVals, Map) [symbol(listCompForForIfsInnerIter)]
                 | listCompForForIfsInnerFilter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, CompFilters, Exp, ArgVals, ArgVals, ArgVals, ArgVals, Map) [symbol(listCompForForIfsInnerFilter)]
                 | listCompForForIfsInnerFilterNext(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, CompFilters, Exp, ArgVals, ArgVals, ArgVals, ArgVals, Map) [symbol(listCompForForIfsInnerFilterNext)]
                 | listCompForForIfsInnerFilterLast(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, ArgVals, ArgVals, Map) [symbol(listCompForForIfsInnerFilterLast)]
                 | listCompForForIfsNext(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, ArgVals, ArgVals, Map) [symbol(listCompForForIfsNext)]
                 | setCompIter(Id, Exp, ArgVals, ArgVals, Map) [symbol(setCompIter)]
                 | setCompNext(Id, Exp, ArgVals, ArgVals, Map) [symbol(setCompNext)]
                 | setCompIfIter(Id, Exp, Exp, ArgVals, ArgVals, Map) [symbol(setCompIfIter)]
                 | setCompIfFilter(Id, Exp, Exp, ArgVals, ArgVals, Map) [symbol(setCompIfFilter)]
                 | setCompIfNext(Id, Exp, Exp, ArgVals, ArgVals, Map) [symbol(setCompIfNext)]
                 | setCompIfsIter(Id, CompFilters, Exp, ArgVals, ArgVals, Map) [symbol(setCompIfsIter)]
                 | setCompIfsFilter(Id, CompFilters, CompFilters, Exp, ArgVals, ArgVals, Map) [symbol(setCompIfsFilter)]
                 | setCompIfsFilterNext(Id, CompFilters, CompFilters, Exp, ArgVals, ArgVals, Map) [symbol(setCompIfsFilterNext)]
                 | setCompIfsFilterLast(Id, CompFilters, Exp, ArgVals, ArgVals, Map) [symbol(setCompIfsFilterLast)]
                 | setCompIfsNext(Id, CompFilters, Exp, ArgVals, ArgVals, Map) [symbol(setCompIfsNext)]
                 | setCompForIter(Id, Exp, Id, Exp, ArgVals, ArgVals, Map) [symbol(setCompForIter)]
                 | setCompForInner(Id, Exp, Id, Exp, ArgVals, ArgVals, Map) [symbol(setCompForInner)]
                 | setCompForInnerIter(Id, Exp, Id, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(setCompForInnerIter)]
                 | setCompForNext(Id, Exp, Id, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(setCompForNext)]
                 | setCompForForIter(Id, Exp, Id, Exp, Id, Exp, ArgVals, ArgVals, Map) [symbol(setCompForForIter)]
                 | setCompForForMiddle(Id, Exp, Id, Exp, Id, Exp, ArgVals, ArgVals, Map) [symbol(setCompForForMiddle)]
                 | setCompForForMiddleIter(Id, Exp, Id, Exp, Id, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(setCompForForMiddleIter)]
                 | setCompForForInner(Id, Exp, Id, Exp, Id, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(setCompForForInner)]
                 | setCompForForInnerIter(Id, Exp, Id, Exp, Id, Exp, ArgVals, ArgVals, ArgVals, ArgVals, Map) [symbol(setCompForForInnerIter)]
                 | setCompForForNext(Id, Exp, Id, Exp, Id, Exp, ArgVals, ArgVals, ArgVals, ArgVals, Map) [symbol(setCompForForNext)]
                 | setCompForForIfsIter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, Map) [symbol(setCompForForIfsIter)]
                 | setCompForForIfsOuterFilter(Id, MaybeCompFilters, CompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, Map) [symbol(setCompForForIfsOuterFilter)]
                 | setCompForForIfsOuterFilterNext(Id, MaybeCompFilters, CompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, Map) [symbol(setCompForForIfsOuterFilterNext)]
                 | setCompForForIfsOuterFilterLast(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, Map) [symbol(setCompForForIfsOuterFilterLast)]
                 | setCompForForIfsMiddle(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, Map) [symbol(setCompForForIfsMiddle)]
                 | setCompForForIfsMiddleIter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(setCompForForIfsMiddleIter)]
                 | setCompForForIfsMiddleFilter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, CompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(setCompForForIfsMiddleFilter)]
                 | setCompForForIfsMiddleFilterNext(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, CompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(setCompForForIfsMiddleFilterNext)]
                 | setCompForForIfsMiddleFilterLast(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(setCompForForIfsMiddleFilterLast)]
                 | setCompForForIfsInner(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(setCompForForIfsInner)]
                 | setCompForForIfsInnerIter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, ArgVals, ArgVals, Map) [symbol(setCompForForIfsInnerIter)]
                 | setCompForForIfsInnerFilter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, CompFilters, Exp, ArgVals, ArgVals, ArgVals, ArgVals, Map) [symbol(setCompForForIfsInnerFilter)]
                 | setCompForForIfsInnerFilterNext(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, CompFilters, Exp, ArgVals, ArgVals, ArgVals, ArgVals, Map) [symbol(setCompForForIfsInnerFilterNext)]
                 | setCompForForIfsInnerFilterLast(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, ArgVals, ArgVals, Map) [symbol(setCompForForIfsInnerFilterLast)]
                 | setCompForForIfsNext(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, ArgVals, ArgVals, Map) [symbol(setCompForForIfsNext)]
                 | setCompForIfsIter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, Map) [symbol(setCompForIfsIter)]
                 | setCompForIfsOuterFilter(Id, MaybeCompFilters, CompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, Map) [symbol(setCompForIfsOuterFilter)]
                 | setCompForIfsOuterFilterNext(Id, MaybeCompFilters, CompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, Map) [symbol(setCompForIfsOuterFilterNext)]
                 | setCompForIfsOuterFilterLast(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, Map) [symbol(setCompForIfsOuterFilterLast)]
                 | setCompForIfsInner(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, Map) [symbol(setCompForIfsInner)]
                 | setCompForIfsInnerIter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(setCompForIfsInnerIter)]
                 | setCompForIfsInnerFilter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, CompFilters, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(setCompForIfsInnerFilter)]
                 | setCompForIfsInnerFilterNext(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, CompFilters, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(setCompForIfsInnerFilterNext)]
                 | setCompForIfsInnerFilterLast(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(setCompForIfsInnerFilterLast)]
                 | setCompForIfsNext(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, ArgVals, ArgVals, ArgVals, Map) [symbol(setCompForIfsNext)]
                 | "buildTuple" [symbol(buildTuple)]
                 | "buildSet" [symbol(buildSet)]
                 | "minArgsResult" [symbol(minArgsResult)]
                 | "maxArgsResult" [symbol(maxArgsResult)]
                 | evalDict(DictExps, DictVals) [symbol(evalDict)]
                 | evalDictValue(Exp, DictExps, DictVals) [symbol(evalDictValue)]
                 | evalDictNext(DictExps, DictVals, Val) [symbol(evalDictNext)]
                 | evalDictStarNext(DictExps, DictVals) [symbol(evalDictStarNext)]
                 | "buildDict" [symbol(buildDict)]
                 | "buildDictCtorKw" [symbol(buildDictCtorKw)]
                 | buildDictCtorMixed(Val) [symbol(buildDictCtorMixed)]
                 | dictCompIter(Id, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompIter)]
                 | dictCompKey(Id, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompKey)]
                 | dictCompValue(Id, Exp, Exp, ArgVals, DictVals, Map, Val) [symbol(dictCompValue)]
                 | dictCompIfIter(Id, Exp, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompIfIter)]
                 | dictCompIfFilter(Id, Exp, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompIfFilter)]
                 | dictCompIfKey(Id, Exp, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompIfKey)]
                 | dictCompIfValue(Id, Exp, Exp, Exp, ArgVals, DictVals, Map, Val) [symbol(dictCompIfValue)]
                 | dictCompIfsIter(Id, CompFilters, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompIfsIter)]
                 | dictCompIfsFilter(Id, CompFilters, CompFilters, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompIfsFilter)]
                 | dictCompIfsFilterNext(Id, CompFilters, CompFilters, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompIfsFilterNext)]
                 | dictCompIfsFilterLast(Id, CompFilters, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompIfsFilterLast)]
                 | dictCompIfsKey(Id, CompFilters, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompIfsKey)]
                 | dictCompIfsValue(Id, CompFilters, Exp, Exp, ArgVals, DictVals, Map, Val) [symbol(dictCompIfsValue)]
                 | dictCompForIter(Id, Exp, Id, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompForIter)]
                 | dictCompForInner(Id, Exp, Id, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompForInner)]
                 | dictCompForInnerIter(Id, Exp, Id, Exp, Exp, ArgVals, ArgVals, DictVals, Map) [symbol(dictCompForInnerIter)]
                 | dictCompForKey(Id, Exp, Id, Exp, Exp, ArgVals, ArgVals, DictVals, Map) [symbol(dictCompForKey)]
                 | dictCompForValue(Id, Exp, Id, Exp, Exp, ArgVals, ArgVals, DictVals, Map, Val) [symbol(dictCompForValue)]
                 | dictCompForForIter(Id, Exp, Id, Exp, Id, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompForForIter)]
                 | dictCompForForMiddle(Id, Exp, Id, Exp, Id, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompForForMiddle)]
                 | dictCompForForMiddleIter(Id, Exp, Id, Exp, Id, Exp, Exp, ArgVals, ArgVals, DictVals, Map) [symbol(dictCompForForMiddleIter)]
                 | dictCompForForInner(Id, Exp, Id, Exp, Id, Exp, Exp, ArgVals, ArgVals, DictVals, Map) [symbol(dictCompForForInner)]
                 | dictCompForForInnerIter(Id, Exp, Id, Exp, Id, Exp, Exp, ArgVals, ArgVals, ArgVals, DictVals, Map) [symbol(dictCompForForInnerIter)]
                 | dictCompForForKey(Id, Exp, Id, Exp, Id, Exp, Exp, ArgVals, ArgVals, ArgVals, DictVals, Map) [symbol(dictCompForForKey)]
                 | dictCompForForValue(Id, Exp, Id, Exp, Id, Exp, Exp, ArgVals, ArgVals, ArgVals, DictVals, Map, Val) [symbol(dictCompForForValue)]
                 | dictCompForForIfsIter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompForForIfsIter)]
                 | dictCompForForIfsOuterFilter(Id, MaybeCompFilters, CompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompForForIfsOuterFilter)]
                 | dictCompForForIfsOuterFilterNext(Id, MaybeCompFilters, CompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompForForIfsOuterFilterNext)]
                 | dictCompForForIfsOuterFilterLast(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompForForIfsOuterFilterLast)]
                 | dictCompForForIfsMiddle(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompForForIfsMiddle)]
                 | dictCompForForIfsMiddleIter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Exp, ArgVals, ArgVals, DictVals, Map) [symbol(dictCompForForIfsMiddleIter)]
                 | dictCompForForIfsMiddleFilter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, CompFilters, Exp, Id, MaybeCompFilters, Exp, Exp, ArgVals, ArgVals, DictVals, Map) [symbol(dictCompForForIfsMiddleFilter)]
                 | dictCompForForIfsMiddleFilterNext(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, CompFilters, Exp, Id, MaybeCompFilters, Exp, Exp, ArgVals, ArgVals, DictVals, Map) [symbol(dictCompForForIfsMiddleFilterNext)]
                 | dictCompForForIfsMiddleFilterLast(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Exp, ArgVals, ArgVals, DictVals, Map) [symbol(dictCompForForIfsMiddleFilterLast)]
                 | dictCompForForIfsInner(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Exp, ArgVals, ArgVals, DictVals, Map) [symbol(dictCompForForIfsInner)]
                 | dictCompForForIfsInnerIter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Exp, ArgVals, ArgVals, ArgVals, DictVals, Map) [symbol(dictCompForForIfsInnerIter)]
                 | dictCompForForIfsInnerFilter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, CompFilters, Exp, Exp, ArgVals, ArgVals, ArgVals, DictVals, Map) [symbol(dictCompForForIfsInnerFilter)]
                 | dictCompForForIfsInnerFilterNext(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, CompFilters, Exp, Exp, ArgVals, ArgVals, ArgVals, DictVals, Map) [symbol(dictCompForForIfsInnerFilterNext)]
                 | dictCompForForIfsInnerFilterLast(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Exp, ArgVals, ArgVals, ArgVals, DictVals, Map) [symbol(dictCompForForIfsInnerFilterLast)]
                 | dictCompForForIfsKey(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Exp, ArgVals, ArgVals, ArgVals, DictVals, Map) [symbol(dictCompForForIfsKey)]
                 | dictCompForForIfsValue(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Exp, ArgVals, ArgVals, ArgVals, DictVals, Map, Val) [symbol(dictCompForForIfsValue)]
                 | dictCompForIfsIter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompForIfsIter)]
                 | dictCompForIfsOuterFilter(Id, MaybeCompFilters, CompFilters, Exp, Id, MaybeCompFilters, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompForIfsOuterFilter)]
                 | dictCompForIfsOuterFilterNext(Id, MaybeCompFilters, CompFilters, Exp, Id, MaybeCompFilters, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompForIfsOuterFilterNext)]
                 | dictCompForIfsOuterFilterLast(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompForIfsOuterFilterLast)]
                 | dictCompForIfsInner(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Exp, ArgVals, DictVals, Map) [symbol(dictCompForIfsInner)]
                 | dictCompForIfsInnerIter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Exp, ArgVals, ArgVals, DictVals, Map) [symbol(dictCompForIfsInnerIter)]
                 | dictCompForIfsInnerFilter(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, CompFilters, Exp, Exp, ArgVals, ArgVals, DictVals, Map) [symbol(dictCompForIfsInnerFilter)]
                 | dictCompForIfsInnerFilterNext(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, CompFilters, Exp, Exp, ArgVals, ArgVals, DictVals, Map) [symbol(dictCompForIfsInnerFilterNext)]
                 | dictCompForIfsInnerFilterLast(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Exp, ArgVals, ArgVals, DictVals, Map) [symbol(dictCompForIfsInnerFilterLast)]
                 | dictCompForIfsKey(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Exp, ArgVals, ArgVals, DictVals, Map) [symbol(dictCompForIfsKey)]
                 | dictCompForIfsValue(Id, MaybeCompFilters, Exp, Id, MaybeCompFilters, Exp, Exp, ArgVals, ArgVals, DictVals, Map, Val) [symbol(dictCompForIfsValue)]
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
                 | forTargetUnpackIter(Targets, Block) [symbol(forTargetUnpackIter)]
                 | forTargetUnpackItems(Targets, ValItems, Block) [symbol(forTargetUnpackItems)]
                 | forStarUnpackIter(IdItems, Id, IdItems, Block) [symbol(forStarUnpackIter)]
                 | forStarUnpackItems(IdItems, Id, IdItems, ValItems, Block) [symbol(forStarUnpackItems)]
                 | forRange(Id, Int, Int, Block) [symbol(forRange)]
                 | forRangeAgain(Id, Int, Int, Block) [symbol(forRangeAgain)]
                 | forRangeStep(Id, Int, Int, Int, Block) [symbol(forRangeStep)]
                 | forRangeStepAgain(Id, Int, Int, Int, Block) [symbol(forRangeStepAgain)]
                 | forElseIter(Id, Block, Block) [symbol(forElseIter)]
                 | forElseItems(Id, ValItems, Block, Block) [symbol(forElseItems)]
                 | forElseDone(Block) [symbol(forElseDone)]
                 | forUnpackElseIter(IdItems, Block, Block) [symbol(forUnpackElseIter)]
                 | forUnpackElseItems(IdItems, ValItems, Block, Block) [symbol(forUnpackElseItems)]
                 | forTargetUnpackElseIter(Targets, Block, Block) [symbol(forTargetUnpackElseIter)]
                 | forTargetUnpackElseItems(Targets, ValItems, Block, Block) [symbol(forTargetUnpackElseItems)]
                 | forUnpackElseDone(Block) [symbol(forUnpackElseDone)]
                 | forStarUnpackElseIter(IdItems, Id, IdItems, Block, Block) [symbol(forStarUnpackElseIter)]
                 | forStarUnpackElseItems(IdItems, Id, IdItems, ValItems, Block, Block) [symbol(forStarUnpackElseItems)]
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
                 | bindFunctionDefaults(Id, IdItems, Block) [symbol(bindFunctionDefaults)]
                 | bindFunctionVarArgsDefaults(Id, IdItems, Id, Block) [symbol(bindFunctionVarArgsDefaults)]
                 | bindFunctionKwDefaults(Id, IdItems, Block) [symbol(bindFunctionKwDefaults)]
                 | bindFunctionPosKwDefaults(Id, IdItems, ArgExps, IdItems, Block) [symbol(bindFunctionPosKwDefaults)]
                 | bindFunctionPosKwDefaultVals(Id, IdItems, ArgVals, IdItems, Block) [symbol(bindFunctionPosKwDefaultVals)]
                 | assignMany(IdItems, Val) [symbol(assignMany)]

  syntax Bool ::= truthy(Val) [function, symbol(truthy)]
                | isIntLike(Val) [function, symbol(isIntLike)]
                | isFloatLike(Val) [function, symbol(isFloatLike)]
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
                | varArgsCallArityOk(IdItems, ArgVals) [function, symbol(varArgsCallArityOk)]
                | varArgsDefaultsCallArityOk(IdItems, ArgVals, ArgVals) [function, symbol(varArgsDefaultsCallArityOk)]
                | varArgsMixedCallArityOk(IdItems, ArgVals, KwArgVals) [function, symbol(varArgsMixedCallArityOk)]
                | varArgsMixedDefaultsCallArityOk(IdItems, ArgVals, KwArgVals, ArgVals) [function, symbol(varArgsMixedDefaultsCallArityOk)]
                | varArgsMixedNoPosKeyword(IdItems, ArgVals, KwArgVals) [function, symbol(varArgsMixedNoPosKeyword)]
                | varArgsMixedRequiredPresent(IdItems, ArgVals, KwArgVals) [function, symbol(varArgsMixedRequiredPresent)]
                | kwargsPosCallArityOk(IdItems, ArgVals) [function, symbol(kwargsPosCallArityOk)]
                | kwargsKeywordCallArityOk(IdItems, KwArgVals) [function, symbol(kwargsKeywordCallArityOk)]
                | kwargsMixedCallArityOk(IdItems, ArgVals, KwArgVals) [function, symbol(kwargsMixedCallArityOk)]
                | posOnlyArgsCallArityOk(IdItems, IdItems, ArgVals) [function, symbol(posOnlyArgsCallArityOk)]
                | posOnlyKeywordCallArityOk(IdItems, IdItems, KwArgVals) [function, symbol(posOnlyKeywordCallArityOk)]
                | posOnlyMixedCallArityOk(IdItems, IdItems, ArgVals, KwArgVals) [function, symbol(posOnlyMixedCallArityOk)]
                | sameIdValArity(IdItems, ValItems) [function, symbol(sameIdValArity)]
                | starUnpackArityOk(IdItems, IdItems, Int) [function, symbol(starUnpackArityOk)]
                | defaultsCallArityOk(IdItems, ArgVals, ArgVals) [function, symbol(defaultsCallArityOk)]
                | keywordOnlyCallArityOk(IdItems, KwArgVals, ArgVals) [function, symbol(keywordOnlyCallArityOk)]
                | mixedCallArityOk(IdItems, ArgVals, KwArgVals, ArgVals) [function, symbol(mixedCallArityOk)]
                | posKwOnlyArgsDefaultsCallArityOk(IdItems, IdItems, ArgVals, ArgVals, ArgVals) [function, symbol(posKwOnlyArgsDefaultsCallArityOk)]
                | posKwOnlyKeywordCallArityOk(IdItems, IdItems, KwArgVals) [function, symbol(posKwOnlyKeywordCallArityOk)]
                | posKwOnlyMixedCallArityOk(IdItems, IdItems, ArgVals, KwArgVals) [function, symbol(posKwOnlyMixedCallArityOk)]
                | posKwOnlyKeywordDefaultsCallArityOk(IdItems, IdItems, KwArgVals, ArgVals, ArgVals) [function, symbol(posKwOnlyKeywordDefaultsCallArityOk)]
                | posKwOnlyMixedDefaultsCallArityOk(IdItems, IdItems, ArgVals, KwArgVals, ArgVals, ArgVals) [function, symbol(posKwOnlyMixedDefaultsCallArityOk)]
                | mixedNoPosKeyword(IdItems, ArgVals, KwArgVals) [function, symbol(mixedNoPosKeyword)]
                | mixedRequiredPresent(IdItems, ArgVals, KwArgVals, ArgVals) [function, symbol(mixedRequiredPresent)]
                | sameTargetsValArity(Targets, ValItems) [function, symbol(sameTargetsValArity)]
                | targetValueArityOk(Target, Val) [function, symbol(targetValueArityOk)]
                | emptyArgVals(ArgVals) [function, symbol(emptyArgVals)]
                | emptyKwArgVals(KwArgVals) [function, symbol(emptyKwArgVals)]
                | emptyDictVals(DictVals) [function, symbol(emptyDictVals)]
                | idContains(Id, IdItems) [function, symbol(idContains)]
                | kwContains(Id, KwArgVals) [function, symbol(kwContains)]
                | kwStringContains(String, KwArgVals) [function, symbol(kwStringContains)]
                | kwNoDuplicates(KwArgVals) [function, symbol(kwNoDuplicates)]
                | kwAllInIds(KwArgVals, IdItems) [function, symbol(kwAllInIds)]
                | kwAllInEitherIds(KwArgVals, IdItems, IdItems) [function, symbol(kwAllInEitherIds)]
                | stringIdContains(String, IdItems) [function, symbol(stringIdContains)]
                | kwRequiredPresent(IdItems, KwArgVals, ArgVals) [function, symbol(kwRequiredPresent)]
                | kwRequiredAlignedPresent(IdItems, KwArgVals, ArgVals) [function, symbol(kwRequiredAlignedPresent)]
                | hasKwDefaultMissing(ArgVals) [function, symbol(hasKwDefaultMissing)]
                | isKwDefaultMissing(Val) [function, symbol(isKwDefaultMissing)]
                | containsVal(Val, ValItems) [function, symbol(containsVal)]
                | containsKey(Val, DictItems) [function, symbol(containsKey)]
                | rangeContains(Val, Int, Int) [function, symbol(rangeContains)]
                | rangeContains(Val, Int, Int, Int) [function, symbol(rangeContainsStep)]
                | rangeContainsFloat(Float, Int, Int, Int, Int) [function, symbol(rangeContainsFloat)]
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
               | argValsLen(ArgVals) [function, symbol(argValsLen)]
               | kwArgValsLen(KwArgVals) [function, symbol(kwArgValsLen)]
               | dictItemsLen(DictItems) [function, symbol(dictItemsLen)]
               | rangeGet(Int, Int, Int, Int) [function, symbol(rangeGet)]
               | sumValItems(ValItems) [function, symbol(sumValItems)]
               | rangeSum(Int, Int, Int) [function, symbol(rangeSum)]
               | minValItems(ValItems) [function, symbol(minValItems)]
               | maxValItems(ValItems) [function, symbol(maxValItems)]
               | minArgVals(ArgVals) [function, symbol(minArgVals)]
               | maxArgVals(ArgVals) [function, symbol(maxArgVals)]
               | rangeMin(Int, Int, Int) [function, symbol(rangeMin)]
               | rangeMax(Int, Int, Int) [function, symbol(rangeMax)]
  syntax Float ::= floatValue(Val) [function, symbol(floatValue)]
                 | pyFloatFloorDiv(Float, Float) [function, symbol(pyFloatFloorDiv)]
                 | pyFloatModulo(Float, Float) [function, symbol(pyFloatModulo)]
  syntax String ::= repeatString(String, Int) [function, symbol(repeatString)]
                  | sliceString(String, Int, Int) [function, symbol(sliceString)]
                  | sliceStepString(String, Int, Int, Int) [function, symbol(sliceStepString)]
  syntax ArgVals ::= "#noArgVals" [symbol(noArgVals)]
                   | argValsCons(Val, ArgVals) [symbol(argValsCons)]
                   | appendArgVal(ArgVals, Val) [function, symbol(appendArgVal)]
                   | concatArgVals(ArgVals, ArgVals) [function, symbol(concatArgVals)]
                   | dropArgVals(ArgVals, Int) [function, symbol(dropArgVals)]
                   | takeArgVals(ArgVals, Int) [function, symbol(takeArgVals)]
                   | varArgTail(ArgVals, Int) [function, symbol(varArgTail)]
                   | completeDefaultArgs(IdItems, ArgVals, ArgVals) [function, symbol(completeDefaultArgs)]
                   | completeVarArgsDefaultArgs(IdItems, ArgVals, ArgVals) [function, symbol(completeVarArgsDefaultArgs)]
                   | buildKwDefaultArgs(IdItems, KwArgVals, ArgVals) [function, symbol(buildKwDefaultArgs)]
                   | buildMixedDefaultArgs(IdItems, ArgVals, KwArgVals, ArgVals) [function, symbol(buildMixedDefaultArgs)]
                   | buildVarArgsMixedPosArgs(IdItems, ArgVals, KwArgVals) [function, symbol(buildVarArgsMixedPosArgs)]
                   | buildVarArgsMixedDefaultArgs(IdItems, ArgVals, KwArgVals, ArgVals) [function, symbol(buildVarArgsMixedDefaultArgs)]
                   | valItemsToArgVals(ValItems) [function, symbol(valItemsToArgVals)]
                   | iterableArgVals(Val) [function, symbol(iterableArgVals)]
  syntax Val ::= argValsToTupleVal(ArgVals) [function, symbol(argValsToTupleVal)]
               | setFromArgVals(ArgVals) [function, symbol(setFromArgVals)]
  syntax Val ::= kwExtrasDict(KwArgVals, IdItems) [function, symbol(kwExtrasDict)]
  syntax KwArgVals ::= "#noKwArgVals" [symbol(noKwArgVals)]
                     | kwArgValsCons(Id, Val, KwArgVals) [symbol(kwArgValsCons)]
                     | kwArgStringValsCons(String, Val, KwArgVals) [symbol(kwArgStringValsCons)]
                     | appendKwArgVal(KwArgVals, Id, Val) [function, symbol(appendKwArgVal)]
                     | appendKwStringArgVal(KwArgVals, String, Val) [function, symbol(appendKwStringArgVal)]
                     | appendKwUnpack(KwArgVals, Val) [function, symbol(appendKwUnpack)]
                     | appendKwDictItems(KwArgVals, DictItems) [function, symbol(appendKwDictItems)]
  syntax DictVals ::= "#noDictVals" [symbol(noDictVals)]
                    | dictValsCons(Val, Val, DictVals) [symbol(dictValsCons)]
                    | appendDictVal(DictVals, Val, Val) [function, symbol(appendDictVal)]
                    | appendDictUnpack(DictVals, Val) [function, symbol(appendDictUnpack)]
                    | appendDictItems(DictVals, DictItems) [function, symbol(appendDictItems)]
                    | appendDictPairVal(DictVals, Val) [function, symbol(appendDictPairVal)]
                    | dictCtorPairs(ValItems, DictVals) [function, symbol(dictCtorPairs)]
                    | appendKwDictVals(DictVals, KwArgVals) [function, symbol(appendKwDictVals)]
                    | kwExtrasDictVals(KwArgVals, IdItems) [function, symbol(kwExtrasDictVals)]
  syntax Map ::= bindArgs(Map, IdItems, ArgVals) [function, symbol(bindArgs)]
  syntax Map ::= bindVarArgs(Map, IdItems, Id, ArgVals) [function, symbol(bindVarArgs)]
  syntax Map ::= bindKwArgs(Map, IdItems, Id, ArgVals, KwArgVals) [function, symbol(bindKwArgs)]
  syntax Map ::= bindPosOnlyArgs(Map, IdItems, IdItems, ArgVals) [function, symbol(bindPosOnlyArgs)]
  syntax Map ::= bindPosOnlyMixedArgs(Map, IdItems, IdItems, ArgVals, KwArgVals) [function, symbol(bindPosOnlyMixedArgs)]
  syntax Map ::= bindVals(Map, IdItems, ValItems) [function, symbol(bindVals)]
  syntax Map ::= bindTarget(Map, Target, Val) [function, symbol(bindTarget)]
  syntax Map ::= bindTargets(Map, Targets, ValItems) [function, symbol(bindTargets)]
  syntax Map ::= delIds(Map, IdItems) [function, symbol(delIds)]
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
  syntax Val ::= dictFromDictVals(DictVals) [function, symbol(dictFromDictVals)]
  syntax Val ::= dictCtorFromPairs(ValItems) [function, symbol(dictCtorFromPairs)]
  syntax Val ::= dictCtorFromKwArgs(KwArgVals) [function, symbol(dictCtorFromKwArgs)]
  syntax Val ::= dictCtorMergeKw(Val, KwArgVals) [function, symbol(dictCtorMergeKw)]
  syntax Val ::= listSlice(ValItems, Int, Int) [function, symbol(listSlice)]
               | tupleSlice(ValItems, Int, Int) [function, symbol(tupleSlice)]
               | listSliceStep(ValItems, Int, Int, Int) [function, symbol(listSliceStep)]
               | tupleSliceStep(ValItems, Int, Int, Int) [function, symbol(tupleSliceStep)]
               | listGet(ValItems, Int) [function, symbol(listGet)]
               | rangeSlice(Int, Int, Int, Int, Int) [function, symbol(rangeSlice)]
               | rangeSliceStep(Int, Int, Int, Int, Int, Int) [function, symbol(rangeSliceStep)]
  syntax Val ::= dictGet(DictItems, Val) [function, symbol(dictGet)]
  syntax Val ::= kwLookup(Id, KwArgVals) [function, symbol(kwLookup)]
  syntax Val ::= boolValue(Bool) [function, symbol(boolValue)]

  rule truthy(0) => false
  rule truthy(I:Int) => true requires I =/=Int 0
  rule truthy(F:Float) => F =/=Float 0.0
  rule truthy(S:String) => lengthString(S) =/=Int 0
  rule truthy(True) => true
  rule truthy(False) => false
  rule truthy(None) => false
  rule truthy(Ellipsis) => true
  rule truthy([]) => false
  rule truthy(listVal(_:ValItems)) => true
  rule truthy(()) => false
  rule truthy(tupleVal(_:ValItems)) => true
  rule truthy({}) => false
  rule truthy(dictVal(_:DictItems)) => true
  rule truthy(set()) => false
  rule truthy(setVal(_:ValItems)) => true
  rule truthy(#kwDefaultMissing) => false
  rule truthy(closure(_:Id, _:Exp)) => true
  rule truthy(closureArgs(_:IdItems, _:Exp)) => true
  rule truthy(closureDefaults(_:IdItems, _:ArgVals, _:Exp)) => true
  rule truthy(closureVarArgs(_:IdItems, _:Id, _:Exp)) => true
  rule truthy(closureVarArgsDefaults(_:IdItems, _:ArgVals, _:Id, _:Exp)) => true
  rule truthy(closureKwArgs(_:IdItems, _:Id, _:Exp)) => true
  rule truthy(closurePosOnly(_:IdItems, _:IdItems, _:Exp)) => true
  rule truthy(closureKwOnly(_:IdItems, _:Exp)) => true
  rule truthy(closureKwDefaults(_:IdItems, _:ArgVals, _:Exp)) => true
  rule truthy(closurePosKwOnly(_:IdItems, _:IdItems, _:Exp)) => true
  rule truthy(closurePosKwDefaults(_:IdItems, _:ArgVals, _:IdItems, _:ArgVals, _:Exp)) => true
  rule truthy(functionVal(_:Id, _:Block)) => true
  rule truthy(functionValArgs(_:IdItems, _:Block)) => true
  rule truthy(functionValDefaults(_:IdItems, _:ArgVals, _:Block)) => true
  rule truthy(functionValVarArgs(_:IdItems, _:Id, _:Block)) => true
  rule truthy(functionValVarArgsDefaults(_:IdItems, _:ArgVals, _:Id, _:Block)) => true
  rule truthy(functionValKwArgs(_:IdItems, _:Id, _:Block)) => true
  rule truthy(functionValPosOnly(_:IdItems, _:IdItems, _:Block)) => true
  rule truthy(functionValKwOnly(_:IdItems, _:Block)) => true
  rule truthy(functionValKwDefaults(_:IdItems, _:ArgVals, _:Block)) => true
  rule truthy(functionValPosKwOnly(_:IdItems, _:IdItems, _:Block)) => true
  rule truthy(functionValPosKwDefaults(_:IdItems, _:ArgVals, _:IdItems, _:ArgVals, _:Block)) => true
  rule truthy(rangeVal(Start:Int, Stop:Int)) => Start <Int Stop
  rule truthy(rangeVal(Start:Int, Stop:Int, Step:Int)) => pyRangeLen(Start, Stop, Step) >Int 0
    requires Step =/=Int 0
  rule truthy(sliceVal(_:Val, _:Val, _:Val)) => true
  rule truthy(argsVal(_:ArgVals)) => true
  rule truthy(dictArgsVal(_:DictVals)) => true

  rule #debug => True

  rule isIntLike(_:Int) => true
  rule isIntLike(_:Float) => false
  rule isIntLike(_:String) => false
  rule isIntLike(True) => true
  rule isIntLike(False) => true
  rule isIntLike(None) => false
  rule isIntLike(Ellipsis) => false
  rule isIntLike([]) => false
  rule isIntLike(listVal(_:ValItems)) => false
  rule isIntLike(()) => false
  rule isIntLike(tupleVal(_:ValItems)) => false
  rule isIntLike({}) => false
  rule isIntLike(dictVal(_:DictItems)) => false
  rule isIntLike(set()) => false
  rule isIntLike(setVal(_:ValItems)) => false
  rule isIntLike(#kwDefaultMissing) => false
  rule isIntLike(closure(_:Id, _:Exp)) => false
  rule isIntLike(closureArgs(_:IdItems, _:Exp)) => false
  rule isIntLike(closureDefaults(_:IdItems, _:ArgVals, _:Exp)) => false
  rule isIntLike(closureVarArgs(_:IdItems, _:Id, _:Exp)) => false
  rule isIntLike(closureVarArgsDefaults(_:IdItems, _:ArgVals, _:Id, _:Exp)) => false
  rule isIntLike(closureKwArgs(_:IdItems, _:Id, _:Exp)) => false
  rule isIntLike(closurePosOnly(_:IdItems, _:IdItems, _:Exp)) => false
  rule isIntLike(closureKwOnly(_:IdItems, _:Exp)) => false
  rule isIntLike(closureKwDefaults(_:IdItems, _:ArgVals, _:Exp)) => false
  rule isIntLike(closurePosKwOnly(_:IdItems, _:IdItems, _:Exp)) => false
  rule isIntLike(closurePosKwDefaults(_:IdItems, _:ArgVals, _:IdItems, _:ArgVals, _:Exp)) => false
  rule isIntLike(functionVal(_:Id, _:Block)) => false
  rule isIntLike(functionValArgs(_:IdItems, _:Block)) => false
  rule isIntLike(functionValDefaults(_:IdItems, _:ArgVals, _:Block)) => false
  rule isIntLike(functionValVarArgs(_:IdItems, _:Id, _:Block)) => false
  rule isIntLike(functionValVarArgsDefaults(_:IdItems, _:ArgVals, _:Id, _:Block)) => false
  rule isIntLike(functionValKwArgs(_:IdItems, _:Id, _:Block)) => false
  rule isIntLike(functionValPosOnly(_:IdItems, _:IdItems, _:Block)) => false
  rule isIntLike(functionValKwOnly(_:IdItems, _:Block)) => false
  rule isIntLike(functionValKwDefaults(_:IdItems, _:ArgVals, _:Block)) => false
  rule isIntLike(functionValPosKwOnly(_:IdItems, _:IdItems, _:Block)) => false
  rule isIntLike(functionValPosKwDefaults(_:IdItems, _:ArgVals, _:IdItems, _:ArgVals, _:Block)) => false
  rule isIntLike(rangeVal(_:Int, _:Int)) => false
  rule isIntLike(rangeVal(_:Int, _:Int, _:Int)) => false
  rule isIntLike(sliceVal(_:Val, _:Val, _:Val)) => false
  rule isIntLike(argsVal(_:ArgVals)) => false
  rule isIntLike(dictArgsVal(_:DictVals)) => false

  rule isFloatLike(_:Float) => true
  rule isFloatLike(V:Val) => isIntLike(V) [owise]

  rule singletonIdentity(True) => true
  rule singletonIdentity(False) => true
  rule singletonIdentity(None) => true
  rule singletonIdentity(Ellipsis) => true
  rule singletonIdentity(_:Int) => false
  rule singletonIdentity(_:Float) => false
  rule singletonIdentity(_:String) => false
  rule singletonIdentity([]) => false
  rule singletonIdentity(listVal(_:ValItems)) => false
  rule singletonIdentity(()) => false
  rule singletonIdentity(tupleVal(_:ValItems)) => false
  rule singletonIdentity({}) => false
  rule singletonIdentity(dictVal(_:DictItems)) => false
  rule singletonIdentity(set()) => false
  rule singletonIdentity(setVal(_:ValItems)) => false
  rule singletonIdentity(#kwDefaultMissing) => false
  rule singletonIdentity(closure(_:Id, _:Exp)) => false
  rule singletonIdentity(closureArgs(_:IdItems, _:Exp)) => false
  rule singletonIdentity(closureDefaults(_:IdItems, _:ArgVals, _:Exp)) => false
  rule singletonIdentity(closureVarArgs(_:IdItems, _:Id, _:Exp)) => false
  rule singletonIdentity(closureVarArgsDefaults(_:IdItems, _:ArgVals, _:Id, _:Exp)) => false
  rule singletonIdentity(closureKwArgs(_:IdItems, _:Id, _:Exp)) => false
  rule singletonIdentity(closurePosOnly(_:IdItems, _:IdItems, _:Exp)) => false
  rule singletonIdentity(closureKwOnly(_:IdItems, _:Exp)) => false
  rule singletonIdentity(closureKwDefaults(_:IdItems, _:ArgVals, _:Exp)) => false
  rule singletonIdentity(closurePosKwOnly(_:IdItems, _:IdItems, _:Exp)) => false
  rule singletonIdentity(closurePosKwDefaults(_:IdItems, _:ArgVals, _:IdItems, _:ArgVals, _:Exp)) => false
  rule singletonIdentity(functionVal(_:Id, _:Block)) => false
  rule singletonIdentity(functionValArgs(_:IdItems, _:Block)) => false
  rule singletonIdentity(functionValDefaults(_:IdItems, _:ArgVals, _:Block)) => false
  rule singletonIdentity(functionValVarArgs(_:IdItems, _:Id, _:Block)) => false
  rule singletonIdentity(functionValVarArgsDefaults(_:IdItems, _:ArgVals, _:Id, _:Block)) => false
  rule singletonIdentity(functionValKwArgs(_:IdItems, _:Id, _:Block)) => false
  rule singletonIdentity(functionValPosOnly(_:IdItems, _:IdItems, _:Block)) => false
  rule singletonIdentity(functionValKwOnly(_:IdItems, _:Block)) => false
  rule singletonIdentity(functionValKwDefaults(_:IdItems, _:ArgVals, _:Block)) => false
  rule singletonIdentity(functionValPosKwOnly(_:IdItems, _:IdItems, _:Block)) => false
  rule singletonIdentity(functionValPosKwDefaults(_:IdItems, _:ArgVals, _:IdItems, _:ArgVals, _:Block)) => false
  rule singletonIdentity(rangeVal(_:Int, _:Int)) => false
  rule singletonIdentity(rangeVal(_:Int, _:Int, _:Int)) => false
  rule singletonIdentity(sliceVal(_:Val, _:Val, _:Val)) => false
  rule singletonIdentity(argsVal(_:ArgVals)) => false
  rule singletonIdentity(dictArgsVal(_:DictVals)) => false

  rule intValue(I:Int) => I
  rule intValue(True) => 1
  rule intValue(False) => 0

  rule floatValue(F:Float) => F
  rule floatValue(V:Val) => Int2Float(intValue(V), 53, 11)
    requires isIntLike(V)

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
    requires notBool isIntLike(V) andBool notBool isFloatLike(V)
  rule rangeContains(F:Float, Start:Int, Stop:Int) => rangeContainsFloat(F, Start, Stop, 1, 0)
  rule rangeContains(V:Val, Start:Int, Stop:Int) =>
    intValue(V) >=Int Start andBool intValue(V) <Int Stop
    requires isIntLike(V)
  rule rangeContains(V:Val, _Start:Int, _Stop:Int, Step:Int) => false
    requires notBool isIntLike(V) andBool notBool isFloatLike(V) andBool Step =/=Int 0
  rule rangeContains(F:Float, Start:Int, Stop:Int, Step:Int) => rangeContainsFloat(F, Start, Stop, Step, 0)
    requires Step =/=Int 0
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

  rule rangeContainsFloat(_F:Float, Start:Int, Stop:Int, Step:Int, I:Int) => false
    requires Step =/=Int 0 andBool I >=Int pyRangeLen(Start, Stop, Step)
  rule rangeContainsFloat(F:Float, Start:Int, Stop:Int, Step:Int, I:Int) => true
    requires Step =/=Int 0
      andBool I <Int pyRangeLen(Start, Stop, Step)
      andBool F ==Float Int2Float(rangeGet(Start, Stop, Step, I), 53, 11)
  rule rangeContainsFloat(F:Float, Start:Int, Stop:Int, Step:Int, I:Int) =>
    rangeContainsFloat(F, Start, Stop, Step, I +Int 1)
    requires Step =/=Int 0
      andBool I <Int pyRangeLen(Start, Stop, Step)
      andBool F =/=Float Int2Float(rangeGet(Start, Stop, Step, I), 53, 11)

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

  rule argValsLen(#noArgVals) => 0
  rule argValsLen(argValsCons(_:Val, VS:ArgVals)) => 1 +Int argValsLen(VS)

  rule kwArgValsLen(#noKwArgVals) => 0
  rule kwArgValsLen(kwArgValsCons(_:Id, _:Val, VS:KwArgVals)) => 1 +Int kwArgValsLen(VS)
  rule kwArgValsLen(kwArgStringValsCons(_:String, _:Val, VS:KwArgVals)) => 1 +Int kwArgValsLen(VS)

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

  rule pyFloatFloorDiv(F1:Float, F2:Float) => floorFloat(F1 /Float F2)
    requires F2 =/=Float 0.0

  rule pyFloatModulo(F1:Float, F2:Float) => F1 -Float (F2 *Float pyFloatFloorDiv(F1, F2))
    requires F2 =/=Float 0.0

  rule boolValue(true) => True
  rule boolValue(false) => False

  rule valEq(I1:Int, I2:Int) => I1 ==Int I2
  rule valEq(F1:Float, F2:Float) => F1 ==Float F2
  rule valEq(I:Int, F:Float) => Int2Float(I, 53, 11) ==Float F
  rule valEq(F:Float, I:Int) => F ==Float Int2Float(I, 53, 11)
  rule valEq(True, F:Float) => Int2Float(1, 53, 11) ==Float F
  rule valEq(False, F:Float) => Int2Float(0, 53, 11) ==Float F
  rule valEq(F:Float, True) => F ==Float Int2Float(1, 53, 11)
  rule valEq(F:Float, False) => F ==Float Int2Float(0, 53, 11)
  rule valEq(_:Float, _:Val) => false [owise]
  rule valEq(_:Val, _:Float) => false [owise]
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
  rule valEq(sliceVal(Start1:Val, Stop1:Val, Step1:Val), sliceVal(Start2:Val, Stop2:Val, Step2:Val)) =>
    valEq(Start1, Start2) andBool valEq(Stop1, Stop2) andBool valEq(Step1, Step2)
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
  rule valEq(Ellipsis, Ellipsis) => true
  rule valEq(None, _:Int) => false
  rule valEq(_:Int, None) => false
  rule valEq(None, True) => false
  rule valEq(None, False) => false
  rule valEq(True, None) => false
  rule valEq(False, None) => false
  rule valEq(Ellipsis, None) => false
  rule valEq(None, Ellipsis) => false
  rule valEq(Ellipsis, True) => false
  rule valEq(Ellipsis, False) => false
  rule valEq(True, Ellipsis) => false
  rule valEq(False, Ellipsis) => false
  rule valEq(Ellipsis, _:Int) => false
  rule valEq(_:Int, Ellipsis) => false
  rule valEq(Ellipsis, _:Float) => false
  rule valEq(_:Float, Ellipsis) => false
  rule valEq(Ellipsis, _:String) => false
  rule valEq(_:String, Ellipsis) => false

  rule valIs(V1:Val, V2:Val) => valEq(V1, V2)
    requires singletonIdentity(V1) andBool singletonIdentity(V2)
  rule valIs(V1:Val, V2:Val) => false
    requires singletonIdentity(V1) andBool notBool singletonIdentity(V2)
  rule valIs(V1:Val, V2:Val) => false
    requires notBool singletonIdentity(V1) andBool singletonIdentity(V2)

  rule cmpHolds(#lt, V1:Val, V2:Val) => intValue(V1) <Int intValue(V2)
    requires isIntLike(V1) andBool isIntLike(V2)
  rule cmpHolds(#lt, F1:Float, F2:Float) => F1 <Float F2
  rule cmpHolds(#lt, F:Float, V:Val) => F <Float floatValue(V)
    requires isIntLike(V)
  rule cmpHolds(#lt, V:Val, F:Float) => floatValue(V) <Float F
    requires isIntLike(V)
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
  rule cmpHolds(#le, F1:Float, F2:Float) => F1 <=Float F2
  rule cmpHolds(#le, F:Float, V:Val) => F <=Float floatValue(V)
    requires isIntLike(V)
  rule cmpHolds(#le, V:Val, F:Float) => floatValue(V) <=Float F
    requires isIntLike(V)
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
  rule cmpHolds(#gt, F1:Float, F2:Float) => F1 >Float F2
  rule cmpHolds(#gt, F:Float, V:Val) => F >Float floatValue(V)
    requires isIntLike(V)
  rule cmpHolds(#gt, V:Val, F:Float) => floatValue(V) >Float F
    requires isIntLike(V)
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
  rule cmpHolds(#ge, F1:Float, F2:Float) => F1 >=Float F2
  rule cmpHolds(#ge, F:Float, V:Val) => F >=Float floatValue(V)
    requires isIntLike(V)
  rule cmpHolds(#ge, V:Val, F:Float) => floatValue(V) >=Float F
    requires isIntLike(V)
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

  rule varArgsCallArityOk(IDS:IdItems, VS:ArgVals) => argValsLen(VS) >=Int idItemsLen(IDS)

  rule varArgsDefaultsCallArityOk(IDS:IdItems, VS:ArgVals, Defaults:ArgVals) =>
    argValsLen(Defaults) <=Int idItemsLen(IDS)
      andBool (argValsLen(VS) >=Int idItemsLen(IDS)
        orBool idItemsLen(IDS) -Int argValsLen(VS) <=Int argValsLen(Defaults))

  rule varArgsMixedCallArityOk(IDS:IdItems, VS:ArgVals, KWS:KwArgVals) =>
    kwNoDuplicates(KWS)
      andBool kwAllInIds(KWS, IDS)
      andBool varArgsMixedNoPosKeyword(IDS, VS, KWS)
      andBool varArgsMixedRequiredPresent(IDS, VS, KWS)

  rule varArgsMixedDefaultsCallArityOk(IDS:IdItems, VS:ArgVals, KWS:KwArgVals, Defaults:ArgVals) =>
    argValsLen(Defaults) <=Int idItemsLen(IDS)
      andBool kwNoDuplicates(KWS)
      andBool kwAllInIds(KWS, IDS)
      andBool varArgsMixedNoPosKeyword(IDS, VS, KWS)
      andBool mixedRequiredPresent(IDS, takeArgVals(VS, idItemsLen(IDS)), KWS, Defaults)

  rule varArgsMixedNoPosKeyword(#noIds, _:ArgVals, _:KwArgVals) => true
  rule varArgsMixedNoPosKeyword(idItemsLast(_:Id), #noArgVals, _:KwArgVals) => true
  rule varArgsMixedNoPosKeyword(idItemsLast(X:Id), argValsCons(_:Val, _:ArgVals), KWS:KwArgVals) =>
    notBool kwContains(X, KWS)
  rule varArgsMixedNoPosKeyword(idItemsCons(_:Id, _:IdItems), #noArgVals, _:KwArgVals) => true
  rule varArgsMixedNoPosKeyword(idItemsCons(X:Id, IDS:IdItems), argValsCons(_:Val, VS:ArgVals), KWS:KwArgVals) =>
    notBool kwContains(X, KWS) andBool varArgsMixedNoPosKeyword(IDS, VS, KWS)

  rule varArgsMixedRequiredPresent(#noIds, _:ArgVals, _:KwArgVals) => true
  rule varArgsMixedRequiredPresent(idItemsLast(X:Id), #noArgVals, KWS:KwArgVals) => kwContains(X, KWS)
  rule varArgsMixedRequiredPresent(idItemsLast(_:Id), argValsCons(_:Val, _:ArgVals), _:KwArgVals) => true
  rule varArgsMixedRequiredPresent(idItemsCons(X:Id, IDS:IdItems), #noArgVals, KWS:KwArgVals) =>
    kwContains(X, KWS) andBool varArgsMixedRequiredPresent(IDS, #noArgVals, KWS)
  rule varArgsMixedRequiredPresent(idItemsCons(_:Id, IDS:IdItems), argValsCons(_:Val, VS:ArgVals), KWS:KwArgVals) =>
    varArgsMixedRequiredPresent(IDS, VS, KWS)

  rule kwargsPosCallArityOk(IDS:IdItems, VS:ArgVals) => sameArity(IDS, VS)

  rule kwargsKeywordCallArityOk(IDS:IdItems, KWS:KwArgVals) =>
    kwNoDuplicates(KWS)
      andBool kwRequiredPresent(IDS, KWS, #noArgVals)

  rule kwargsMixedCallArityOk(IDS:IdItems, VS:ArgVals, KWS:KwArgVals) =>
    argValsLen(VS) <=Int idItemsLen(IDS)
      andBool kwNoDuplicates(KWS)
      andBool mixedNoPosKeyword(IDS, VS, KWS)
      andBool mixedRequiredPresent(IDS, VS, KWS, #noArgVals)

  rule posOnlyArgsCallArityOk(Pos:IdItems, Rest:IdItems, VS:ArgVals) =>
    argValsLen(VS) ==Int idItemsLen(Pos) +Int idItemsLen(Rest)

  rule posOnlyKeywordCallArityOk(Pos:IdItems, Rest:IdItems, KWS:KwArgVals) =>
    idItemsLen(Pos) ==Int 0
      andBool keywordOnlyCallArityOk(Rest, KWS, #noArgVals)

  rule posOnlyMixedCallArityOk(Pos:IdItems, Rest:IdItems, VS:ArgVals, KWS:KwArgVals) =>
    argValsLen(VS) >=Int idItemsLen(Pos)
      andBool argValsLen(VS) <=Int idItemsLen(Pos) +Int idItemsLen(Rest)
      andBool kwNoDuplicates(KWS)
      andBool kwAllInIds(KWS, Rest)
      andBool mixedNoPosKeyword(Rest, dropArgVals(VS, idItemsLen(Pos)), KWS)
      andBool mixedRequiredPresent(Rest, dropArgVals(VS, idItemsLen(Pos)), KWS, #noArgVals)

  rule sameIdValArity(idItemsLast(_:Id), valItemsLast(_:Val)) => true
  rule sameIdValArity(idItemsLast(_:Id), valItemsCons(_:Val, _:ValItems)) => false
  rule sameIdValArity(idItemsCons(_:Id, _:IdItems), valItemsLast(_:Val)) => false
  rule sameIdValArity(idItemsCons(_:Id, IDS:IdItems), valItemsCons(_:Val, VS:ValItems)) =>
    sameIdValArity(IDS, VS)

  rule sameTargetsValArity(targetsLast(T:Target), valItemsLast(V:Val)) =>
    targetValueArityOk(T, V)
  rule sameTargetsValArity(targetsLast(_:Target), valItemsCons(_:Val, _:ValItems)) => false
  rule sameTargetsValArity(targetsCons(_:Target, _:Targets), valItemsLast(_:Val)) => false
  rule sameTargetsValArity(targetsCons(T:Target, TS:Targets), valItemsCons(V:Val, VS:ValItems)) =>
    targetValueArityOk(T, V) andBool sameTargetsValArity(TS, VS)

  rule targetValueArityOk(targetName(_:Id), _:Val) => true
  rule targetValueArityOk(targetSeq(TS:Targets), listVal(VS:ValItems)) =>
    sameTargetsValArity(TS, VS)
  rule targetValueArityOk(targetSeq(TS:Targets), tupleVal(VS:ValItems)) =>
    sameTargetsValArity(TS, VS)
  rule targetValueArityOk(targetSeq(TS:Targets), setVal(VS:ValItems)) =>
    sameTargetsValArity(TS, VS)
  rule targetValueArityOk(targetSeq(_:Targets), _:Val) => false
    [owise]

  rule starUnpackArityOk(Prefix:IdItems, Suffix:IdItems, Len:Int) =>
    idItemsLen(Prefix) +Int idItemsLen(Suffix) <=Int Len

  rule defaultsCallArityOk(IDS:IdItems, VS:ArgVals, Defaults:ArgVals) =>
    argValsLen(VS) <=Int idItemsLen(IDS)
      andBool idItemsLen(IDS) -Int argValsLen(VS) <=Int argValsLen(Defaults)
      andBool argValsLen(Defaults) <=Int idItemsLen(IDS)

  rule keywordOnlyCallArityOk(IDS:IdItems, KWS:KwArgVals, Defaults:ArgVals) =>
    kwNoDuplicates(KWS)
      andBool kwAllInIds(KWS, IDS)
      andBool kwRequiredPresent(IDS, KWS, Defaults)
      andBool argValsLen(Defaults) <=Int idItemsLen(IDS)

  rule mixedCallArityOk(IDS:IdItems, VS:ArgVals, KWS:KwArgVals, Defaults:ArgVals) =>
    argValsLen(VS) <=Int idItemsLen(IDS)
      andBool argValsLen(Defaults) <=Int idItemsLen(IDS)
      andBool kwNoDuplicates(KWS)
      andBool kwAllInIds(KWS, IDS)
      andBool mixedNoPosKeyword(IDS, VS, KWS)
      andBool mixedRequiredPresent(IDS, VS, KWS, Defaults)

  rule posKwOnlyKeywordCallArityOk(Pos:IdItems, KwOnly:IdItems, KWS:KwArgVals) =>
    kwNoDuplicates(KWS)
      andBool kwAllInEitherIds(KWS, Pos, KwOnly)
      andBool kwRequiredPresent(Pos, KWS, #noArgVals)
      andBool kwRequiredPresent(KwOnly, KWS, #noArgVals)

  rule posKwOnlyMixedCallArityOk(Pos:IdItems, KwOnly:IdItems, VS:ArgVals, KWS:KwArgVals) =>
    argValsLen(VS) <=Int idItemsLen(Pos)
      andBool kwNoDuplicates(KWS)
      andBool kwAllInEitherIds(KWS, Pos, KwOnly)
      andBool mixedNoPosKeyword(Pos, VS, KWS)
      andBool mixedRequiredPresent(Pos, VS, KWS, #noArgVals)
      andBool kwRequiredPresent(KwOnly, KWS, #noArgVals)

  rule posKwOnlyArgsDefaultsCallArityOk(Pos:IdItems, KwOnly:IdItems, VS:ArgVals, PosDefaults:ArgVals, KwDefaults:ArgVals) =>
    defaultsCallArityOk(Pos, VS, PosDefaults)
      andBool argValsLen(KwDefaults) <=Int idItemsLen(KwOnly)
      andBool kwRequiredPresent(KwOnly, #noKwArgVals, KwDefaults)

  rule posKwOnlyKeywordDefaultsCallArityOk(Pos:IdItems, KwOnly:IdItems, KWS:KwArgVals, PosDefaults:ArgVals, KwDefaults:ArgVals) =>
    kwNoDuplicates(KWS)
      andBool kwAllInEitherIds(KWS, Pos, KwOnly)
      andBool argValsLen(PosDefaults) <=Int idItemsLen(Pos)
      andBool argValsLen(KwDefaults) <=Int idItemsLen(KwOnly)
      andBool kwRequiredPresent(Pos, KWS, PosDefaults)
      andBool kwRequiredPresent(KwOnly, KWS, KwDefaults)

  rule posKwOnlyMixedDefaultsCallArityOk(Pos:IdItems, KwOnly:IdItems, VS:ArgVals, KWS:KwArgVals, PosDefaults:ArgVals, KwDefaults:ArgVals) =>
    argValsLen(VS) <=Int idItemsLen(Pos)
      andBool argValsLen(PosDefaults) <=Int idItemsLen(Pos)
      andBool argValsLen(KwDefaults) <=Int idItemsLen(KwOnly)
      andBool kwNoDuplicates(KWS)
      andBool kwAllInEitherIds(KWS, Pos, KwOnly)
      andBool mixedNoPosKeyword(Pos, VS, KWS)
      andBool mixedRequiredPresent(Pos, VS, KWS, PosDefaults)
      andBool kwRequiredPresent(KwOnly, KWS, KwDefaults)

  rule emptyArgVals(#noArgVals) => true
  rule emptyArgVals(argValsCons(_:Val, _:ArgVals)) => false

  rule emptyKwArgVals(#noKwArgVals) => true
  rule emptyKwArgVals(kwArgValsCons(_:Id, _:Val, _:KwArgVals)) => false
  rule emptyKwArgVals(kwArgStringValsCons(_:String, _:Val, _:KwArgVals)) => false

  rule emptyDictVals(#noDictVals) => true
  rule emptyDictVals(dictValsCons(_:Val, _:Val, _:DictVals)) => false

  rule idContains(_:Id, #noIds) => false
  rule idContains(X:Id, idItemsLast(X)) => true
  rule idContains(_X:Id, idItemsLast(_Y:Id)) => false
    [owise]
  rule idContains(X:Id, idItemsCons(X, _:IdItems)) => true
  rule idContains(X:Id, idItemsCons(_Y:Id, IDS:IdItems)) => idContains(X, IDS)
    [owise]

  rule stringIdContains(_:String, #noIds) => false
  rule stringIdContains(S:String, idItemsLast(X:Id)) => S ==String Id2String(X)
  rule stringIdContains(S:String, idItemsCons(X:Id, IDS:IdItems)) =>
    S ==String Id2String(X) orBool stringIdContains(S, IDS)

  rule kwContains(_:Id, #noKwArgVals) => false
  rule kwContains(X:Id, kwArgValsCons(X, _:Val, _:KwArgVals)) => true
  rule kwContains(X:Id, kwArgValsCons(_Y:Id, _:Val, KWS:KwArgVals)) => kwContains(X, KWS)
    [owise]
  rule kwContains(X:Id, kwArgStringValsCons(S:String, _:Val, KWS:KwArgVals)) =>
    Id2String(X) ==String S orBool kwContains(X, KWS)

  rule kwStringContains(_:String, #noKwArgVals) => false
  rule kwStringContains(S:String, kwArgValsCons(X:Id, _:Val, KWS:KwArgVals)) =>
    S ==String Id2String(X) orBool kwStringContains(S, KWS)
  rule kwStringContains(S:String, kwArgStringValsCons(S, _:Val, _:KwArgVals)) => true
  rule kwStringContains(S:String, kwArgStringValsCons(_T:String, _:Val, KWS:KwArgVals)) => kwStringContains(S, KWS)
    [owise]

  rule kwLookup(X:Id, kwArgValsCons(X, V:Val, _:KwArgVals)) => V
  rule kwLookup(X:Id, kwArgValsCons(_Y:Id, _:Val, KWS:KwArgVals)) => kwLookup(X, KWS)
    [owise]
  rule kwLookup(X:Id, kwArgStringValsCons(S:String, V:Val, _:KwArgVals)) => V
    requires Id2String(X) ==String S
  rule kwLookup(X:Id, kwArgStringValsCons(_S:String, _:Val, KWS:KwArgVals)) => kwLookup(X, KWS)
    [owise]

  rule kwNoDuplicates(#noKwArgVals) => true
  rule kwNoDuplicates(kwArgValsCons(X:Id, _:Val, KWS:KwArgVals)) =>
    notBool kwContains(X, KWS) andBool kwNoDuplicates(KWS)
  rule kwNoDuplicates(kwArgStringValsCons(S:String, _:Val, KWS:KwArgVals)) =>
    notBool kwStringContains(S, KWS) andBool kwNoDuplicates(KWS)

  rule kwAllInIds(#noKwArgVals, _:IdItems) => true
  rule kwAllInIds(kwArgValsCons(X:Id, _:Val, KWS:KwArgVals), IDS:IdItems) =>
    idContains(X, IDS) andBool kwAllInIds(KWS, IDS)
  rule kwAllInIds(kwArgStringValsCons(S:String, _:Val, KWS:KwArgVals), IDS:IdItems) =>
    stringIdContains(S, IDS) andBool kwAllInIds(KWS, IDS)

  rule kwAllInEitherIds(#noKwArgVals, _:IdItems, _:IdItems) => true
  rule kwAllInEitherIds(kwArgValsCons(X:Id, _:Val, KWS:KwArgVals), Pos:IdItems, KwOnly:IdItems) =>
    (idContains(X, Pos) orBool idContains(X, KwOnly)) andBool kwAllInEitherIds(KWS, Pos, KwOnly)
  rule kwAllInEitherIds(kwArgStringValsCons(S:String, _:Val, KWS:KwArgVals), Pos:IdItems, KwOnly:IdItems) =>
    (stringIdContains(S, Pos) orBool stringIdContains(S, KwOnly)) andBool kwAllInEitherIds(KWS, Pos, KwOnly)

  rule isKwDefaultMissing(#kwDefaultMissing) => true
  rule isKwDefaultMissing(_:Val) => false
    [owise]

  rule hasKwDefaultMissing(#noArgVals) => false
  rule hasKwDefaultMissing(argValsCons(V:Val, VS:ArgVals)) =>
    isKwDefaultMissing(V) orBool hasKwDefaultMissing(VS)

  rule kwRequiredPresent(#noIds, _:KwArgVals, _:ArgVals) => true
  rule kwRequiredPresent(idItemsLast(X:Id), KWS:KwArgVals, #noArgVals) => kwContains(X, KWS)
  rule kwRequiredPresent(IDS:IdItems, _:KwArgVals, Defaults:ArgVals) => true
    requires idItemsLen(IDS) <=Int argValsLen(Defaults)
      andBool notBool hasKwDefaultMissing(Defaults)
  rule kwRequiredPresent(IDS:IdItems, KWS:KwArgVals, Defaults:ArgVals) =>
    kwRequiredAlignedPresent(IDS, KWS, Defaults)
    requires idItemsLen(IDS) ==Int argValsLen(Defaults)
      andBool hasKwDefaultMissing(Defaults)
  rule kwRequiredPresent(idItemsCons(X:Id, IDS:IdItems), KWS:KwArgVals, Defaults:ArgVals) =>
    kwContains(X, KWS) andBool kwRequiredPresent(IDS, KWS, Defaults)
    requires idItemsLen(idItemsCons(X, IDS)) >Int argValsLen(Defaults)

  rule kwRequiredAlignedPresent(#noIds, _:KwArgVals, #noArgVals) => true
  rule kwRequiredAlignedPresent(idItemsLast(X:Id), KWS:KwArgVals, argValsCons(Default:Val, #noArgVals)) =>
    kwContains(X, KWS)
    requires isKwDefaultMissing(Default)
  rule kwRequiredAlignedPresent(idItemsLast(_:Id), _:KwArgVals, argValsCons(Default:Val, #noArgVals)) => true
    requires notBool isKwDefaultMissing(Default)
  rule kwRequiredAlignedPresent(idItemsCons(X:Id, IDS:IdItems), KWS:KwArgVals, argValsCons(Default:Val, Defaults:ArgVals)) =>
    ((notBool isKwDefaultMissing(Default)) orBool kwContains(X, KWS))
      andBool kwRequiredAlignedPresent(IDS, KWS, Defaults)

  rule mixedNoPosKeyword(#noIds, argValsCons(_:Val, _:ArgVals), _:KwArgVals) => false
  rule mixedNoPosKeyword(_:IdItems, #noArgVals, _:KwArgVals) => true
  rule mixedNoPosKeyword(idItemsLast(X:Id), argValsCons(_:Val, #noArgVals), KWS:KwArgVals) =>
    notBool kwContains(X, KWS)
  rule mixedNoPosKeyword(idItemsLast(_:Id), argValsCons(_:Val, argValsCons(_:Val, _:ArgVals)), _:KwArgVals) =>
    false
  rule mixedNoPosKeyword(idItemsCons(X:Id, IDS:IdItems), argValsCons(_:Val, VS:ArgVals), KWS:KwArgVals) =>
    notBool kwContains(X, KWS) andBool mixedNoPosKeyword(IDS, VS, KWS)

  rule mixedRequiredPresent(#noIds, argValsCons(_:Val, _:ArgVals), _:KwArgVals, _:ArgVals) => false
  rule mixedRequiredPresent(IDS:IdItems, #noArgVals, KWS:KwArgVals, Defaults:ArgVals) =>
    kwRequiredPresent(IDS, KWS, Defaults)
  rule mixedRequiredPresent(idItemsLast(_:Id), argValsCons(_:Val, #noArgVals), _:KwArgVals, _:ArgVals) =>
    true
  rule mixedRequiredPresent(idItemsLast(_:Id), argValsCons(_:Val, argValsCons(_:Val, _:ArgVals)), _:KwArgVals, _:ArgVals) =>
    false
  rule mixedRequiredPresent(idItemsCons(X:Id, IDS:IdItems), argValsCons(_:Val, VS:ArgVals), KWS:KwArgVals, Defaults:ArgVals) =>
    mixedRequiredPresent(IDS, VS, KWS, Defaults)
    requires idItemsLen(idItemsCons(X, IDS)) >Int argValsLen(Defaults)
  rule mixedRequiredPresent(idItemsCons(X:Id, IDS:IdItems), argValsCons(_:Val, VS:ArgVals), KWS:KwArgVals, argValsCons(_:Val, Defaults:ArgVals)) =>
    mixedRequiredPresent(IDS, VS, KWS, Defaults)
    requires idItemsLen(idItemsCons(X, IDS)) ==Int 1 +Int argValsLen(Defaults)

  rule appendArgVal(#noArgVals, V:Val) => argValsCons(V, #noArgVals)
  rule appendArgVal(argValsCons(V0:Val, VS:ArgVals), V:Val) =>
    argValsCons(V0, appendArgVal(VS, V))

  rule concatArgVals(#noArgVals, VS:ArgVals) => VS
  rule concatArgVals(argValsCons(V:Val, VS1:ArgVals), VS2:ArgVals) =>
    argValsCons(V, concatArgVals(VS1, VS2))

  rule dropArgVals(VS:ArgVals, 0) => VS
  rule dropArgVals(#noArgVals, N:Int) => #noArgVals
    requires N >Int 0
  rule dropArgVals(argValsCons(_:Val, VS:ArgVals), N:Int) => dropArgVals(VS, N -Int 1)
    requires N >Int 0

  rule takeArgVals(_:ArgVals, 0) => #noArgVals
  rule takeArgVals(#noArgVals, N:Int) => #noArgVals
    requires N >Int 0
  rule takeArgVals(argValsCons(V:Val, VS:ArgVals), N:Int) =>
    argValsCons(V, takeArgVals(VS, N -Int 1))
    requires N >Int 0

  rule varArgTail(VS:ArgVals, 0) => VS
  rule varArgTail(#noArgVals, N:Int) => #noArgVals
    requires N >Int 0
  rule varArgTail(argValsCons(_:Val, VS:ArgVals), N:Int) => varArgTail(VS, N -Int 1)
    requires N >Int 0

  rule completeVarArgsDefaultArgs(IDS:IdItems, VS:ArgVals, Defaults:ArgVals) =>
    concatArgVals(completeDefaultArgs(IDS, takeArgVals(VS, idItemsLen(IDS)), Defaults), varArgTail(VS, idItemsLen(IDS)))
    requires varArgsDefaultsCallArityOk(IDS, VS, Defaults)

  rule buildVarArgsMixedPosArgs(#noIds, _:ArgVals, _:KwArgVals) => #noArgVals
  rule buildVarArgsMixedPosArgs(idItemsLast(X:Id), #noArgVals, KWS:KwArgVals) =>
    argValsCons(kwLookup(X, KWS), #noArgVals)
    requires kwContains(X, KWS)
  rule buildVarArgsMixedPosArgs(idItemsLast(_:Id), argValsCons(V:Val, _:ArgVals), _:KwArgVals) =>
    argValsCons(V, #noArgVals)
  rule buildVarArgsMixedPosArgs(idItemsCons(X:Id, IDS:IdItems), #noArgVals, KWS:KwArgVals) =>
    argValsCons(kwLookup(X, KWS), buildVarArgsMixedPosArgs(IDS, #noArgVals, KWS))
    requires kwContains(X, KWS)
  rule buildVarArgsMixedPosArgs(idItemsCons(_:Id, IDS:IdItems), argValsCons(V:Val, VS:ArgVals), KWS:KwArgVals) =>
    argValsCons(V, buildVarArgsMixedPosArgs(IDS, VS, KWS))

  rule buildVarArgsMixedDefaultArgs(IDS:IdItems, VS:ArgVals, KWS:KwArgVals, Defaults:ArgVals) =>
    concatArgVals(buildMixedDefaultArgs(IDS, takeArgVals(VS, idItemsLen(IDS)), KWS, Defaults), varArgTail(VS, idItemsLen(IDS)))
    requires varArgsMixedDefaultsCallArityOk(IDS, VS, KWS, Defaults)

  rule valItemsToArgVals(valItemsLast(V:Val)) => argValsCons(V, #noArgVals)
  rule valItemsToArgVals(valItemsCons(V:Val, VS:ValItems)) =>
    argValsCons(V, valItemsToArgVals(VS))

  rule iterableArgVals([]) => #noArgVals
  rule iterableArgVals(listVal(VS:ValItems)) => valItemsToArgVals(VS)
  rule iterableArgVals(()) => #noArgVals
  rule iterableArgVals(tupleVal(VS:ValItems)) => valItemsToArgVals(VS)
  rule iterableArgVals(S:String) => #noArgVals
    requires lengthString(S) ==Int 0
  rule iterableArgVals(S:String) => valItemsToArgVals(stringToValItems(S, 0, lengthString(S)))
    requires lengthString(S) >Int 0
  rule iterableArgVals(({}):Val) => #noArgVals
  rule iterableArgVals(dictVal(DS:DictItems)) => valItemsToArgVals(dictKeysToValItems(DS))
  rule iterableArgVals(set()) => #noArgVals
  rule iterableArgVals(setVal(VS:ValItems)) => valItemsToArgVals(VS)
  rule iterableArgVals(rangeVal(Start:Int, Stop:Int)) => #noArgVals
    requires pyRangeLen(Start, Stop, 1) ==Int 0
  rule iterableArgVals(rangeVal(Start:Int, Stop:Int)) =>
    valItemsToArgVals(rangeToValItems(Start, Stop, 1, 0, pyRangeLen(Start, Stop, 1)))
    requires pyRangeLen(Start, Stop, 1) >Int 0
  rule iterableArgVals(rangeVal(Start:Int, Stop:Int, Step:Int)) => #noArgVals
    requires Step =/=Int 0 andBool pyRangeLen(Start, Stop, Step) ==Int 0
  rule iterableArgVals(rangeVal(Start:Int, Stop:Int, Step:Int)) =>
    valItemsToArgVals(rangeToValItems(Start, Stop, Step, 0, pyRangeLen(Start, Stop, Step)))
    requires Step =/=Int 0 andBool pyRangeLen(Start, Stop, Step) >Int 0

  rule completeDefaultArgs(IDS:IdItems, VS:ArgVals, Defaults:ArgVals) =>
    concatArgVals(
      VS,
      dropArgVals(
        Defaults,
        argValsLen(Defaults) -Int (idItemsLen(IDS) -Int argValsLen(VS))))
    requires defaultsCallArityOk(IDS, VS, Defaults)

  rule appendKwArgVal(#noKwArgVals, X:Id, V:Val) => kwArgValsCons(X, V, #noKwArgVals)
  rule appendKwArgVal(kwArgValsCons(X0:Id, V0:Val, KWS:KwArgVals), X:Id, V:Val) =>
    kwArgValsCons(X0, V0, appendKwArgVal(KWS, X, V))
  rule appendKwArgVal(kwArgStringValsCons(S0:String, V0:Val, KWS:KwArgVals), X:Id, V:Val) =>
    kwArgStringValsCons(S0, V0, appendKwArgVal(KWS, X, V))

  rule appendKwStringArgVal(#noKwArgVals, S:String, V:Val) => kwArgStringValsCons(S, V, #noKwArgVals)
  rule appendKwStringArgVal(kwArgValsCons(X0:Id, V0:Val, KWS:KwArgVals), S:String, V:Val) =>
    kwArgValsCons(X0, V0, appendKwStringArgVal(KWS, S, V))
  rule appendKwStringArgVal(kwArgStringValsCons(S0:String, V0:Val, KWS:KwArgVals), S:String, V:Val) =>
    kwArgStringValsCons(S0, V0, appendKwStringArgVal(KWS, S, V))

  rule appendKwUnpack(KWS:KwArgVals, ({}):Val) => KWS
  rule appendKwUnpack(KWS:KwArgVals, dictVal(DS:DictItems)) => appendKwDictItems(KWS, DS)

  rule appendKwDictItems(KWS:KwArgVals, dictItemsLast(S:String, V:Val)) =>
    appendKwStringArgVal(KWS, S, V)
  rule appendKwDictItems(KWS:KwArgVals, dictItemsCons(S:String, V:Val, DS:DictItems)) =>
    appendKwDictItems(appendKwStringArgVal(KWS, S, V), DS)

  rule buildKwDefaultArgs(#noIds, _:KwArgVals, _:ArgVals) => #noArgVals
  rule buildKwDefaultArgs(idItemsLast(X:Id), KWS:KwArgVals, #noArgVals) =>
    argValsCons(kwLookup(X, KWS), #noArgVals)
    requires kwContains(X, KWS)
  rule buildKwDefaultArgs(idItemsLast(X:Id), KWS:KwArgVals, argValsCons(_Default:Val, #noArgVals)) =>
    argValsCons(kwLookup(X, KWS), #noArgVals)
    requires kwContains(X, KWS)
  rule buildKwDefaultArgs(idItemsLast(X:Id), KWS:KwArgVals, argValsCons(Default:Val, #noArgVals)) =>
    argValsCons(Default, #noArgVals)
    requires notBool kwContains(X, KWS)
      andBool notBool isKwDefaultMissing(Default)
  rule buildKwDefaultArgs(idItemsCons(X:Id, IDS:IdItems), KWS:KwArgVals, Defaults:ArgVals) =>
    argValsCons(kwLookup(X, KWS), buildKwDefaultArgs(IDS, KWS, Defaults))
    requires idItemsLen(idItemsCons(X, IDS)) >Int argValsLen(Defaults)
      andBool kwContains(X, KWS)
  rule buildKwDefaultArgs(idItemsCons(X:Id, IDS:IdItems), KWS:KwArgVals, argValsCons(Default:Val, Defaults:ArgVals)) =>
    argValsCons(kwLookup(X, KWS), buildKwDefaultArgs(IDS, KWS, Defaults))
    requires idItemsLen(idItemsCons(X, IDS)) ==Int argValsLen(argValsCons(Default, Defaults))
      andBool kwContains(X, KWS)
  rule buildKwDefaultArgs(idItemsCons(X:Id, IDS:IdItems), KWS:KwArgVals, argValsCons(Default:Val, Defaults:ArgVals)) =>
    argValsCons(Default, buildKwDefaultArgs(IDS, KWS, Defaults))
    requires idItemsLen(idItemsCons(X, IDS)) ==Int argValsLen(argValsCons(Default, Defaults))
      andBool notBool kwContains(X, KWS)
      andBool notBool isKwDefaultMissing(Default)

  rule buildMixedDefaultArgs(IDS:IdItems, #noArgVals, KWS:KwArgVals, Defaults:ArgVals) =>
    buildKwDefaultArgs(IDS, KWS, Defaults)
  rule buildMixedDefaultArgs(idItemsLast(_:Id), argValsCons(V:Val, #noArgVals), _:KwArgVals, _:ArgVals) =>
    argValsCons(V, #noArgVals)
  rule buildMixedDefaultArgs(idItemsCons(X:Id, IDS:IdItems), argValsCons(V:Val, VS:ArgVals), KWS:KwArgVals, Defaults:ArgVals) =>
    argValsCons(V, buildMixedDefaultArgs(IDS, VS, KWS, Defaults))
    requires idItemsLen(idItemsCons(X, IDS)) >Int argValsLen(Defaults)
  rule buildMixedDefaultArgs(idItemsCons(X:Id, IDS:IdItems), argValsCons(V:Val, VS:ArgVals), KWS:KwArgVals, argValsCons(_:Val, Defaults:ArgVals)) =>
    argValsCons(V, buildMixedDefaultArgs(IDS, VS, KWS, Defaults))
    requires idItemsLen(idItemsCons(X, IDS)) ==Int 1 +Int argValsLen(Defaults)

  rule kwExtrasDict(KWS:KwArgVals, IDS:IdItems) => ({}):Val
    requires emptyDictVals(kwExtrasDictVals(KWS, IDS))
  rule kwExtrasDict(KWS:KwArgVals, IDS:IdItems) => dictVal(dictValsToDictItems(kwExtrasDictVals(KWS, IDS)))
    requires notBool emptyDictVals(kwExtrasDictVals(KWS, IDS))

  rule dictFromDictVals(DVS:DictVals) => ({}):Val
    requires emptyDictVals(DVS)
  rule dictFromDictVals(DVS:DictVals) => dictVal(dictValsToDictItems(DVS))
    requires notBool emptyDictVals(DVS)

  rule dictCtorFromKwArgs(KWS:KwArgVals) => dictFromDictVals(appendKwDictVals(#noDictVals, KWS))

  rule dictCtorMergeKw(({}):Val, KWS:KwArgVals) => dictCtorFromKwArgs(KWS)
  rule dictCtorMergeKw(dictVal(DS:DictItems), KWS:KwArgVals) =>
    dictFromDictVals(appendKwDictVals(appendDictItems(#noDictVals, DS), KWS))
  rule dictCtorMergeKw([], KWS:KwArgVals) => dictCtorFromKwArgs(KWS)
  rule dictCtorMergeKw(listVal(VS:ValItems), KWS:KwArgVals) =>
    dictFromDictVals(appendKwDictVals(dictCtorPairs(VS, #noDictVals), KWS))
  rule dictCtorMergeKw((), KWS:KwArgVals) => dictCtorFromKwArgs(KWS)
  rule dictCtorMergeKw(tupleVal(VS:ValItems), KWS:KwArgVals) =>
    dictFromDictVals(appendKwDictVals(dictCtorPairs(VS, #noDictVals), KWS))

  rule appendKwDictVals(DVS:DictVals, #noKwArgVals) => DVS
  rule appendKwDictVals(DVS:DictVals, kwArgValsCons(X:Id, V:Val, KWS:KwArgVals)) =>
    appendKwDictVals(appendDictVal(DVS, Id2String(X), V), KWS)
  rule appendKwDictVals(DVS:DictVals, kwArgStringValsCons(S:String, V:Val, KWS:KwArgVals)) =>
    appendKwDictVals(appendDictVal(DVS, S, V), KWS)

  rule kwExtrasDictVals(#noKwArgVals, _:IdItems) => #noDictVals
  rule kwExtrasDictVals(kwArgValsCons(X:Id, _:Val, KWS:KwArgVals), IDS:IdItems) =>
    kwExtrasDictVals(KWS, IDS)
    requires idContains(X, IDS)
  rule kwExtrasDictVals(kwArgValsCons(X:Id, V:Val, KWS:KwArgVals), IDS:IdItems) =>
    dictValsCons(Id2String(X), V, kwExtrasDictVals(KWS, IDS))
    requires notBool idContains(X, IDS)
  rule kwExtrasDictVals(kwArgStringValsCons(S:String, _:Val, KWS:KwArgVals), IDS:IdItems) =>
    kwExtrasDictVals(KWS, IDS)
    requires stringIdContains(S, IDS)
  rule kwExtrasDictVals(kwArgStringValsCons(S:String, V:Val, KWS:KwArgVals), IDS:IdItems) =>
    dictValsCons(S, V, kwExtrasDictVals(KWS, IDS))
    requires notBool stringIdContains(S, IDS)

  rule appendDictVal(#noDictVals, K:Val, V:Val) => dictValsCons(K, V, #noDictVals)
  rule appendDictVal(dictValsCons(K0:Val, _:Val, DVS:DictVals), K:Val, V:Val) =>
    dictValsCons(K0, V, DVS)
    requires valEq(K, K0)
  rule appendDictVal(dictValsCons(K0:Val, V0:Val, DVS:DictVals), K:Val, V:Val) =>
    dictValsCons(K0, V0, appendDictVal(DVS, K, V))
    requires notBool valEq(K, K0)

  rule appendDictUnpack(DVS:DictVals, ({}):Val) => DVS
  rule appendDictUnpack(DVS:DictVals, dictVal(DS:DictItems)) => appendDictItems(DVS, DS)

  rule appendDictItems(DVS:DictVals, dictItemsLast(K:Val, V:Val)) =>
    appendDictVal(DVS, K, V)
  rule appendDictItems(DVS:DictVals, dictItemsCons(K:Val, V:Val, DS:DictItems)) =>
    appendDictItems(appendDictVal(DVS, K, V), DS)

  rule appendDictPairVal(DVS:DictVals, listVal(valItemsCons(K:Val, valItemsLast(V:Val)))) =>
    appendDictVal(DVS, K, V)
  rule appendDictPairVal(DVS:DictVals, tupleVal(valItemsCons(K:Val, valItemsLast(V:Val)))) =>
    appendDictVal(DVS, K, V)

  rule dictCtorPairs(valItemsLast(Pair:Val), DVS:DictVals) =>
    appendDictPairVal(DVS, Pair)
  rule dictCtorPairs(valItemsCons(Pair:Val, Rest:ValItems), DVS:DictVals) =>
    dictCtorPairs(Rest, appendDictPairVal(DVS, Pair))

  rule bindArgs(Rho:Map, #noIds, #noArgVals) => Rho
  rule bindArgs(Rho:Map, idItemsLast(X:Id), argValsCons(V:Val, #noArgVals)) => Rho [ X <- V ]
  rule bindArgs(Rho:Map, idItemsCons(X:Id, IDS:IdItems), argValsCons(V:Val, VS:ArgVals)) =>
    bindArgs(Rho [ X <- V ], IDS, VS)

  rule bindVarArgs(Rho:Map, #noIds, Var:Id, VS:ArgVals) =>
    Rho [ Var <- argValsToTupleVal(VS) ]
  rule bindVarArgs(Rho:Map, idItemsLast(X:Id), Var:Id, argValsCons(V:Val, VS:ArgVals)) =>
    (Rho [ X <- V ]) [ Var <- argValsToTupleVal(VS) ]
  rule bindVarArgs(Rho:Map, idItemsCons(X:Id, IDS:IdItems), Var:Id, argValsCons(V:Val, VS:ArgVals)) =>
    bindVarArgs(Rho [ X <- V ], IDS, Var, VS)

  rule bindKwArgs(Rho:Map, IDS:IdItems, Kw:Id, VS:ArgVals, KWS:KwArgVals) =>
    (bindArgs(Rho, IDS, VS)) [ Kw <- kwExtrasDict(KWS, IDS) ]

  rule bindPosOnlyArgs(Rho:Map, Pos:IdItems, Rest:IdItems, VS:ArgVals) =>
    bindArgs(bindArgs(Rho, Pos, takeArgVals(VS, idItemsLen(Pos))), Rest, dropArgVals(VS, idItemsLen(Pos)))

  rule bindPosOnlyMixedArgs(Rho:Map, Pos:IdItems, Rest:IdItems, VS:ArgVals, KWS:KwArgVals) =>
    bindArgs(
      bindArgs(Rho, Pos, takeArgVals(VS, idItemsLen(Pos))),
      Rest,
      buildMixedDefaultArgs(Rest, dropArgVals(VS, idItemsLen(Pos)), KWS, #noArgVals))

  rule bindVals(Rho:Map, idItemsLast(X:Id), valItemsLast(V:Val)) => Rho [ X <- V ]
  rule bindVals(Rho:Map, idItemsCons(X:Id, IDS:IdItems), valItemsCons(V:Val, VS:ValItems)) =>
    bindVals(Rho [ X <- V ], IDS, VS)

  rule bindTarget(Rho:Map, targetName(X:Id), V:Val) => Rho [ X <- V ]
  rule bindTarget(Rho:Map, targetSeq(TS:Targets), listVal(VS:ValItems)) =>
    bindTargets(Rho, TS, VS)
  rule bindTarget(Rho:Map, targetSeq(TS:Targets), tupleVal(VS:ValItems)) =>
    bindTargets(Rho, TS, VS)
  rule bindTarget(Rho:Map, targetSeq(TS:Targets), setVal(VS:ValItems)) =>
    bindTargets(Rho, TS, VS)

  rule bindTargets(Rho:Map, targetsLast(T:Target), valItemsLast(V:Val)) =>
    bindTarget(Rho, T, V)
  rule bindTargets(Rho:Map, targetsCons(T:Target, TS:Targets), valItemsCons(V:Val, VS:ValItems)) =>
    bindTargets(bindTarget(Rho, T, V), TS, VS)

  rule delIds(Rho:Map, #noIds) => Rho
  rule delIds(Rho:Map, idItemsLast(X:Id)) => Rho [ X <- undef ]
  rule delIds(Rho:Map, idItemsCons(X:Id, IDS:IdItems)) => delIds(Rho [ X <- undef ], IDS)

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

  rule argValsToTupleVal(#noArgVals) => ()
  rule argValsToTupleVal(VS:ArgVals) => tupleVal(argValsToValItems(VS))
    requires notBool emptyArgVals(VS)

  rule setFromArgVals(#noArgVals) => set()
  rule setFromArgVals(VS:ArgVals) => setVal(argValsToSetItems(VS))
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
  rule minArgVals(argValsCons(V:Val, #noArgVals)) => intValue(V)
    requires isIntLike(V)
  rule minArgVals(argValsCons(V:Val, VS:ArgVals)) => intValue(V)
    requires notBool emptyArgVals(VS)
      andBool isIntLike(V)
      andBool intValue(V) <=Int minArgVals(VS)
  rule minArgVals(argValsCons(V:Val, VS:ArgVals)) => minArgVals(VS)
    requires notBool emptyArgVals(VS)
      andBool isIntLike(V)
      andBool intValue(V) >Int minArgVals(VS)
  rule maxArgVals(argValsCons(V:Val, #noArgVals)) => intValue(V)
    requires isIntLike(V)
  rule maxArgVals(argValsCons(V:Val, VS:ArgVals)) => intValue(V)
    requires notBool emptyArgVals(VS)
      andBool isIntLike(V)
      andBool intValue(V) >=Int maxArgVals(VS)
  rule maxArgVals(argValsCons(V:Val, VS:ArgVals)) => maxArgVals(VS)
    requires notBool emptyArgVals(VS)
      andBool isIntLike(V)
      andBool intValue(V) <Int maxArgVals(VS)
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
  rule isListSequence(#kwDefaultMissing) => false
  rule isListSequence(closure(_:Id, _:Exp)) => false
  rule isListSequence(closureArgs(_:IdItems, _:Exp)) => false
  rule isListSequence(closureDefaults(_:IdItems, _:ArgVals, _:Exp)) => false
  rule isListSequence(closureVarArgs(_:IdItems, _:Id, _:Exp)) => false
  rule isListSequence(closureVarArgsDefaults(_:IdItems, _:ArgVals, _:Id, _:Exp)) => false
  rule isListSequence(closureKwArgs(_:IdItems, _:Id, _:Exp)) => false
  rule isListSequence(closurePosOnly(_:IdItems, _:IdItems, _:Exp)) => false
  rule isListSequence(closureKwOnly(_:IdItems, _:Exp)) => false
  rule isListSequence(closureKwDefaults(_:IdItems, _:ArgVals, _:Exp)) => false
  rule isListSequence(closurePosKwOnly(_:IdItems, _:IdItems, _:Exp)) => false
  rule isListSequence(closurePosKwDefaults(_:IdItems, _:ArgVals, _:IdItems, _:ArgVals, _:Exp)) => false
  rule isListSequence(functionVal(_:Id, _:Block)) => false
  rule isListSequence(functionValArgs(_:IdItems, _:Block)) => false
  rule isListSequence(functionValDefaults(_:IdItems, _:ArgVals, _:Block)) => false
  rule isListSequence(functionValVarArgs(_:IdItems, _:Id, _:Block)) => false
  rule isListSequence(functionValVarArgsDefaults(_:IdItems, _:ArgVals, _:Id, _:Block)) => false
  rule isListSequence(functionValKwArgs(_:IdItems, _:Id, _:Block)) => false
  rule isListSequence(functionValPosOnly(_:IdItems, _:IdItems, _:Block)) => false
  rule isListSequence(functionValKwOnly(_:IdItems, _:Block)) => false
  rule isListSequence(functionValKwDefaults(_:IdItems, _:ArgVals, _:Block)) => false
  rule isListSequence(functionValPosKwOnly(_:IdItems, _:IdItems, _:Block)) => false
  rule isListSequence(functionValPosKwDefaults(_:IdItems, _:ArgVals, _:IdItems, _:ArgVals, _:Block)) => false
  rule isListSequence(rangeVal(_:Int, _:Int)) => false
  rule isListSequence(rangeVal(_:Int, _:Int, _:Int)) => false
  rule isListSequence(argsVal(_:ArgVals)) => false
  rule isListSequence(dictArgsVal(_:DictVals)) => false
  rule isListSequence(_:Float) => false

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
  rule isTupleSequence(#kwDefaultMissing) => false
  rule isTupleSequence(closure(_:Id, _:Exp)) => false
  rule isTupleSequence(closureArgs(_:IdItems, _:Exp)) => false
  rule isTupleSequence(closureDefaults(_:IdItems, _:ArgVals, _:Exp)) => false
  rule isTupleSequence(closureVarArgs(_:IdItems, _:Id, _:Exp)) => false
  rule isTupleSequence(closureVarArgsDefaults(_:IdItems, _:ArgVals, _:Id, _:Exp)) => false
  rule isTupleSequence(closureKwArgs(_:IdItems, _:Id, _:Exp)) => false
  rule isTupleSequence(closurePosOnly(_:IdItems, _:IdItems, _:Exp)) => false
  rule isTupleSequence(closureKwOnly(_:IdItems, _:Exp)) => false
  rule isTupleSequence(closureKwDefaults(_:IdItems, _:ArgVals, _:Exp)) => false
  rule isTupleSequence(closurePosKwOnly(_:IdItems, _:IdItems, _:Exp)) => false
  rule isTupleSequence(closurePosKwDefaults(_:IdItems, _:ArgVals, _:IdItems, _:ArgVals, _:Exp)) => false
  rule isTupleSequence(functionVal(_:Id, _:Block)) => false
  rule isTupleSequence(functionValArgs(_:IdItems, _:Block)) => false
  rule isTupleSequence(functionValDefaults(_:IdItems, _:ArgVals, _:Block)) => false
  rule isTupleSequence(functionValVarArgs(_:IdItems, _:Id, _:Block)) => false
  rule isTupleSequence(functionValVarArgsDefaults(_:IdItems, _:ArgVals, _:Id, _:Block)) => false
  rule isTupleSequence(functionValKwArgs(_:IdItems, _:Id, _:Block)) => false
  rule isTupleSequence(functionValPosOnly(_:IdItems, _:IdItems, _:Block)) => false
  rule isTupleSequence(functionValKwOnly(_:IdItems, _:Block)) => false
  rule isTupleSequence(functionValKwDefaults(_:IdItems, _:ArgVals, _:Block)) => false
  rule isTupleSequence(functionValPosKwOnly(_:IdItems, _:IdItems, _:Block)) => false
  rule isTupleSequence(functionValPosKwDefaults(_:IdItems, _:ArgVals, _:IdItems, _:ArgVals, _:Block)) => false
  rule isTupleSequence(rangeVal(_:Int, _:Int)) => false
  rule isTupleSequence(rangeVal(_:Int, _:Int, _:Int)) => false
  rule isTupleSequence(argsVal(_:ArgVals)) => false
  rule isTupleSequence(dictArgsVal(_:DictVals)) => false
  rule isTupleSequence(_:Float) => false

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
  rule + F:Float => F
  rule - V:Val => 0 -Int intValue(V) requires isIntLike(V)
  rule - F:Float => --Float F
  rule ~ V:Val => ~Int intValue(V) requires isIntLike(V)

  rule V1:Val + V2:Val => intValue(V1) +Int intValue(V2)
    requires isIntLike(V1) andBool isIntLike(V2)
  rule F1:Float + F2:Float => F1 +Float F2
  rule F:Float + V:Val => F +Float floatValue(V)
    requires isIntLike(V)
  rule V:Val + F:Float => floatValue(V) +Float F
    requires isIntLike(V)
  rule V1:Val - V2:Val => intValue(V1) -Int intValue(V2)
    requires isIntLike(V1) andBool isIntLike(V2)
  rule F1:Float - F2:Float => F1 -Float F2
  rule F:Float - V:Val => F -Float floatValue(V)
    requires isIntLike(V)
  rule V:Val - F:Float => floatValue(V) -Float F
    requires isIntLike(V)
  rule V1:Val * V2:Val => intValue(V1) *Int intValue(V2)
    requires isIntLike(V1) andBool isIntLike(V2)
  rule F1:Float * F2:Float => F1 *Float F2
  rule F:Float * V:Val => F *Float floatValue(V)
    requires isIntLike(V)
  rule V:Val * F:Float => floatValue(V) *Float F
    requires isIntLike(V)
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
  rule V1:Val ** V2:Val => Int2Float(intValue(V1), 53, 11) ^Float Int2Float(intValue(V2), 53, 11)
    requires isIntLike(V1) andBool isIntLike(V2) andBool intValue(V1) =/=Int 0 andBool intValue(V2) <Int 0
  rule F1:Float ** F2:Float => F1 ^Float F2
    requires F1 >=Float 0.0 andBool (F1 =/=Float 0.0 orBool F2 >=Float 0.0)
  rule F:Float ** V:Val => F ^Float floatValue(V)
    requires isIntLike(V) andBool F >=Float 0.0 andBool (F =/=Float 0.0 orBool intValue(V) >=Int 0)
  rule V:Val ** F:Float => floatValue(V) ^Float F
    requires isIntLike(V) andBool floatValue(V) >=Float 0.0 andBool (intValue(V) =/=Int 0 orBool F >=Float 0.0)
  rule floorDivExp(V1:Val, V2:Val) => pyFloorDiv(intValue(V1), intValue(V2))
    requires isIntLike(V1) andBool isIntLike(V2) andBool intValue(V2) =/=Int 0
  rule floorDivExp(F1:Float, F2:Float) => pyFloatFloorDiv(F1, F2)
    requires F2 =/=Float 0.0
  rule floorDivExp(F:Float, V:Val) => pyFloatFloorDiv(F, floatValue(V))
    requires isIntLike(V) andBool intValue(V) =/=Int 0
  rule floorDivExp(V:Val, F:Float) => pyFloatFloorDiv(floatValue(V), F)
    requires isIntLike(V) andBool F =/=Float 0.0
  rule floorDivInternal(V1:Val, V2:Val) => pyFloorDiv(intValue(V1), intValue(V2))
    requires isIntLike(V1) andBool isIntLike(V2) andBool intValue(V2) =/=Int 0
  rule floorDivInternal(F1:Float, F2:Float) => pyFloatFloorDiv(F1, F2)
    requires F2 =/=Float 0.0
  rule floorDivInternal(F:Float, V:Val) => pyFloatFloorDiv(F, floatValue(V))
    requires isIntLike(V) andBool intValue(V) =/=Int 0
  rule floorDivInternal(V:Val, F:Float) => pyFloatFloorDiv(floatValue(V), F)
    requires isIntLike(V) andBool F =/=Float 0.0
  rule trueDivInternal(V1:Val, V2:Val) =>
    Int2Float(intValue(V1), 53, 11) /Float Int2Float(intValue(V2), 53, 11)
    requires isIntLike(V1) andBool isIntLike(V2) andBool intValue(V2) =/=Int 0
  rule trueDivInternal(F1:Float, F2:Float) => F1 /Float F2
    requires F2 =/=Float 0.0
  rule trueDivInternal(F:Float, V:Val) => F /Float floatValue(V)
    requires isIntLike(V) andBool intValue(V) =/=Int 0
  rule trueDivInternal(V:Val, F:Float) => floatValue(V) /Float F
    requires isIntLike(V) andBool F =/=Float 0.0
  rule V1:Val % V2:Val => pyModulo(intValue(V1), intValue(V2))
    requires isIntLike(V1) andBool isIntLike(V2) andBool intValue(V2) =/=Int 0
  rule F1:Float % F2:Float => pyFloatModulo(F1, F2)
    requires F2 =/=Float 0.0
  rule F:Float % V:Val => pyFloatModulo(F, floatValue(V))
    requires isIntLike(V) andBool intValue(V) =/=Int 0
  rule V:Val % F:Float => pyFloatModulo(floatValue(V), F)
    requires isIntLike(V) andBool F =/=Float 0.0
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

  rule attrExp(rangeVal(Start:Int, _:Int), Attr:Id) => Start
    requires Id2String(Attr) ==String "start"
  rule attrExp(rangeVal(_:Int, Stop:Int), Attr:Id) => Stop
    requires Id2String(Attr) ==String "stop"
  rule attrExp(rangeVal(_:Int, _:Int), Attr:Id) => 1
    requires Id2String(Attr) ==String "step"
  rule attrExp(rangeVal(Start:Int, _:Int, _:Int), Attr:Id) => Start
    requires Id2String(Attr) ==String "start"
  rule attrExp(rangeVal(_:Int, Stop:Int, _:Int), Attr:Id) => Stop
    requires Id2String(Attr) ==String "stop"
  rule attrExp(rangeVal(_:Int, _:Int, Step:Int), Attr:Id) => Step
    requires Id2String(Attr) ==String "step"
  rule attrExp(sliceVal(Start:Val, _:Val, _:Val), Attr:Id) => Start
    requires Id2String(Attr) ==String "start"
  rule attrExp(sliceVal(_:Val, Stop:Val, _:Val), Attr:Id) => Stop
    requires Id2String(Attr) ==String "stop"
  rule attrExp(sliceVal(_:Val, _:Val, Step:Val), Attr:Id) => Step
    requires Id2String(Attr) ==String "step"

  rule V1:Val < V2:Val => boolValue(intValue(V1) <Int intValue(V2))
    requires isIntLike(V1) andBool isIntLike(V2)
  rule F1:Float < F2:Float => boolValue(F1 <Float F2)
  rule F:Float < V:Val => boolValue(F <Float floatValue(V))
    requires isIntLike(V)
  rule V:Val < F:Float => boolValue(floatValue(V) <Float F)
    requires isIntLike(V)
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
  rule F1:Float <= F2:Float => boolValue(F1 <=Float F2)
  rule F:Float <= V:Val => boolValue(F <=Float floatValue(V))
    requires isIntLike(V)
  rule V:Val <= F:Float => boolValue(floatValue(V) <=Float F)
    requires isIntLike(V)
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
  rule F1:Float > F2:Float => boolValue(F1 >Float F2)
  rule F:Float > V:Val => boolValue(F >Float floatValue(V))
    requires isIntLike(V)
  rule V:Val > F:Float => boolValue(floatValue(V) >Float F)
    requires isIntLike(V)
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
  rule F1:Float >= F2:Float => boolValue(F1 >=Float F2)
  rule F:Float >= V:Val => boolValue(F >=Float floatValue(V))
    requires isIntLike(V)
  rule V:Val >= F:Float => boolValue(floatValue(V) >=Float F)
    requires isIntLike(V)
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
  rule subscriptExp(V:Val, sliceVal(Lower:Val, Upper:Val, None)) => sliceExp(V, Lower, Upper)
  rule subscriptExp(V:Val, sliceVal(Lower:Val, Upper:Val, Step:Val)) => sliceStepExp(V, Lower, Upper, Step)
    requires isIntLike(Step)
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
  rule <k> lambdaDefaultsExp(IDS:IdItems, Defaults:ArgExps, Body:Exp) =>
           evalArgs(Defaults, #noArgVals) ~> bindLambdaDefaults(IDS, Body)
       ... </k>
  rule <k> argsVal(Defaults:ArgVals) ~> bindLambdaDefaults(IDS:IdItems, Body:Exp) =>
           closureDefaults(IDS, Defaults, Body)
       ... </k>
  rule <k> lambdaVarArgsExp(IDS:IdItems, Var:Id, Body:Exp) => closureVarArgs(IDS, Var, Body) ... </k>
  rule <k> lambdaVarArgsDefaultsExp(IDS:IdItems, Defaults:ArgExps, Var:Id, Body:Exp) =>
           evalArgs(Defaults, #noArgVals) ~> bindLambdaVarArgsDefaults(IDS, Var, Body)
       ... </k>
  rule <k> argsVal(Defaults:ArgVals) ~> bindLambdaVarArgsDefaults(IDS:IdItems, Var:Id, Body:Exp) =>
           closureVarArgsDefaults(IDS, Defaults, Var, Body)
       ... </k>
  rule <k> lambdaKwArgsExp(IDS:IdItems, Kw:Id, Body:Exp) => closureKwArgs(IDS, Kw, Body) ... </k>
  rule <k> lambdaPosOnlyExp(Pos:IdItems, Rest:IdItems, Body:Exp) => closurePosOnly(Pos, Rest, Body) ... </k>
  rule <k> lambdaKwOnlyExp(IDS:IdItems, Body:Exp) => closureKwOnly(IDS, Body) ... </k>
  rule <k> lambdaKwDefaultsExp(IDS:IdItems, Defaults:ArgExps, Body:Exp) =>
           evalArgs(Defaults, #noArgVals) ~> bindLambdaKwDefaults(IDS, Body)
       ... </k>
  rule <k> argsVal(Defaults:ArgVals) ~> bindLambdaKwDefaults(IDS:IdItems, Body:Exp) =>
           closureKwDefaults(IDS, Defaults, Body)
       ... </k>
  rule <k> lambdaPosKwOnlyExp(Pos:IdItems, KwOnly:IdItems, Body:Exp) =>
           closurePosKwOnly(Pos, KwOnly, Body)
       ... </k>
  rule <k> lambdaPosKwDefaultsExp(Pos:IdItems, PosDefaults:ArgExps, KwOnly:IdItems, KwDefaults:ArgExps, Body:Exp) =>
           evalArgs(PosDefaults, #noArgVals) ~> bindLambdaPosKwDefaults(Pos, KwDefaults, KwOnly, Body)
       ... </k>
  rule <k> argsVal(PosDefaults:ArgVals) ~> bindLambdaPosKwDefaults(Pos:IdItems, KwDefaults:ArgExps, KwOnly:IdItems, Body:Exp) =>
           evalArgs(KwDefaults, #noArgVals) ~> bindLambdaPosKwDefaultVals(Pos, PosDefaults, KwOnly, Body)
       ... </k>
  rule <k> argsVal(KwDefaults:ArgVals) ~> bindLambdaPosKwDefaultVals(Pos:IdItems, PosDefaults:ArgVals, KwOnly:IdItems, Body:Exp) =>
           closurePosKwDefaults(Pos, PosDefaults, KwOnly, KwDefaults, Body)
       ... </k>
  rule <k> callExp(F:Exp, Arg:Exp) => F ~> callArg(Arg) ... </k>
  rule <k> F:Val ~> callArg(Arg:Exp) => Arg ~> callApply(F) ... </k>
  rule <k> A:Val ~> callApply(closure(X:Id, Body:Exp)) => Body ~> restoreEnv(Rho) ... </k>
       <env> Rho => Rho [ X <- A ] </env>
  rule <k> A:Val ~> callApply(closureDefaults(IDS:IdItems, Defaults:ArgVals, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, completeDefaultArgs(IDS, argValsCons(A, #noArgVals), Defaults)) </env>
    requires defaultsCallArityOk(IDS, argValsCons(A, #noArgVals), Defaults)
  rule <k> A:Val ~> callApply(closureVarArgs(IDS:IdItems, Var:Id, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, argValsCons(A, #noArgVals)) </env>
    requires varArgsCallArityOk(IDS, argValsCons(A, #noArgVals))
  rule <k> A:Val ~> callApply(closureVarArgsDefaults(IDS:IdItems, Defaults:ArgVals, Var:Id, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, completeVarArgsDefaultArgs(IDS, argValsCons(A, #noArgVals), Defaults)) </env>
    requires varArgsDefaultsCallArityOk(IDS, argValsCons(A, #noArgVals), Defaults)
  rule <k> A:Val ~> callApply(closureKwArgs(IDS:IdItems, Kw:Id, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindKwArgs(Rho, IDS, Kw, argValsCons(A, #noArgVals), #noKwArgVals) </env>
    requires kwargsPosCallArityOk(IDS, argValsCons(A, #noArgVals))
  rule <k> A:Val ~> callApply(closurePosOnly(Pos:IdItems, Rest:IdItems, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindPosOnlyArgs(Rho, Pos, Rest, argValsCons(A, #noArgVals)) </env>
    requires posOnlyArgsCallArityOk(Pos, Rest, argValsCons(A, #noArgVals))
  rule <k> A:Val ~> callApply(closurePosKwDefaults(Pos:IdItems, PosDefaults:ArgVals, KwOnly:IdItems, KwDefaults:ArgVals, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(bindArgs(Rho, Pos, completeDefaultArgs(Pos, argValsCons(A, #noArgVals), PosDefaults)), KwOnly, buildKwDefaultArgs(KwOnly, #noKwArgVals, KwDefaults)) </env>
    requires posKwOnlyArgsDefaultsCallArityOk(Pos, KwOnly, argValsCons(A, #noArgVals), PosDefaults, KwDefaults)
  rule <k> A:Val ~> callApply(functionVal(X:Id, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => Rho [ X <- A ] </env>
  rule <k> A:Val ~> callApply(functionVal(X:Id, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => Rho [ X <- A ] </env>
  rule <k> A:Val ~> callApply(functionValDefaults(IDS:IdItems, Defaults:ArgVals, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, completeDefaultArgs(IDS, argValsCons(A, #noArgVals), Defaults)) </env>
    requires defaultsCallArityOk(IDS, argValsCons(A, #noArgVals), Defaults)
  rule <k> A:Val ~> callApply(functionValDefaults(IDS:IdItems, Defaults:ArgVals, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, completeDefaultArgs(IDS, argValsCons(A, #noArgVals), Defaults)) </env>
    requires defaultsCallArityOk(IDS, argValsCons(A, #noArgVals), Defaults)
  rule <k> A:Val ~> callApply(functionValVarArgs(IDS:IdItems, Var:Id, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, argValsCons(A, #noArgVals)) </env>
    requires varArgsCallArityOk(IDS, argValsCons(A, #noArgVals))
  rule <k> A:Val ~> callApply(functionValVarArgs(IDS:IdItems, Var:Id, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, argValsCons(A, #noArgVals)) </env>
    requires varArgsCallArityOk(IDS, argValsCons(A, #noArgVals))
  rule <k> A:Val ~> callApply(functionValVarArgsDefaults(IDS:IdItems, Defaults:ArgVals, Var:Id, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, completeVarArgsDefaultArgs(IDS, argValsCons(A, #noArgVals), Defaults)) </env>
    requires varArgsDefaultsCallArityOk(IDS, argValsCons(A, #noArgVals), Defaults)
  rule <k> A:Val ~> callApply(functionValVarArgsDefaults(IDS:IdItems, Defaults:ArgVals, Var:Id, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, completeVarArgsDefaultArgs(IDS, argValsCons(A, #noArgVals), Defaults)) </env>
    requires varArgsDefaultsCallArityOk(IDS, argValsCons(A, #noArgVals), Defaults)
  rule <k> A:Val ~> callApply(functionValKwArgs(IDS:IdItems, Kw:Id, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindKwArgs(Rho, IDS, Kw, argValsCons(A, #noArgVals), #noKwArgVals) </env>
    requires kwargsPosCallArityOk(IDS, argValsCons(A, #noArgVals))
  rule <k> A:Val ~> callApply(functionValKwArgs(IDS:IdItems, Kw:Id, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindKwArgs(Rho, IDS, Kw, argValsCons(A, #noArgVals), #noKwArgVals) </env>
    requires kwargsPosCallArityOk(IDS, argValsCons(A, #noArgVals))
  rule <k> A:Val ~> callApply(functionValPosOnly(Pos:IdItems, Rest:IdItems, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindPosOnlyArgs(Rho, Pos, Rest, argValsCons(A, #noArgVals)) </env>
    requires posOnlyArgsCallArityOk(Pos, Rest, argValsCons(A, #noArgVals))
  rule <k> A:Val ~> callApply(functionValPosOnly(Pos:IdItems, Rest:IdItems, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindPosOnlyArgs(Rho, Pos, Rest, argValsCons(A, #noArgVals)) </env>
    requires posOnlyArgsCallArityOk(Pos, Rest, argValsCons(A, #noArgVals))
  rule <k> A:Val ~> callApply(functionValPosKwDefaults(Pos:IdItems, PosDefaults:ArgVals, KwOnly:IdItems, KwDefaults:ArgVals, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindArgs(bindArgs(Rho, Pos, completeDefaultArgs(Pos, argValsCons(A, #noArgVals), PosDefaults)), KwOnly, buildKwDefaultArgs(KwOnly, #noKwArgVals, KwDefaults)) </env>
    requires posKwOnlyArgsDefaultsCallArityOk(Pos, KwOnly, argValsCons(A, #noArgVals), PosDefaults, KwDefaults)
  rule <k> A:Val ~> callApply(functionValPosKwDefaults(Pos:IdItems, PosDefaults:ArgVals, KwOnly:IdItems, KwDefaults:ArgVals, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(bindArgs(Rho, Pos, completeDefaultArgs(Pos, argValsCons(A, #noArgVals), PosDefaults)), KwOnly, buildKwDefaultArgs(KwOnly, #noKwArgVals, KwDefaults)) </env>
    requires posKwOnlyArgsDefaultsCallArityOk(Pos, KwOnly, argValsCons(A, #noArgVals), PosDefaults, KwDefaults)
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
  rule <k> evalArgs(starArgExp(E:Exp), VS:ArgVals) =>
           E ~> evalStarArgNext(#noArgs, VS)
       ... </k>
  rule <k> evalArgs(starArgExpsCons(E:Exp, ES:ArgExps), VS:ArgVals) =>
           E ~> evalStarArgNext(ES, VS)
       ... </k>
  rule <k> V:Val ~> evalArgNext(ES:ArgExps, VS:ArgVals) =>
           evalArgs(ES, appendArgVal(VS, V))
       ... </k>
  rule <k> V:Val ~> evalStarArgNext(ES:ArgExps, VS:ArgVals) =>
           evalArgs(ES, concatArgVals(VS, iterableArgVals(V)))
       ... </k>
  rule <k> argsVal(VS:ArgVals) ~> callApplyArgs(closureArgs(IDS:IdItems, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, VS) </env>
    requires sameArity(IDS, VS)
  rule <k> argsVal(VS:ArgVals) ~> callApplyArgs(closureDefaults(IDS:IdItems, Defaults:ArgVals, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, completeDefaultArgs(IDS, VS, Defaults)) </env>
    requires defaultsCallArityOk(IDS, VS, Defaults)
  rule <k> argsVal(VS:ArgVals) ~> callApplyArgs(closureVarArgs(IDS:IdItems, Var:Id, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, VS) </env>
    requires varArgsCallArityOk(IDS, VS)
  rule <k> argsVal(VS:ArgVals) ~> callApplyArgs(closureVarArgsDefaults(IDS:IdItems, Defaults:ArgVals, Var:Id, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, completeVarArgsDefaultArgs(IDS, VS, Defaults)) </env>
    requires varArgsDefaultsCallArityOk(IDS, VS, Defaults)
  rule <k> argsVal(VS:ArgVals) ~> callApplyArgs(closureKwArgs(IDS:IdItems, Kw:Id, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindKwArgs(Rho, IDS, Kw, VS, #noKwArgVals) </env>
    requires kwargsPosCallArityOk(IDS, VS)
  rule <k> argsVal(VS:ArgVals) ~> callApplyArgs(closurePosOnly(Pos:IdItems, Rest:IdItems, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindPosOnlyArgs(Rho, Pos, Rest, VS) </env>
    requires posOnlyArgsCallArityOk(Pos, Rest, VS)
  rule <k> argsVal(VS:ArgVals) ~> callApplyArgs(closurePosKwDefaults(Pos:IdItems, PosDefaults:ArgVals, KwOnly:IdItems, KwDefaults:ArgVals, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(bindArgs(Rho, Pos, completeDefaultArgs(Pos, VS, PosDefaults)), KwOnly, buildKwDefaultArgs(KwOnly, #noKwArgVals, KwDefaults)) </env>
    requires posKwOnlyArgsDefaultsCallArityOk(Pos, KwOnly, VS, PosDefaults, KwDefaults)
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
  rule <k> argsVal(VS:ArgVals) ~> callApplyArgs(functionValDefaults(IDS:IdItems, Defaults:ArgVals, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, completeDefaultArgs(IDS, VS, Defaults)) </env>
    requires defaultsCallArityOk(IDS, VS, Defaults)
  rule <k> argsVal(VS:ArgVals) ~> callApplyArgs(functionValDefaults(IDS:IdItems, Defaults:ArgVals, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, completeDefaultArgs(IDS, VS, Defaults)) </env>
    requires defaultsCallArityOk(IDS, VS, Defaults)
  rule <k> argsVal(VS:ArgVals) ~> callApplyArgs(functionValVarArgs(IDS:IdItems, Var:Id, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, VS) </env>
    requires varArgsCallArityOk(IDS, VS)
  rule <k> argsVal(VS:ArgVals) ~> callApplyArgs(functionValVarArgs(IDS:IdItems, Var:Id, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, VS) </env>
    requires varArgsCallArityOk(IDS, VS)
  rule <k> argsVal(VS:ArgVals) ~> callApplyArgs(functionValVarArgsDefaults(IDS:IdItems, Defaults:ArgVals, Var:Id, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, completeVarArgsDefaultArgs(IDS, VS, Defaults)) </env>
    requires varArgsDefaultsCallArityOk(IDS, VS, Defaults)
  rule <k> argsVal(VS:ArgVals) ~> callApplyArgs(functionValVarArgsDefaults(IDS:IdItems, Defaults:ArgVals, Var:Id, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, completeVarArgsDefaultArgs(IDS, VS, Defaults)) </env>
    requires varArgsDefaultsCallArityOk(IDS, VS, Defaults)
  rule <k> argsVal(VS:ArgVals) ~> callApplyArgs(functionValKwArgs(IDS:IdItems, Kw:Id, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindKwArgs(Rho, IDS, Kw, VS, #noKwArgVals) </env>
    requires kwargsPosCallArityOk(IDS, VS)
  rule <k> argsVal(VS:ArgVals) ~> callApplyArgs(functionValKwArgs(IDS:IdItems, Kw:Id, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindKwArgs(Rho, IDS, Kw, VS, #noKwArgVals) </env>
    requires kwargsPosCallArityOk(IDS, VS)
  rule <k> argsVal(VS:ArgVals) ~> callApplyArgs(functionValPosOnly(Pos:IdItems, Rest:IdItems, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindPosOnlyArgs(Rho, Pos, Rest, VS) </env>
    requires posOnlyArgsCallArityOk(Pos, Rest, VS)
  rule <k> argsVal(VS:ArgVals) ~> callApplyArgs(functionValPosOnly(Pos:IdItems, Rest:IdItems, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindPosOnlyArgs(Rho, Pos, Rest, VS) </env>
    requires posOnlyArgsCallArityOk(Pos, Rest, VS)
  rule <k> argsVal(VS:ArgVals) ~> callApplyArgs(functionValPosKwDefaults(Pos:IdItems, PosDefaults:ArgVals, KwOnly:IdItems, KwDefaults:ArgVals, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindArgs(bindArgs(Rho, Pos, completeDefaultArgs(Pos, VS, PosDefaults)), KwOnly, buildKwDefaultArgs(KwOnly, #noKwArgVals, KwDefaults)) </env>
    requires posKwOnlyArgsDefaultsCallArityOk(Pos, KwOnly, VS, PosDefaults, KwDefaults)
  rule <k> argsVal(VS:ArgVals) ~> callApplyArgs(functionValPosKwDefaults(Pos:IdItems, PosDefaults:ArgVals, KwOnly:IdItems, KwDefaults:ArgVals, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(bindArgs(Rho, Pos, completeDefaultArgs(Pos, VS, PosDefaults)), KwOnly, buildKwDefaultArgs(KwOnly, #noKwArgVals, KwDefaults)) </env>
    requires posKwOnlyArgsDefaultsCallArityOk(Pos, KwOnly, VS, PosDefaults, KwDefaults)

  rule <k> callKwArgsExp(F:Exp, KWS:KwArgExps) => F ~> callKwArgs(KWS) ... </k>
  rule <k> F:Val ~> callKwArgs(KWS:KwArgExps) =>
           evalKwArgs(KWS, #noKwArgVals) ~> callApplyKwArgs(F)
       ... </k>
  rule <k> evalKwArgs(#noKwArgs, KWS:KwArgVals) => kwArgsVal(KWS) ... </k>
  rule <k> evalKwArgs(kwArgExp(X:Id, E:Exp), KWS:KwArgVals) =>
           E ~> evalKwArgNext(X, #noKwArgs, KWS)
       ... </k>
  rule <k> evalKwArgs(kwArgExpsCons(X:Id, E:Exp, Rest:KwArgExps), KWS:KwArgVals) =>
           E ~> evalKwArgNext(X, Rest, KWS)
       ... </k>
  rule <k> evalKwArgs(kwStarArgExp(E:Exp), KWS:KwArgVals) =>
           E ~> evalKwStarArgNext(#noKwArgs, KWS)
       ... </k>
  rule <k> evalKwArgs(kwStarArgExpsCons(E:Exp, Rest:KwArgExps), KWS:KwArgVals) =>
           E ~> evalKwStarArgNext(Rest, KWS)
       ... </k>
  rule <k> V:Val ~> evalKwArgNext(X:Id, Rest:KwArgExps, KWS:KwArgVals) =>
           evalKwArgs(Rest, appendKwArgVal(KWS, X, V))
       ... </k>
  rule <k> V:Val ~> evalKwStarArgNext(Rest:KwArgExps, KWS:KwArgVals) =>
           evalKwArgs(Rest, appendKwUnpack(KWS, V))
       ... </k>
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(closure(X:Id, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, idItemsLast(X), buildKwDefaultArgs(idItemsLast(X), KWS, #noArgVals)) </env>
    requires keywordOnlyCallArityOk(idItemsLast(X), KWS, #noArgVals)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(closureArgs(IDS:IdItems, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, buildKwDefaultArgs(IDS, KWS, #noArgVals)) </env>
    requires keywordOnlyCallArityOk(IDS, KWS, #noArgVals)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(closureDefaults(IDS:IdItems, Defaults:ArgVals, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, buildKwDefaultArgs(IDS, KWS, Defaults)) </env>
    requires keywordOnlyCallArityOk(IDS, KWS, Defaults)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(closureVarArgs(IDS:IdItems, Var:Id, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, buildKwDefaultArgs(IDS, KWS, #noArgVals)) </env>
    requires keywordOnlyCallArityOk(IDS, KWS, #noArgVals)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(closureVarArgsDefaults(IDS:IdItems, Defaults:ArgVals, Var:Id, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, buildKwDefaultArgs(IDS, KWS, Defaults)) </env>
    requires keywordOnlyCallArityOk(IDS, KWS, Defaults)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(closureKwArgs(IDS:IdItems, Kw:Id, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindKwArgs(Rho, IDS, Kw, buildKwDefaultArgs(IDS, KWS, #noArgVals), KWS) </env>
    requires kwargsKeywordCallArityOk(IDS, KWS)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(closurePosOnly(Pos:IdItems, Rest:IdItems, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindPosOnlyMixedArgs(Rho, Pos, Rest, #noArgVals, KWS) </env>
    requires posOnlyKeywordCallArityOk(Pos, Rest, KWS)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(closureKwOnly(IDS:IdItems, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, buildKwDefaultArgs(IDS, KWS, #noArgVals)) </env>
    requires keywordOnlyCallArityOk(IDS, KWS, #noArgVals)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(closureKwDefaults(IDS:IdItems, Defaults:ArgVals, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, buildKwDefaultArgs(IDS, KWS, Defaults)) </env>
    requires keywordOnlyCallArityOk(IDS, KWS, Defaults)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(closurePosKwOnly(Pos:IdItems, KwOnly:IdItems, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(bindArgs(Rho, Pos, buildKwDefaultArgs(Pos, KWS, #noArgVals)), KwOnly, buildKwDefaultArgs(KwOnly, KWS, #noArgVals)) </env>
    requires posKwOnlyKeywordCallArityOk(Pos, KwOnly, KWS)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(closurePosKwDefaults(Pos:IdItems, PosDefaults:ArgVals, KwOnly:IdItems, KwDefaults:ArgVals, Body:Exp)) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(bindArgs(Rho, Pos, buildKwDefaultArgs(Pos, KWS, PosDefaults)), KwOnly, buildKwDefaultArgs(KwOnly, KWS, KwDefaults)) </env>
    requires posKwOnlyKeywordDefaultsCallArityOk(Pos, KwOnly, KWS, PosDefaults, KwDefaults)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(functionVal(X:Id, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, idItemsLast(X), buildKwDefaultArgs(idItemsLast(X), KWS, #noArgVals)) </env>
    requires keywordOnlyCallArityOk(idItemsLast(X), KWS, #noArgVals)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(functionVal(X:Id, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, idItemsLast(X), buildKwDefaultArgs(idItemsLast(X), KWS, #noArgVals)) </env>
    requires keywordOnlyCallArityOk(idItemsLast(X), KWS, #noArgVals)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(functionValArgs(IDS:IdItems, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, buildKwDefaultArgs(IDS, KWS, #noArgVals)) </env>
    requires keywordOnlyCallArityOk(IDS, KWS, #noArgVals)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(functionValArgs(IDS:IdItems, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, buildKwDefaultArgs(IDS, KWS, #noArgVals)) </env>
    requires keywordOnlyCallArityOk(IDS, KWS, #noArgVals)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(functionValDefaults(IDS:IdItems, Defaults:ArgVals, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, buildKwDefaultArgs(IDS, KWS, Defaults)) </env>
    requires keywordOnlyCallArityOk(IDS, KWS, Defaults)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(functionValDefaults(IDS:IdItems, Defaults:ArgVals, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, buildKwDefaultArgs(IDS, KWS, Defaults)) </env>
    requires keywordOnlyCallArityOk(IDS, KWS, Defaults)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(functionValVarArgs(IDS:IdItems, Var:Id, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, buildKwDefaultArgs(IDS, KWS, #noArgVals)) </env>
    requires keywordOnlyCallArityOk(IDS, KWS, #noArgVals)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(functionValVarArgs(IDS:IdItems, Var:Id, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, buildKwDefaultArgs(IDS, KWS, #noArgVals)) </env>
    requires keywordOnlyCallArityOk(IDS, KWS, #noArgVals)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(functionValVarArgsDefaults(IDS:IdItems, Defaults:ArgVals, Var:Id, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, buildKwDefaultArgs(IDS, KWS, Defaults)) </env>
    requires keywordOnlyCallArityOk(IDS, KWS, Defaults)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(functionValVarArgsDefaults(IDS:IdItems, Defaults:ArgVals, Var:Id, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, buildKwDefaultArgs(IDS, KWS, Defaults)) </env>
    requires keywordOnlyCallArityOk(IDS, KWS, Defaults)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(functionValKwArgs(IDS:IdItems, Kw:Id, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindKwArgs(Rho, IDS, Kw, buildKwDefaultArgs(IDS, KWS, #noArgVals), KWS) </env>
    requires kwargsKeywordCallArityOk(IDS, KWS)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(functionValKwArgs(IDS:IdItems, Kw:Id, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindKwArgs(Rho, IDS, Kw, buildKwDefaultArgs(IDS, KWS, #noArgVals), KWS) </env>
    requires kwargsKeywordCallArityOk(IDS, KWS)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(functionValPosOnly(Pos:IdItems, Rest:IdItems, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindPosOnlyMixedArgs(Rho, Pos, Rest, #noArgVals, KWS) </env>
    requires posOnlyKeywordCallArityOk(Pos, Rest, KWS)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(functionValPosOnly(Pos:IdItems, Rest:IdItems, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindPosOnlyMixedArgs(Rho, Pos, Rest, #noArgVals, KWS) </env>
    requires posOnlyKeywordCallArityOk(Pos, Rest, KWS)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(functionValKwOnly(IDS:IdItems, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, buildKwDefaultArgs(IDS, KWS, #noArgVals)) </env>
    requires keywordOnlyCallArityOk(IDS, KWS, #noArgVals)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(functionValKwOnly(IDS:IdItems, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, buildKwDefaultArgs(IDS, KWS, #noArgVals)) </env>
    requires keywordOnlyCallArityOk(IDS, KWS, #noArgVals)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(functionValKwDefaults(IDS:IdItems, Defaults:ArgVals, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, buildKwDefaultArgs(IDS, KWS, Defaults)) </env>
    requires keywordOnlyCallArityOk(IDS, KWS, Defaults)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(functionValKwDefaults(IDS:IdItems, Defaults:ArgVals, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, buildKwDefaultArgs(IDS, KWS, Defaults)) </env>
    requires keywordOnlyCallArityOk(IDS, KWS, Defaults)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(functionValPosKwOnly(Pos:IdItems, KwOnly:IdItems, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindArgs(bindArgs(Rho, Pos, buildKwDefaultArgs(Pos, KWS, #noArgVals)), KwOnly, buildKwDefaultArgs(KwOnly, KWS, #noArgVals)) </env>
    requires posKwOnlyKeywordCallArityOk(Pos, KwOnly, KWS)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(functionValPosKwOnly(Pos:IdItems, KwOnly:IdItems, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(bindArgs(Rho, Pos, buildKwDefaultArgs(Pos, KWS, #noArgVals)), KwOnly, buildKwDefaultArgs(KwOnly, KWS, #noArgVals)) </env>
    requires posKwOnlyKeywordCallArityOk(Pos, KwOnly, KWS)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(functionValPosKwDefaults(Pos:IdItems, PosDefaults:ArgVals, KwOnly:IdItems, KwDefaults:ArgVals, block(SS:Stmts))) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindArgs(bindArgs(Rho, Pos, buildKwDefaultArgs(Pos, KWS, PosDefaults)), KwOnly, buildKwDefaultArgs(KwOnly, KWS, KwDefaults)) </env>
    requires posKwOnlyKeywordDefaultsCallArityOk(Pos, KwOnly, KWS, PosDefaults, KwDefaults)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyKwArgs(functionValPosKwDefaults(Pos:IdItems, PosDefaults:ArgVals, KwOnly:IdItems, KwDefaults:ArgVals, {})) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(bindArgs(Rho, Pos, buildKwDefaultArgs(Pos, KWS, PosDefaults)), KwOnly, buildKwDefaultArgs(KwOnly, KWS, KwDefaults)) </env>
    requires posKwOnlyKeywordDefaultsCallArityOk(Pos, KwOnly, KWS, PosDefaults, KwDefaults)

  rule <k> callMixedArgsExp(F:Exp, Args:ArgExps, KWS:KwArgExps) => F ~> callMixedArgs(Args, KWS) ... </k>
  rule <k> F:Val ~> callMixedArgs(Args:ArgExps, KWS:KwArgExps) =>
           evalArgs(Args, #noArgVals) ~> evalMixedKwArgs(KWS, F)
       ... </k>
  rule <k> argsVal(VS:ArgVals) ~> evalMixedKwArgs(KWS:KwArgExps, F:Val) =>
           evalKwArgs(KWS, #noKwArgVals) ~> callApplyMixedArgs(F, VS)
       ... </k>
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(closure(X:Id, Body:Exp), VS:ArgVals) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, idItemsLast(X), buildMixedDefaultArgs(idItemsLast(X), VS, KWS, #noArgVals)) </env>
    requires mixedCallArityOk(idItemsLast(X), VS, KWS, #noArgVals)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(closureArgs(IDS:IdItems, Body:Exp), VS:ArgVals) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, buildMixedDefaultArgs(IDS, VS, KWS, #noArgVals)) </env>
    requires mixedCallArityOk(IDS, VS, KWS, #noArgVals)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(closureDefaults(IDS:IdItems, Defaults:ArgVals, Body:Exp), VS:ArgVals) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, buildMixedDefaultArgs(IDS, VS, KWS, Defaults)) </env>
    requires mixedCallArityOk(IDS, VS, KWS, Defaults)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(closureVarArgs(IDS:IdItems, Var:Id, Body:Exp), VS:ArgVals) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, concatArgVals(buildVarArgsMixedPosArgs(IDS, VS, KWS), varArgTail(VS, idItemsLen(IDS)))) </env>
    requires varArgsMixedCallArityOk(IDS, VS, KWS)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(closureVarArgsDefaults(IDS:IdItems, Defaults:ArgVals, Var:Id, Body:Exp), VS:ArgVals) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, buildVarArgsMixedDefaultArgs(IDS, VS, KWS, Defaults)) </env>
    requires varArgsMixedDefaultsCallArityOk(IDS, VS, KWS, Defaults)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(closureKwArgs(IDS:IdItems, Kw:Id, Body:Exp), VS:ArgVals) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindKwArgs(Rho, IDS, Kw, buildMixedDefaultArgs(IDS, VS, KWS, #noArgVals), KWS) </env>
    requires kwargsMixedCallArityOk(IDS, VS, KWS)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(closurePosOnly(Pos:IdItems, Rest:IdItems, Body:Exp), VS:ArgVals) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindPosOnlyMixedArgs(Rho, Pos, Rest, VS, KWS) </env>
    requires posOnlyMixedCallArityOk(Pos, Rest, VS, KWS)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(closurePosKwOnly(Pos:IdItems, KwOnly:IdItems, Body:Exp), VS:ArgVals) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(bindArgs(Rho, Pos, buildMixedDefaultArgs(Pos, VS, KWS, #noArgVals)), KwOnly, buildKwDefaultArgs(KwOnly, KWS, #noArgVals)) </env>
    requires posKwOnlyMixedCallArityOk(Pos, KwOnly, VS, KWS)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(closurePosKwDefaults(Pos:IdItems, PosDefaults:ArgVals, KwOnly:IdItems, KwDefaults:ArgVals, Body:Exp), VS:ArgVals) =>
           Body ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(bindArgs(Rho, Pos, buildMixedDefaultArgs(Pos, VS, KWS, PosDefaults)), KwOnly, buildKwDefaultArgs(KwOnly, KWS, KwDefaults)) </env>
    requires posKwOnlyMixedDefaultsCallArityOk(Pos, KwOnly, VS, KWS, PosDefaults, KwDefaults)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(functionVal(X:Id, block(SS:Stmts)), VS:ArgVals) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, idItemsLast(X), buildMixedDefaultArgs(idItemsLast(X), VS, KWS, #noArgVals)) </env>
    requires mixedCallArityOk(idItemsLast(X), VS, KWS, #noArgVals)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(functionVal(X:Id, {}), VS:ArgVals) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, idItemsLast(X), buildMixedDefaultArgs(idItemsLast(X), VS, KWS, #noArgVals)) </env>
    requires mixedCallArityOk(idItemsLast(X), VS, KWS, #noArgVals)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(functionValArgs(IDS:IdItems, block(SS:Stmts)), VS:ArgVals) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, buildMixedDefaultArgs(IDS, VS, KWS, #noArgVals)) </env>
    requires mixedCallArityOk(IDS, VS, KWS, #noArgVals)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(functionValArgs(IDS:IdItems, {}), VS:ArgVals) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, buildMixedDefaultArgs(IDS, VS, KWS, #noArgVals)) </env>
    requires mixedCallArityOk(IDS, VS, KWS, #noArgVals)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(functionValDefaults(IDS:IdItems, Defaults:ArgVals, block(SS:Stmts)), VS:ArgVals) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, buildMixedDefaultArgs(IDS, VS, KWS, Defaults)) </env>
    requires mixedCallArityOk(IDS, VS, KWS, Defaults)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(functionValDefaults(IDS:IdItems, Defaults:ArgVals, {}), VS:ArgVals) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(Rho, IDS, buildMixedDefaultArgs(IDS, VS, KWS, Defaults)) </env>
    requires mixedCallArityOk(IDS, VS, KWS, Defaults)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(functionValVarArgs(IDS:IdItems, Var:Id, block(SS:Stmts)), VS:ArgVals) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, concatArgVals(buildVarArgsMixedPosArgs(IDS, VS, KWS), varArgTail(VS, idItemsLen(IDS)))) </env>
    requires varArgsMixedCallArityOk(IDS, VS, KWS)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(functionValVarArgs(IDS:IdItems, Var:Id, {}), VS:ArgVals) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, concatArgVals(buildVarArgsMixedPosArgs(IDS, VS, KWS), varArgTail(VS, idItemsLen(IDS)))) </env>
    requires varArgsMixedCallArityOk(IDS, VS, KWS)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(functionValVarArgsDefaults(IDS:IdItems, Defaults:ArgVals, Var:Id, block(SS:Stmts)), VS:ArgVals) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, buildVarArgsMixedDefaultArgs(IDS, VS, KWS, Defaults)) </env>
    requires varArgsMixedDefaultsCallArityOk(IDS, VS, KWS, Defaults)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(functionValVarArgsDefaults(IDS:IdItems, Defaults:ArgVals, Var:Id, {}), VS:ArgVals) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindVarArgs(Rho, IDS, Var, buildVarArgsMixedDefaultArgs(IDS, VS, KWS, Defaults)) </env>
    requires varArgsMixedDefaultsCallArityOk(IDS, VS, KWS, Defaults)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(functionValKwArgs(IDS:IdItems, Kw:Id, block(SS:Stmts)), VS:ArgVals) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindKwArgs(Rho, IDS, Kw, buildMixedDefaultArgs(IDS, VS, KWS, #noArgVals), KWS) </env>
    requires kwargsMixedCallArityOk(IDS, VS, KWS)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(functionValKwArgs(IDS:IdItems, Kw:Id, {}), VS:ArgVals) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindKwArgs(Rho, IDS, Kw, buildMixedDefaultArgs(IDS, VS, KWS, #noArgVals), KWS) </env>
    requires kwargsMixedCallArityOk(IDS, VS, KWS)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(functionValPosOnly(Pos:IdItems, Rest:IdItems, block(SS:Stmts)), VS:ArgVals) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindPosOnlyMixedArgs(Rho, Pos, Rest, VS, KWS) </env>
    requires posOnlyMixedCallArityOk(Pos, Rest, VS, KWS)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(functionValPosOnly(Pos:IdItems, Rest:IdItems, {}), VS:ArgVals) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindPosOnlyMixedArgs(Rho, Pos, Rest, VS, KWS) </env>
    requires posOnlyMixedCallArityOk(Pos, Rest, VS, KWS)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(functionValPosKwOnly(Pos:IdItems, KwOnly:IdItems, block(SS:Stmts)), VS:ArgVals) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindArgs(bindArgs(Rho, Pos, buildMixedDefaultArgs(Pos, VS, KWS, #noArgVals)), KwOnly, buildKwDefaultArgs(KwOnly, KWS, #noArgVals)) </env>
    requires posKwOnlyMixedCallArityOk(Pos, KwOnly, VS, KWS)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(functionValPosKwOnly(Pos:IdItems, KwOnly:IdItems, {}), VS:ArgVals) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(bindArgs(Rho, Pos, buildMixedDefaultArgs(Pos, VS, KWS, #noArgVals)), KwOnly, buildKwDefaultArgs(KwOnly, KWS, #noArgVals)) </env>
    requires posKwOnlyMixedCallArityOk(Pos, KwOnly, VS, KWS)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(functionValPosKwDefaults(Pos:IdItems, PosDefaults:ArgVals, KwOnly:IdItems, KwDefaults:ArgVals, block(SS:Stmts)), VS:ArgVals) =>
           SS ~> functionDone(Rho)
       ... </k>
       <env> Rho => bindArgs(bindArgs(Rho, Pos, buildMixedDefaultArgs(Pos, VS, KWS, PosDefaults)), KwOnly, buildKwDefaultArgs(KwOnly, KWS, KwDefaults)) </env>
    requires posKwOnlyMixedDefaultsCallArityOk(Pos, KwOnly, VS, KWS, PosDefaults, KwDefaults)
  rule <k> kwArgsVal(KWS:KwArgVals) ~> callApplyMixedArgs(functionValPosKwDefaults(Pos:IdItems, PosDefaults:ArgVals, KwOnly:IdItems, KwDefaults:ArgVals, {}), VS:ArgVals) =>
           None ~> restoreEnv(Rho)
       ... </k>
       <env> Rho => bindArgs(bindArgs(Rho, Pos, buildMixedDefaultArgs(Pos, VS, KWS, PosDefaults)), KwOnly, buildKwDefaultArgs(KwOnly, KWS, KwDefaults)) </env>
    requires posKwOnlyMixedDefaultsCallArityOk(Pos, KwOnly, VS, KWS, PosDefaults, KwDefaults)

  rule <k> listDisplayExp(Args:ArgExps) => evalArgs(Args, #noArgVals) ~> buildList ... </k>
  rule <k> argsVal(#noArgVals) ~> buildList => [] ... </k>
  rule <k> argsVal(VS:ArgVals) ~> buildList => listVal(argValsToValItems(VS)) ... </k>
    requires notBool emptyArgVals(VS)
  rule <k> listCompExp(Iter:Val, X:Id, Elem:Exp) =>
           listCompIter(X, Elem, iterableArgVals(Iter), #noArgVals, Rho)
       ... </k>
       <env> Rho </env>
  rule <k> listCompIter(_:Id, _:Exp, #noArgVals, #noArgVals, Rho:Map) =>
           [] ~> restoreEnv(Rho)
       ... </k>
  rule <k> listCompIter(_:Id, _:Exp, #noArgVals, Acc:ArgVals, Rho:Map) =>
           listVal(argValsToValItems(Acc)) ~> restoreEnv(Rho)
       ... </k>
    requires notBool emptyArgVals(Acc)
  rule <k> listCompIter(X:Id, Elem:Exp, argValsCons(V:Val, Rest:ArgVals), Acc:ArgVals, Rho:Map) =>
           Elem ~> listCompNext(X, Elem, Rest, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> V:Val ~> listCompNext(X:Id, Elem:Exp, Rest:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompIter(X, Elem, Rest, appendArgVal(Acc, V), Rho)
       ... </k>
  rule <k> listCompIfExp(Iter:Val, X:Id, Filter:Exp, Elem:Exp) =>
           listCompIfIter(X, Filter, Elem, iterableArgVals(Iter), #noArgVals, Rho)
       ... </k>
       <env> Rho </env>
  rule <k> listCompIfIter(_:Id, _:Exp, _:Exp, #noArgVals, #noArgVals, Rho:Map) =>
           [] ~> restoreEnv(Rho)
       ... </k>
  rule <k> listCompIfIter(_:Id, _:Exp, _:Exp, #noArgVals, Acc:ArgVals, Rho:Map) =>
           listVal(argValsToValItems(Acc)) ~> restoreEnv(Rho)
       ... </k>
    requires notBool emptyArgVals(Acc)
  rule <k> listCompIfIter(X:Id, Filter:Exp, Elem:Exp, argValsCons(V:Val, Rest:ArgVals), Acc:ArgVals, Rho:Map) =>
           Filter ~> listCompIfFilter(X, Filter, Elem, Rest, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> V:Val ~> listCompIfFilter(X:Id, Filter:Exp, Elem:Exp, Rest:ArgVals, Acc:ArgVals, Rho:Map) =>
           Elem ~> listCompIfNext(X, Filter, Elem, Rest, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> listCompIfFilter(X:Id, Filter:Exp, Elem:Exp, Rest:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompIfIter(X, Filter, Elem, Rest, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> listCompIfNext(X:Id, Filter:Exp, Elem:Exp, Rest:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompIfIter(X, Filter, Elem, Rest, appendArgVal(Acc, V), Rho)
       ... </k>
  rule <k> listCompIfsExp(Iter:Val, X:Id, Filters:CompFilters, Elem:Exp) =>
           listCompIfsIter(X, Filters, Elem, iterableArgVals(Iter), #noArgVals, Rho)
       ... </k>
       <env> Rho </env>
  rule <k> listCompIfsIter(_:Id, _:CompFilters, _:Exp, #noArgVals, #noArgVals, Rho:Map) =>
           [] ~> restoreEnv(Rho)
       ... </k>
  rule <k> listCompIfsIter(_:Id, _:CompFilters, _:Exp, #noArgVals, Acc:ArgVals, Rho:Map) =>
           listVal(argValsToValItems(Acc)) ~> restoreEnv(Rho)
       ... </k>
    requires notBool emptyArgVals(Acc)
  rule <k> listCompIfsIter(X:Id, Filters:CompFilters, Elem:Exp, argValsCons(V:Val, Rest:ArgVals), Acc:ArgVals, Rho:Map) =>
           listCompIfsFilter(X, Filters, Filters, Elem, Rest, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> listCompIfsFilter(X:Id, Filters:CompFilters, #filters(Filter:Exp, RestFilters:CompFilters), Elem:Exp, Rest:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> listCompIfsFilterNext(X, Filters, RestFilters, Elem, Rest, Acc, Rho)
       ... </k>
  rule <k> listCompIfsFilter(X:Id, Filters:CompFilters, #filter(Filter:Exp), Elem:Exp, Rest:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> listCompIfsFilterLast(X, Filters, Elem, Rest, Acc, Rho)
       ... </k>
  rule <k> V:Val ~> listCompIfsFilterNext(X:Id, Filters:CompFilters, RestFilters:CompFilters, Elem:Exp, Rest:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompIfsFilter(X, Filters, RestFilters, Elem, Rest, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> listCompIfsFilterNext(X:Id, Filters:CompFilters, _:CompFilters, Elem:Exp, Rest:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompIfsIter(X, Filters, Elem, Rest, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> listCompIfsFilterLast(X:Id, Filters:CompFilters, Elem:Exp, Rest:ArgVals, Acc:ArgVals, Rho:Map) =>
           Elem ~> listCompIfsNext(X, Filters, Elem, Rest, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> listCompIfsFilterLast(X:Id, Filters:CompFilters, Elem:Exp, Rest:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompIfsIter(X, Filters, Elem, Rest, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> listCompIfsNext(X:Id, Filters:CompFilters, Elem:Exp, Rest:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompIfsIter(X, Filters, Elem, Rest, appendArgVal(Acc, V), Rho)
       ... </k>
  rule <k> listCompForExp(Iter:Val, X:Id, Inner:Exp, Y:Id, Elem:Exp) =>
           listCompForIter(X, Inner, Y, Elem, iterableArgVals(Iter), #noArgVals, Rho)
       ... </k>
       <env> Rho </env>
  rule <k> listCompForIter(_:Id, _:Exp, _:Id, _:Exp, #noArgVals, #noArgVals, Rho:Map) =>
           [] ~> restoreEnv(Rho)
       ... </k>
  rule <k> listCompForIter(_:Id, _:Exp, _:Id, _:Exp, #noArgVals, Acc:ArgVals, Rho:Map) =>
           listVal(argValsToValItems(Acc)) ~> restoreEnv(Rho)
       ... </k>
    requires notBool emptyArgVals(Acc)
  rule <k> listCompForIter(X:Id, Inner:Exp, Y:Id, Elem:Exp, argValsCons(V:Val, RestOuter:ArgVals), Acc:ArgVals, Rho:Map) =>
           Inner ~> listCompForInner(X, Inner, Y, Elem, RestOuter, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> InnerIter:Val ~> listCompForInner(X:Id, Inner:Exp, Y:Id, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForInnerIter(X, Inner, Y, Elem, RestOuter, iterableArgVals(InnerIter), Acc, Rho)
       ... </k>
  rule <k> listCompForInnerIter(X:Id, Inner:Exp, Y:Id, Elem:Exp, RestOuter:ArgVals, #noArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForIter(X, Inner, Y, Elem, RestOuter, Acc, Rho)
       ... </k>
  rule <k> listCompForInnerIter(X:Id, Inner:Exp, Y:Id, Elem:Exp, RestOuter:ArgVals, argValsCons(V:Val, RestInner:ArgVals), Acc:ArgVals, Rho:Map) =>
           Elem ~> listCompForNext(X, Inner, Y, Elem, RestOuter, RestInner, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Y <- V ] </env>
  rule <k> V:Val ~> listCompForNext(X:Id, Inner:Exp, Y:Id, Elem:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForInnerIter(X, Inner, Y, Elem, RestOuter, RestInner, appendArgVal(Acc, V), Rho)
       ... </k>
  rule <k> listCompForIfsExp(Iter:Val, X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp) =>
           listCompForIfsIter(X, OuterFilters, Inner, Y, InnerFilters, Elem, iterableArgVals(Iter), #noArgVals, Rho)
       ... </k>
       <env> Rho </env>
  rule <k> listCompForIfsIter(_:Id, _:MaybeCompFilters, _:Exp, _:Id, _:MaybeCompFilters, _:Exp, #noArgVals, #noArgVals, Rho:Map) =>
           [] ~> restoreEnv(Rho)
       ... </k>
  rule <k> listCompForIfsIter(_:Id, _:MaybeCompFilters, _:Exp, _:Id, _:MaybeCompFilters, _:Exp, #noArgVals, Acc:ArgVals, Rho:Map) =>
           listVal(argValsToValItems(Acc)) ~> restoreEnv(Rho)
       ... </k>
    requires notBool emptyArgVals(Acc)
  rule <k> listCompForIfsIter(X:Id, #noFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, argValsCons(V:Val, RestOuter:ArgVals), Acc:ArgVals, Rho:Map) =>
           Inner ~> listCompForIfsInner(X, #noFilters, Inner, Y, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> listCompForIfsIter(X:Id, OuterFilters:CompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, argValsCons(V:Val, RestOuter:ArgVals), Acc:ArgVals, Rho:Map) =>
           listCompForIfsOuterFilter(X, OuterFilters, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> listCompForIfsOuterFilter(X:Id, OuterFilters:MaybeCompFilters, #filters(Filter:Exp, RestFilters:CompFilters), Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> listCompForIfsOuterFilterNext(X, OuterFilters, RestFilters, Inner, Y, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
  rule <k> listCompForIfsOuterFilter(X:Id, OuterFilters:MaybeCompFilters, #filter(Filter:Exp), Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> listCompForIfsOuterFilterLast(X, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
  rule <k> V:Val ~> listCompForIfsOuterFilterNext(X:Id, OuterFilters:MaybeCompFilters, RestFilters:CompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForIfsOuterFilter(X, OuterFilters, RestFilters, Inner, Y, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> listCompForIfsOuterFilterNext(X:Id, OuterFilters:MaybeCompFilters, _:CompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForIfsIter(X, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> listCompForIfsOuterFilterLast(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           Inner ~> listCompForIfsInner(X, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> listCompForIfsOuterFilterLast(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForIfsIter(X, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> InnerIter:Val ~> listCompForIfsInner(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForIfsInnerIter(X, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, iterableArgVals(InnerIter), Acc, Rho)
       ... </k>
  rule <k> listCompForIfsInnerIter(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, #noArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForIfsIter(X, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
  rule <k> listCompForIfsInnerIter(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, #noFilters, Elem:Exp, RestOuter:ArgVals, argValsCons(V:Val, RestInner:ArgVals), Acc:ArgVals, Rho:Map) =>
           Elem ~> listCompForIfsNext(X, OuterFilters, Inner, Y, #noFilters, Elem, RestOuter, RestInner, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Y <- V ] </env>
  rule <k> listCompForIfsInnerIter(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:CompFilters, Elem:Exp, RestOuter:ArgVals, argValsCons(V:Val, RestInner:ArgVals), Acc:ArgVals, Rho:Map) =>
           listCompForIfsInnerFilter(X, OuterFilters, Inner, Y, InnerFilters, InnerFilters, Elem, RestOuter, RestInner, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Y <- V ] </env>
  rule <k> listCompForIfsInnerFilter(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, #filters(Filter:Exp, RestFilters:CompFilters), Elem:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> listCompForIfsInnerFilterNext(X, OuterFilters, Inner, Y, InnerFilters, RestFilters, Elem, RestOuter, RestInner, Acc, Rho)
       ... </k>
  rule <k> listCompForIfsInnerFilter(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, #filter(Filter:Exp), Elem:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> listCompForIfsInnerFilterLast(X, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, RestInner, Acc, Rho)
       ... </k>
  rule <k> V:Val ~> listCompForIfsInnerFilterNext(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, RestFilters:CompFilters, Elem:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForIfsInnerFilter(X, OuterFilters, Inner, Y, InnerFilters, RestFilters, Elem, RestOuter, RestInner, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> listCompForIfsInnerFilterNext(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, _:CompFilters, Elem:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForIfsInnerIter(X, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, RestInner, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> listCompForIfsInnerFilterLast(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           Elem ~> listCompForIfsNext(X, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, RestInner, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> listCompForIfsInnerFilterLast(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForIfsInnerIter(X, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, RestInner, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> listCompForIfsNext(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForIfsInnerIter(X, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, RestInner, appendArgVal(Acc, V), Rho)
       ... </k>
  rule <k> listCompForForExp(Iter:Val, X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Elem:Exp) =>
           listCompForForIter(X, Middle, Y, Inner, Z, Elem, iterableArgVals(Iter), #noArgVals, Rho)
       ... </k>
       <env> Rho </env>
  rule <k> listCompForForIter(_:Id, _:Exp, _:Id, _:Exp, _:Id, _:Exp, #noArgVals, #noArgVals, Rho:Map) =>
           [] ~> restoreEnv(Rho)
       ... </k>
  rule <k> listCompForForIter(_:Id, _:Exp, _:Id, _:Exp, _:Id, _:Exp, #noArgVals, Acc:ArgVals, Rho:Map) =>
           listVal(argValsToValItems(Acc)) ~> restoreEnv(Rho)
       ... </k>
    requires notBool emptyArgVals(Acc)
  rule <k> listCompForForIter(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Elem:Exp, argValsCons(V:Val, RestOuter:ArgVals), Acc:ArgVals, Rho:Map) =>
           Middle ~> listCompForForMiddle(X, Middle, Y, Inner, Z, Elem, RestOuter, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> MiddleIter:Val ~> listCompForForMiddle(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForForMiddleIter(X, Middle, Y, Inner, Z, Elem, RestOuter, iterableArgVals(MiddleIter), Acc, Rho)
       ... </k>
  rule <k> listCompForForMiddleIter(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Elem:Exp, RestOuter:ArgVals, #noArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForForIter(X, Middle, Y, Inner, Z, Elem, RestOuter, Acc, Rho)
       ... </k>
  rule <k> listCompForForMiddleIter(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Elem:Exp, RestOuter:ArgVals, argValsCons(V:Val, RestMiddle:ArgVals), Acc:ArgVals, Rho:Map) =>
           Inner ~> listCompForForInner(X, Middle, Y, Inner, Z, Elem, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Y <- V ] </env>
  rule <k> InnerIter:Val ~> listCompForForInner(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForForInnerIter(X, Middle, Y, Inner, Z, Elem, RestOuter, RestMiddle, iterableArgVals(InnerIter), Acc, Rho)
       ... </k>
  rule <k> listCompForForInnerIter(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, #noArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForForMiddleIter(X, Middle, Y, Inner, Z, Elem, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
  rule <k> listCompForForInnerIter(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, argValsCons(V:Val, RestInner:ArgVals), Acc:ArgVals, Rho:Map) =>
           Elem ~> listCompForForNext(X, Middle, Y, Inner, Z, Elem, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Z <- V ] </env>
  rule <k> V:Val ~> listCompForForNext(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForForInnerIter(X, Middle, Y, Inner, Z, Elem, RestOuter, RestMiddle, RestInner, appendArgVal(Acc, V), Rho)
       ... </k>
  rule <k> listCompForForIfsExp(Iter:Val, X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp) =>
           listCompForForIfsIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, iterableArgVals(Iter), #noArgVals, Rho)
       ... </k>
       <env> Rho </env>
  rule <k> listCompForForIfsIter(_:Id, _:MaybeCompFilters, _:Exp, _:Id, _:MaybeCompFilters, _:Exp, _:Id, _:MaybeCompFilters, _:Exp, #noArgVals, #noArgVals, Rho:Map) =>
           [] ~> restoreEnv(Rho)
       ... </k>
  rule <k> listCompForForIfsIter(_:Id, _:MaybeCompFilters, _:Exp, _:Id, _:MaybeCompFilters, _:Exp, _:Id, _:MaybeCompFilters, _:Exp, #noArgVals, Acc:ArgVals, Rho:Map) =>
           listVal(argValsToValItems(Acc)) ~> restoreEnv(Rho)
       ... </k>
    requires notBool emptyArgVals(Acc)
  rule <k> listCompForForIfsIter(X:Id, #noFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, argValsCons(V:Val, RestOuter:ArgVals), Acc:ArgVals, Rho:Map) =>
           Middle ~> listCompForForIfsMiddle(X, #noFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> listCompForForIfsIter(X:Id, OuterFilters:CompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, argValsCons(V:Val, RestOuter:ArgVals), Acc:ArgVals, Rho:Map) =>
           listCompForForIfsOuterFilter(X, OuterFilters, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> listCompForForIfsOuterFilter(X:Id, OuterFilters:MaybeCompFilters, #filters(Filter:Exp, RestFilters:CompFilters), Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> listCompForForIfsOuterFilterNext(X, OuterFilters, RestFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
  rule <k> listCompForForIfsOuterFilter(X:Id, OuterFilters:MaybeCompFilters, #filter(Filter:Exp), Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> listCompForForIfsOuterFilterLast(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
  rule <k> V:Val ~> listCompForForIfsOuterFilterNext(X:Id, OuterFilters:MaybeCompFilters, RestFilters:CompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForForIfsOuterFilter(X, OuterFilters, RestFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> listCompForForIfsOuterFilterNext(X:Id, OuterFilters:MaybeCompFilters, _:CompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForForIfsIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> listCompForForIfsOuterFilterLast(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           Middle ~> listCompForForIfsMiddle(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> listCompForForIfsOuterFilterLast(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForForIfsIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> MiddleIter:Val ~> listCompForForIfsMiddle(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForForIfsMiddleIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, iterableArgVals(MiddleIter), Acc, Rho)
       ... </k>
  rule <k> listCompForForIfsMiddleIter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, #noArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForForIfsIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
  rule <k> listCompForForIfsMiddleIter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, #noFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, argValsCons(V:Val, RestMiddle:ArgVals), Acc:ArgVals, Rho:Map) =>
           Inner ~> listCompForForIfsInner(X, OuterFilters, Middle, Y, #noFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Y <- V ] </env>
  rule <k> listCompForForIfsMiddleIter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:CompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, argValsCons(V:Val, RestMiddle:ArgVals), Acc:ArgVals, Rho:Map) =>
           listCompForForIfsMiddleFilter(X, OuterFilters, Middle, Y, MiddleFilters, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Y <- V ] </env>
  rule <k> listCompForForIfsMiddleFilter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, #filters(Filter:Exp, RestFilters:CompFilters), Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> listCompForForIfsMiddleFilterNext(X, OuterFilters, Middle, Y, MiddleFilters, RestFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
  rule <k> listCompForForIfsMiddleFilter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, #filter(Filter:Exp), Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> listCompForForIfsMiddleFilterLast(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
  rule <k> V:Val ~> listCompForForIfsMiddleFilterNext(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, RestFilters:CompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForForIfsMiddleFilter(X, OuterFilters, Middle, Y, MiddleFilters, RestFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> listCompForForIfsMiddleFilterNext(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, _:CompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForForIfsMiddleIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> listCompForForIfsMiddleFilterLast(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:ArgVals, Rho:Map) =>
           Inner ~> listCompForForIfsInner(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> listCompForForIfsMiddleFilterLast(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForForIfsMiddleIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> InnerIter:Val ~> listCompForForIfsInner(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForForIfsInnerIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, iterableArgVals(InnerIter), Acc, Rho)
       ... </k>
  rule <k> listCompForForIfsInnerIter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, #noArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForForIfsMiddleIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
  rule <k> listCompForForIfsInnerIter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, #noFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, argValsCons(V:Val, RestInner:ArgVals), Acc:ArgVals, Rho:Map) =>
           Elem ~> listCompForForIfsNext(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, #noFilters, Elem, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Z <- V ] </env>
  rule <k> listCompForForIfsInnerIter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:CompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, argValsCons(V:Val, RestInner:ArgVals), Acc:ArgVals, Rho:Map) =>
           listCompForForIfsInnerFilter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, InnerFilters, Elem, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Z <- V ] </env>
  rule <k> listCompForForIfsInnerFilter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, #filters(Filter:Exp, RestFilters:CompFilters), Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> listCompForForIfsInnerFilterNext(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, RestFilters, Elem, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
  rule <k> listCompForForIfsInnerFilter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, #filter(Filter:Exp), Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> listCompForForIfsInnerFilterLast(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
  rule <k> V:Val ~> listCompForForIfsInnerFilterNext(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, RestFilters:CompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForForIfsInnerFilter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, RestFilters, Elem, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> listCompForForIfsInnerFilterNext(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, _:CompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForForIfsInnerIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> listCompForForIfsInnerFilterLast(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           Elem ~> listCompForForIfsNext(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> listCompForForIfsInnerFilterLast(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForForIfsInnerIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> listCompForForIfsNext(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           listCompForForIfsInnerIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, RestInner, appendArgVal(Acc, V), Rho)
       ... </k>
  rule <k> setCompExp(Iter:Val, X:Id, Elem:Exp) =>
           setCompIter(X, Elem, iterableArgVals(Iter), #noArgVals, Rho)
       ... </k>
       <env> Rho </env>
  rule <k> setCompIter(_:Id, _:Exp, #noArgVals, #noArgVals, Rho:Map) =>
           set() ~> restoreEnv(Rho)
       ... </k>
  rule <k> setCompIter(_:Id, _:Exp, #noArgVals, Acc:ArgVals, Rho:Map) =>
           setFromArgVals(Acc) ~> restoreEnv(Rho)
       ... </k>
    requires notBool emptyArgVals(Acc)
  rule <k> setCompIter(X:Id, Elem:Exp, argValsCons(V:Val, Rest:ArgVals), Acc:ArgVals, Rho:Map) =>
           Elem ~> setCompNext(X, Elem, Rest, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> V:Val ~> setCompNext(X:Id, Elem:Exp, Rest:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompIter(X, Elem, Rest, appendArgVal(Acc, V), Rho)
       ... </k>
  rule <k> setCompIfExp(Iter:Val, X:Id, Filter:Exp, Elem:Exp) =>
           setCompIfIter(X, Filter, Elem, iterableArgVals(Iter), #noArgVals, Rho)
       ... </k>
       <env> Rho </env>
  rule <k> setCompIfIter(_:Id, _:Exp, _:Exp, #noArgVals, #noArgVals, Rho:Map) =>
           set() ~> restoreEnv(Rho)
       ... </k>
  rule <k> setCompIfIter(_:Id, _:Exp, _:Exp, #noArgVals, Acc:ArgVals, Rho:Map) =>
           setFromArgVals(Acc) ~> restoreEnv(Rho)
       ... </k>
    requires notBool emptyArgVals(Acc)
  rule <k> setCompIfIter(X:Id, Filter:Exp, Elem:Exp, argValsCons(V:Val, Rest:ArgVals), Acc:ArgVals, Rho:Map) =>
           Filter ~> setCompIfFilter(X, Filter, Elem, Rest, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> V:Val ~> setCompIfFilter(X:Id, Filter:Exp, Elem:Exp, Rest:ArgVals, Acc:ArgVals, Rho:Map) =>
           Elem ~> setCompIfNext(X, Filter, Elem, Rest, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> setCompIfFilter(X:Id, Filter:Exp, Elem:Exp, Rest:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompIfIter(X, Filter, Elem, Rest, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> setCompIfNext(X:Id, Filter:Exp, Elem:Exp, Rest:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompIfIter(X, Filter, Elem, Rest, appendArgVal(Acc, V), Rho)
       ... </k>
  rule <k> setCompIfsExp(Iter:Val, X:Id, Filters:CompFilters, Elem:Exp) =>
           setCompIfsIter(X, Filters, Elem, iterableArgVals(Iter), #noArgVals, Rho)
       ... </k>
       <env> Rho </env>
  rule <k> setCompIfsIter(_:Id, _:CompFilters, _:Exp, #noArgVals, #noArgVals, Rho:Map) =>
           set() ~> restoreEnv(Rho)
       ... </k>
  rule <k> setCompIfsIter(_:Id, _:CompFilters, _:Exp, #noArgVals, Acc:ArgVals, Rho:Map) =>
           setFromArgVals(Acc) ~> restoreEnv(Rho)
       ... </k>
    requires notBool emptyArgVals(Acc)
  rule <k> setCompIfsIter(X:Id, Filters:CompFilters, Elem:Exp, argValsCons(V:Val, Rest:ArgVals), Acc:ArgVals, Rho:Map) =>
           setCompIfsFilter(X, Filters, Filters, Elem, Rest, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> setCompIfsFilter(X:Id, Filters:CompFilters, #filters(Filter:Exp, RestFilters:CompFilters), Elem:Exp, Rest:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> setCompIfsFilterNext(X, Filters, RestFilters, Elem, Rest, Acc, Rho)
       ... </k>
  rule <k> setCompIfsFilter(X:Id, Filters:CompFilters, #filter(Filter:Exp), Elem:Exp, Rest:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> setCompIfsFilterLast(X, Filters, Elem, Rest, Acc, Rho)
       ... </k>
  rule <k> V:Val ~> setCompIfsFilterNext(X:Id, Filters:CompFilters, RestFilters:CompFilters, Elem:Exp, Rest:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompIfsFilter(X, Filters, RestFilters, Elem, Rest, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> setCompIfsFilterNext(X:Id, Filters:CompFilters, _:CompFilters, Elem:Exp, Rest:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompIfsIter(X, Filters, Elem, Rest, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> setCompIfsFilterLast(X:Id, Filters:CompFilters, Elem:Exp, Rest:ArgVals, Acc:ArgVals, Rho:Map) =>
           Elem ~> setCompIfsNext(X, Filters, Elem, Rest, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> setCompIfsFilterLast(X:Id, Filters:CompFilters, Elem:Exp, Rest:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompIfsIter(X, Filters, Elem, Rest, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> setCompIfsNext(X:Id, Filters:CompFilters, Elem:Exp, Rest:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompIfsIter(X, Filters, Elem, Rest, appendArgVal(Acc, V), Rho)
       ... </k>
  rule <k> setCompForExp(Iter:Val, X:Id, Inner:Exp, Y:Id, Elem:Exp) =>
           setCompForIter(X, Inner, Y, Elem, iterableArgVals(Iter), #noArgVals, Rho)
       ... </k>
       <env> Rho </env>
  rule <k> setCompForIter(_:Id, _:Exp, _:Id, _:Exp, #noArgVals, #noArgVals, Rho:Map) =>
           set() ~> restoreEnv(Rho)
       ... </k>
  rule <k> setCompForIter(_:Id, _:Exp, _:Id, _:Exp, #noArgVals, Acc:ArgVals, Rho:Map) =>
           setFromArgVals(Acc) ~> restoreEnv(Rho)
       ... </k>
    requires notBool emptyArgVals(Acc)
  rule <k> setCompForIter(X:Id, Inner:Exp, Y:Id, Elem:Exp, argValsCons(V:Val, RestOuter:ArgVals), Acc:ArgVals, Rho:Map) =>
           Inner ~> setCompForInner(X, Inner, Y, Elem, RestOuter, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> InnerIter:Val ~> setCompForInner(X:Id, Inner:Exp, Y:Id, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForInnerIter(X, Inner, Y, Elem, RestOuter, iterableArgVals(InnerIter), Acc, Rho)
       ... </k>
  rule <k> setCompForInnerIter(X:Id, Inner:Exp, Y:Id, Elem:Exp, RestOuter:ArgVals, #noArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForIter(X, Inner, Y, Elem, RestOuter, Acc, Rho)
       ... </k>
  rule <k> setCompForInnerIter(X:Id, Inner:Exp, Y:Id, Elem:Exp, RestOuter:ArgVals, argValsCons(V:Val, RestInner:ArgVals), Acc:ArgVals, Rho:Map) =>
           Elem ~> setCompForNext(X, Inner, Y, Elem, RestOuter, RestInner, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Y <- V ] </env>
  rule <k> V:Val ~> setCompForNext(X:Id, Inner:Exp, Y:Id, Elem:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForInnerIter(X, Inner, Y, Elem, RestOuter, RestInner, appendArgVal(Acc, V), Rho)
       ... </k>
  rule <k> setCompForForExp(Iter:Val, X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Elem:Exp) =>
           setCompForForIter(X, Middle, Y, Inner, Z, Elem, iterableArgVals(Iter), #noArgVals, Rho)
       ... </k>
       <env> Rho </env>
  rule <k> setCompForForIter(_:Id, _:Exp, _:Id, _:Exp, _:Id, _:Exp, #noArgVals, #noArgVals, Rho:Map) =>
           set() ~> restoreEnv(Rho)
       ... </k>
  rule <k> setCompForForIter(_:Id, _:Exp, _:Id, _:Exp, _:Id, _:Exp, #noArgVals, Acc:ArgVals, Rho:Map) =>
           setFromArgVals(Acc) ~> restoreEnv(Rho)
       ... </k>
    requires notBool emptyArgVals(Acc)
  rule <k> setCompForForIter(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Elem:Exp, argValsCons(V:Val, RestOuter:ArgVals), Acc:ArgVals, Rho:Map) =>
           Middle ~> setCompForForMiddle(X, Middle, Y, Inner, Z, Elem, RestOuter, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> MiddleIter:Val ~> setCompForForMiddle(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForForMiddleIter(X, Middle, Y, Inner, Z, Elem, RestOuter, iterableArgVals(MiddleIter), Acc, Rho)
       ... </k>
  rule <k> setCompForForMiddleIter(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Elem:Exp, RestOuter:ArgVals, #noArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForForIter(X, Middle, Y, Inner, Z, Elem, RestOuter, Acc, Rho)
       ... </k>
  rule <k> setCompForForMiddleIter(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Elem:Exp, RestOuter:ArgVals, argValsCons(V:Val, RestMiddle:ArgVals), Acc:ArgVals, Rho:Map) =>
           Inner ~> setCompForForInner(X, Middle, Y, Inner, Z, Elem, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Y <- V ] </env>
  rule <k> InnerIter:Val ~> setCompForForInner(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForForInnerIter(X, Middle, Y, Inner, Z, Elem, RestOuter, RestMiddle, iterableArgVals(InnerIter), Acc, Rho)
       ... </k>
  rule <k> setCompForForInnerIter(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, #noArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForForMiddleIter(X, Middle, Y, Inner, Z, Elem, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
  rule <k> setCompForForInnerIter(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, argValsCons(V:Val, RestInner:ArgVals), Acc:ArgVals, Rho:Map) =>
           Elem ~> setCompForForNext(X, Middle, Y, Inner, Z, Elem, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Z <- V ] </env>
  rule <k> V:Val ~> setCompForForNext(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForForInnerIter(X, Middle, Y, Inner, Z, Elem, RestOuter, RestMiddle, RestInner, appendArgVal(Acc, V), Rho)
       ... </k>
  rule <k> setCompForForIfsExp(Iter:Val, X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp) =>
           setCompForForIfsIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, iterableArgVals(Iter), #noArgVals, Rho)
       ... </k>
       <env> Rho </env>
  rule <k> setCompForForIfsIter(_:Id, _:MaybeCompFilters, _:Exp, _:Id, _:MaybeCompFilters, _:Exp, _:Id, _:MaybeCompFilters, _:Exp, #noArgVals, #noArgVals, Rho:Map) =>
           set() ~> restoreEnv(Rho)
       ... </k>
  rule <k> setCompForForIfsIter(_:Id, _:MaybeCompFilters, _:Exp, _:Id, _:MaybeCompFilters, _:Exp, _:Id, _:MaybeCompFilters, _:Exp, #noArgVals, Acc:ArgVals, Rho:Map) =>
           setFromArgVals(Acc) ~> restoreEnv(Rho)
       ... </k>
    requires notBool emptyArgVals(Acc)
  rule <k> setCompForForIfsIter(X:Id, #noFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, argValsCons(V:Val, RestOuter:ArgVals), Acc:ArgVals, Rho:Map) =>
           Middle ~> setCompForForIfsMiddle(X, #noFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> setCompForForIfsIter(X:Id, OuterFilters:CompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, argValsCons(V:Val, RestOuter:ArgVals), Acc:ArgVals, Rho:Map) =>
           setCompForForIfsOuterFilter(X, OuterFilters, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> setCompForForIfsOuterFilter(X:Id, OuterFilters:MaybeCompFilters, #filters(Filter:Exp, RestFilters:CompFilters), Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> setCompForForIfsOuterFilterNext(X, OuterFilters, RestFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
  rule <k> setCompForForIfsOuterFilter(X:Id, OuterFilters:MaybeCompFilters, #filter(Filter:Exp), Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> setCompForForIfsOuterFilterLast(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
  rule <k> V:Val ~> setCompForForIfsOuterFilterNext(X:Id, OuterFilters:MaybeCompFilters, RestFilters:CompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForForIfsOuterFilter(X, OuterFilters, RestFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> setCompForForIfsOuterFilterNext(X:Id, OuterFilters:MaybeCompFilters, _:CompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForForIfsIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> setCompForForIfsOuterFilterLast(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           Middle ~> setCompForForIfsMiddle(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> setCompForForIfsOuterFilterLast(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForForIfsIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> MiddleIter:Val ~> setCompForForIfsMiddle(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForForIfsMiddleIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, iterableArgVals(MiddleIter), Acc, Rho)
       ... </k>
  rule <k> setCompForForIfsMiddleIter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, #noArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForForIfsIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
  rule <k> setCompForForIfsMiddleIter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, #noFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, argValsCons(V:Val, RestMiddle:ArgVals), Acc:ArgVals, Rho:Map) =>
           Inner ~> setCompForForIfsInner(X, OuterFilters, Middle, Y, #noFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Y <- V ] </env>
  rule <k> setCompForForIfsMiddleIter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:CompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, argValsCons(V:Val, RestMiddle:ArgVals), Acc:ArgVals, Rho:Map) =>
           setCompForForIfsMiddleFilter(X, OuterFilters, Middle, Y, MiddleFilters, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Y <- V ] </env>
  rule <k> setCompForForIfsMiddleFilter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, #filters(Filter:Exp, RestFilters:CompFilters), Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> setCompForForIfsMiddleFilterNext(X, OuterFilters, Middle, Y, MiddleFilters, RestFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
  rule <k> setCompForForIfsMiddleFilter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, #filter(Filter:Exp), Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> setCompForForIfsMiddleFilterLast(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
  rule <k> V:Val ~> setCompForForIfsMiddleFilterNext(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, RestFilters:CompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForForIfsMiddleFilter(X, OuterFilters, Middle, Y, MiddleFilters, RestFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> setCompForForIfsMiddleFilterNext(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, _:CompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForForIfsMiddleIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> setCompForForIfsMiddleFilterLast(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:ArgVals, Rho:Map) =>
           Inner ~> setCompForForIfsInner(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> setCompForForIfsMiddleFilterLast(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForForIfsMiddleIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> InnerIter:Val ~> setCompForForIfsInner(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForForIfsInnerIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, iterableArgVals(InnerIter), Acc, Rho)
       ... </k>
  rule <k> setCompForForIfsInnerIter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, #noArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForForIfsMiddleIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
  rule <k> setCompForForIfsInnerIter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, #noFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, argValsCons(V:Val, RestInner:ArgVals), Acc:ArgVals, Rho:Map) =>
           Elem ~> setCompForForIfsNext(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, #noFilters, Elem, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Z <- V ] </env>
  rule <k> setCompForForIfsInnerIter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:CompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, argValsCons(V:Val, RestInner:ArgVals), Acc:ArgVals, Rho:Map) =>
           setCompForForIfsInnerFilter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, InnerFilters, Elem, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Z <- V ] </env>
  rule <k> setCompForForIfsInnerFilter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, #filters(Filter:Exp, RestFilters:CompFilters), Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> setCompForForIfsInnerFilterNext(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, RestFilters, Elem, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
  rule <k> setCompForForIfsInnerFilter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, #filter(Filter:Exp), Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> setCompForForIfsInnerFilterLast(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
  rule <k> V:Val ~> setCompForForIfsInnerFilterNext(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, RestFilters:CompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForForIfsInnerFilter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, RestFilters, Elem, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> setCompForForIfsInnerFilterNext(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, _:CompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForForIfsInnerIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> setCompForForIfsInnerFilterLast(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           Elem ~> setCompForForIfsNext(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> setCompForForIfsInnerFilterLast(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForForIfsInnerIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> setCompForForIfsNext(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForForIfsInnerIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Elem, RestOuter, RestMiddle, RestInner, appendArgVal(Acc, V), Rho)
       ... </k>
  rule <k> setCompForIfsExp(Iter:Val, X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp) =>
           setCompForIfsIter(X, OuterFilters, Inner, Y, InnerFilters, Elem, iterableArgVals(Iter), #noArgVals, Rho)
       ... </k>
       <env> Rho </env>
  rule <k> setCompForIfsIter(_:Id, _:MaybeCompFilters, _:Exp, _:Id, _:MaybeCompFilters, _:Exp, #noArgVals, #noArgVals, Rho:Map) =>
           set() ~> restoreEnv(Rho)
       ... </k>
  rule <k> setCompForIfsIter(_:Id, _:MaybeCompFilters, _:Exp, _:Id, _:MaybeCompFilters, _:Exp, #noArgVals, Acc:ArgVals, Rho:Map) =>
           setFromArgVals(Acc) ~> restoreEnv(Rho)
       ... </k>
    requires notBool emptyArgVals(Acc)
  rule <k> setCompForIfsIter(X:Id, #noFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, argValsCons(V:Val, RestOuter:ArgVals), Acc:ArgVals, Rho:Map) =>
           Inner ~> setCompForIfsInner(X, #noFilters, Inner, Y, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> setCompForIfsIter(X:Id, OuterFilters:CompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, argValsCons(V:Val, RestOuter:ArgVals), Acc:ArgVals, Rho:Map) =>
           setCompForIfsOuterFilter(X, OuterFilters, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> setCompForIfsOuterFilter(X:Id, OuterFilters:MaybeCompFilters, #filters(Filter:Exp, RestFilters:CompFilters), Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> setCompForIfsOuterFilterNext(X, OuterFilters, RestFilters, Inner, Y, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
  rule <k> setCompForIfsOuterFilter(X:Id, OuterFilters:MaybeCompFilters, #filter(Filter:Exp), Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> setCompForIfsOuterFilterLast(X, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
  rule <k> V:Val ~> setCompForIfsOuterFilterNext(X:Id, OuterFilters:MaybeCompFilters, RestFilters:CompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForIfsOuterFilter(X, OuterFilters, RestFilters, Inner, Y, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> setCompForIfsOuterFilterNext(X:Id, OuterFilters:MaybeCompFilters, _:CompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForIfsIter(X, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> setCompForIfsOuterFilterLast(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           Inner ~> setCompForIfsInner(X, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> setCompForIfsOuterFilterLast(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForIfsIter(X, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> InnerIter:Val ~> setCompForIfsInner(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForIfsInnerIter(X, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, iterableArgVals(InnerIter), Acc, Rho)
       ... </k>
  rule <k> setCompForIfsInnerIter(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, #noArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForIfsIter(X, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, Acc, Rho)
       ... </k>
  rule <k> setCompForIfsInnerIter(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, #noFilters, Elem:Exp, RestOuter:ArgVals, argValsCons(V:Val, RestInner:ArgVals), Acc:ArgVals, Rho:Map) =>
           Elem ~> setCompForIfsNext(X, OuterFilters, Inner, Y, #noFilters, Elem, RestOuter, RestInner, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Y <- V ] </env>
  rule <k> setCompForIfsInnerIter(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:CompFilters, Elem:Exp, RestOuter:ArgVals, argValsCons(V:Val, RestInner:ArgVals), Acc:ArgVals, Rho:Map) =>
           setCompForIfsInnerFilter(X, OuterFilters, Inner, Y, InnerFilters, InnerFilters, Elem, RestOuter, RestInner, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Y <- V ] </env>
  rule <k> setCompForIfsInnerFilter(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, #filters(Filter:Exp, RestFilters:CompFilters), Elem:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> setCompForIfsInnerFilterNext(X, OuterFilters, Inner, Y, InnerFilters, RestFilters, Elem, RestOuter, RestInner, Acc, Rho)
       ... </k>
  rule <k> setCompForIfsInnerFilter(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, #filter(Filter:Exp), Elem:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           Filter ~> setCompForIfsInnerFilterLast(X, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, RestInner, Acc, Rho)
       ... </k>
  rule <k> V:Val ~> setCompForIfsInnerFilterNext(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, RestFilters:CompFilters, Elem:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForIfsInnerFilter(X, OuterFilters, Inner, Y, InnerFilters, RestFilters, Elem, RestOuter, RestInner, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> setCompForIfsInnerFilterNext(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, _:CompFilters, Elem:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForIfsInnerIter(X, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, RestInner, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> setCompForIfsInnerFilterLast(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           Elem ~> setCompForIfsNext(X, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, RestInner, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> setCompForIfsInnerFilterLast(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForIfsInnerIter(X, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, RestInner, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> setCompForIfsNext(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Elem:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:ArgVals, Rho:Map) =>
           setCompForIfsInnerIter(X, OuterFilters, Inner, Y, InnerFilters, Elem, RestOuter, RestInner, appendArgVal(Acc, V), Rho)
       ... </k>

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
  rule <k> evalDict(dictStarExpItem(E:Exp), DVS:DictVals) =>
           E ~> evalDictStarNext(#noDictItems, DVS)
       ... </k>
  rule <k> evalDict(dictStarExpsCons(E:Exp, Rest:DictExps), DVS:DictVals) =>
           E ~> evalDictStarNext(Rest, DVS)
       ... </k>
  rule <k> K:Val ~> evalDictValue(V:Exp, Rest:DictExps, DVS:DictVals) =>
           V ~> evalDictNext(Rest, DVS, K)
       ... </k>
  rule <k> V:Val ~> evalDictNext(Rest:DictExps, DVS:DictVals, K:Val) =>
           evalDict(Rest, appendDictVal(DVS, K, V))
       ... </k>
  rule <k> V:Val ~> evalDictStarNext(Rest:DictExps, DVS:DictVals) =>
           evalDict(Rest, appendDictUnpack(DVS, V))
       ... </k>
  rule <k> dictArgsVal(#noDictVals) ~> buildDict => ({}):Val ... </k>
  rule <k> dictArgsVal(DVS:DictVals) ~> buildDict => dictVal(dictValsToDictItems(DVS)) ... </k>
    requires notBool emptyDictVals(DVS)
  rule <k> dictCompExp(Iter:Val, X:Id, Key:Exp, Value:Exp) =>
           dictCompIter(X, Key, Value, iterableArgVals(Iter), #noDictVals, Rho)
       ... </k>
       <env> Rho </env>
  rule <k> dictCompIter(_:Id, _:Exp, _:Exp, #noArgVals, #noDictVals, Rho:Map) =>
           ({}):Val ~> restoreEnv(Rho)
       ... </k>
  rule <k> dictCompIter(_:Id, _:Exp, _:Exp, #noArgVals, Acc:DictVals, Rho:Map) =>
           dictVal(dictValsToDictItems(Acc)) ~> restoreEnv(Rho)
       ... </k>
    requires notBool emptyDictVals(Acc)
  rule <k> dictCompIter(X:Id, Key:Exp, Value:Exp, argValsCons(V:Val, Rest:ArgVals), Acc:DictVals, Rho:Map) =>
           Key ~> dictCompKey(X, Key, Value, Rest, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> K:Val ~> dictCompKey(X:Id, Key:Exp, Value:Exp, Rest:ArgVals, Acc:DictVals, Rho:Map) =>
           Value ~> dictCompValue(X, Key, Value, Rest, Acc, Rho, K)
       ... </k>
  rule <k> V:Val ~> dictCompValue(X:Id, Key:Exp, Value:Exp, Rest:ArgVals, Acc:DictVals, Rho:Map, K:Val) =>
           dictCompIter(X, Key, Value, Rest, appendDictVal(Acc, K, V), Rho)
       ... </k>
  rule <k> dictCompIfExp(Iter:Val, X:Id, Filter:Exp, Key:Exp, Value:Exp) =>
           dictCompIfIter(X, Filter, Key, Value, iterableArgVals(Iter), #noDictVals, Rho)
       ... </k>
       <env> Rho </env>
  rule <k> dictCompIfIter(_:Id, _:Exp, _:Exp, _:Exp, #noArgVals, #noDictVals, Rho:Map) =>
           ({}):Val ~> restoreEnv(Rho)
       ... </k>
  rule <k> dictCompIfIter(_:Id, _:Exp, _:Exp, _:Exp, #noArgVals, Acc:DictVals, Rho:Map) =>
           dictVal(dictValsToDictItems(Acc)) ~> restoreEnv(Rho)
       ... </k>
    requires notBool emptyDictVals(Acc)
  rule <k> dictCompIfIter(X:Id, Filter:Exp, Key:Exp, Value:Exp, argValsCons(V:Val, Rest:ArgVals), Acc:DictVals, Rho:Map) =>
           Filter ~> dictCompIfFilter(X, Filter, Key, Value, Rest, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> V:Val ~> dictCompIfFilter(X:Id, Filter:Exp, Key:Exp, Value:Exp, Rest:ArgVals, Acc:DictVals, Rho:Map) =>
           Key ~> dictCompIfKey(X, Filter, Key, Value, Rest, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> dictCompIfFilter(X:Id, Filter:Exp, Key:Exp, Value:Exp, Rest:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompIfIter(X, Filter, Key, Value, Rest, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> K:Val ~> dictCompIfKey(X:Id, Filter:Exp, Key:Exp, Value:Exp, Rest:ArgVals, Acc:DictVals, Rho:Map) =>
           Value ~> dictCompIfValue(X, Filter, Key, Value, Rest, Acc, Rho, K)
       ... </k>
  rule <k> V:Val ~> dictCompIfValue(X:Id, Filter:Exp, Key:Exp, Value:Exp, Rest:ArgVals, Acc:DictVals, Rho:Map, K:Val) =>
           dictCompIfIter(X, Filter, Key, Value, Rest, appendDictVal(Acc, K, V), Rho)
       ... </k>
  rule <k> dictCompIfsExp(Iter:Val, X:Id, Filters:CompFilters, Key:Exp, Value:Exp) =>
           dictCompIfsIter(X, Filters, Key, Value, iterableArgVals(Iter), #noDictVals, Rho)
       ... </k>
       <env> Rho </env>
  rule <k> dictCompIfsIter(_:Id, _:CompFilters, _:Exp, _:Exp, #noArgVals, #noDictVals, Rho:Map) =>
           ({}):Val ~> restoreEnv(Rho)
       ... </k>
  rule <k> dictCompIfsIter(_:Id, _:CompFilters, _:Exp, _:Exp, #noArgVals, Acc:DictVals, Rho:Map) =>
           dictVal(dictValsToDictItems(Acc)) ~> restoreEnv(Rho)
       ... </k>
    requires notBool emptyDictVals(Acc)
  rule <k> dictCompIfsIter(X:Id, Filters:CompFilters, Key:Exp, Value:Exp, argValsCons(V:Val, Rest:ArgVals), Acc:DictVals, Rho:Map) =>
           dictCompIfsFilter(X, Filters, Filters, Key, Value, Rest, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> dictCompIfsFilter(X:Id, Filters:CompFilters, #filters(Filter:Exp, RestFilters:CompFilters), Key:Exp, Value:Exp, Rest:ArgVals, Acc:DictVals, Rho:Map) =>
           Filter ~> dictCompIfsFilterNext(X, Filters, RestFilters, Key, Value, Rest, Acc, Rho)
       ... </k>
  rule <k> dictCompIfsFilter(X:Id, Filters:CompFilters, #filter(Filter:Exp), Key:Exp, Value:Exp, Rest:ArgVals, Acc:DictVals, Rho:Map) =>
           Filter ~> dictCompIfsFilterLast(X, Filters, Key, Value, Rest, Acc, Rho)
       ... </k>
  rule <k> V:Val ~> dictCompIfsFilterNext(X:Id, Filters:CompFilters, RestFilters:CompFilters, Key:Exp, Value:Exp, Rest:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompIfsFilter(X, Filters, RestFilters, Key, Value, Rest, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> dictCompIfsFilterNext(X:Id, Filters:CompFilters, _:CompFilters, Key:Exp, Value:Exp, Rest:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompIfsIter(X, Filters, Key, Value, Rest, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> dictCompIfsFilterLast(X:Id, Filters:CompFilters, Key:Exp, Value:Exp, Rest:ArgVals, Acc:DictVals, Rho:Map) =>
           Key ~> dictCompIfsKey(X, Filters, Key, Value, Rest, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> dictCompIfsFilterLast(X:Id, Filters:CompFilters, Key:Exp, Value:Exp, Rest:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompIfsIter(X, Filters, Key, Value, Rest, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> K:Val ~> dictCompIfsKey(X:Id, Filters:CompFilters, Key:Exp, Value:Exp, Rest:ArgVals, Acc:DictVals, Rho:Map) =>
           Value ~> dictCompIfsValue(X, Filters, Key, Value, Rest, Acc, Rho, K)
       ... </k>
  rule <k> V:Val ~> dictCompIfsValue(X:Id, Filters:CompFilters, Key:Exp, Value:Exp, Rest:ArgVals, Acc:DictVals, Rho:Map, K:Val) =>
           dictCompIfsIter(X, Filters, Key, Value, Rest, appendDictVal(Acc, K, V), Rho)
       ... </k>
  rule <k> dictCompForExp(Iter:Val, X:Id, Inner:Exp, Y:Id, Key:Exp, Value:Exp) =>
           dictCompForIter(X, Inner, Y, Key, Value, iterableArgVals(Iter), #noDictVals, Rho)
       ... </k>
       <env> Rho </env>
  rule <k> dictCompForIter(_:Id, _:Exp, _:Id, _:Exp, _:Exp, #noArgVals, #noDictVals, Rho:Map) =>
           ({}):Val ~> restoreEnv(Rho)
       ... </k>
  rule <k> dictCompForIter(_:Id, _:Exp, _:Id, _:Exp, _:Exp, #noArgVals, Acc:DictVals, Rho:Map) =>
           dictVal(dictValsToDictItems(Acc)) ~> restoreEnv(Rho)
       ... </k>
    requires notBool emptyDictVals(Acc)
  rule <k> dictCompForIter(X:Id, Inner:Exp, Y:Id, Key:Exp, Value:Exp, argValsCons(V:Val, RestOuter:ArgVals), Acc:DictVals, Rho:Map) =>
           Inner ~> dictCompForInner(X, Inner, Y, Key, Value, RestOuter, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> InnerIter:Val ~> dictCompForInner(X:Id, Inner:Exp, Y:Id, Key:Exp, Value:Exp, RestOuter:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForInnerIter(X, Inner, Y, Key, Value, RestOuter, iterableArgVals(InnerIter), Acc, Rho)
       ... </k>
  rule <k> dictCompForInnerIter(X:Id, Inner:Exp, Y:Id, Key:Exp, Value:Exp, RestOuter:ArgVals, #noArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForIter(X, Inner, Y, Key, Value, RestOuter, Acc, Rho)
       ... </k>
  rule <k> dictCompForInnerIter(X:Id, Inner:Exp, Y:Id, Key:Exp, Value:Exp, RestOuter:ArgVals, argValsCons(V:Val, RestInner:ArgVals), Acc:DictVals, Rho:Map) =>
           Key ~> dictCompForKey(X, Inner, Y, Key, Value, RestOuter, RestInner, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Y <- V ] </env>
  rule <k> K:Val ~> dictCompForKey(X:Id, Inner:Exp, Y:Id, Key:Exp, Value:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:DictVals, Rho:Map) =>
           Value ~> dictCompForValue(X, Inner, Y, Key, Value, RestOuter, RestInner, Acc, Rho, K)
       ... </k>
  rule <k> V:Val ~> dictCompForValue(X:Id, Inner:Exp, Y:Id, Key:Exp, Value:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:DictVals, Rho:Map, K:Val) =>
           dictCompForInnerIter(X, Inner, Y, Key, Value, RestOuter, RestInner, appendDictVal(Acc, K, V), Rho)
       ... </k>
  rule <k> dictCompForForExp(Iter:Val, X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Key:Exp, Value:Exp) =>
           dictCompForForIter(X, Middle, Y, Inner, Z, Key, Value, iterableArgVals(Iter), #noDictVals, Rho)
       ... </k>
       <env> Rho </env>
  rule <k> dictCompForForIter(_:Id, _:Exp, _:Id, _:Exp, _:Id, _:Exp, _:Exp, #noArgVals, #noDictVals, Rho:Map) =>
           ({}):Val ~> restoreEnv(Rho)
       ... </k>
  rule <k> dictCompForForIter(_:Id, _:Exp, _:Id, _:Exp, _:Id, _:Exp, _:Exp, #noArgVals, Acc:DictVals, Rho:Map) =>
           dictVal(dictValsToDictItems(Acc)) ~> restoreEnv(Rho)
       ... </k>
    requires notBool emptyDictVals(Acc)
  rule <k> dictCompForForIter(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Key:Exp, Value:Exp, argValsCons(V:Val, RestOuter:ArgVals), Acc:DictVals, Rho:Map) =>
           Middle ~> dictCompForForMiddle(X, Middle, Y, Inner, Z, Key, Value, RestOuter, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> MiddleIter:Val ~> dictCompForForMiddle(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Key:Exp, Value:Exp, RestOuter:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForForMiddleIter(X, Middle, Y, Inner, Z, Key, Value, RestOuter, iterableArgVals(MiddleIter), Acc, Rho)
       ... </k>
  rule <k> dictCompForForMiddleIter(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Key:Exp, Value:Exp, RestOuter:ArgVals, #noArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForForIter(X, Middle, Y, Inner, Z, Key, Value, RestOuter, Acc, Rho)
       ... </k>
  rule <k> dictCompForForMiddleIter(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Key:Exp, Value:Exp, RestOuter:ArgVals, argValsCons(V:Val, RestMiddle:ArgVals), Acc:DictVals, Rho:Map) =>
           Inner ~> dictCompForForInner(X, Middle, Y, Inner, Z, Key, Value, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Y <- V ] </env>
  rule <k> InnerIter:Val ~> dictCompForForInner(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Key:Exp, Value:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForForInnerIter(X, Middle, Y, Inner, Z, Key, Value, RestOuter, RestMiddle, iterableArgVals(InnerIter), Acc, Rho)
       ... </k>
  rule <k> dictCompForForInnerIter(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Key:Exp, Value:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, #noArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForForMiddleIter(X, Middle, Y, Inner, Z, Key, Value, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
  rule <k> dictCompForForInnerIter(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Key:Exp, Value:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, argValsCons(V:Val, RestInner:ArgVals), Acc:DictVals, Rho:Map) =>
           Key ~> dictCompForForKey(X, Middle, Y, Inner, Z, Key, Value, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Z <- V ] </env>
  rule <k> K:Val ~> dictCompForForKey(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Key:Exp, Value:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:DictVals, Rho:Map) =>
           Value ~> dictCompForForValue(X, Middle, Y, Inner, Z, Key, Value, RestOuter, RestMiddle, RestInner, Acc, Rho, K)
       ... </k>
  rule <k> V:Val ~> dictCompForForValue(X:Id, Middle:Exp, Y:Id, Inner:Exp, Z:Id, Key:Exp, Value:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:DictVals, Rho:Map, K:Val) =>
           dictCompForForInnerIter(X, Middle, Y, Inner, Z, Key, Value, RestOuter, RestMiddle, RestInner, appendDictVal(Acc, K, V), Rho)
       ... </k>
  rule <k> dictCompForForIfsExp(Iter:Val, X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp) =>
           dictCompForForIfsIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Key, Value, iterableArgVals(Iter), #noDictVals, Rho)
       ... </k>
       <env> Rho </env>
  rule <k> dictCompForForIfsIter(_:Id, _:MaybeCompFilters, _:Exp, _:Id, _:MaybeCompFilters, _:Exp, _:Id, _:MaybeCompFilters, _:Exp, _:Exp, #noArgVals, #noDictVals, Rho:Map) =>
           ({}):Val ~> restoreEnv(Rho)
       ... </k>
  rule <k> dictCompForForIfsIter(_:Id, _:MaybeCompFilters, _:Exp, _:Id, _:MaybeCompFilters, _:Exp, _:Id, _:MaybeCompFilters, _:Exp, _:Exp, #noArgVals, Acc:DictVals, Rho:Map) =>
           dictVal(dictValsToDictItems(Acc)) ~> restoreEnv(Rho)
       ... </k>
    requires notBool emptyDictVals(Acc)
  rule <k> dictCompForForIfsIter(X:Id, #noFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, argValsCons(V:Val, RestOuter:ArgVals), Acc:DictVals, Rho:Map) =>
           Middle ~> dictCompForForIfsMiddle(X, #noFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> dictCompForForIfsIter(X:Id, OuterFilters:CompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, argValsCons(V:Val, RestOuter:ArgVals), Acc:DictVals, Rho:Map) =>
           dictCompForForIfsOuterFilter(X, OuterFilters, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> dictCompForForIfsOuterFilter(X:Id, OuterFilters:MaybeCompFilters, #filters(Filter:Exp, RestFilters:CompFilters), Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, Acc:DictVals, Rho:Map) =>
           Filter ~> dictCompForForIfsOuterFilterNext(X, OuterFilters, RestFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, Acc, Rho)
       ... </k>
  rule <k> dictCompForForIfsOuterFilter(X:Id, OuterFilters:MaybeCompFilters, #filter(Filter:Exp), Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, Acc:DictVals, Rho:Map) =>
           Filter ~> dictCompForForIfsOuterFilterLast(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, Acc, Rho)
       ... </k>
  rule <k> V:Val ~> dictCompForForIfsOuterFilterNext(X:Id, OuterFilters:MaybeCompFilters, RestFilters:CompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForForIfsOuterFilter(X, OuterFilters, RestFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> dictCompForForIfsOuterFilterNext(X:Id, OuterFilters:MaybeCompFilters, _:CompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForForIfsIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> dictCompForForIfsOuterFilterLast(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, Acc:DictVals, Rho:Map) =>
           Middle ~> dictCompForForIfsMiddle(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> dictCompForForIfsOuterFilterLast(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForForIfsIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> MiddleIter:Val ~> dictCompForForIfsMiddle(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForForIfsMiddleIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, iterableArgVals(MiddleIter), Acc, Rho)
       ... </k>
  rule <k> dictCompForForIfsMiddleIter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, #noArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForForIfsIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, Acc, Rho)
       ... </k>
  rule <k> dictCompForForIfsMiddleIter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, #noFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, argValsCons(V:Val, RestMiddle:ArgVals), Acc:DictVals, Rho:Map) =>
           Inner ~> dictCompForForIfsInner(X, OuterFilters, Middle, Y, #noFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Y <- V ] </env>
  rule <k> dictCompForForIfsMiddleIter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:CompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, argValsCons(V:Val, RestMiddle:ArgVals), Acc:DictVals, Rho:Map) =>
           dictCompForForIfsMiddleFilter(X, OuterFilters, Middle, Y, MiddleFilters, MiddleFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Y <- V ] </env>
  rule <k> dictCompForForIfsMiddleFilter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, #filters(Filter:Exp, RestFilters:CompFilters), Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:DictVals, Rho:Map) =>
           Filter ~> dictCompForForIfsMiddleFilterNext(X, OuterFilters, Middle, Y, MiddleFilters, RestFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
  rule <k> dictCompForForIfsMiddleFilter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, #filter(Filter:Exp), Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:DictVals, Rho:Map) =>
           Filter ~> dictCompForForIfsMiddleFilterLast(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
  rule <k> V:Val ~> dictCompForForIfsMiddleFilterNext(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, RestFilters:CompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForForIfsMiddleFilter(X, OuterFilters, Middle, Y, MiddleFilters, RestFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> dictCompForForIfsMiddleFilterNext(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, _:CompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForForIfsMiddleIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> dictCompForForIfsMiddleFilterLast(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:DictVals, Rho:Map) =>
           Inner ~> dictCompForForIfsInner(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> dictCompForForIfsMiddleFilterLast(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForForIfsMiddleIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> InnerIter:Val ~> dictCompForForIfsInner(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForForIfsInnerIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, RestMiddle, iterableArgVals(InnerIter), Acc, Rho)
       ... </k>
  rule <k> dictCompForForIfsInnerIter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, #noArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForForIfsMiddleIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, RestMiddle, Acc, Rho)
       ... </k>
  rule <k> dictCompForForIfsInnerIter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, #noFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, argValsCons(V:Val, RestInner:ArgVals), Acc:DictVals, Rho:Map) =>
           Key ~> dictCompForForIfsKey(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, #noFilters, Key, Value, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Z <- V ] </env>
  rule <k> dictCompForForIfsInnerIter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:CompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, argValsCons(V:Val, RestInner:ArgVals), Acc:DictVals, Rho:Map) =>
           dictCompForForIfsInnerFilter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, InnerFilters, Key, Value, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Z <- V ] </env>
  rule <k> dictCompForForIfsInnerFilter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, #filters(Filter:Exp, RestFilters:CompFilters), Key:Exp, Value:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:DictVals, Rho:Map) =>
           Filter ~> dictCompForForIfsInnerFilterNext(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, RestFilters, Key, Value, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
  rule <k> dictCompForForIfsInnerFilter(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, #filter(Filter:Exp), Key:Exp, Value:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:DictVals, Rho:Map) =>
           Filter ~> dictCompForForIfsInnerFilterLast(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
  rule <k> V:Val ~> dictCompForForIfsInnerFilterNext(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, RestFilters:CompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForForIfsInnerFilter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, RestFilters, Key, Value, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> dictCompForForIfsInnerFilterNext(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, _:CompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForForIfsInnerIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> dictCompForForIfsInnerFilterLast(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:DictVals, Rho:Map) =>
           Key ~> dictCompForForIfsKey(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> dictCompForForIfsInnerFilterLast(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForForIfsInnerIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, RestMiddle, RestInner, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> K:Val ~> dictCompForForIfsKey(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:DictVals, Rho:Map) =>
           Value ~> dictCompForForIfsValue(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, RestMiddle, RestInner, Acc, Rho, K)
       ... </k>
  rule <k> V:Val ~> dictCompForForIfsValue(X:Id, OuterFilters:MaybeCompFilters, Middle:Exp, Y:Id, MiddleFilters:MaybeCompFilters, Inner:Exp, Z:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, RestMiddle:ArgVals, RestInner:ArgVals, Acc:DictVals, Rho:Map, K:Val) =>
           dictCompForForIfsInnerIter(X, OuterFilters, Middle, Y, MiddleFilters, Inner, Z, InnerFilters, Key, Value, RestOuter, RestMiddle, RestInner, appendDictVal(Acc, K, V), Rho)
       ... </k>
  rule <k> dictCompForIfsExp(Iter:Val, X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp) =>
           dictCompForIfsIter(X, OuterFilters, Inner, Y, InnerFilters, Key, Value, iterableArgVals(Iter), #noDictVals, Rho)
       ... </k>
       <env> Rho </env>
  rule <k> dictCompForIfsIter(_:Id, _:MaybeCompFilters, _:Exp, _:Id, _:MaybeCompFilters, _:Exp, _:Exp, #noArgVals, #noDictVals, Rho:Map) =>
           ({}):Val ~> restoreEnv(Rho)
       ... </k>
  rule <k> dictCompForIfsIter(_:Id, _:MaybeCompFilters, _:Exp, _:Id, _:MaybeCompFilters, _:Exp, _:Exp, #noArgVals, Acc:DictVals, Rho:Map) =>
           dictVal(dictValsToDictItems(Acc)) ~> restoreEnv(Rho)
       ... </k>
    requires notBool emptyDictVals(Acc)
  rule <k> dictCompForIfsIter(X:Id, #noFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, argValsCons(V:Val, RestOuter:ArgVals), Acc:DictVals, Rho:Map) =>
           Inner ~> dictCompForIfsInner(X, #noFilters, Inner, Y, InnerFilters, Key, Value, RestOuter, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> dictCompForIfsIter(X:Id, OuterFilters:CompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, argValsCons(V:Val, RestOuter:ArgVals), Acc:DictVals, Rho:Map) =>
           dictCompForIfsOuterFilter(X, OuterFilters, OuterFilters, Inner, Y, InnerFilters, Key, Value, RestOuter, Acc, Rho)
       ... </k>
       <env> _ => Rho [ X <- V ] </env>
  rule <k> dictCompForIfsOuterFilter(X:Id, OuterFilters:MaybeCompFilters, #filters(Filter:Exp, RestFilters:CompFilters), Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, Acc:DictVals, Rho:Map) =>
           Filter ~> dictCompForIfsOuterFilterNext(X, OuterFilters, RestFilters, Inner, Y, InnerFilters, Key, Value, RestOuter, Acc, Rho)
       ... </k>
  rule <k> dictCompForIfsOuterFilter(X:Id, OuterFilters:MaybeCompFilters, #filter(Filter:Exp), Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, Acc:DictVals, Rho:Map) =>
           Filter ~> dictCompForIfsOuterFilterLast(X, OuterFilters, Inner, Y, InnerFilters, Key, Value, RestOuter, Acc, Rho)
       ... </k>
  rule <k> V:Val ~> dictCompForIfsOuterFilterNext(X:Id, OuterFilters:MaybeCompFilters, RestFilters:CompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForIfsOuterFilter(X, OuterFilters, RestFilters, Inner, Y, InnerFilters, Key, Value, RestOuter, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> dictCompForIfsOuterFilterNext(X:Id, OuterFilters:MaybeCompFilters, _:CompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForIfsIter(X, OuterFilters, Inner, Y, InnerFilters, Key, Value, RestOuter, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> dictCompForIfsOuterFilterLast(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, Acc:DictVals, Rho:Map) =>
           Inner ~> dictCompForIfsInner(X, OuterFilters, Inner, Y, InnerFilters, Key, Value, RestOuter, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> dictCompForIfsOuterFilterLast(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForIfsIter(X, OuterFilters, Inner, Y, InnerFilters, Key, Value, RestOuter, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> InnerIter:Val ~> dictCompForIfsInner(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForIfsInnerIter(X, OuterFilters, Inner, Y, InnerFilters, Key, Value, RestOuter, iterableArgVals(InnerIter), Acc, Rho)
       ... </k>
  rule <k> dictCompForIfsInnerIter(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, #noArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForIfsIter(X, OuterFilters, Inner, Y, InnerFilters, Key, Value, RestOuter, Acc, Rho)
       ... </k>
  rule <k> dictCompForIfsInnerIter(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, #noFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, argValsCons(V:Val, RestInner:ArgVals), Acc:DictVals, Rho:Map) =>
           Key ~> dictCompForIfsKey(X, OuterFilters, Inner, Y, #noFilters, Key, Value, RestOuter, RestInner, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Y <- V ] </env>
  rule <k> dictCompForIfsInnerIter(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:CompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, argValsCons(V:Val, RestInner:ArgVals), Acc:DictVals, Rho:Map) =>
           dictCompForIfsInnerFilter(X, OuterFilters, Inner, Y, InnerFilters, InnerFilters, Key, Value, RestOuter, RestInner, Acc, Rho)
       ... </k>
       <env> RhoCurrent:Map => RhoCurrent [ Y <- V ] </env>
  rule <k> dictCompForIfsInnerFilter(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, #filters(Filter:Exp, RestFilters:CompFilters), Key:Exp, Value:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:DictVals, Rho:Map) =>
           Filter ~> dictCompForIfsInnerFilterNext(X, OuterFilters, Inner, Y, InnerFilters, RestFilters, Key, Value, RestOuter, RestInner, Acc, Rho)
       ... </k>
  rule <k> dictCompForIfsInnerFilter(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, #filter(Filter:Exp), Key:Exp, Value:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:DictVals, Rho:Map) =>
           Filter ~> dictCompForIfsInnerFilterLast(X, OuterFilters, Inner, Y, InnerFilters, Key, Value, RestOuter, RestInner, Acc, Rho)
       ... </k>
  rule <k> V:Val ~> dictCompForIfsInnerFilterNext(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, RestFilters:CompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForIfsInnerFilter(X, OuterFilters, Inner, Y, InnerFilters, RestFilters, Key, Value, RestOuter, RestInner, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> dictCompForIfsInnerFilterNext(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, _:CompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForIfsInnerIter(X, OuterFilters, Inner, Y, InnerFilters, Key, Value, RestOuter, RestInner, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> V:Val ~> dictCompForIfsInnerFilterLast(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:DictVals, Rho:Map) =>
           Key ~> dictCompForIfsKey(X, OuterFilters, Inner, Y, InnerFilters, Key, Value, RestOuter, RestInner, Acc, Rho)
       ... </k>
    requires truthy(V)
  rule <k> V:Val ~> dictCompForIfsInnerFilterLast(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:DictVals, Rho:Map) =>
           dictCompForIfsInnerIter(X, OuterFilters, Inner, Y, InnerFilters, Key, Value, RestOuter, RestInner, Acc, Rho)
       ... </k>
    requires notBool truthy(V)
  rule <k> K:Val ~> dictCompForIfsKey(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:DictVals, Rho:Map) =>
           Value ~> dictCompForIfsValue(X, OuterFilters, Inner, Y, InnerFilters, Key, Value, RestOuter, RestInner, Acc, Rho, K)
       ... </k>
  rule <k> V:Val ~> dictCompForIfsValue(X:Id, OuterFilters:MaybeCompFilters, Inner:Exp, Y:Id, InnerFilters:MaybeCompFilters, Key:Exp, Value:Exp, RestOuter:ArgVals, RestInner:ArgVals, Acc:DictVals, Rho:Map, K:Val) =>
           dictCompForIfsInnerIter(X, OuterFilters, Inner, Y, InnerFilters, Key, Value, RestOuter, RestInner, appendDictVal(Acc, K, V), Rho)
       ... </k>

  rule <k> dictCtorKwExp(KWS:KwArgExps) =>
           evalKwArgs(KWS, #noKwArgVals) ~> buildDictCtorKw
       ... </k>
  rule <k> kwArgsVal(KWS:KwArgVals) ~> buildDictCtorKw =>
           dictCtorFromKwArgs(KWS)
       ... </k>
  rule <k> dictCtorMixedExp(Base:Val, KWS:KwArgExps) =>
           evalKwArgs(KWS, #noKwArgVals) ~> buildDictCtorMixed(Base)
       ... </k>
  rule <k> kwArgsVal(KWS:KwArgVals) ~> buildDictCtorMixed(Base:Val) =>
           dictCtorMergeKw(Base, KWS)
       ... </k>

  rule #listCtor() => []
  rule #tupleCtor() => ()
  rule #dictCtor() => ({}):Val
  rule #setCtor() => set()
  rule #setCtor(V:Val) => setFromArgVals(iterableArgVals(V))
  rule #dictCtor(({}):Val) => ({}):Val
  rule #dictCtor(dictVal(DS:DictItems)) => dictVal(DS)
  rule #dictCtor([]) => ({}):Val
  rule #dictCtor(listVal(VS:ValItems)) => dictCtorFromPairs(VS)
  rule #dictCtor(()) => ({}):Val
  rule #dictCtor(tupleVal(VS:ValItems)) => dictCtorFromPairs(VS)
  rule dictCtorFromPairs(VS:ValItems) => ({}):Val
    requires emptyDictVals(dictCtorPairs(VS, #noDictVals))
  rule dictCtorFromPairs(VS:ValItems) => dictVal(dictValsToDictItems(dictCtorPairs(VS, #noDictVals)))
    requires notBool emptyDictVals(dictCtorPairs(VS, #noDictVals))
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
  rule #listCtor(set()) => []
  rule #listCtor(setVal(VS:ValItems)) => listVal(VS)
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
  rule #tupleCtor(set()) => ()
  rule #tupleCtor(setVal(VS:ValItems)) => tupleVal(VS)
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
  rule <k> minArgsExp(Args:ArgExps) => evalArgs(Args, #noArgVals) ~> minArgsResult ... </k>
  rule <k> argsVal(VS:ArgVals) ~> minArgsResult => minArgVals(VS) ... </k>
    requires notBool emptyArgVals(VS)
  rule <k> maxArgsExp(Args:ArgExps) => evalArgs(Args, #noArgVals) ~> maxArgsResult ... </k>
  rule <k> argsVal(VS:ArgVals) ~> maxArgsResult => maxArgVals(VS) ... </k>
    requires notBool emptyArgVals(VS)
  rule #sliceCtor(Stop:Val) => sliceVal(None, Stop, None)
  rule #sliceCtor(Start:Val, Stop:Val) => sliceVal(Start, Stop, None)
  rule #sliceCtor(Start:Val, Stop:Val, Step:Val) => sliceVal(Start, Stop, Step)
  rule #intCtor() => 0
  rule #intCtor(V:Val) => intValue(V)
    requires isIntLike(V)
  rule #floatCtor() => 0.0
  rule #floatCtor(F:Float) => F
  rule #floatCtor(V:Val) => floatValue(V)
    requires isIntLike(V)
  rule #abs(V:Val) => 0 -Int intValue(V)
    requires isIntLike(V) andBool intValue(V) <Int 0
  rule #abs(V:Val) => intValue(V)
    requires isIntLike(V) andBool intValue(V) >=Int 0
  rule #abs(F:Float) => --Float F
    requires F <Float 0.0
  rule #abs(F:Float) => F
    requires F >=Float 0.0
  rule #divmod(V1:Val, V2:Val) =>
    tupleVal(valItemsCons(pyFloorDiv(intValue(V1), intValue(V2)), valItemsLast(pyModulo(intValue(V1), intValue(V2)))))
    requires isIntLike(V1) andBool isIntLike(V2) andBool intValue(V2) =/=Int 0
  rule #divmod(F1:Float, F2:Float) =>
    tupleVal(valItemsCons(pyFloatFloorDiv(F1, F2), valItemsLast(pyFloatModulo(F1, F2))))
    requires F2 =/=Float 0.0
  rule #divmod(F:Float, V:Val) =>
    tupleVal(valItemsCons(pyFloatFloorDiv(F, floatValue(V)), valItemsLast(pyFloatModulo(F, floatValue(V)))))
    requires isIntLike(V) andBool intValue(V) =/=Int 0
  rule #divmod(V:Val, F:Float) =>
    tupleVal(valItemsCons(pyFloatFloorDiv(floatValue(V), F), valItemsLast(pyFloatModulo(floatValue(V), F))))
    requires isIntLike(V) andBool F =/=Float 0.0
  rule #pow(V1:Val, V2:Val) => intValue(V1) ^Int intValue(V2)
    requires isIntLike(V1) andBool isIntLike(V2) andBool intValue(V2) >=Int 0
  rule #pow(V1:Val, V2:Val) => Int2Float(intValue(V1), 53, 11) ^Float Int2Float(intValue(V2), 53, 11)
    requires isIntLike(V1) andBool isIntLike(V2) andBool intValue(V1) =/=Int 0 andBool intValue(V2) <Int 0
  rule #pow(F1:Float, F2:Float) => F1 ^Float F2
    requires F1 >=Float 0.0 andBool (F1 =/=Float 0.0 orBool F2 >=Float 0.0)
  rule #pow(F:Float, V:Val) => F ^Float floatValue(V)
    requires isIntLike(V) andBool F >=Float 0.0 andBool (F =/=Float 0.0 orBool intValue(V) >=Int 0)
  rule #pow(V:Val, F:Float) => floatValue(V) ^Float F
    requires isIntLike(V) andBool floatValue(V) >=Float 0.0 andBool (intValue(V) =/=Int 0 orBool F >=Float 0.0)
  rule #pow(V1:Val, V2:Val, V3:Val) => pyModulo(intValue(V1) ^Int intValue(V2), intValue(V3))
    requires isIntLike(V1)
      andBool isIntLike(V2)
      andBool isIntLike(V3)
      andBool intValue(V2) >=Int 0
      andBool intValue(V3) =/=Int 0

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
  rule <k> augTrueDivStmt(X:Id, E:Exp) => assignStmt(X, #trueDiv(X, E)) ... </k>
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
  rule <k> unpackAssignStmt(IDS:IdItems, setVal(VS:ValItems)) => stmtNoResult ... </k>
       <env> Rho => bindVals(Rho, IDS, VS) </env>
       <result> _ => .K </result>
    requires sameIdValArity(IDS, VS)
  rule <k> unpackAssignStmt(IDS:IdItems, dictVal(DS:DictItems)) => stmtNoResult ... </k>
       <env> Rho => bindVals(Rho, IDS, dictKeysToValItems(DS)) </env>
       <result> _ => .K </result>
    requires sameIdValArity(IDS, dictKeysToValItems(DS))

  rule <k> unpackTargetAssignStmt(TS:Targets, listVal(VS:ValItems)) => stmtNoResult ... </k>
       <env> Rho => bindTargets(Rho, TS, VS) </env>
       <result> _ => .K </result>
    requires sameTargetsValArity(TS, VS)
  rule <k> unpackTargetAssignStmt(TS:Targets, tupleVal(VS:ValItems)) => stmtNoResult ... </k>
       <env> Rho => bindTargets(Rho, TS, VS) </env>
       <result> _ => .K </result>
    requires sameTargetsValArity(TS, VS)
  rule <k> unpackTargetAssignStmt(TS:Targets, setVal(VS:ValItems)) => stmtNoResult ... </k>
       <env> Rho => bindTargets(Rho, TS, VS) </env>
       <result> _ => .K </result>
    requires sameTargetsValArity(TS, VS)
  rule <k> unpackTargetAssignStmt(TS:Targets, dictVal(DS:DictItems)) => stmtNoResult ... </k>
       <env> Rho => bindTargets(Rho, TS, dictKeysToValItems(DS)) </env>
       <result> _ => .K </result>
    requires sameTargetsValArity(TS, dictKeysToValItems(DS))

  rule <k> unpackStarAssignStmt(Prefix:IdItems, Star:Id, Suffix:IdItems, listVal(VS:ValItems)) => stmtNoResult ... </k>
       <env> Rho => bindStarUnpack(Rho, Prefix, Star, Suffix, VS) </env>
       <result> _ => .K </result>
    requires starUnpackArityOk(Prefix, Suffix, valItemsLen(VS))
  rule <k> unpackStarAssignStmt(Prefix:IdItems, Star:Id, Suffix:IdItems, tupleVal(VS:ValItems)) => stmtNoResult ... </k>
       <env> Rho => bindStarUnpack(Rho, Prefix, Star, Suffix, VS) </env>
       <result> _ => .K </result>
    requires starUnpackArityOk(Prefix, Suffix, valItemsLen(VS))
  rule <k> unpackStarAssignStmt(Prefix:IdItems, Star:Id, Suffix:IdItems, setVal(VS:ValItems)) => stmtNoResult ... </k>
       <env> Rho => bindStarUnpack(Rho, Prefix, Star, Suffix, VS) </env>
       <result> _ => .K </result>
    requires starUnpackArityOk(Prefix, Suffix, valItemsLen(VS))
  rule <k> unpackStarAssignStmt(Prefix:IdItems, Star:Id, Suffix:IdItems, dictVal(DS:DictItems)) => stmtNoResult ... </k>
       <env> Rho => bindStarUnpack(Rho, Prefix, Star, Suffix, dictKeysToValItems(DS)) </env>
       <result> _ => .K </result>
    requires starUnpackArityOk(Prefix, Suffix, valItemsLen(dictKeysToValItems(DS)))
  rule <k> unpackStarAssignStmt(Prefix:IdItems, Star:Id, Suffix:IdItems, []) => stmtNoResult ... </k>
       <env> Rho => Rho [ Star <- [] ] </env>
       <result> _ => .K </result>
    requires idItemsLen(Prefix) +Int idItemsLen(Suffix) ==Int 0
  rule <k> unpackStarAssignStmt(Prefix:IdItems, Star:Id, Suffix:IdItems, ()) => stmtNoResult ... </k>
       <env> Rho => Rho [ Star <- [] ] </env>
       <result> _ => .K </result>
    requires idItemsLen(Prefix) +Int idItemsLen(Suffix) ==Int 0
  rule <k> unpackStarAssignStmt(Prefix:IdItems, Star:Id, Suffix:IdItems, set()) => stmtNoResult ... </k>
       <env> Rho => Rho [ Star <- [] ] </env>
       <result> _ => .K </result>
    requires idItemsLen(Prefix) +Int idItemsLen(Suffix) ==Int 0
  rule <k> unpackStarAssignStmt(Prefix:IdItems, Star:Id, Suffix:IdItems, ({}):Val) => stmtNoResult ... </k>
       <env> Rho => Rho [ Star <- [] ] </env>
       <result> _ => .K </result>
    requires idItemsLen(Prefix) +Int idItemsLen(Suffix) ==Int 0

  rule <k> functionDefStmt(F:Id, X:Id, Body:Block) => stmtNoResult ... </k>
       <env> Rho => Rho [ F <- functionVal(X, Body) ] </env>
       <result> _ => .K </result>
  rule <k> functionDefArgsStmt(F:Id, IDS:IdItems, Body:Block) => stmtNoResult ... </k>
       <env> Rho => Rho [ F <- functionValArgs(IDS, Body) ] </env>
       <result> _ => .K </result>
  rule <k> functionDefVarArgsStmt(F:Id, IDS:IdItems, Var:Id, Body:Block) => stmtNoResult ... </k>
       <env> Rho => Rho [ F <- functionValVarArgs(IDS, Var, Body) ] </env>
       <result> _ => .K </result>
  rule <k> functionDefVarArgsDefaultsStmt(F:Id, IDS:IdItems, Defaults:ArgExps, Var:Id, Body:Block) =>
           evalArgs(Defaults, #noArgVals) ~> bindFunctionVarArgsDefaults(F, IDS, Var, Body)
       ... </k>
  rule <k> argsVal(Defaults:ArgVals) ~> bindFunctionVarArgsDefaults(F:Id, IDS:IdItems, Var:Id, Body:Block) => stmtNoResult ... </k>
       <env> Rho => Rho [ F <- functionValVarArgsDefaults(IDS, Defaults, Var, Body) ] </env>
       <result> _ => .K </result>
  rule <k> functionDefKwArgsStmt(F:Id, IDS:IdItems, Kw:Id, Body:Block) => stmtNoResult ... </k>
       <env> Rho => Rho [ F <- functionValKwArgs(IDS, Kw, Body) ] </env>
       <result> _ => .K </result>
  rule <k> functionDefPosOnlyStmt(F:Id, Pos:IdItems, Rest:IdItems, Body:Block) => stmtNoResult ... </k>
       <env> Rho => Rho [ F <- functionValPosOnly(Pos, Rest, Body) ] </env>
       <result> _ => .K </result>
  rule <k> functionDefKwOnlyStmt(F:Id, IDS:IdItems, Body:Block) => stmtNoResult ... </k>
       <env> Rho => Rho [ F <- functionValKwOnly(IDS, Body) ] </env>
       <result> _ => .K </result>
  rule <k> functionDefPosKwOnlyStmt(F:Id, Pos:IdItems, KwOnly:IdItems, Body:Block) => stmtNoResult ... </k>
       <env> Rho => Rho [ F <- functionValPosKwOnly(Pos, KwOnly, Body) ] </env>
       <result> _ => .K </result>
  rule <k> functionDefPosKwDefaultsStmt(F:Id, Pos:IdItems, PosDefaults:ArgExps, KwOnly:IdItems, KwDefaults:ArgExps, Body:Block) =>
           evalArgs(PosDefaults, #noArgVals) ~> bindFunctionPosKwDefaults(F, Pos, KwDefaults, KwOnly, Body)
       ... </k>
  rule <k> argsVal(PosDefaults:ArgVals) ~> bindFunctionPosKwDefaults(F:Id, Pos:IdItems, KwDefaults:ArgExps, KwOnly:IdItems, Body:Block) =>
           evalArgs(KwDefaults, #noArgVals) ~> bindFunctionPosKwDefaultVals(F, Pos, PosDefaults, KwOnly, Body)
       ... </k>
  rule <k> argsVal(KwDefaults:ArgVals) ~> bindFunctionPosKwDefaultVals(F:Id, Pos:IdItems, PosDefaults:ArgVals, KwOnly:IdItems, Body:Block) => stmtNoResult ... </k>
       <env> Rho => Rho [ F <- functionValPosKwDefaults(Pos, PosDefaults, KwOnly, KwDefaults, Body) ] </env>
       <result> _ => .K </result>
  rule <k> functionDefKwDefaultsStmt(F:Id, IDS:IdItems, Defaults:ArgExps, Body:Block) =>
           evalArgs(Defaults, #noArgVals) ~> bindFunctionKwDefaults(F, IDS, Body)
       ... </k>
  rule <k> argsVal(Defaults:ArgVals) ~> bindFunctionKwDefaults(F:Id, IDS:IdItems, Body:Block) => stmtNoResult ... </k>
       <env> Rho => Rho [ F <- functionValKwDefaults(IDS, Defaults, Body) ] </env>
       <result> _ => .K </result>
  rule <k> functionDefDefaultsStmt(F:Id, IDS:IdItems, Defaults:ArgExps, Body:Block) =>
           evalArgs(Defaults, #noArgVals) ~> bindFunctionDefaults(F, IDS, Body)
       ... </k>
  rule <k> argsVal(Defaults:ArgVals) ~> bindFunctionDefaults(F:Id, IDS:IdItems, Body:Block) => stmtNoResult ... </k>
       <env> Rho => Rho [ F <- functionValDefaults(IDS, Defaults, Body) ] </env>
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
  rule <k> set() ~> forIter(_:Id, _:Block) => stmtNoResult ... </k>
  rule <k> setVal(VS:ValItems) ~> forIter(X:Id, Body:Block) =>
           forItems(X, VS, Body)
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
  rule <k> ({}):Val ~> forUnpackIter(_:IdItems, _:Block) => stmtNoResult ... </k>
  rule <k> dictVal(DS:DictItems) ~> forUnpackIter(IDS:IdItems, Body:Block) =>
           forUnpackItems(IDS, dictKeysToValItems(DS), Body)
       ... </k>
  rule <k> set() ~> forUnpackIter(_:IdItems, _:Block) => stmtNoResult ... </k>
  rule <k> setVal(VS:ValItems) ~> forUnpackIter(IDS:IdItems, Body:Block) =>
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

  rule <k> forTargetUnpackStmt(TS:Targets, E:Exp, Body:Block) =>
           E ~> forTargetUnpackIter(TS, Body)
       ... </k>
  rule <k> [] ~> forTargetUnpackIter(_:Targets, _:Block) => stmtNoResult ... </k>
  rule <k> listVal(VS:ValItems) ~> forTargetUnpackIter(TS:Targets, Body:Block) =>
           forTargetUnpackItems(TS, VS, Body)
       ... </k>
  rule <k> () ~> forTargetUnpackIter(_:Targets, _:Block) => stmtNoResult ... </k>
  rule <k> tupleVal(VS:ValItems) ~> forTargetUnpackIter(TS:Targets, Body:Block) =>
           forTargetUnpackItems(TS, VS, Body)
       ... </k>
  rule <k> ({}):Val ~> forTargetUnpackIter(_:Targets, _:Block) => stmtNoResult ... </k>
  rule <k> dictVal(DS:DictItems) ~> forTargetUnpackIter(TS:Targets, Body:Block) =>
           forTargetUnpackItems(TS, dictKeysToValItems(DS), Body)
       ... </k>
  rule <k> set() ~> forTargetUnpackIter(_:Targets, _:Block) => stmtNoResult ... </k>
  rule <k> setVal(VS:ValItems) ~> forTargetUnpackIter(TS:Targets, Body:Block) =>
           forTargetUnpackItems(TS, VS, Body)
       ... </k>

  rule <k> forTargetUnpackItems(TS:Targets, valItemsCons(V:Val, Rest:ValItems), block(SS:Stmts)) =>
           SS ~> forTargetUnpackItems(TS, Rest, block(SS))
       ... </k>
       <env> Rho => bindTarget(Rho, targetSeq(TS), V) </env>
    requires targetValueArityOk(targetSeq(TS), V)
  rule <k> forTargetUnpackItems(TS:Targets, valItemsLast(V:Val), block(SS:Stmts)) =>
           SS ~> forDone
       ... </k>
       <env> Rho => bindTarget(Rho, targetSeq(TS), V) </env>
    requires targetValueArityOk(targetSeq(TS), V)
  rule <k> forTargetUnpackItems(TS:Targets, valItemsCons(V:Val, Rest:ValItems), {}) =>
           forTargetUnpackItems(TS, Rest, {})
       ... </k>
       <env> Rho => bindTarget(Rho, targetSeq(TS), V) </env>
    requires targetValueArityOk(targetSeq(TS), V)
  rule <k> forTargetUnpackItems(TS:Targets, valItemsLast(V:Val), {}) =>
           stmtNoResult
       ... </k>
       <env> Rho => bindTarget(Rho, targetSeq(TS), V) </env>
    requires targetValueArityOk(targetSeq(TS), V)

  rule <k> forStarUnpackStmt(Prefix:IdItems, Star:Id, Suffix:IdItems, E:Exp, Body:Block) =>
           E ~> forStarUnpackIter(Prefix, Star, Suffix, Body)
       ... </k>
  rule <k> [] ~> forStarUnpackIter(_:IdItems, _:Id, _:IdItems, _:Block) => stmtNoResult ... </k>
  rule <k> listVal(VS:ValItems) ~> forStarUnpackIter(Prefix:IdItems, Star:Id, Suffix:IdItems, Body:Block) =>
           forStarUnpackItems(Prefix, Star, Suffix, VS, Body)
       ... </k>
  rule <k> () ~> forStarUnpackIter(_:IdItems, _:Id, _:IdItems, _:Block) => stmtNoResult ... </k>
  rule <k> tupleVal(VS:ValItems) ~> forStarUnpackIter(Prefix:IdItems, Star:Id, Suffix:IdItems, Body:Block) =>
           forStarUnpackItems(Prefix, Star, Suffix, VS, Body)
       ... </k>
  rule <k> ({}):Val ~> forStarUnpackIter(_:IdItems, _:Id, _:IdItems, _:Block) => stmtNoResult ... </k>
  rule <k> dictVal(DS:DictItems) ~> forStarUnpackIter(Prefix:IdItems, Star:Id, Suffix:IdItems, Body:Block) =>
           forStarUnpackItems(Prefix, Star, Suffix, dictKeysToValItems(DS), Body)
       ... </k>
  rule <k> set() ~> forStarUnpackIter(_:IdItems, _:Id, _:IdItems, _:Block) => stmtNoResult ... </k>
  rule <k> setVal(VS:ValItems) ~> forStarUnpackIter(Prefix:IdItems, Star:Id, Suffix:IdItems, Body:Block) =>
           forStarUnpackItems(Prefix, Star, Suffix, VS, Body)
       ... </k>

  rule <k> forStarUnpackItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsCons(listVal(VS:ValItems), Rest:ValItems), block(SS:Stmts)) =>
           SS ~> forStarUnpackItems(Prefix, Star, Suffix, Rest, block(SS))
       ... </k>
       <env> Rho => bindStarUnpack(Rho, Prefix, Star, Suffix, VS) </env>
    requires starUnpackArityOk(Prefix, Suffix, valItemsLen(VS))
  rule <k> forStarUnpackItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsCons(tupleVal(VS:ValItems), Rest:ValItems), block(SS:Stmts)) =>
           SS ~> forStarUnpackItems(Prefix, Star, Suffix, Rest, block(SS))
       ... </k>
       <env> Rho => bindStarUnpack(Rho, Prefix, Star, Suffix, VS) </env>
    requires starUnpackArityOk(Prefix, Suffix, valItemsLen(VS))
  rule <k> forStarUnpackItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsCons([], Rest:ValItems), block(SS:Stmts)) =>
           SS ~> forStarUnpackItems(Prefix, Star, Suffix, Rest, block(SS))
       ... </k>
       <env> Rho => Rho [ Star <- [] ] </env>
    requires idItemsLen(Prefix) +Int idItemsLen(Suffix) ==Int 0
  rule <k> forStarUnpackItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsCons((), Rest:ValItems), block(SS:Stmts)) =>
           SS ~> forStarUnpackItems(Prefix, Star, Suffix, Rest, block(SS))
       ... </k>
       <env> Rho => Rho [ Star <- [] ] </env>
    requires idItemsLen(Prefix) +Int idItemsLen(Suffix) ==Int 0
  rule <k> forStarUnpackItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsLast(listVal(VS:ValItems)), block(SS:Stmts)) =>
           SS ~> forDone
       ... </k>
       <env> Rho => bindStarUnpack(Rho, Prefix, Star, Suffix, VS) </env>
    requires starUnpackArityOk(Prefix, Suffix, valItemsLen(VS))
  rule <k> forStarUnpackItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsLast(tupleVal(VS:ValItems)), block(SS:Stmts)) =>
           SS ~> forDone
       ... </k>
       <env> Rho => bindStarUnpack(Rho, Prefix, Star, Suffix, VS) </env>
    requires starUnpackArityOk(Prefix, Suffix, valItemsLen(VS))
  rule <k> forStarUnpackItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsLast([]), block(SS:Stmts)) =>
           SS ~> forDone
       ... </k>
       <env> Rho => Rho [ Star <- [] ] </env>
    requires idItemsLen(Prefix) +Int idItemsLen(Suffix) ==Int 0
  rule <k> forStarUnpackItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsLast(()), block(SS:Stmts)) =>
           SS ~> forDone
       ... </k>
       <env> Rho => Rho [ Star <- [] ] </env>
    requires idItemsLen(Prefix) +Int idItemsLen(Suffix) ==Int 0
  rule <k> forStarUnpackItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsCons(listVal(VS:ValItems), Rest:ValItems), {}) =>
           forStarUnpackItems(Prefix, Star, Suffix, Rest, {})
       ... </k>
       <env> Rho => bindStarUnpack(Rho, Prefix, Star, Suffix, VS) </env>
    requires starUnpackArityOk(Prefix, Suffix, valItemsLen(VS))
  rule <k> forStarUnpackItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsCons(tupleVal(VS:ValItems), Rest:ValItems), {}) =>
           forStarUnpackItems(Prefix, Star, Suffix, Rest, {})
       ... </k>
       <env> Rho => bindStarUnpack(Rho, Prefix, Star, Suffix, VS) </env>
    requires starUnpackArityOk(Prefix, Suffix, valItemsLen(VS))
  rule <k> forStarUnpackItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsCons([], Rest:ValItems), {}) =>
           forStarUnpackItems(Prefix, Star, Suffix, Rest, {})
       ... </k>
       <env> Rho => Rho [ Star <- [] ] </env>
    requires idItemsLen(Prefix) +Int idItemsLen(Suffix) ==Int 0
  rule <k> forStarUnpackItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsCons((), Rest:ValItems), {}) =>
           forStarUnpackItems(Prefix, Star, Suffix, Rest, {})
       ... </k>
       <env> Rho => Rho [ Star <- [] ] </env>
    requires idItemsLen(Prefix) +Int idItemsLen(Suffix) ==Int 0
  rule <k> forStarUnpackItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsLast(listVal(VS:ValItems)), {}) =>
           stmtNoResult
       ... </k>
       <env> Rho => bindStarUnpack(Rho, Prefix, Star, Suffix, VS) </env>
    requires starUnpackArityOk(Prefix, Suffix, valItemsLen(VS))
  rule <k> forStarUnpackItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsLast(tupleVal(VS:ValItems)), {}) =>
           stmtNoResult
       ... </k>
       <env> Rho => bindStarUnpack(Rho, Prefix, Star, Suffix, VS) </env>
    requires starUnpackArityOk(Prefix, Suffix, valItemsLen(VS))
  rule <k> forStarUnpackItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsLast([]), {}) =>
           stmtNoResult
       ... </k>
       <env> Rho => Rho [ Star <- [] ] </env>
    requires idItemsLen(Prefix) +Int idItemsLen(Suffix) ==Int 0
  rule <k> forStarUnpackItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsLast(()), {}) =>
           stmtNoResult
       ... </k>
       <env> Rho => Rho [ Star <- [] ] </env>
    requires idItemsLen(Prefix) +Int idItemsLen(Suffix) ==Int 0

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
  rule <k> set() ~> forElseIter(_:Id, _:Block, Else:Block) => runLoopElse(Else) ... </k>
  rule <k> setVal(VS:ValItems) ~> forElseIter(X:Id, Body:Block, Else:Block) =>
           forElseItems(X, VS, Body, Else)
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
  rule <k> ({}):Val ~> forUnpackElseIter(_:IdItems, _:Block, Else:Block) => runLoopElse(Else) ... </k>
  rule <k> dictVal(DS:DictItems) ~> forUnpackElseIter(IDS:IdItems, Body:Block, Else:Block) =>
           forUnpackElseItems(IDS, dictKeysToValItems(DS), Body, Else)
       ... </k>
  rule <k> set() ~> forUnpackElseIter(_:IdItems, _:Block, Else:Block) => runLoopElse(Else) ... </k>
  rule <k> setVal(VS:ValItems) ~> forUnpackElseIter(IDS:IdItems, Body:Block, Else:Block) =>
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

  rule <k> forTargetUnpackElseStmt(TS:Targets, E:Exp, Body:Block, Else:Block) =>
           E ~> forTargetUnpackElseIter(TS, Body, Else)
       ... </k>
  rule <k> [] ~> forTargetUnpackElseIter(_:Targets, _:Block, Else:Block) => runLoopElse(Else) ... </k>
  rule <k> listVal(VS:ValItems) ~> forTargetUnpackElseIter(TS:Targets, Body:Block, Else:Block) =>
           forTargetUnpackElseItems(TS, VS, Body, Else)
       ... </k>
  rule <k> () ~> forTargetUnpackElseIter(_:Targets, _:Block, Else:Block) => runLoopElse(Else) ... </k>
  rule <k> tupleVal(VS:ValItems) ~> forTargetUnpackElseIter(TS:Targets, Body:Block, Else:Block) =>
           forTargetUnpackElseItems(TS, VS, Body, Else)
       ... </k>
  rule <k> ({}):Val ~> forTargetUnpackElseIter(_:Targets, _:Block, Else:Block) => runLoopElse(Else) ... </k>
  rule <k> dictVal(DS:DictItems) ~> forTargetUnpackElseIter(TS:Targets, Body:Block, Else:Block) =>
           forTargetUnpackElseItems(TS, dictKeysToValItems(DS), Body, Else)
       ... </k>
  rule <k> set() ~> forTargetUnpackElseIter(_:Targets, _:Block, Else:Block) => runLoopElse(Else) ... </k>
  rule <k> setVal(VS:ValItems) ~> forTargetUnpackElseIter(TS:Targets, Body:Block, Else:Block) =>
           forTargetUnpackElseItems(TS, VS, Body, Else)
       ... </k>

  rule <k> forTargetUnpackElseItems(TS:Targets, valItemsCons(V:Val, Rest:ValItems), block(SS:Stmts), Else:Block) =>
           SS ~> forTargetUnpackElseItems(TS, Rest, block(SS), Else)
       ... </k>
       <env> Rho => bindTarget(Rho, targetSeq(TS), V) </env>
    requires targetValueArityOk(targetSeq(TS), V)
  rule <k> forTargetUnpackElseItems(TS:Targets, valItemsLast(V:Val), block(SS:Stmts), Else:Block) =>
           SS ~> forUnpackElseDone(Else)
       ... </k>
       <env> Rho => bindTarget(Rho, targetSeq(TS), V) </env>
    requires targetValueArityOk(targetSeq(TS), V)
  rule <k> forTargetUnpackElseItems(TS:Targets, valItemsCons(V:Val, Rest:ValItems), {}, Else:Block) =>
           forTargetUnpackElseItems(TS, Rest, {}, Else)
       ... </k>
       <env> Rho => bindTarget(Rho, targetSeq(TS), V) </env>
    requires targetValueArityOk(targetSeq(TS), V)
  rule <k> forTargetUnpackElseItems(TS:Targets, valItemsLast(V:Val), {}, Else:Block) =>
           runLoopElse(Else)
       ... </k>
       <env> Rho => bindTarget(Rho, targetSeq(TS), V) </env>
    requires targetValueArityOk(targetSeq(TS), V)

  rule <k> forStarUnpackElseStmt(Prefix:IdItems, Star:Id, Suffix:IdItems, E:Exp, Body:Block, Else:Block) =>
           E ~> forStarUnpackElseIter(Prefix, Star, Suffix, Body, Else)
       ... </k>
  rule <k> [] ~> forStarUnpackElseIter(_:IdItems, _:Id, _:IdItems, _:Block, Else:Block) => runLoopElse(Else) ... </k>
  rule <k> listVal(VS:ValItems) ~> forStarUnpackElseIter(Prefix:IdItems, Star:Id, Suffix:IdItems, Body:Block, Else:Block) =>
           forStarUnpackElseItems(Prefix, Star, Suffix, VS, Body, Else)
       ... </k>
  rule <k> () ~> forStarUnpackElseIter(_:IdItems, _:Id, _:IdItems, _:Block, Else:Block) => runLoopElse(Else) ... </k>
  rule <k> tupleVal(VS:ValItems) ~> forStarUnpackElseIter(Prefix:IdItems, Star:Id, Suffix:IdItems, Body:Block, Else:Block) =>
           forStarUnpackElseItems(Prefix, Star, Suffix, VS, Body, Else)
       ... </k>
  rule <k> ({}):Val ~> forStarUnpackElseIter(_:IdItems, _:Id, _:IdItems, _:Block, Else:Block) => runLoopElse(Else) ... </k>
  rule <k> dictVal(DS:DictItems) ~> forStarUnpackElseIter(Prefix:IdItems, Star:Id, Suffix:IdItems, Body:Block, Else:Block) =>
           forStarUnpackElseItems(Prefix, Star, Suffix, dictKeysToValItems(DS), Body, Else)
       ... </k>
  rule <k> set() ~> forStarUnpackElseIter(_:IdItems, _:Id, _:IdItems, _:Block, Else:Block) => runLoopElse(Else) ... </k>
  rule <k> setVal(VS:ValItems) ~> forStarUnpackElseIter(Prefix:IdItems, Star:Id, Suffix:IdItems, Body:Block, Else:Block) =>
           forStarUnpackElseItems(Prefix, Star, Suffix, VS, Body, Else)
       ... </k>

  rule <k> forStarUnpackElseItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsCons(listVal(VS:ValItems), Rest:ValItems), block(SS:Stmts), Else:Block) =>
           SS ~> forStarUnpackElseItems(Prefix, Star, Suffix, Rest, block(SS), Else)
       ... </k>
       <env> Rho => bindStarUnpack(Rho, Prefix, Star, Suffix, VS) </env>
    requires starUnpackArityOk(Prefix, Suffix, valItemsLen(VS))
  rule <k> forStarUnpackElseItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsCons(tupleVal(VS:ValItems), Rest:ValItems), block(SS:Stmts), Else:Block) =>
           SS ~> forStarUnpackElseItems(Prefix, Star, Suffix, Rest, block(SS), Else)
       ... </k>
       <env> Rho => bindStarUnpack(Rho, Prefix, Star, Suffix, VS) </env>
    requires starUnpackArityOk(Prefix, Suffix, valItemsLen(VS))
  rule <k> forStarUnpackElseItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsCons([], Rest:ValItems), block(SS:Stmts), Else:Block) =>
           SS ~> forStarUnpackElseItems(Prefix, Star, Suffix, Rest, block(SS), Else)
       ... </k>
       <env> Rho => Rho [ Star <- [] ] </env>
    requires idItemsLen(Prefix) +Int idItemsLen(Suffix) ==Int 0
  rule <k> forStarUnpackElseItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsCons((), Rest:ValItems), block(SS:Stmts), Else:Block) =>
           SS ~> forStarUnpackElseItems(Prefix, Star, Suffix, Rest, block(SS), Else)
       ... </k>
       <env> Rho => Rho [ Star <- [] ] </env>
    requires idItemsLen(Prefix) +Int idItemsLen(Suffix) ==Int 0
  rule <k> forStarUnpackElseItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsLast(listVal(VS:ValItems)), block(SS:Stmts), Else:Block) =>
           SS ~> forUnpackElseDone(Else)
       ... </k>
       <env> Rho => bindStarUnpack(Rho, Prefix, Star, Suffix, VS) </env>
    requires starUnpackArityOk(Prefix, Suffix, valItemsLen(VS))
  rule <k> forStarUnpackElseItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsLast(tupleVal(VS:ValItems)), block(SS:Stmts), Else:Block) =>
           SS ~> forUnpackElseDone(Else)
       ... </k>
       <env> Rho => bindStarUnpack(Rho, Prefix, Star, Suffix, VS) </env>
    requires starUnpackArityOk(Prefix, Suffix, valItemsLen(VS))
  rule <k> forStarUnpackElseItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsLast([]), block(SS:Stmts), Else:Block) =>
           SS ~> forUnpackElseDone(Else)
       ... </k>
       <env> Rho => Rho [ Star <- [] ] </env>
    requires idItemsLen(Prefix) +Int idItemsLen(Suffix) ==Int 0
  rule <k> forStarUnpackElseItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsLast(()), block(SS:Stmts), Else:Block) =>
           SS ~> forUnpackElseDone(Else)
       ... </k>
       <env> Rho => Rho [ Star <- [] ] </env>
    requires idItemsLen(Prefix) +Int idItemsLen(Suffix) ==Int 0
  rule <k> forStarUnpackElseItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsCons(listVal(VS:ValItems), Rest:ValItems), {}, Else:Block) =>
           forStarUnpackElseItems(Prefix, Star, Suffix, Rest, {}, Else)
       ... </k>
       <env> Rho => bindStarUnpack(Rho, Prefix, Star, Suffix, VS) </env>
    requires starUnpackArityOk(Prefix, Suffix, valItemsLen(VS))
  rule <k> forStarUnpackElseItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsCons(tupleVal(VS:ValItems), Rest:ValItems), {}, Else:Block) =>
           forStarUnpackElseItems(Prefix, Star, Suffix, Rest, {}, Else)
       ... </k>
       <env> Rho => bindStarUnpack(Rho, Prefix, Star, Suffix, VS) </env>
    requires starUnpackArityOk(Prefix, Suffix, valItemsLen(VS))
  rule <k> forStarUnpackElseItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsCons([], Rest:ValItems), {}, Else:Block) =>
           forStarUnpackElseItems(Prefix, Star, Suffix, Rest, {}, Else)
       ... </k>
       <env> Rho => Rho [ Star <- [] ] </env>
    requires idItemsLen(Prefix) +Int idItemsLen(Suffix) ==Int 0
  rule <k> forStarUnpackElseItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsCons((), Rest:ValItems), {}, Else:Block) =>
           forStarUnpackElseItems(Prefix, Star, Suffix, Rest, {}, Else)
       ... </k>
       <env> Rho => Rho [ Star <- [] ] </env>
    requires idItemsLen(Prefix) +Int idItemsLen(Suffix) ==Int 0
  rule <k> forStarUnpackElseItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsLast(listVal(VS:ValItems)), {}, Else:Block) =>
           runLoopElse(Else)
       ... </k>
       <env> Rho => bindStarUnpack(Rho, Prefix, Star, Suffix, VS) </env>
    requires starUnpackArityOk(Prefix, Suffix, valItemsLen(VS))
  rule <k> forStarUnpackElseItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsLast(tupleVal(VS:ValItems)), {}, Else:Block) =>
           runLoopElse(Else)
       ... </k>
       <env> Rho => bindStarUnpack(Rho, Prefix, Star, Suffix, VS) </env>
    requires starUnpackArityOk(Prefix, Suffix, valItemsLen(VS))
  rule <k> forStarUnpackElseItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsLast([]), {}, Else:Block) =>
           runLoopElse(Else)
       ... </k>
       <env> Rho => Rho [ Star <- [] ] </env>
    requires idItemsLen(Prefix) +Int idItemsLen(Suffix) ==Int 0
  rule <k> forStarUnpackElseItems(Prefix:IdItems, Star:Id, Suffix:IdItems, valItemsLast(()), {}, Else:Block) =>
           runLoopElse(Else)
       ... </k>
       <env> Rho => Rho [ Star <- [] ] </env>
    requires idItemsLen(Prefix) +Int idItemsLen(Suffix) ==Int 0

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
  rule <k> return => returnSignal(None) ... </k>
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
  rule <k> breakSignal ~> forTargetUnpackItems(_:Targets, _:ValItems, _:Block) => stmtNoResult ... </k>
  rule <k> continueSignal ~> forTargetUnpackItems(TS:Targets, VS:ValItems, Body:Block) =>
           forTargetUnpackItems(TS, VS, Body)
       ... </k>
  rule <k> returnSignal(V:Val) ~> forTargetUnpackItems(_:Targets, _:ValItems, _:Block) => returnSignal(V) ... </k>
  rule <k> breakSignal ~> forStarUnpackItems(_:IdItems, _:Id, _:IdItems, _:ValItems, _:Block) => stmtNoResult ... </k>
  rule <k> continueSignal ~> forStarUnpackItems(Prefix:IdItems, Star:Id, Suffix:IdItems, VS:ValItems, Body:Block) =>
           forStarUnpackItems(Prefix, Star, Suffix, VS, Body)
       ... </k>
  rule <k> returnSignal(V:Val) ~> forStarUnpackItems(_:IdItems, _:Id, _:IdItems, _:ValItems, _:Block) => returnSignal(V) ... </k>
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
  rule <k> breakSignal ~> forTargetUnpackElseItems(_:Targets, _:ValItems, _:Block, _:Block) => stmtNoResult ... </k>
  rule <k> continueSignal ~> forTargetUnpackElseItems(TS:Targets, VS:ValItems, Body:Block, Else:Block) =>
           forTargetUnpackElseItems(TS, VS, Body, Else)
       ... </k>
  rule <k> returnSignal(V:Val) ~> forTargetUnpackElseItems(_:Targets, _:ValItems, _:Block, _:Block) => returnSignal(V) ... </k>
  rule <k> breakSignal ~> forStarUnpackElseItems(_:IdItems, _:Id, _:IdItems, _:ValItems, _:Block, _:Block) => stmtNoResult ... </k>
  rule <k> continueSignal ~> forStarUnpackElseItems(Prefix:IdItems, Star:Id, Suffix:IdItems, VS:ValItems, Body:Block, Else:Block) =>
           forStarUnpackElseItems(Prefix, Star, Suffix, VS, Body, Else)
       ... </k>
  rule <k> returnSignal(V:Val) ~> forStarUnpackElseItems(_:IdItems, _:Id, _:IdItems, _:ValItems, _:Block, _:Block) => returnSignal(V) ... </k>
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
  rule <k> delManyStmt(IDS:IdItems) => stmtNoResult ... </k>
       <env> Rho => delIds(Rho, IDS) </env>
       <result> _ => .K </result>

  rule <k> pass => stmtNoResult ... </k>
  rule <k> assertStmt(V:Val) => stmtNoResult ... </k>
    requires truthy(V)
  rule <k> assertMsgStmt(V:Val, _Msg:Exp) => stmtNoResult ... </k>
    requires truthy(V)
  rule <k> globalStmt(_:Id) => stmtNoResult ... </k>
  rule <k> globalManyStmt(_:IdItems) => stmtNoResult ... </k>

  rule <k> stmtNoResult ~> stmtNext(SS:Stmts) => SS ... </k>
  rule <k> stmtNoResult ~> stmtEnd => .K ... </k>
endmodule
