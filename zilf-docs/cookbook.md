[← Back to Main Index](./index.md)

# ZILF Cookbook
---

## Core Functions

### ASCII
```zil
<ASCII !\A>  ;  65
<ASCII 65>  ;  !\A
```


### ATOM
```zil
<ATOM "FOO">  ;  FOO!-#FALSE ()
<==? <ATOM "FOO"> <ATOM "FOO">>  ;  #FALSE
```


### AVALUE
```zil
<DEFINE LAST-ASOC ()
    <REPEAT ((A <ASSOCIATIONS>))
        <COND (<=? .A <>> <RETURN <>>)
        (<=? <NEXT .A> <>> <RETURN .A>)>
    <SET A <NEXT .A>>>>
<PUTPROP NEW-ASOC TEXT "Hello, world!">
<SET A <LAST-ASOC>>
<AVALUE .A>  ;  "Hello, world!"
```


### BEGIN-SEGMENT
```zil
; From The Abyss
<BEGIN-SEGMENT 0>
; Code
<END-SEGMENT>

; From Shogun
<BEGIN-SEGMENT RECORD>
; Code
<END-SEGMENT>
```


### BIND
```zil
<BIND ((X 1)) #DECL ((X) FIX)  
<BIND ((X 2)) <PRIN1 .X>> <PRIN1 .X>>  ;  "21"

<DEFINE TEST-BIND-AS-REPEAT () 
    <PRINC "START "> 
    <BIND ACT ((X 0)) 
        <SET X <+ .X 1>> 
        <PRIN1 .X> 
        <COND (<=? .X 3> <RETURN T .ACT>)>  ;  "--> exit block"
        <AGAIN .ACT>  ;  "--> repeat"
    >
    <PRINC " END">
>
<TEST-BIND-AS-REPEAT>  ;  "START 123 END"
```


### BLOCK
```zil
<SETG FOO 111>
<SET BAR 222>
<DEFINE TEST-BLOCK () <PRINT "OUTSIDE BLOCK">>
<BLOCK (<MOBLIST NEW-OBLIST> <ROOT>)>
<SETG FOO 333>
<SET BAR 444>
<DEFINE TEST-BLOCK () <PRINT "INSIDE BLOCK">>
<GVAL FOO>  ;  333
<LVAL BAR>  ;  444 
<TEST-BLOCK>  ;  "INSIDE BLOCK"
<ENDBLOCK>
<GVAL FOO>  ;  111
<LVAL BAR>  ;  222
<TEST-BLOCK>  ;  "OUTSIDE BLOCK"
```


### BOUND?
```zil
<SET X 42>
<ASSIGNED? X>  ;  True
<GBOUND? X>  ;  True
<GUNASSIGN X>
<GASSIGNED? X>  ;  False
<GBOUND? X>  ;  True
```


### BYTE
```zil
<BYTE 42>  ;  #BYTE 42
#BYTE 42  ;  #BYTE 42
<CHTYPE 42 BYTE>  ;  #BYTE 42
```


### CHECK-VERSION?
```zil
<VERSION XZIP>
<CHECK-VERSION? ZIP>  ;  #FALSE
<CHECK-VERSION? 5>  ;  T
```


### CHRSET
```zil
;"    1         2         3
67890123456789012345678901
zyxwvutsrqponmlkjihgfedcba
 z=6   i=23  l=20
1 00110 10111 10100"

<VERSION 5>

<CHRSET 0 "zyxwvutsrqponmlkjihgfedcba">
<CONSTANT ENCODED-TEXT <TABLE #2 1001101011110100>>
<CONSTANT MYTEXT "zil">

<ROUTINE GO () <TEST-CHRSET>>

<ROUTINE TEST-CHRSET ()
    <PRINTB ,ENCODED-TEXT> <CRLF>
    <PRINT ,MYTEXT> <CRLF>
    <PRINTN <GET ,ENCODED-TEXT 0>> <CRLF>
    <PRINTN <GET <* 4 ,MYTEXT> 0>> <CRLF> ;"Multiply by 4 to get packed address in v 5."
    <PRINTN <- <GET <* 4 ,MYTEXT> 0> <GET ,ENCODED-TEXT 0>>>
    <CRLF>>

;  Expected output
;  zil
;  zil
;  -25868
;  -25868
;  0
```


### COMPILATION-FLAG
```zil
<COMPILATION-FLAG MYFLAG>
<COMPILATION-FLAG-VALUE MYFLAG>  ;  T
<COMPILATION-FLAG “MYFLAG” 123>
<COMPILATION-FLAG-VALUE MYFLAG>  ;  123
```


### COMPILATION-FLAG-DEFAULT
```zil
<COMPILATION-FLAG-DEFAULT MYFLAG T>
<COMPILATION-FLAG-VALUE MYFLAG>  ;  T 
<COMPILATION-FLAG “MYFLAG” 123>
<COMPILATION-FLAG-VALUE MYFLAG>  ;  123 
<COMPILATION-FLAG-DEFAULT MYFLAG T>
<COMPILATION-FLAG-VALUE MYFLAG>  ;  123
```


### COMPILATION-FLAG-VALUE
```zil
<COMPILATION-FLAG MYFLAG 123>
<COMPILATION-FLAG-VALUE MYFLAG>  ;  123
<COMPILATION-FLAG-VALUE ASDFGHJKL>  ;  #FALSE
```


### CONS
```zil
<CONS 1 (2 3)>  ;  (1 2 3)
<SET S1 (!\B !\C)>
<SET S2 <CONS !\A .S1>>
<PUT .S1 2 !\D>
.S2  ;  (!\A !\B !\D)
```


### CONSTANT
```zil
<CONSTANT MSG-CANT-DO-THAT "You can't do that!">
...
<TELL ,MSG-CANT-DO-THAT CR>
```


### CRLF
```zil
<CRLF>  ;  "\n"
```


### DECL-CHECK
```zil
<DECL-CHECK <>>
<GDECL (FOO) FIX>
<SETG FOO <>>  ;  Ok!
<DECL-CHECK T>
<SETG FOO <>>  ;  Error
```


### DECL?
```zil
;  Simple DECL
<DECL? 1 FIX>  ;  T
<DECL? "hi" STRING>  ;  T
<DECL? FOO STRING>  ;  #FALSE

;  OR DECL
<DECL? 1 '<OR FIX FALSE>>  ;  T
<DECL? "hi" '<OR VECTOR STRING>>  ;  T
<DECL? FOO '<OR STRING FIX>>  ;  #FALSE

;  Structure DECL
<DECL? '(1) '<LIST FIX>  ;  T
<DECL? '(1) '<LIST ATOM>>  ;  #FALSE
<DECL? '<1> '<LIST FIX>>  ;  #FALSE
<DECL? '<1> '<<OR FORM LIST> FIX>>  ;  T
<DECL? '<1> '<<OR <PRIMTYPE LIST> <PRIMTYPE STRING>> FIX>>  ;  T
<DECL? '(1) '<<PRIMTYPE LIST> FIX>>  ;  T
<DECL? '<1> '<<PRIMTYPE LIST> FIX>>  ;  T

;  NTH DECL
<DECL? '["hi" 456 789 1011] '<VECTOR STRING [4 FIX]>>  ;  #FALSE
<DECL? '["hi" 456 789 1011] '<VECTOR STRING [3 FIX]>>  ;  T
<DECL? '["hi" 456 789 1011] '<VECTOR [3 FIX]>>  ;  #FALSE
<DECL? '["hi" 456 789 1011] '<VECTOR STRING [2 FIX]>>  ;  T
<DECL? '["hi" 456 789 1011] '<VECTOR STRING [2 FIX] FIX>>  ;  T
<DECL? '["hi" 456 789 1011] '<VECTOR STRING [2 FIX] ATOM>>  ;  #FALSE
<DECL? '(1 MONEY 2 SHOW 3 READY 4 GO) '<LIST [4 FIX ATOM]>>  ;  T
<DECL? '(1 MONEY 2 SHOW 3 READY 4 GO) '<LIST [4 FIX]>>  ;  #FALSE
<DECL? '(1 MONEY 2 SHOW 3 READY 4 GO)
    '<LIST [3 FIX ATOM] FIX ATOM>>  ;  T
<DECL? '(1 MONEY 2 SHOW 3 READY 4 GO) '<LIST [3 FIX ATOM]>>  ;  T

;  REST DECL
<DECL? '["hi" 456 789 1011] '<VECTOR STRING FIX [REST FIX]>>  ;  T
<DECL? '(FOO BAR) '<LIST STRING [REST FIX]>>  ;  #FALSE
<DECL? '(FOO BAR) '<LIST ATOM [REST FIX]>>  ;  #FALSE
<DECL? '(FOO BAR) '<LIST ATOM ATOM [REST FIX]>>  ;  T

;  OPT DECL
<DECL? '(FOO BAR) '<LIST [OPT FIX FIX] [REST ATOM]>>  ;  T
<DECL? '(1 FOO BAR) '<LIST [OPT FIX FIX] [REST ATOM]>>  ;  T
<DECL? '(1 2 FOO BAR) '<LIST [OPT FIX] [REST ATOM]>>  ;  #FALSE
<DECL? '(1 2 FOO BAR) '<LIST [OPT FIX FIX] [REST ATOM]>>  ;  T
<DECL? '(1 2) '<LIST [OPT FIX FIX] [REST ATOM]>>  ;  T
 
;  QUOTE DECL
<DECL? FOO ''FOO>  ;  T
<DECL? FOO ''BAR>  ;  #FALSE
<DECL? '<OR FIX FALSE> ''<OR FIX FALSE>>  ;  T
<DECL? 123 ''<OR FIX FALSE>>  ;  #FALSE

;  Segment DECL
<DECL? '(1 2 3) '<LIST FIX FIX>>  ;  T
<DECL? '(1 2 3) '!<LIST FIX FIX>>  ;  #FALSE
<DECL? '(1 2) '!<LIST FIX FIX>>  ;  T
<DECL? '(1 2) '!<LIST [REST FIX FIX]>>  ;  T
<DECL? '(1 2 3) '!<LIST [REST FIX FIX]>>  ;  #FALSE
<DECL? '(1 2 3 4) '!<LIST [REST FIX FIX]>>  ;  T

;  LVAL/GVAL DECL
<DECL? '.X LVAL>  ;  T
<DECL? '.X GVAL>  ;  #FALSE
<DECL? ',X GVAL>  ;  T
<DECL? ',X LVAL>  ;  #FALSE
<DECL? '.X '<PRIMTYPE ATOM>>  ;  T
<DECL? ',X '<PRIMTYPE ATOM>>  ;  T
```


