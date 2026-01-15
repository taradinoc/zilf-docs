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


### GLOBAL
```zil
<GLOBAL MYVAR 0>
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


### REMOVE
```zil
<OBJECT ANIMAL>
<OBJECT CAT (LOC ANIMAL)>
<REMOVE ,CAT)  ;  Detach CAT from ANIMAL
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


### SET
```zil
<PROG (X) <SET X 5> <RETURN .X>> ; Returns 5 after setting X.
```


### SETG
```zil
<SETG MYVAR 42> ; Store 42 in global atom MYVAR
```


### SETG20
```zil
<SETG20 MYVAR 42> ; Store 42 in global atom MYVAR
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


### VALID-TYPE?
```zil
<VALID-TYPE? VECTOR>  ;  VECTOR
<VALID-TYPE? FOO>  ;  #FALSE
<NEWTYPE FOO FIX> 
<VALID-TYPE? FOO>  ;  FOO
```


### VALUE
```zil
<SETG X 3>
<SET X 4>
<VALUE X>  ;  4
<UNASSIGN X>
<VALUE X>  ;  3
```


### VERB-SYNONYM
```zil
<VERB-SYNONYM SAY TELL>
<VERB-SYNONYM GO MOVE>
<VERB-SYNONYM MAKE CREATE BUILD>
<VERB-SYNONYM GET OBTAIN ACQUIRE>
```
