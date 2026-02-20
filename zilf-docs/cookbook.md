[← Back to Main Index](./index.md)

# ZILF Cookbook
---

### ADJ-SYNONYM
```zil
<ADJ-SYNONYM HAPPY JOYFUL>
<ADJ-SYNONYM INTELLIGENT SMART>
<ADJ-SYNONYM BAD AWFUL>
<ADJ-SYNONYM STRONG SOLID>
```


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


### BIT-SYNONYM
```zil
<BIT-SYNONYM TAKEBIT GETBIT PICKBIT>
<BIT-SYNONYM LIGHTBIT DAYBIT>
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


### BUZZ
```zil
<BUZZ A AN AND ANY ALL EVERY EVERYTHING BUT EXCEPT OF ONE
              THE THEN UNDO OOPS \. \, \">
```


### BYTE
```zil
<BYTE 42>  ;  #BYTE 42
#BYTE 42  ;  #BYTE 42
<CHTYPE 42 BYTE>  ;  #BYTE 42
```


### CATCH
```zil
<SETG CATCH-POINT <CATCH>>  ;  Saves the current stack fram in global variable.
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


### ERASE
```zil
<ERASE 1>  ;  Clears from cursor to end of line
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


### F?
```zil
<F? <=? 1 1>>  ;  False
<F? <=? 1 2>>  ;  True
```


### FCLEAR
```zil
<FCLEAR ,TRAP-DOOR ,OPENBIT>  ;  Marks the trap-door as closed
```


### FILE-LENGTH
```zil
;  "ZILF ver 0.9"
<SET CH <OPEN "READ" "../zillib/parser.zil">>
<FILE-LENGTH .CH>  ;  115629
<CLOSE .CH>
```


### FIRST?
```zil
<SET RM <FIRST? ,ROOMS>>  ;  Sets RM to first object in ROOMS. Also evaluates to true (all values not 0 is true)
```


### FONT
```zil
<FONT 4>  ;  Sets fixed-pitch font. In versions 3-4, this is done by setting bit 1 of Flags 2 in header <PUT 0 8 <BOR <GET 0 8> 2>>
```


### FORM
```zil
<FORM + 1 2>  ;  <+ 1 2> 
<DEFINE INC-FORM (A) 
    <FORM SET .A <FORM + 1 <FORM LVAL .A>>>> 
<INC-FORM X>  ;  <SET X <+ 1 .X>
```


### FSET
```zil
<FSET ,TRAP-DOOR ,OPENBIT> --> Marks the trap-door as open
```


### FSET?
```zil
<FSET? ,TRAP-DOOR ,OPENBIT>  ;  True if OPENBIT is set
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


### GET
```zil
<GET <TABLE 0 1 2 3> 2>  ;  2
```


### GET-DECL
```zil
<GET-DECL BOOLEAN>  ;  #FALSE
<PUT-DECL BOOLEAN '<OR ATOM FALSE>>
<GET-DECL BOOLEAN>  ;  <OR ATOM FALSE>
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


### GETPT
```zil
<OBJECT MYOBJ (MYPROP 123)>
<GET <GETPT ,MYOBJ ,P?MYPROP> 0>  ;  123
<GETPT ,MYOBJ ,P?MYPROP2>  ;  0
```


### GLOBAL
```zil
<GLOBAL MYVAR 0>
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


### ISTRING
```zil
<ISTRING 4 !\A>  ;  "AAAA"
<SET A 64>
<ISTRING 4 '<ASCII <SET A <+ .A 1>>>>  ;  "ABCD"
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


### OR
```zil
<OR <=? 1 2> <=? 1 1>>  ;  True 
 <OR <=? 1 1> <SET X 2>> ;  X is never set to 2 because first predicate evaluates to true 
 <SET X <OR 0 1 2 3>>  ;  X is set to 0 
 <SET X <OR <> 1 2 3>>  ;  X is set to 1
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


### PNAME
```zil
<PNAME FOO> ; "FOO"
<PNAME FOO!-NEW-OBLIST> ; "FOO"
<UNPARSE FOO!-NEW-OBLIST> ; "FOO!-NEW-OBLIST"
```


### POP
```zil
<PUSH .FOO>
<SET FOO some-new-value>
;code
<SET FOO <POP>>
```


### PREP-SYNONYM
```zil
<PREP-SYNONYM INTO IN>
<PREP-SYNONYM UPON ON>
<PREP-SYNONYM ACROSS OVER BEYOND>
<PREP-SYNONYM ABOUT REGARDING CONCERNING>
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


### PTABLE
```zil
<PTABLE 1 2 3 4>
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


### PropAdjective
```zil
ADJECTIVE BRASS SMALL
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


### RANDOM
```zil
<- <RANDOM 101> 1>  ;  Generates random number between 0-100
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


### REMOVE
```zil
<OBJECT ANIMAL>
<OBJECT CAT (LOC ANIMAL)>
<REMOVE ,CAT)  ;  Detach CAT from ANIMAL
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


### RFALSE
```zil
<RFALSE>
```


### RFATAL
```zil
<RFATAL>
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


### SETG20
```zil
<SETG20 MYVAR 42> ; Store 42 in global atom MYVAR
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


### SPNAME
```zil
<SPNAME atom>
```


### STRING
```zil
<STRING !\A <ASCII 66> "CD"> ; "ABCD"
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


### USL
```zil
<USL>
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


### VERB-SYNONYM
```zil
<VERB-SYNONYM SAY TELL>
<VERB-SYNONYM GO MOVE>
<VERB-SYNONYM MAKE CREATE BUILD>
<VERB-SYNONYM GET OBTAIN ACQUIRE>
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