### DEFAULT-DEFINITION
```zil
<ROUTINE MY-ROUTINE ()  
    <TELL "Original version of MY-ROUTINE" CR> 
> 
<SET REDEFINE T> 
    <ROUTINE MY-ROUTINE ()  
        <TELL "Replaced version of MY-ROUTINE" CR> 
    > 
<SET REDEFINE <>> 
<MY-ROUTINE>  ;  "Replaced version of MY-ROUTINE"
```


### DEFINE
```zil
<DEFINE MYADD (X1 X2) <+ .X1 .X2>>
<MYADD 4 5>  ;  9
<DEFINE SQUARE (X) <* .X .X>>
<SQUARE 5>  ;  25
<DEFINE POWER-TO ACT (X "OPT" (Y 2)) 
    <COND (<=? .Y 0> <RETURN 1 .ACT>)> 
    <REPEAT ((Z 1)(I 0)) 
        <SET Z <* .Z .X>> 
        <SET I <+ .I 1>> 
        <COND (<=? .I .Y> <RETURN .Z>)> 
    > 
> 
<POWER-TO 2 3>  ;  8
<POWER-TO 3 4>  ;  81
<POWER-TO 3 0>  ;  1
```


### DEFINE-GLOBALS
```zil
;  From Bureaucracy
<DEFINE-GLOBALS COMPUTER-GLOBALS
    (LAST-LINE-USED:FIX BYTE 0)
    (TIMES-THROUGH-LOOP:FIX BYTE 0)
    (FILES-ON-SCREEN? BYTE <>)
    (TELECOM? BYTE <>)
    (EXITED-ALREADY? BYTE <>)
    (COMPUTER-DEAD? BYTE <>)
    (COMP-X:FIX BYTE 0)
    (COMP-Y:FIX BYTE 0)
    (CURRENT-TARGET-NAME <>)  ;  "String for interrupt messages"
    (REAL-TARGET-NAME <>)  ; "LTABLE for looking stuff up in directory"
    (REMAINING-TARGET-TURNS:FIX BYTE 0)  ;  "Turns left until this one's done"
    (LINES-TO-NEXT-TARGET:FIX BYTE 0)  ;  "Lines to output before select next target"
    (TERMINATE-CURRENT:FIX BYTE 0)  ;  "Lines to output before terminating this one"
    (COMMANDS-SINCE-START:FIX BYTE 0)  ;  "Command lines read since target started"
    (DIE-ON-NEXT-COMMAND BYTE <>)  ;  "To avoid hair of faking non-local return"
    (WILL-WIN? BYTE <>)  ;  "True if killed computer"
    (FERROR-ACTIVE? BYTE <>)>
```


### DEFINITIONS
```zil
;"Define PACKAGE" 
<REMOVE ANSWER> ;"Secure that ATOM not on any OBLIST"  
<DEFINITIONS "FOO"> 
<SETG ANSWER 42> 
<END-DEFINITIONS> 

<TYPE? <GETPROP FOO!-PACKAGE OBLIST> OBLIST>  ;  OBLIST
<GASSIGNED? ANSWER>  ;  #FALSE
<GASSIGNED? ANSWER!-FOO!-PACKAGE>  ;  T
,ANSWER!-FOO!-PACKAGE  ;  42

<REMOVE ANSWER> ;"Secure that ATOM not on any OBLIST"
<INCLUDE "FOO">
,ANSWER  ;  42
```


### DEFMAC
```zil
<DEFMAC INC (ATM "OPTIONAL" (N 1))
    <FORM SET .ATM 
        <FORM + <FORM LVAL .ATM> .N>>>
<SET X 1>
<INC X 2>  ;  3
<EXPAND '<INC X 2>>  ;  <SET X <+ .X 2>>
```


### DELAY-DEFINITION
```zil
;"REPLACE can be defined after DEFAULT" 
<DELAY-DEFINITION FOO-ROUTINE> 
<DEFAULT-DEFINITION FOO-ROUTINE <DEFINE FOO () 123>> 
<REPLACE-DEFINITION FOO-ROUTINE <DEFINE FOO () 456>>
<FOO>  ;  456

;"DELAY means that REPLACE is evaluated at right place" 
<DELAY-DEFINITION BAR-ROUTINE> 
<SETG BAR-RESULT 789> 
<REPLACE-DEFINITION BAR-ROUTINE 
<EVAL <FORM DEFINE BAR '() ,BAR-RESULT>>> 
<SETG BAR-RESULT 123> 
<DEFAULT-DEFINITION BAR-ROUTINE 
<EVAL <FORM DEFINE BAR '() ,BAR-RESULT>>>
<BAR>  ;  789 ("123 without DELAY")
```


### EMPTY?
```zil
<EMPTY? [1 2 3]>  ;  False
<EMPTY? []>  ;  True
```


### END-SEGMENT
```zil
; From The Abyss
<BEGIN-SEGMENT 0>
; Code
<END-SEGMENT>

; From Shogun
<BEGIN-SEGMENT RECORD>
; Code
<END-SEGMENT>
```


### ENDBLOCK
```zil
XYZZY!-MY-OBLIST 
<SETG FIRST!- FOO> 
<BLOCK (<GETPROP MY-OBLIST OBLIST> <ROOT>)> 
<SETG SECOND!- FOO> 
<ENDBLOCK> 
<=? ,FIRST!- ,SECOND!->  ;  #FALSE
```


### ENTRY
```zil
<REMOVE ANSWER>  ;  "Secure that ATOM not on any OBLIST"
<PACKAGE "FOO">
<SETG ANSWER 42>
<1 .OBLIST>  ;  #OBLIST (("ANSWER" ANSWER)) 
<2 .OBLIST>  ;  #OBLIST (("IFOO" IFOO))
<ENTRY ANSWER>
<1 .OBLIST>  ;  #OBLIST ()
<2 .OBLIST>  ;  #OBLIST (("IFOO" IFOO) ("ANSWER" ANSWER))
<ENDPACKAGE>
,ANSWER  ;  42 (the meaning of life)
```


### EQVB
```zil
<XORB 250 245>  
;  00000000 00000000 00000000 11111010
;  00000000 00000000 00000000 11110101
;  -----------------------------------
;  11111111 11111111 11111111 11110000 = -16
```


### ERROR
```zil
<SET A 616>
<ERROR "MY TYPE OF ERROR." .A> 
; [error MDL0001] <stdin>:1: ERROR: "MY TYPE OF ERROR." 616
```


### EVAL
```zil
<SET F '<+ 1 2>> 
.F ; Sets up the stack operator and operands, + 1 2.
<EVAL .F> ; Evaluates the operands with the given operator from the stack to 3.
<SET A 0>
<DEFINE WRONG ('B "AUX" (A 1)) <EVAL .B>> 
<DEFINE RIGHT ("BIND" E 'B "AUX" (A 1)) <EVAL .B .E>> 
<WRONG .A> ; 1
<RIGHT .A> ; 0
```


### EVAL-IN-SEGMENT
```zil
<SET F '<+ 1 2>> 
.F  ;  <+ 1 2>
<EVAL-IN-SEGMENT "HINTS" .F (1 2 3)>  ;  3
```


### EVALTYPE
```zil
<NEWTYPE GRITCH LIST>
<EVALTYPE GRITCH>  ;  #FALSE
<EVALTYPE GRITCH LIST>  ;  "Evaluate GRITCH as a LIST"
<EVALTYPE GRITCH>  ;  LIST
#GRITCH (A <+ 1 2 3> !<SET A "BC">)
;"Make it like LISP!"  ;  (A 6 !\B !\C)
<EVALTYPE LIST FORM>  ;  "Evaluate LISTs as FORMs!"
<EVALTYPE ATOM ,LVAL>  ;  "Evaluate bare ATOM as LVAL!"
(+ 1 2)  ;  3
(SET 'A 5)
A  ;  5
```


### EXPAND
```zil
<DEFMAC INC2 (ATM "OPTIONAL" (N 1))
    <PARSE "<SET %.ATM <+ %.ATM %.N>>">>
<EXPAND '<INC2 X>>   --> <SET X <+ X 1>>
```


### FILE-LENGTH
```zil
;  "ZILF ver 0.9"
<SET CH <OPEN "READ" "../zillib/parser.zil">>
<FILE-LENGTH .CH>  ;  115629
<CLOSE .CH>
```


### FORM
```zil
<FORM + 1 2>  ;  <+ 1 2> 
<DEFINE INC-FORM (A) 
    <FORM SET .A <FORM + 1 <FORM LVAL .A>>>> 
<INC-FORM X>  ;  <SET X <+ 1 .X>
```


### GASSIGNED?
```zil
<GASSIGNED? X>  ;  False 
<SETG X 1> 
<GASSIGNED? X>  ;  True
```


### GBOUND?
```zil
<SETG X 42> 
<GASSIGNED? X>  ;  True 
<GBOUND? X>  ;  True 
<GUNASSIGN X>
<GASSIGNED? X>  ;  False 
<GBOUND? X>  ;  True
```


### GC
```zil
<GC>  ;  T
<GC 0 T 5>  ;  T
```


### GET-DECL
```zil
<GET-DECL BOOLEAN>  ;  #FALSE
<PUT-DECL BOOLEAN '<OR ATOM FALSE>>
<GET-DECL BOOLEAN>  ;  <OR ATOM FALSE>
```


### GETPROP
```zil
<PUTPROP FOO BAR BAZ> 
<GETPROP FOO BAR>  ;  BAZ  
<GETPROP FOO BAZ>  ;  #FALSE 
<GETPROP FOO BAZ "Value not found.">  ;  "Value not found." 
<SET L (1 2 3)>
<PUTPROP .L FOO 456>
.L  ;  (1 2 3)
<GETPROP .L FOO>  ;  456
```


### GLOBAL
```zil
<GLOBAL MYVAR 0>
```


### GROW
```zil
<SET V1 [1 2 3]>
<SET V2 <GROW .V1 1 1>>
<LVAL V1>  ;  [1 2 3 #FALSE ()]
<LVAL V2>  ;  [#FALSE () 1 2 3 #FALSE ()]
<2 .V1 4>
<LVAL V1>  ;  [1 4 3 #FALSE ()]
<LVAL V2>  ;  [#FALSE () 1 4 3 #FALSE ()]
<TOP .V1>  ;  [#FALSE () 1 4 3 #FALSE ()]
```


### GUNASSIGN
```zil
<SETG X 1>
<GASSIGNED? X>  ;  True
<GUNASSIGN X>
<GASSIGNED? X>  ;  False
```


### GVAL
```zil
<SETG X 5>
<GVAL X>  ;  5 
,X  ;  5
```


### IFFLAG
```zil
<COMPILATION-FLAG MYFLAG <>>
<IFFLAG (MYFLAG <SETG FOO "NOT OFF">) (T <SETG FOO "OFF">)>
,FOO  ;  "OFF"
```


### ILIST
```zil
<ILIST 4 2>  ;  (2 2 2 2)
<SET A 0>
<ILIST 4 '<SET A <+ .A 1>>>  ;  (1 2 3 4)
```


### IMAGE
```zil
<DEFINE FOO () 
    <IMAGE 70> 
    <IMAGE 79> 
    <IMAGE 79> 
    <CRLF>>
<FOO>  ;  "FOO"
```


### INCLUDE
```zil
;"Searches for file "foofoo.zil" which contains the definition for  <DEFINITIONS "FOOFOO"> ..."
<INCLUDE "FOOFOO">
```


### INCLUDE-WHEN
```zil
<DEFINITIONS "FOO">
<SETG AAAA 1234>
<END-DEFINITIONS>
<GASSIGNED? AAAA>  ;  #FALSE
<REMOVE AAAA>  ;  "Secure that ATOM not on any OBLIST"
<INCLUDE-WHEN <=? 1 2> "FOO">
<GASSIGNED? AAAA>  ;  #FALSE
<REMOVE AAAA>  ;  "Secure that ATOM not on any OBLIST"
<INCLUDE-WHEN <=? 1 1> "FOO">
,AAAA  ;  1234
```


### INDENT-TO
```zil
<DEFINE PRINT-2-COL (LST) 
    <REPEAT ((I 0)) 
        <SET I <+ .I 1>> 
        <COND (<G? .I <LENGTH .LST>> <RETURN>)> 
        <COND (<1? <MOD .I 2>> 
                            <INDENT-TO 3>  
                            <PRINC <.I .LST>>) 
                       (T  <INDENT-TO 15>  
                           <PRINC <.I .LST>>  
                           <CRLF>)>> 
    <CRLF>> 
<PRINT-2-COL ("Apple" "Banana" "Orange" "Lime")> 
;  Apple       Banana 
;  Orange  Lime
```


### INDEX
```zil
<SETG OFF3 <OFFSET 3 '<VECTOR> 'STRING>>
<INDEX ,OFF3>  ;  3
```


### INDICATOR
```zil
<DEFINE LAST-ASOC ()
    <REPEAT ((A <ASSOCIATIONS>))
        <COND (<=? .A <>> <RETURN <>>)
        (<=? <NEXT .A> <>> <RETURN .A>)>
   <SET A <NEXT .A>>>>
<PUTPROP NEW-ASOC TEXT "Hello, world!">
<SET A <LAST-ASOC>>
<INDICATOR .A>  ;  TEXT
```


### INSERT
```zil
<INSERT "FOO-1" <MOBLIST OB>>  ;  FOO-1!-OB
<INSERT <ATOM "FOO-2"> <MOBLIST OB>>  ;  FOO-2!-OB
<INSERT <REMOVE "FOO-2" <MOBLIST OB>> <MOBLIST OB2>>  ;  FOO-2!-OB2
<INSERT FOO-3 <MOBLIST OB>>  ;  Error (Interpreter already placed it on <1 .OBLIST>

;  "Returns FOO from OB. Creates ATOM/OBLIST if needed."
<OR <LOOKUP "FOO" <MOBLIST OB>> <INSERT "FOO" <MOBLIST OB>>  ;  FOO!-OB
FOO!-OB  ;  FOO!-OB
BAR!-OB  ;  BAR!-OB
<MOBLIST OB>  ;  #OBLIST (("FOO" FOO!-OB) ("BAR" BAR!-OB))
```


### INSERT-FILE
```zil
<INSERT-FILE "rooms">  ;  Include "rooms.zil" from current directory 
<INSERT-FILE "zillib/parser">  ;  Include "parser.zil" from subdir "zilllib"
```


### ISTRING
```zil
<ISTRING 4 !\A>  ;  "AAAA"
<SET A 64>
<ISTRING 4 '<ASCII <SET A <+ .A 1>>>>  ;  "ABCD"
```


### ITEM
```zil
<DEFINE LAST-ASOC ()
    <REPEAT ((A <ASSOCIATIONS>))
        <COND (<=? .A <>> <RETURN <>>)
        (<=? <NEXT .A> <>> <RETURN .A>)>
    <SET A <NEXT .A>>>>
<PUTPROP NEW-ASOC TEXT "Hello, world!">
<SET A <LAST-ASOC>>
<ITEM .A>  ;  NEW-ASOC
```


### IVECTOR
```zil
<IVECTOR 4 2>  ;  [2 2 2 2]
<SET A 0>
<IVECTOR 4 '<SET A <+ .A 1>>>  ;  [1 2 3 4]
```


### LEGAL?
```zil
;  "Activation"
<DEFINE FOO ACT () <SETG ACT .ACT> <LEGAL? .ACT>>
<FOO>  ;  T, "ACT legal inside function"
<LEGAL? ,ACT>  ;  #FALSE, "ACT illegal outside function"

;  "Environment"
<DEFINE BAR () <BAZ>>
<DEFINE BAZ ("BIND" ENV) <SETG ENV .ENV> <LEGAL? .ENV>>
<BAR>  ;  T, "Sets ENV to BARs environment"
<LEGAL? ,ENV>  ;  #FALSE, "BARs environment illegal"
<BAZ>  ;  T, "Sets ENV to ROOT environment" 
<LEGAL? ,ENV>  ;  T, "ROOTs environment always legal"
```


### LENGTH
```zil
<LENGTH <LIST 1 2 3>>  ;  3
```


### LENGTH?
```zil
<LENGTH? (1 2 3) 1>  ;  False
<LENGTH? (1 2 3) 3>  ;  3
<NOT <NOT <LENGTH? (1 2 3) 4>>>  ;  True
```


### LIST
```zil
<LIST 1 2 "AB" !\C>  ;  (1 2 "AB" !\C)
(1 2 "AB" !\C)  ;  (1 2 "AB" !\C)
```


### LONG-WORDS?
```zil
;  For example, the table might be defined as equivalent to the following.

<CONSTANT LONG-WORDS-TABLE
    <CONSTANT LONG-WORDS-TABLE
        ,W?HEMIDEMIS "hemidemisemiquaver"
        ,W?SUPERCALI "supercalifragilisticexpialidocious">>

;  For another example.
<VERSION 5>
<LONG-WORDS? T>
<OBJECT FOO (SYNONYM HEMIDEMISEMI)>
<VOC "SUPERCALIFRAG">
<ROUTINE GO ()
    <TELL "Table length = " N <GET ,LONG-WORD-TABLE 0> CR>
    <TELL "W?SUPERCALIFRAG = " N ,W?SUPERCALIFRAG CR>
    <TELL "WORD 1 = " N <GET ,LONG-WORD-TABLE 1> CR>
    <TELL "WORD 2 = " <GET ,LONG-WORD-TABLE 2> CR>
    <TELL "W?HEMIDEMISEMI = " N ,W?HEMIDEMISEMI CR>
    <TELL "WORD 3 = " N <GET ,LONG-WORD-TABLE 3> CR>
    <TELL "WORD 4 = " <GET ,LONG-WORD-TABLE 4> CR>
>
```


### LOOKUP
```zil
<LOOKUP "FIX" <ROOT>>  ;  FIX
FOO!-MYOBLIST
<LOOKUP "FOO" <ROOT>>  ;  #FALSE
<LOOKUP "FOO" <MOBLIST MYOBLIST>>  ;  FOO!-MYOBLIST
```


### LPARSE
```zil
<LPARSE "1 FOO [3]">  ;  (1 FOO [3])
<LPARSE " ">  ;  ()
<SET A 0>
<DEFINE NXT () <SET A <+ .A 1>>>
<LPARSE "%<NXT> %<NXT> %<NXT>">  ;  (1 2 3)
```


### LSH
```zil
<LSH 4 1>  ;  8 
<LSH 4 -2>  ;  1
```


### M-HPOS
```zil
<PRINC "Hello"><M-HPOS .OUTCHAN>  ;  Hello5
```


### MAKE-GVAL
```zil
<SET FOO BAR>
<SETG BAR 123>
<MAKE-GVAL .FOO>  ;  ,BAR
<EVAL <MAKE-GVAL .FOO>>  ;  123
```


### MAPF
```zil
<MAPF ,VECTOR ,+ (1 2 3) [10 11 12]>  ;  [11 13 15]
<MAPF ,STRING 1
    ["Zil" "is" "lots of" "fun"]>  ;  "Zilf"
<MAPF ,VECTOR
    <FUNCTION (N) <* .N .N>> (1 2 3)>  ;  [1 4 9]
<DEFINE SETG-MANY ("TUPLE" TUP)
    <MAPF <>
    ,SETG
    .TUP
    <REST .TUP </ <LENGTH .TUP> 2>>>>
<SETG-MANY VAR-1 VAR-2 VAR-3 100 55 616>
,VAR-1  ;  100
,VAR-2  ;  55
,VAR-3  ;  616
<DEFINE LNUM (N)
  <MAPF ,LIST
    <FUNCTION ()
      <COND (<=? 0 <SET N <- .N 1>>> <MAPSTOP .N>)
                     (ELSE .N)>>>>
<LNUM 5>  ;  (4 3 2 1 0)
```


### MAPLEAVE
```zil
;  "Return first non-zero value in STRUC" 
<DEFINE FIRST-N0 (STRUC) 
  <MAPF <> <FUNCTION (X) 
    <COND (<N==? .X 0> <MAPLEAVE .X>)>> .STRUC>> 
<FIRST-N0 [0 0 0 "ZIL" 6 0]>  ;  "ZIL"
```


### MAPR
```zil
<SET FOO [1 2 3]> 
;  "Triple value of struct" 
<MAPR <> <FUNCTION (L) <1 .L <* <1 .L> 3>>> .FOO> 
.FOO  ;  [3 6 9]
```


### MAPRET
```zil
<SET FOO (65 66 67 68)>
<MAPF ,LIST
    #FUNCTION ((L)
    <MAPRET <ASCII .L>>) .FOO>  ;  (!\A !\B !\C !\D)
```


### MAPSTOP
```zil
<DEFINE FIRST-THREE (STRUC "AUX" (I 3))
    <MAPF ,LIST
    <FUNCTION (E)
        <COND (<0? <SET I <- .I 1>>> <MAPSTOP .E>)>
    .E> .STRUC>>
<FIRST-THREE "ABCDEFG">  ;  (!\A !\B !\C)
```


### MAX
```zil
<MAX 2 3 4 1>  ;  4
```


### MEMBER
```zil
<MEMBER "BC" "ABCD">  ;  "BCD"
<MEMBER 2 (1 2 3 4)>  ;  (2 3 4)
<MEMBER 0 (1 2 3 4)>  ;  #FALSE <>
```


### MEMQ
```zil
<MEMQ "BC" "ABCD">  ;  #FALSE <>
<MEMQ 2 (1 2 3 4)>  ;  (2 3 4)
<MEMQ 0 (1 2 3 4)>  ;  #FALSE <>
```


### MIN
```zil
<MIN 2 3 4 1>  ;  1
```


### MOBLIST
```zil
<INSERT "FOO" <MOBLIST NEW-OBLIST>>  ;  FOO!-NEW-OBLIST
FOO!-NEW-OBLIST  ;  "This can also be done with trailer"
```


### MSETG
```zil
<MSETG MSG-CANT-DO-THAT "You can't do that!">
...
<TELL ,MSG-CANT-DO-THAT CR>
```


### NEWTYPE
```zil
<NEWTYPE GARGLE CHARACTER>
<TYPEPRIM GARGLE>  ;  FIX
<SET A <CHTYPE 65 GARGLE>>
<TYPE .A>  ;  GARGLE
<PRIMTYPE .A>  ;  FIX

<NEWTYPE FIRSTNAME ATOM>
<NEWTYPE LASTNAME FIRSTNAME>
<=? ALFONSO #FIRSTNAME ALFONSO>  ;  #FALSE
<=? #FIRSTNAME MADISON #LASTNAME MADISON>  ;  #FALSE
<=? #LASTNAME MADISON #LASTNAME MADISON>  ;  T
<NEWTYPE 2FIXLIST LIST '!<LIST FIX FIX>>
#2FIXLIST (1 2)  ;  Ok
#2FIXLIST (1 2 3)  ;  Error
```


### NEXT
```zil
<DEFINE FIND-ASOC (ITEM)
  <REPEAT ((A <ASSOCIATIONS>))
    <COND (<=? .A <>> <RETURN <>>)>
    <COND (<==? .ITEM <ITEM .A>> <RETURN .A>)>
  <SET A <NEXT .A>>>>
<PUTPROP NEW-ASOC TEXT "Hello, world!">
<FIND-ASOC NEW-ASOC>  ;  #ASOC (NEW-ASOC TEXT "Hello, world!")
```


### NOT
```zil
<NOT <>>  ;  T
<NOT T>  ;  #FALSE <>
<NOT <=? 1 2>>  ;  T (Same as <N=? 1 2>
```


### NTH
```zil
<NTH <VECTOR "AB" "CD" "EF"> 2>  ;  "CD"
<2 <VECTOR "AB" "CD" "EF">>  ;  "CD"
```


### OBLIST?
```zil
<==? <OBLIST? STRING> <ROOT>>  ;  T   
<OBLIST? <ATOM "SPANK-NEW-ATOM">>  ;  #FALSE
<==? <OBLIST? FOO!-MY-OBLST> <MOBLIST MY-OBLST>>  ;  T
```


### OFFSET
```zil
<SETG OFF1 <OFFSET 1 '<VECTOR FIX>>>
<SETG OFF2 <OFFSET 2 '<VECTOR FIX CHARACTER>>>
<SETG OFF3 <OFFSET 3 '<VECTOR> 'STRING>>
<GET-DECL ,OFF2>  ;  <VECTOR FIX CHARACTER>
<SET V [1 !\A "BCD"]>
<OFF1 .V>  ;  1
<OFF3 .V>  ;  "BCD"
<OFF2 .V !\B>  ;  [1 !\B "BCD"]
<OFF1 .V !\A>  ;  ERROR
<2 .V 65>
<OFF2 .V>  ;  ERROR
```


### OPEN
```zil
;  "ZILF ver 0.9"
 <SET CH <OPEN "READ" "../zillib/parser.zil">>
 <SET BUFFER <ISTRING 1000>>
 <READSTRING .BUFFER .CH ";">  ;  124 ;"READ until first ;"
 <CLOSE .CH>
```


### OR
```zil
<OR <=? 1 2> <=? 1 1>>  ;  True 
 <OR <=? 1 1> <SET X 2>> ;  X is never set to 2 because first predicate evaluates to true 
 <SET X <OR 0 1 2 3>>  ;  X is set to 0 
 <SET X <OR <> 1 2 3>>  ;  X is set to 1
```


### ORB
```zil
<ORB 33 96>  ;  97
<ORB 33 96 64>  ;  97
```


### PACKAGE
```zil
;  "Define PACKAGE"
<REMOVE ANSWER>  ;  "Secure that ATOM not on any OBLIST"
<REMOVE DBL-ANSWER>
<REMOVE ROOT-ANSWER>
<REMOVE SECRET>
<PACKAGE "FOO">
<ENTRY ANSWER>
<SETG ANSWER 42>
<SETG SECRET 12345>
<RENTRY ROOT-ANSWER>
<SETG ROOT-ANSWER 21>
<ENDPACKAGE>
<TYPE? <GETPROP FOO!-PACKAGE OBLIST> OBLIST>  ;  OBLIST
<TYPE? <GETPROP IFOO!-FOO!-PACKAGE OBLIST> OBLIST>  ;  OBLIST
<GASSIGNED? ANSWER>  ;  #FALSE
<GASSIGNED? ANSWER!-FOO!-PACKAGE>  ;  T
<GASSIGNED? SECRET!-IFOO!-FOO!-PACKAGE>  ;  T
,ANSWER!-FOO!-PACKAGE  ;  42
,SECRET!-IFOO!-FOO!-PACKAGE  ;  12345
,ROOT-ANSWER  ;  21

;  "PACKAGEs can be defined additive"
<PACKAGE "FOO">
<SETG DBL-ANSWER <* ,ANSWER 2>>
<ENTRY DBL-ANSWER>
<ENDPACKAGE>
,ANSWER!-FOO!-PACKAGE  ;  42
,DBL-ANSWER!-FOO!-PACKAGE  ;  84

;  "USE adds external OBLIST to local OBLIST-path"
<REMOVE ANSWER>  ;  "Secure that ATOM not on any OBLIST"
<LENGTH .OBLIST>  ;  2
<USE "FOO">
<LENGTH .OBLIST>  ;  3
,ANSWER  ;  42
<GASSIGNED? SECRET>  ;  #FALSE
,SECRET!-IFOO  ;  12345
```


### PARSE
```zil
<PARSE "FOO">  ;  FOO
<PARSE "+">  ;  + 
<PARSE "+" 10 <GETPROP PACKAGE OBLIST>>  ;  +!-PACKAGE
<PARSE "23">  ;  23
<PARSE "(1 2 3)">  ;  (1 2 3)
<PARSE "<+ 12 34>">  ;  <+ 12 34>
<PARSE "%<+ 12 34>">  ;  46
<PARSE "<+ .A .B>" 10 <MOBLIST OB>>  ;  <+!-OB <LVAL!-OB A!-OB> <LVAL!-OB B!-OB>>
<PARSE " ">  ;  ERROR (No expression)
<PARSE "1 2 3">  ;  1 (Only 1st expression)
```


### PNAME
```zil
<PNAME FOO> ; "FOO"
<PNAME FOO!-NEW-OBLIST> ; "FOO"
<UNPARSE FOO!-NEW-OBLIST> ; "FOO!-NEW-OBLIST"
```


### PRIMTYPE
```zil
<PRIMTYPE !\A>  ;  FIX
<PRIMTYPE <+1 2>>  ;  FIX
<PRIMTYPE "ABC">  ;  STRING
```


### PRIN1
```zil
<PRIN1 !\A>  ;  !\A
<PRIN1 42>  ; 42
<PRIN1 "Hello, world!">  ;  "Hello, world!"
<PRIN1 (1 2 3)>  ;  (1 2 3)
<PRIN1 <+ 1 2>>  ;  3
```


### PRINC
```zil
<PRINC !\A>  ;  !\A
<PRINC 42>  ; 42
<PRINC "Hello, world!">  ;  "Hello, world!"
<PRINC (1 2 3)>  ;  (1 2 3)
<PRINC <+ 1 2>>  ;  3
```


### PRINT
```zil
<PRINT !\A>  ;  !\A<space>
<PRINT 42>  ; 42<space>
<PRINT "Hello, world!">  ;  "Hello, world!"<space>
<PRINT (1 2 3)>  ;  (1 2 3)<space>
<PRINT <+ 1 2>>  ;  3<space>
```


### PRINT-MANY
```zil
<PRINT-MANY .OUTCHAN PRINC "Hello" !\! PRMANY-CRLF>  ;  Hello!\n
<PRINT-MANY .OUTCHAN PRIN1 "string" !\c PRMANY-CRLF>  ;  "string"!\c\n
```


### PRINTTYPE
```zil
<DEFINE ROMAN-PRINT (ROMAN "AUX" (RNUM <CHTYPE .ROMAN FIX>))
<COND (<OR <L=? .RNUM 0> <G? .RNUM 3999>>
     <PRINC <CHTYPE .NUMB TIME>>)
    (T
        <RCPRINT </ .RNUM 1000> '![!\M]>
        <RCPRINT </ .RNUM 100>  '![!\C !\D !\M]>
        <RCPRINT </ .RNUM 10>   '![!\X !\L !\C]>
        <RCPRINT    .RNUM       '![!\I !\V !\X]>)>>
<DEFINE RCPRINT (MODN V)
<SET MODN <MOD .MODN 10>>
<COND (<==? 0 .MODN>)
        (<==? 1 .MODN> <PRINC <1 .V>>)
        (<==? 2 .MODN> <PRINC <1 .V>> <PRINC <1 .V>>)
        (<==? 3 .MODN> <PRINC <1 .V>> <PRINC <1 .V>>
                                                                      <PRINC <1 .V>>)
        (<==? 4 .MODN> <PRINC <1 .V>> <PRINC <2 .V>>)
        (<==? 5 .MODN> <PRINC <2 .V>>)
        (<==? 6 .MODN> <PRINC <2 .V>> <PRINC <1 .V>>)
        (<==? 7 .MODN> <PRINC <2 .V>> <PRINC <1 .V>>
                                                                      <PRINC <1 .V>>)
        (<==? 8 .MODN> <PRINC <2 .V>> <PRINC <1 .V>>
                                       <PRINC <1 .V>> <PRINC <1 .V>>) 
        (<==? 9 .MODN> <PRINC <1 .V>> <PRINC <3 .V>>)>> 
<NEWTYPE ROMAN FIX>
<PRINTTYPE ROMAN ,ROMAN-PRINT>
<==? <PRINTTYPE ROMAN> ,ROMAN-PRINT>
 #ROMAN 1984  ;  MCMLXXXIV

<NEWTYPE ROMAN2 FIX>
<PRINTTYPE ROMAN2 ROMAN>  ;  "Copies active handler, if exists"
#ROMAN2 2020  ;  MMXX

<PRINTTYPE ROMAN FIX>
<=? <PRINTTYPE ROMAN> <>>  ;  T
#ROMAN 2020  ;  2020
;  "Change in ROMAN doesn’t affect ROMAN2"

#ROMAN2 2020  ;  MMXX
<PRINTTYPE FIX ,ROMAN-PRINT>  ;  "Works on built-in too!"
23  ;  XXIII
<PRINTTYPE FORM <FUNCTION (F) <PRIN1 <CHTYPE .F LIST>>>>
<FORM + 1 2>  ;  (+ I II)
```


### PROG
```zil
<PROG ((X 1)) #DECL ((X) FIX)  
    <PROG ((X 2)) <PRIN1 .X>> <PRIN1 .X>>  ;  "21" 
<DEFINE TEST-PROG-AS-REPEAT ()
    <PRINC "START ">
    <PROG ((X 0))
        <SET X <+ .X 1>>
        <PRIN1 .X>
        <COND (<=? .X 3> <RETURN>)>  ;  "--> exit block"
        <AGAIN>  ;  "--> repeat"
    >
    <PRINC " END">
>
    <TEST-PROG-AS-REPEAT>  ;  "START 123 END"
```


### PROPDEF
```zil
;  "Ordinary property"
<PROPDEF HEIGHT 72>
<OBJECT OBJ1>
<OBJECT OBJ2 (HEIGHT 80)>

;  "Implies, inside routine"
<GETP ,OBJ1 ,P?HEIGHT>  ;  72
<GETP ,OBJ2 ,P?HEIGHT>  ;  80

;  "Basic pattern"
<PROPDEF HEIGHT <>
    (HEIGHT FEET:FIX FOOT INCHES:FIX = 2 <WORD .FEET>
        <BYTE .INCHES>)
    (HEIGHT FEET:FIX FT INCHES:FIX = 2 <WORD .FEET>
        <BYTE .INCHES>)>
<OBJECT GIANT (HEIGHT 10 FT 8)>

;  "Implies, inside routine"
<=? <GET <GETPT ,GIANT ,P?HEIGHT> 0> 10>
<=? <GETB <GETPT ,GIANT ,P?HEIGHT> 2> 8>

;  "Basic pattern with OPT"
<PROPDEF HEIGHT <> (HEIGHT FEET:FIX FT "OPT" INCHES:FIX =
    <WORD .FEET> <BYTE .INCHES>)>
<OBJECT GIANT1 (HEIGHT 100 FT)>
<OBJECT GIANT2 (HEIGHT 50 FT 11)>

;  "Implies, inside routine"
<=? <PTSIZE <GETPT ,GIANT1 ,P?HEIGHT>> 3>
<=? <GET <GETPT ,GIANT1 ,P?HEIGHT> 0> 100>
<=? <GETB <GETPT ,GIANT1 ,P?HEIGHT> 2> 0>
<=? <PTSIZE <GETPT ,GIANT2 ,P?HEIGHT>> 3>
<=? <GET <GETPT ,GIANT2 ,P?HEIGHT> 0> 50>
<=? <GETB <GETPT ,GIANT2 ,P?HEIGHT> 2> 11>

;"Basic pattern with MANY"
<PROPDEF TRANSLATE <> (TRANSLATE "MANY" A:ATOM N:FIX =
    "MANY" <VOC .A BUZZ> <WORD .N>)>
<OBJECT NUMBERS (TRANSLATE ONE 1 TWO 2)>

;"Implies, inside routine"
<=? <PTSIZE <GETPT ,NUMBERS ,P?TRANSLATE>> 8>
<=? <GET <GETPT ,NUMBERS ,P?TRANSLATE> 0> ,W?ONE>
<=? <GET <GETPT ,NUMBERS ,P?TRANSLATE> 1> 1>
<=? <GET <GETPT ,NUMBERS ,P?TRANSLATE> 2> ,W?TWO>
<=? <GET <GETPT ,NUMBERS ,P?TRANSLATE> 3> 2>

;  "Pattern with constants"
<PROPDEF HEIGHT <> (HEIGHT FEET:FIX FT INCHES:FIX =
    (HEIGHTSIZE 3) (H-FEET <WORD .FEET>)
    (H-INCHES <BYTE .INCHES>))>
<=? ,HEIGHTSIZE 3>
<=? ,H-FEET 0>
<=? ,H-INCHES 2>

;  "DIR sets pattern for all DIRECTIONS"
<PROPDEF DIRECTIONS <> (DIR GOES TO R:ROOM =
    (MY-UEXIT 3) <WORD 0> (MY-REXIT <ROOM .R>))>
<DIRECTIONS NORTH SOUTH>
<OBJECT HOUSE (SOUTH GOES TO WOODS)>
<OBJECT WOODS (NORTH GOES TO HOUSE)>

;  "Implies, inside routine"
<=? <PTSIZE <GETPT ,HOUSE ,P?SOUTH>> ,MY-UEXIT>
<=? <GETB <GETPT ,HOUSE ,P?SOUTH> ,MY-REXIT> ,WOODS>

;  "DIR sets implicit DIRECTIONS"
<PROPDEF DIRECTIONS <> (DIR GOES TO R:ROOM =
    (MY-UEXIT 3) <WORD 0> (MY-REXIT <ROOM .R>))>
<DIRECTIONS NORTH SOUTH>
<OBJECT HOUSE (EAST GOES TO WOODS)>
<OBJECT WOODS (WEST GOES TO HOUSE)>

;  "Implies, inside routine"
<=? <PTSIZE <GETPT ,HOUSE ,P?EAST>> ,MY-UEXIT>
<=? <GETB <GETPT ,HOUSE ,P?EAST> ,MY-REXIT> ,WOODS>
<BAND <GETB ,W?EAST 4> ,PS?DIRECTION>

;  "VOC in pattern adds word to vocabulary"
<PROPDEF FOO <> (FOO A:ATOM = <VOC .A PREP>)>
<OBJECT BAR (FOO FOO)>

;  "Implies, inside routine"
<=? <GETP ,BAR ,P?FOO> ,W?FOO>

;  "Complex PROPDEF (DIRECTIONS from Zork Zero)"
<PROPDEF DIRECTIONS <>
    (DIR TO R:ROOM = (UEXIT 1) (REXIT <ROOM .R>))
    (DIR S:STRING = (NEXIT 2) (NEXITSTR <STRING .S>))
    (DIR SORRY S:STRING = (NEXIT 2) (NEXITSTR <STRING .S>))
    (DIR PER F:FCN = (FEXIT 3)
        (FEXITFCN <WORD .F>) <BYTE 0>)
    (DIR TO R:ROOM IF F:GLOBAL "OPT" ELSE S:STRING =
        (CEXIT 4) (REXIT <ROOM .R>) (CEXITFLAG <GLOBAL .F>)
        (CEXITSTR <STRING .S>))
    (DIR TO R:ROOM IF O:OBJECT IS OPEN "OPT" ELSE S:STRING =
        (DEXIT 5) (DEXITOBJ <OBJECT .O>)
        (DEXITSTR <STRING .S>) (DEXITRM <ROOM .R>))>
```


### PTABLE
```zil
<PTABLE 1 2 3 4>
```


### PUT-DECL
```zil
<DECL? T BOOLEAN>  ;  Error 
<PUT-DECL BOOLEAN '<OR ATOM FALSE>>
<DECL? T BOOLEAN>  ;  T
<DECL? "Hi" BOOLEAN>  ;  #FALSE
```


### PUTPROP
```zil
<SET L (1 2 3)>
<PUTPROP .L FOO "Hello">  ;  (1 2 3)
<GETPROP .L FOO>  ;  "Hello"
<PUTPROP .L FOO>  ;  "Hello"
<GETPROP .L FOO>  ;  #FALSE

;  "PROPSPEC, loop through all words and add to buzz"
<VERSION XZIP>
<OBJECT FOO
    (ADJECTIVE SMALL CURIOUS)
    (MYBUZZ "ABCD" "BAR" "BAZ")>
<DEFINE MYBUZZ-PROP (L)
    <SET L <REST .L>>  ;  "Ignore MYBUZZ in LIST"
    <MAPF ,LIST <FUNCTION (W) <VOC .W BUZZ>> .L>>
<PUTPROP MYBUZZ PROPSPEC MYBUZZ-PROP>
<ROUTINE GO () <TEST-PROPSPEC>>
<ROUTINE TEST-PROPSPEC ("AUX" W)
    <TELL "Part-of-Speech, 4 = BUZZ" CR>
    <SET W W?ABCD>
    <TELL "ABCD = " N <GETB .W 6> CR>
    <SET W W?BAR>
    <TELL "BAR = " N <GETB .W 6> CR>
    <SET W W?BAZ>
    <TELL "BAZ = " N <GETB .W 6> CR>>
```


### PUTREST
```zil
<PUTREST (1 2 3) (A B)>  ;  (1 A B)

<SET L1 [<SET L2 (1 2 3)>]>
<PUTREST .L2 (A B)>
.L1 ;  [(1 A B)]

<SET L1 [1 2 3]>
<SET L2 <PUTREST (!.L1) (A B)>>
.L1  ;  [1 2 3]
.L2  ;  (1 A B)

<SET L1 (1 2 3 4 5 6 7 8 9)>
<PUTREST <REST .L1 3> <REST .L1 7>>
.L1  ;  (1 2 3 4 8 9)
```


### QUIT
```zil
<QUIT>
```


### QUOTE
```zil
<SET F <QUOTE <+ 1 2>> ; Or <SET F '<+ 1 2>>
.F  ;  <+ 1 2>
<EVAL .F>  ;  3
'%<+ 1 2>  ;  3
```


### READSTRING
```zil
;"ZILF ver 0.9"
<SET CH <OPEN "READ" "../zillib/parser.zil">> 
<SET BUFFER <ISTRING 10>>
<READSTRING .BUFFER .CH>  ;  10
<LVAL BUFFER>  ;  "\"Library h"
<READSTRING .BUFFER .CH 6>  ;  6
<LVAL BUFFER>  ;  "eader\"ry h"
<READSTRING .BUFFER .CH "ZIL">  ;  10
<LVAL BUFFER>  ;  "\n\n<SETG "
<CLOSE .CH>  ;  "\n = CR+LF"
```


### RENTRY
```zil
<REMOVE ANSWER>  ;  "Secure that ATOM not on any OBLIST"
<PACKAGE "FOO"> 
<SETG ANSWER 42> 
<RENTRY ANSWER> 
<ENDPACKAGE> 
,ANSWER  ;  42 ;”Accessible without previous USE”
```


### REPEAT
```zil
<REPEAT ((X 1)) #DECL ((X) FIX)  
    <REPEAT ((X 2)) <PRIN1 .X> <RETURN>>  
    <PRIN1 .X> <RETURN>>  ;  "21"
<DEFINE TEST-REPEAT () 
    <PRINC "START "> 
    <REPEAT ((X 0)) 
        <SET X <+ .X 1>> 
        <PRIN1 .X> 
        <COND (<=? .X 3> <RETURN>)>  ;  "--> exit block" 
    > 
    <PRINC " END"> 
> 
    <TEST-REPEAT>  ;  "START 123 END"
```


### REPLACE-DEFINITION
```zil
<REPLACE-DEFINITION MY-ROUTINE 
     <ROUTINE MY-ROUTINE ()  
        <TELL "Replaced version of MY-ROUTINE" CR> 
    > 
> 
<DEFAULT-DEFINITION MY-ROUTINE 
    <ROUTINE MY-ROUTINE ()  
        <TELL "Original version of MY-ROUTINE" CR> 
    > 
> 
<MY-ROUTINE>  ;  "Replaced version of MY-ROUTINE"
```


### REST
```zil
<SETG STRUCT1 [1 2 3 4]>  ;  STRUCT1 = [1 2 3 4]
<SETG STRUCT2 <REST ,STRUCT1>>  ;  STRUCT2 = [2 3 4]
<PUT ,STRUCT2 1 5>  ;  STRUCT1 = [1 5 3 4], STRUCT2 = [5 3 4]
```


### RETURN
```zil
<PROG () <RETURN>>  ;  T
<PROG ACT ()
    <PROG () <RETURN 42 .ACT>>
<RETURN 43>> ;"Never reached"  -->  42
```


### ROOM
```zil
<ROOM INSIDE-HOUSE
    (DESC "Inside House")
    (IN ROOMS)
    (LDESC
"You are standing inside the rotting house. The house is
  sparsely furnished, in fact not at all. On one wall is
  positioned a sign. Beside the sign is a button, and an open
  trap-door is placed on the floor. The exit is west
  and there is a walk-in closet in the eastern wall.")
(UP "You have yet to master the art of flying.")
(EAST TO CLOSET)
(WEST TO OUTSIDE-HOUSE IF FRONT-DOOR-FLAG ELSE ,MSG-025)
(DOWN PER TRAP-DOOR-F)
(ACTION INSIDE-HOUSE-F)
(FLAGS LIGHTBIT NDUNGEONBIT)
(THINGS (<>) (BUTTON) LIGHTBUTTON-F
                 (<>) (SIGN) HOUSE-SIGN-F
                 (<>) (HOUSE FLOOR CLOSET KEYHOLE) STANDARD-F)
(GLOBAL FRONT-DOOR)>
```


### ROOT
```zil
<ROOT>
```


### ROUTINE
```zil
;"Move all child objects from object src to object dst" 
    <ROUTINE MOVE-INVENTORY (SRC DST "AUX" X N) 
        <SET X <FIRST? .SRC>> 
        <REPEAT () 
            <COND (.X 
                <SET N <NEXT? .X>> 
                <MOVE .X .DST> 
                <SET X .N>) 
            (T <RETURN>)>>>
```


### ROUTINE-FLAGS
```zil
<FILE-FLAGS CLEAN-STACK?>
```


### SET
```zil
MDL: <PROG (X) <SET X 5> <RETURN .X>>  ;  Returns 5 after setting X.
Zapf: <SET MYVAR 42>  ;  Store 42 in local variable MYVAR
```


### SET-DEFSTRUCT-FILE-DEFAULTS
```zil
<SET-DEFSTRUCT-FILE-DEFAULTS ('NTH GETB) ('PUT PUTB)
    ('START-OFFSET 0) 'NODECL ('INIT-ARGS (BYTE))>
<DEFSTRUCT B-TBL TABLE (B-TBL-X FIX 65) (B-TBL-Y FIX 111)>
<MAKE-B-TBL>  ;  #B-TBL %<TABLE (BYTE) 65 111>
<B-TBL-Y <MAKE-B-TBL>>  ;  111
```


### SETG
```zil
MDL/Zapf: <SETG MYVAR 42>  ;  Store 42 in global atom MYVAR
```


### SETG20
```zil
<SETG20 MYVAR 42> ; Store 42 in global atom MYVAR
```


### SORT
```zil
<SORT <> [3 4 2 1]>  ;  [1 2 3 4]
<SET V [1 MONEY 2 SHOW 3 READY 4 GO]>
<SORT <> .V 2 1>  ;  [4 GO 1 MONEY 3 READY 2 SHOW]
<SORT ,L? .V 2>  ;  [4 GO 3 READY 2 SHOW 1 MONEY]
<SET V [1 MONEY 2 SHOW 3 READY 4 GO]>
<SORT <> [5 1 6 3 7 2 8 4] 1 0 .V 1>
.V  ;  [MONEY READY SHOW GO 1 2 3 4]
```


### SPNAME
```zil
<SPNAME atom>
```


### STRING
```zil
<STRING !\A <ASCII 66> "CD"> ; "ABCD"
```


### STRUCTURED?
```zil
<STRUCTURED? <LIST 1 2 3>>  ;  T
<STRUCTURED? <TABLE 1 2 3>>  ;  #FALSE
```


### SUBSTRUC
```zil
<SUBSTRUC "ABCD" 1 2>

<SETG STR1 "EEEEEE">  ;  "BC"
<SUBSTRUC "ABCD" 1 2 ,STR1>  ;  STR1 = "BCEEEEEE"
```


### SUPPRESS-WARNINGS?
```zil
;  "Examples must be compiled with -w, otherwise warnings is always suppressed."

;  "Compiles with warnings"
<SUPPRESS-WARNINGS? NONE>
<GLOBAL X 5>
<ROUTINE GO () <TELL N .X>>

;  "Compiles with suppressed warnings"
<SUPPRESS-WARNINGS? ALL>
<GLOBAL X 5>
<ROUTINE GO () <TELL N .X>>

;  "Compiles with suppressed warnings"
<SUPPRESS-WARNINGS? "ZIL0204">
<GLOBAL X 5>
<ROUTINE GO () <TELL N .X>>
```


### TABLE
```zil
<TABLE 1 2 3 4>
|  Element 0 WORD | Element 1 WORD | Element 2 WORD | Element 3 WORD |
| --- | --- | --- | --- |
| 1 | 2 | 3 | 4 |

<TABLE (BYTE LENGTH) 1 2 3 4>
|  Element 0 BYTE | Element 1 BYTE | Element 2 BYTE | Element 3 BYTE | Element 4 BYTE |
| --- | --- | --- | --- |
| 4 | 1 | 2 | 3 | 4 |
```


### TELL-TOKENS
```zil
<TELL-TOKENS
(CR CRLF)  <CRLF>
(N NUM) *  <PRINTN .X>
(C CHAR CHR) * <PRINTC .X>
(D DESC) * <PRINTD .X>
(A AN) *  <PRINTA .X>
THE *  <THE-PRINT .X>
CTHE *  <CTHE-PRINT .X>
THEO   <THE-PRINT>
CTHEO  <CTHE-PRINT>
CTHEI  <CTHEI-PRINT>
THEI   <THEI-PRINT>>
```


### TIME
```zil
<TIME>
```


### TOP
```zil
<SETG STRUCT1 [1 2 3 4 5]>  ;  STRUCT1 = [1 2 3 4 5]
<SETG STRUCT2 <REST ,STRUCT1 2>>  ;  STRUCT2 = [3 4 5]
<TOP ,STRUCT2>  ;  STRUCT2 = [1 2 3 4 5]
```


### TUPLE
```zil
<DEFINE MY+ ("TUPLE" T)
<REPEAT ((M 0))
<COND (<EMPTY? .T> <RETURN .M>)>
<SET M <+ .M <1 .T>>>
<SET T <REST .T>>
> 
>
<MY+ 1 2 3>  ;  6
<MY+ 4 5>  ;  9
<TYPE <TUPLE 1 2 3>>  ;  VECTOR (in ZILF!), TUPLE (in MDL)
```


### TYPE
```zil
<TYPE !\A>  ;  CHARACTER
<TYPE <+1 2>>  ;  FIX
<TYPE #BYTE 42>  ;  BYTE
```


### TYPE?
```zil
<TYPE? !\A CHARACTER FIX>  ;  CHARACTER
<TYPE? <+1 2> CHARACTER FIX>  ;  FIX
<TYPE? #BYTE 42 CHARACTER FIX>  ;  #FALSE ()
```


### TYPEPRIM
```zil
<TYPEPRIM CHARACTER>  ;  FIX
<TYPEPRIM FORM>  ;  LIST
<TYPEPRIM BYTE>  ;  FIX
```


### UNASSIGN
```zil
<SET X 1>
<ASSIGNED? X>  ;  True
<UNASSIGN X>
<ASSIGNED? X>  ;  False
```


### UNPARSE
```zil
<UNPARSE 123>  ;  "123"
<UNPARSE <+ 1 2>>  ;  "3"
<UNPARSE FOO>  ;  "FOO"
<UNPARSE <ATOM "FOO">>  ;  "FOO!-#FALSE ()"
<PNAME <ATOM "FOO">>  ;  "FOO"
```


### USE
```zil
<USE "FOOFOO">  ;  "Searches for file "foofoo.zil" which contains the definition for <PACKAGE "FOOFOO"> ..."
```


### VALID-TYPE?
```zil
<VALID-TYPE? VECTOR>  ;  VECTOR
<VALID-TYPE? FOO>  ;  #FALSE
<NEWTYPE FOO FIX> 
<VALID-TYPE? FOO>  ;  FOO
```


### VALUE
```zil
;  MDL
<SETG X 3>
<SET X 4>
<VALUE X>  ;  4
<UNASSIGN X>
<VALUE X>  ;  3

;  Zapf
<VALUE X>  ;  Loads local or global variable X. Recommended to use LVAL or GVAL instead (.X or ,X)
```


## Z-Code Built-ins

### BACK
```zil
<GLOBAL TBL1 <TABLE 1 2 3 4>>  ;  TBL1 = [1 2 3 4]
<GLOBAL TBL2 <REST ,STRUCT1 4>>  ;  TBL2 = [3 4] Move 4 because WORD-table!
<SETG TBL2 <BACK ,TBL2 2>>  ;  TBL2 = [2 3 4]
```


### BCOM
```zil
<BCOM #2 000011110001111>  ;  #2 1111000011110000
```


### BTST
```zil
<BTST 64 64>  ;  TRUE
<BTST 64 63>  ;  FALSE
<BTST 97 33>  ;  TRUE
```


### BUFOUT
```zil
<BUFOUT <>>  ;  Turns off buffering(disables word-wrap)
<BUFOUT T>  ;  Turns on buffering
```


### CATCH
```zil
<SETG CATCH-POINT <CATCH>>  ;  Saves the current stack fram in global variable.
```


### ERASE
```zil
<ERASE 1>  ;  Clears from cursor to end of line
```


### F?
```zil
<F? <=? 1 1>>  ;  False
<F? <=? 1 2>>  ;  True
```


### FCLEAR
```zil
<FCLEAR ,TRAP-DOOR ,OPENBIT>  ;  Marks the trap-door as closed
```


### FIRST?
```zil
<SET RM <FIRST? ,ROOMS>>  ;  Sets RM to first object in ROOMS. Also evaluates to true (all values not 0 is true)
```


### FONT
```zil
<FONT 4>  ;  Sets fixed-pitch font. In versions 3-4, this is done by setting bit 1 of Flags 2 in header <PUT 0 8 <BOR <GET 0 8> 2>>
```


### FSET
```zil
<FSET ,TRAP-DOOR ,OPENBIT> --> Marks the trap-door as open
```


### FSET?
```zil
<FSET? ,TRAP-DOOR ,OPENBIT>  ;  True if OPENBIT is set
```


### GET
```zil
<GET <TABLE 0 1 2 3> 2>  ;  2
```


### GETB
```zil
<GETB <TABLE (BYTE) !\A !\B !\C !\D> 2>  ;  !\C
```


### GETP
```zil
<OBJECT MYOBJ (MYPROP 123)>
<GETP ,MYOBJ ,P?MYPROP>  ;  123
```


### GETPT
```zil
<OBJECT MYOBJ (MYPROP 123)>
<GET <GETPT ,MYOBJ ,P?MYPROP> 0>  ;  123
<GETPT ,MYOBJ ,P?MYPROP2>  ;  0
```


### IN?
```zil
<OBJECT ANIMAL>
<OBJECT CAT (LOC ANIMAL)>
<IN? ,CAT ,ANIMAL>  ;  T
<IN? ,ANIMAL ,CAT>  ;  <>
```


### INC
```zil
<GLOBAL X 5>
<INC ,X>  ;  X = 6
```


### INPUT
```zil
<INPUT 1>  ;  Wait for keypress

<ROUTINE WAIT-TWO-SECONDS ()
    <INPUT 1 20 ABORT-WAIT>
> 
 
<ROUTINE ABORT-WAIT () <RETURN T>>
 
;  Pause two seconds (if not interrupted by a keypress from the keyboard
<WAIT-TWO-SECONDS>
```


### INTBL?
```zil
<T <INTBL? 3 <TABLE 1 2 3 4> 4>>  ;  T
<T <INTBL? 6 <TABLE 1 2 3 4> 4>>  ;  #FALSE

;  "Search byte-table with record length 3 (ver 5, 7-)"
<T <INTBL? 8 <TABLE (BYTE) 2 0 1 4 0 1 8 0 1> 9 3>>  ;  T
<T <INTBL? 1 <TABLE (BYTE) 2 0 1 4 0 1 8 0 1> 9 3>>  ;  <>

;  "Search word-table with record length 3 (ver 5, 7-)"
<T <INTBL? 8 <TABLE 2 0 1 4 0 1 8 0 1> 9 131>>  ;  T
<T <INTBL? 1 <TABLE 2 0 1 4 0 1 8 0 1> 9 131>>  ;  <>
```


### IRESTORE
```zil
<IRESTORE>
```


### ISAVE
```zil
<ISAVE>
```


### LEX
```zil
<GLOBAL TEXTBUF <TABLE (BYTE) !\c !\a !\t>>
<GLOBAL PARSEBUF <ITABLE 1 (LEXV) 0 0>>
<OBJECT CAT (SYNONYM CAT)>
<LEX ,TEXTBUF ,PARSEBUF>
<PRINTB <GET ,PARSEBUF 1>>  ;  "cat"
```


### LOC
```zil
<OBJECT ANIMAL>
<OBJECT CAT (LOC ANIMAL)>

<=? <LOC ,CAT> ,ANIMAL>  ;  T
<LOC ,ANIMAL>  ;  0
```


### LOWCORE
```zil
;  Monospace bit (bit 1) in flags 2 is set
<LOWCORE FLAGS <BOR <LOWCORE FLAGS> 2>>

;  Do the same as above
<PUT 0 8 <BOR <GET 0 8> 2>>
;  Now print the 11 lower bytes in releaseid
<PRINTN <BAND <LOWCORE RELEASEID> *3777*>>
```


### LOWCORE-TABLE
```zil
;  Reads 6 bytes from SERIAL and print each byte as character 
<LOWCORE-TABLE SERIAL 6 PRINTC>
```


### LVAL
```zil
<SET X 5> 
<LVAL X>  ;  5
.X  ;  5
```


### MAP-CONTENTS
```zil
<OBJECT SURVIVAL-KIT
(DESC "adventure survival kit") (WEIGHT 10)>
<OBJECT SWORD
(IN SURVIVAL-KIT) (DESC "sword") (WEIGHT 10)>
<OBJECT LAMP
 (IN SURVIVAL-KIT) (DESC "brass lamp") (WEIGHT 5)>
<OBJECT SPOON
 (IN SURVIVAL-KIT) (DESC "chrome spoon") (WEIGHT 2)>

<ROUTINE TEST-MAP-CONTENTS ()
    <TELL "Your " D ,SURVIVAL-KIT " contains:" CR>
    <MAP-CONTENTS (F ,SURVIVAL-KIT)
        <TELL "    a " D .F CR>
    >

    <TELL "Your " D ,SURVIVAL-KIT " contains:" CR>
    <MAP-CONTENTS (F N ,SURVIVAL-KIT)
        <TELL "    a " D .F >
        <COND (.N <TELL " (next item is the " D .N ")">)>
        <TELL CR>
    >

    <BIND ((W 0))
        <SET W <GETP ,SURVIVAL-KIT ,P?WEIGHT>>
        <MAP-CONTENTS (F ,SURVIVAL-KIT)
            (END <TELL "Total weight is = " N .W CR>)
            <SET W <+ .W <GETP .F ,P?WEIGHT>>>
        >
    >
>

<TEST-MAP-CONTENTS>
;  Your adventure survival kit contains: 
;      a sword
;      a chrome spoon
;      a brass lamp
;  Your adventure survival kit contains:
;          a sword (next item is the chrome spoon)
;          a chrome spoon (next item is the brass lamp)
;          a brass lamp
;  Total weight is = 27
```


### MAP-DIRECTIONS
```zil
<DIRECTIONS NORTH SOUTH EAST WEST>
 <OBJECT CENTER (DESC "center room")
      (NORTH TO N-ROOM)
      (WEST TO W-ROOM)>
 <OBJECT N-ROOM (DESC "north room")>
 <OBJECT W-ROOM (DESC "west room")>

 <ROUTINE TEST-MAP-DIRECTIONS ()
      <TELL "You're in the " D ,CENTER>
  <TELL CR "Obvious exits:" CR>
      <MAP-DIRECTIONS (D P ,CENTER)
          (END <TELL "Room description done." CR>)
          <COND (<EQUAL? .D ,P?NORTH> <TELL "    North">)
                 (<EQUAL? .D ,P?SOUTH> <TELL "    South">)
                 (<EQUAL? .D ,P?EAST> <TELL "    East">)
                 (<EQUAL? .D ,P?WEST> <TELL "    West">)
          >
          <VERSION?
              (ZIP <TELL " to the " D <GETB .P ,REXIT> CR>)
              (ELSE <TELL " to the " D <GET .P ,REXIT> CR>)
          >
      >
 >
```


### MARGIN
```zil
<MARGIN 1 1>  ;  set 1 pixel margin in window 0
```


### MENU
```zil
;  Example from Journey
<GLOBAL MAC-SPECIAL-MENU 
    <LTABLE <TABLE (STRING LENGTH) "Journey"> 
        <TABLE (STRING LENGTH) "Essences"> 
        <TABLE (STRING LENGTH) "No Defaults">>> 
... 
<MENU 3 ,MAC-SPECIAL-MENU>
```


### MOD
```zil
<MOD 15 4>  ;  3
<MOD -15 4>  ;  -3
<MOD -15 -4>  ;  -3
<MOD 15 -4>  ;  3
```


### PICINF
```zil
<GLOBAL MYPIC <ITABLE 2048 0>>
<PICINFO 1 ,MYPIC>  ;  Writes picture data into MYPIC
```


### PICSET
```zil
; From Zork Zero
<PICSET ,B-PICSET-TBL>
```


### POP
```zil
<PUSH .FOO>
<SET FOO some-new-value>
;code
<SET FOO <POP>>
```


### PTSIZE
```zil
<OBJECT MYOBJECT (FOO 1 2 3)>
<PTSIZE <GETPT ,MYOBJECT ,P?FOO>>  ;  6
```


### PUSH
```zil
<PUSH 123>
```


### PUT
```zil
<PUT ,MYTABLE 1 123>  ;  Stores 123 at position 1 in MYTABLE
<PUT 0 8 <BOR <GET 0 8> 2>>  ;  Sets bit 1 in Flags 2 in header (force monospace)
```


### PUTB
```zil
<PUTB ,MYTABLE 1 !\A>  ;  Stores character A at position 1 in MYTABLE
```


### PUTP
```zil
<OBJECT MYOBJ (MYPROP 123)>
<PUTP ,MYOBJ ,P?MYPROP 456>  ;  Stores 456 in property MYPROP on MYOBJ
```


### QUIT
```zil
<QUIT>
```


### RANDOM
```zil
<- <RANDOM 101> 1>  ;  Generates random number between 0-100
```


### REMOVE
```zil
<OBJECT ANIMAL>
<OBJECT CAT (LOC ANIMAL)>
<REMOVE ,CAT)  ;  Detach CAT from ANIMAL
```


### RFALSE
```zil
<RFALSE>
```


### RFATAL
```zil
<RFATAL>
```


### RSTACK
```zil
<PUSH 42>
<RSTACK>  ;  Returns 42
```


### RTRUE
```zil
<RTRUE>
```


### SAVE
```zil
;  Versions 1-4
<SAVE>

;  Version 5-
;  From Zork Zero
<ROUTINE SOFT-SAVE-DEFS ()
    <CLEAR 0>
    <SCREEN 0>
    <COND (<NOT <SAVE ,FKEY-TBL
                             ,FKEYS-STRTABLE-LEN
                             ,DEFS-NAME>>
                    <TELL "Failed.">)>
    <CLEAR 0>
    <SCREEN ,SOFT-WINDOW>
    <RFALSE>>

<ROUTINE SOFT-RESTORE-DEFS ()
    <CLEAR 0>
    <SCREEN 0>
    <COND (<NOT <RESTORE ,FKEY-TBL ,FKEYS-STRTABLE-LEN ,DEFS-NAME>>
                    <TELL "Failed.">)>
    <CLEAR 0>
    <SCREEN ,SOFT-WINDOW>
    <RFALSE>>
```


### SCREEN
```zil
<SPLIT 3>
<SCREEN 1>
<TELL "West of House">  ;  Split screen in 2 (upper screen is 3 rows) 
                                               ;  and write "West of House" in upper screen
```


### SCROLL
```zil
;  From Arthur
<SETG GL-AUTHOR-SIZE <RT-COUNT-LINES ,K-DIROUT-TBL>>
<SET AY <* ,GL-AUTHOR-SIZE ,GL-FONT-Y>>
<SCROLL 0 .AY>
```


### SET
```zil
MDL: <PROG (X) <SET X 5> <RETURN .X>>  ;  Returns 5 after setting X.
Zapf: <SET MYVAR 42>  ;  Store 42 in local variable MYVAR
```


### SETG
```zil
MDL/Zapf: <SETG MYVAR 42>  ;  Store 42 in global atom MYVAR
```


### SOUND
```zil
;  From Sherlock
<ROUTINE RT-S-CAB-ARRIVES ()
    <COND (<==? ,CAB-RAMP 0>
        <SOUND ,S-HORSE ,S-START 4>)
        (T
        <SETG CAB-RAMP <- ,CAB-RAMP 1>>
        <SOUND ,S-HORSE ,S-START <- 2 ,CAB-RAMP> 1 RT-S-CAB-ARRIVES>)>>
```


### SPLIT
```zil
<SPLIT 3>
<SCREEN 1>
<TELL "West of House">  ;  Split screen in 2 (upper screen is 3 rows) 
                                               ;  and write "West of House" in upper screen
```


### THROW
```zil
<ROUTINE TEST-CATCH ("AUX" X)
    <SET X <CATCH>>
    <THROWER .X>
    123
>

<ROUTINE THROWER (F)
    <THROW 456 .F>
>

<TEST-CATCH>  ;  456
```


### USL
```zil
<USL>
```


### VALUE
```zil
;  MDL
<SETG X 3>
<SET X 4>
<VALUE X>  ;  4
<UNASSIGN X>
<VALUE X>  ;  3

;  Zapf
<VALUE X>  ;  Loads local or global variable X. Recommended to use LVAL or GVAL instead (.X or ,X)
```


### VERIFY
```zil
<VERIFY>
```


### WINGET
```zil
;  From Shogun
<ROUTINE GO
    <CLEAR -1>
    <SPLIT </ <WINGET 0 ,WHIGH> 4>>
    <ANIMATE ,CEL-TABLE>
    <QUIT>>
```


### WINPOS
```zil
;  From Shogun
<ROUTINE WINDEF (W TOP LEFT HIGH WIDE)
    <WINPOS .W .TOP .LEFT>
    <WINSIZE .W .HIGH .WIDE>>
```


### WINPUT
```zil
;  From Shogun
<WINPUT 0 ,WCRFUNC
    <COND (.BORD? ,RESET-MARGIN-1)
        (ELSE ,RESET-MARGIN)>>
<COND (<EQUAL? .P ,P-OAR>
    <SET Y <+ .Y 1>>)>
<WINPUT 0 ,WCRCNT .Y>)>)>
```


### WINSIZE
```zil
;  From Arthur
<SET WX <WINGET 0 ,K-W-XSIZE>>
<WINSIZE 0 .WY .WX>
```


### XPUSH
```zil
<GLOBAL MY-STACK <TABLE 1 0 0 0>>
<XPUSH 123 ,MY-STACK>  ;  MY-STACK <TABLE 2 0 123 0>
```


### ZWSTR
```zil
<GLOBAL SRCBUF <TABLE (STRING) "hello">>
<GLOBAL DSTBUF <TABLE 0 0 0>>

<ZWSTR ,SRCBUF 5 1 ,DSTBUF> 
<PRINTB ,DSTBUF>  ;  "hello"
```


## Parser System

### ADJ-SYNONYM
```zil
<ADJ-SYNONYM HAPPY JOYFUL>
<ADJ-SYNONYM INTELLIGENT SMART>
<ADJ-SYNONYM BAD AWFUL>
<ADJ-SYNONYM STRONG SOLID>
```


### BIT-SYNONYM
```zil
<BIT-SYNONYM TAKEBIT GETBIT PICKBIT>
<BIT-SYNONYM LIGHTBIT DAYBIT>
```


### BUZZ
```zil
<BUZZ A AN AND ANY ALL EVERY EVERYTHING BUT EXCEPT OF ONE
              THE THEN UNDO OOPS \. \, \">
```


### DIR-SYNONYM
```zil
<DIR-SYNONYM FORE F>
<DIR-SYNONYM AFT A>
<DIR-SYNONYM PORT P>
<DIR-SYNONYM STARBOARD SB>
```


### DIRECTIONS
```zil
<DIRECTIONS NORTH SOUTH EAST WEST NE NW SE SW IN OUT UP DOWN>
```


### PREP-SYNONYM
```zil
<PREP-SYNONYM INTO IN>
<PREP-SYNONYM UPON ON>
<PREP-SYNONYM ACROSS OVER BEYOND>
<PREP-SYNONYM ABOUT REGARDING CONCERNING>
```


### SYNONYM
```zil
<SYNONYM NORTH FORE>
<SYNONYM SOUTH AFT>
<SYNONYM WEST PORT>
<SYNONYM EAST STARBOARD>

<SYNTAX PUT OBJECT = V-INSERT>
<VERB-SYNONYM PUT SLIDE DIP SOAK>
```


### SYNTAX
```zil
<SYNTAX QUIT = V-QUIT>
<SYNTAX CONTEMPLATE OBJECT = V-THINK-ABOUT>
<SYNTAX TAKE OBJECT (FIND TAKEBIT) (MANY ON-GROUND IN-ROOM)
    = V-TAKE>
<SYNTAX PUT OBJECT (MANY TAKE HELD CARRIED) IN OBJECT
    (FIND CONTBIT) = V-PUT-IN PRE-PUT-IN>
<SYNTAX WAKE OBJECT (FIND PERSONBIT) = V-WAKE>

<SYNTAX WAKE UP OBJECT (FIND PERSONBIT) = V-WAKE>
<SYNTAX WAKE OBJECT (FIND PERSONBIT) UP OBJECT
    (FIND KLUDGEBIT) = V-WAKE>
```


### VERB-SYNONYM
```zil
<VERB-SYNONYM SAY TELL>
<VERB-SYNONYM GO MOVE>
<VERB-SYNONYM MAKE CREATE BUILD>
<VERB-SYNONYM GET OBTAIN ACQUIRE>
```


## Object System

### OBJECT
```zil
<OBJECT LAMP
  (IN LIVING-ROOM)
  (SYNONYM LAMP LANTERN LIGHT)
  (ADJECTIVE BRASS)
  (DESC "brass lantern")
  (FLAGS TAKEBIT LIGHTBIT)
  (ACTION LANTERN)
  (FDESC "A battery-powered brass lantern is on the trophy case.")
  (LDESC "There is a brass lantern (battery-powered) here.")
  (SIZE 15)>
```


### PropAdjective
```zil
ADJECTIVE BRASS SMALL
```
