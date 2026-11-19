[← Back to Main Index](./index.md)

# Z-Code Built-ins
---

### *
**Usage:** `<* numbers ...>`

**Alternative Usage:** `<MUL numbers ...>`

MDL and Z-code built-in function that multiplies numbers.

**History:** Zapf syntax: MUL, Inform syntax: mul

---

### +
**Usage:** `<+ numbers ...>`

**Alternative Usage:** `<ADD numbers ...>`

MDL and Z-code built-in function that adds numbers.

**History:** Zapf syntax: ADD, Inform syntax: add

---

### -
**Usage:** `<- numbers ...>`

**Alternative Usage:** `<BACK number1 number2>` | `<SUB numbers ...>`

MDL and Z-code built-in function that subtracts the first number by subsequent numbers, or negates a single number.

**History:** Zapf syntax: SUB, Inform syntax: sub

---

### 0?
**Usage:** `<0? value>`

**Alternative Usage:** `<ZERO? value>`

MDL and Z-code built-in predicate that returns true if value is 0, otherwise false.

**History:** Zapf syntax: ZERO?, Inform syntax: jz

---

### 1?
**Usage:** `<1? value>`

MDL and Z-code built-in predicate that returns true if value is 1, otherwise false.

---

### ==?
**Usage:** `<==? value1 value2>`

MDL and Z-code predicate that returns TRUE if value1 and value2 are the same object (or equal to any subsequent argument in Z-code), otherwise FALSE.

**History:** Zapf syntax: EQUAL?, Inform syntax: je

---

### =?
**Usage:** `<=? value1 value2>`

**Alternative Usage:** `<EQUAL? value1 value2 ...>`

MDL and Z-code predicate that returns TRUE if value1 and value2 are of the same TYPE and structurally equal (or equal to any subsequent argument in Z-code), otherwise FALSE.

**History:** Zapf syntax: EQUAL?, Inform syntax: je

---

### AGAIN
**Usage:** `<AGAIN [activation]>`

MDL built-in function (<AGAIN [activation]>) that restarts evaluation from the specified or most recent automatically created activation (PROG or REPEAT) without re-binding arguments or AUX variables.

Z-code built-in function (<AGAIN [activation]>) that restarts a BIND, DO, PROG, REPEAT, or ROUTINE block from the top. Inside a ROUTINE, restarting the ROUTINE itself reinitializes arguments/variables that have default starting values, whereas restarting BIND, DO, PROG, or REPEAT preserves variable values.

---

### AND
**Usage:** `<AND expressions...>`

MDL built-in function that is a boolean AND. Requires that all expressions evaluate to true to return true. Exits on the first expression that evaluates to false (rest of expressions are not evaluated).

> **Note:** Because 0 is considered false and all other values are considered true inside a routine AND returns 0 if one expression is false or the value of the last expression if all expressions are true. Because false is its own TYPE outside a routine AND returns #FALSE if one of the expressions is false or the value of the last expression if all expressions are true.

---

### ANDB
**Usage:** `<ANDB numbers ...>`

MDL built-in function for bitwise AND (and alias for BAND in Z-code).

---

### APPLY
**Usage:** `<APPLY routine values...>`

**Alternative Usage:** `<APPLY applicable args ...>`

MDL built-in function (<APPLY applicable args ...>) that calls an applicable object (FUNCTION, SUBR, FSUBR, MACRO, FIX, or OFFSET) with args.

Z-code built-in function (<APPLY routine values ...>) that calls a Z-machine routine with values, commonly used when the target routine is resolved at runtime (e.g., dispatch tables or object ACTION properties).

---

### ASH
**Usage:** `<ASH number places>`

**Alternative Usage:** `<ASHIFT number places>`

Arithmetic shift. Shift number left when places is positive and right if it is negative. When right shift the sign is preserved (if bit 15 is 1 a 1 is shifted in, otherwise a 0 is shifted in).

1000 0000 0000 1010 --> 1100 0000 0000 0101

> **Note:** ZILF supports ASH, ASHIFT in versions 5-.
>
> Also see LSH.

**History:** Zapf syntax: ASHIFT, Inform syntax: art_shift

---

### ASSIGNED?
**Usage:** `<ASSIGNED? Name>`

**Alternative Usage:** `<ASSIGNED? atom [environment]>`

MDL built-in predicate (<ASSIGNED? atom [environment]>) that returns true if atom has a local value (LVAL) in the given or current environment.

Z-code built-in predicate (<ASSIGNED? name>) that tests if an optional argument named name was supplied in the call to the current ROUTINE.

> **Note:** ZILF supports ASSIGNED? in versions 5-.

**History:** Zapf syntax: ASSIGNED?, Inform syntax: check_arg_count

---

### BACK
**Usage:** `<BACK table [bytes]>`

MDL built-in function (<BACK array [count]>) that moves count elements back in a VECTOR or STRING array.

Z-code built-in function (<BACK table [bytes]>) that returns table with address moved bytes back (or aliases SUB for numbers). If the count moves past the start of the table no error is raised. Default value for bytes is 1. 

Note that this is not a copy of the table, it is pointing to the same table with another starting address. Also see GET, GETB, PUT, PUTB and REST.

---

### BAND
**Usage:** `<BAND numbers ...>`

**Alternative Usage:** `<ANDB numbers ...>`

Bitwise AND function.

> **Note:** ZILF supports BAND in all versions.

---

### BCOM
**Usage:** `<BCOM value>`

Z-code built-in function that is a bitwise NOT, reversing all bits in the WORD value (16 bits).

> **Note:** ZILF supports BCOM in all versions.

**History:** Zapf syntax: BCOM, Inform syntax: not

---

### BIND
**Usage:** `<BIND [activation] (bindings ...) [decl] expressions ...>`

MDL built-in function that defines a program block with its own set of bindings. BIND is similar to PROG and REPEAT but BIND doesn't create a default activation (like PROG and REPEAT) at the start of the block and doesn't have an automatic AGAIN at the end of the block (like REPEAT). If an activation is needed it must be specified. AGAIN and RETURN without specified activation inside a BIND-block will start over or return from the closest surrounding activation within the current function.

The decl is used to specify the valid TYPE of the variables. In its simplest form decl is formatted like: #DECL ((X) FIX), meaning that X must be of the TYPE FIX. For more information on how to format the decl see GDECL. 

Also see AGAIN, PROG, REPEAT and RETURN for more details how to control program flow.

Z-code built-in (<BIND [activation] (bindings...) expressions...>): Inside a ROUTINE, BIND defines a local variable block without creating a default activation; bare AGAIN or RETURN targets the enclosing activation (typically the ROUTINE). Variables in BIND are not reinitialized on AGAIN.

---

### BOR
**Usage:** `<BOR numbers ...>`

**Alternative Usage:** `<ORB numbers ...>`

Z-code built-in function that is a bitwise OR.

> **Note:** ZILF supports BOR in all versions.

**History:** Zapf syntax: BOR, Inform syntax: or

---

### BTST
**Usage:** `<BTST value1 value2>`

Z-code built-in predicate that performs a binary test that evaluates to true if all value2 bits are set in value1. Could be expressed as <=? <BAND value1 value2> value2>.

> **Note:** ZILF supports BTST in all versions.

**History:** Zapf syntax: BTST, Inform syntax: test

---

### BUFOUT
**Usage:** `<BUFOUT value>`

Z-code built-in flag that controls if output is buffered (to enable proper word-wrap). value can be true or false.

> **Note:** ZILF supports BUFOUT in versions 4-.

**History:** Zapf syntax: BUFOUT, Inform syntax: buffer_mode

---

### CATCH
**Usage:** `<CATCH>`

Used in conjunction with THROW, this Z-code built-in function returns the current state of the stack (the "stack frame"). Also see THROW.

> **Note:** ZILF supports CATCH in versions 5-.

**History:** Zapf syntax: CATCH, Inform syntax: catch

---

### CHECKU
**Usage:** `<CHECKU character>`

Checks if a given unicode character can be printed and/or received from the keyboard. Return is in bit 0 and 1 so the return result is either 0, 1, 2 or 3.

* 0 = character can not be printed and not received from keyboard
* 1 = character can be printed but not received from keyboard
* 2 = character can not be printed but received from keyboard
* 3 = character can both be printed and received from keyboard

> **Note:** ZILF supports CHECKU in versions 5-.

**History:** Zapf syntax: CHECKU, Inform syntax: check_unicode

---

### CLEAR
**Usage:** `<CLEAR window-number>`

Clears window with given window-number. If window-number is -1 it unsplit all windows and then clears the resulting window. If window-number is -2 it clears all windows without unsplitting.

> **Note:** ZILF supports CLEAR in versions 4-.

**History:** Zapf syntax: CLEAR, Inform syntax: erase_window

---

### COLOR
**Usage:** `<COLOR fg-color bg-color>  ;  "Version 5"`

**Alternative Usage:** `<COLOR fg-color bg-color [window-number]>  ;  "Versions: 6-"`

Print text in given fg-color and bg-color from this point on (flushing out text in buffer in old colors first). Version 6 supports a third argument, window-number. The colors available (if interpreter supports it) are:

* 0 = Current color
* 1 = Default color
* 2 = Black
* 3 = Red
* 4 = Green
* 5 = Yellow
* 6 = Blue
* 7 = Magenta
* 8 = Cyan
* 9 = White

> **Note:** ZILF supports COLOR in versions 5-.

**History:** Zapf syntax: COLOR, Inform syntax: set_colour

---

### COND
**Usage:** `<COND (condition expressions...)...>`

Test condition (predicate) and if condition evaluates to true expressions are executed.

IF-THEN style: <COND (<AND <=? 1 1> <=? 2 2>> <TELL "IF-THEN <...>">)>

MDL built-in (<COND (condition body ...) ...>): Outside a ROUTINE, evaluates each condition in turn until one is not #FALSE, evaluates all body expressions in that clause, and returns the value of the last evaluated expression (or #FALSE if no condition matches).

---

### COPYT
**Usage:** `<COPYT src-table dest-table length>`

Copies length number of bytes from src-table to dest-table. The tables are allowed to overlap. If length is positive then the copy is done without corrupting the src-table. If length is negative the copy is always forward from src-table to dest-table (the absolute length number of bytes) even if this corrupts src-table.

> **Note:** ZILF supports COPYT in versions 5-.

**History:** Zapf syntax: COPYT, Inform syntax: copy_table

---

### CRLF
**Usage:** `<CRLF [channel]>`

**Alternative Usage:** `<CRLF>`

MDL built-in function (<CRLF [channel]>) that prints a carriage-return and line-feed to channel (default <LVAL OUTCHAN>) and returns true.

Z-code built-in function (<CRLF>) that prints a carriage-return and line-feed to the active Z-machine output stream (takes no channel argument).

> **Note:** ZILF supports CRLF in all versions.

**History:** Zapf syntax: CRLF, Inform syntax: new_line

---

### CURGET
**Usage:** `<CURGET table>`

CURGET puts the current cursor row in record 0 and current cursor column in record 1 of the supplied table.Both row and column are WORD (16-bit).

> **Note:** ZILF supports CURGET in versions 4-.

**History:** Zapf syntax: CURGET, Inform syntax: get_cursor

---

### CURSET
**Usage:** `<CURSET row column>  ;  "Versions: 4-5"`

**Alternative Usage:** `<CURSET row column [window-number]>  ;  "Versions: 6-"`

CURSET moves the cursor to row and column in the current window (or supplied window-number).

> **Note:** ZILF supports CURSET in versions 4-.

**History:** In versions 4-5 it is only possible to move the cursor in the upper window (window-number = 1). In versions 6-, if row is -1 then the cursor is turned off (-2 turns it back on).

---

### DCLEAR
**Usage:** `<DCLEAR picture-number [row] [column]>`

Clears (draw background color) area covered by picture-number, starting at row and column. Also see DISPLAY.

> **Note:** ZILF supports DCLEAR in versions 6-.

**History:** Zapf syntax: DCLEAR, Inform syntax: erase_picture

---

### DEC
**Usage:** `<DEC name>`

Decrease variable (signed) name with 1.

> **Note:** ZILF supports DEC in all versions.

**History:** Zapf syntax: DEC, Inform syntax: dec

---

### DIRIN
**Usage:** `<DIRIN stream-number>`

Select input stream. Only stream-number 0 and 1 are valid.

* 0 = Keyboard 
* 1 = File on host

> **Note:** ZILF supports DIRIN in all versions.

**History:** Zapf syntax: DIRIN, Inform syntax: input_stream

---

### DIROUT
**Usage:** `<DIROUT stream-number [table]>  ;  Versions -5`

**Alternative Usage:** `<DIROUT stream-number [table] [width]>  ;  Versions 6-`

Directs output to one or more output streams (multiple streams can be active simultaneously). Turn on stream with positive stream-number and turn off stream with negative stream-number.

If stream 3 is active a table must be supplied. WORD 0 in table holds number of printed characters and byte 2 onward holds the characters printed. DIROUT can overrun table if not enough space is allocated.

Later versions can format output text to width (number of characters if width is positive or number of pixels if width is negative).

* 1 = Screen 
* 2 = File on host (transcript) 
* 3 = Table 
* 4 = File of commands on host

**History:** Zapf syntax: DIROUT, Inform syntax: output_stream

---

### DISPLAY
**Usage:** `<DISPLAY picture-number [row] [column]>`

Draw picture-number at coordinates row and column. If row and column are omitted the current cursor position is used.

> **Note:** ZILF supports DISPLAY in versions 6-.

**History:** Zapf syntax: DISPLAY, Inform syntax: draw_picture

---

### DIV
**Usage:** `</ numbers ...>`

**Alternative Usage:** `<DIV numbers ...>`

MDL and Z-code built-in function that divides the first number by subsequent numbers.

**History:** Zapf syntax: DIV, Inform syntax: div

---

### DLESS?
**Usage:** `<DLESS? name value>`

Predicate. Decrease variable (signed) name with 1 and returns true if variable name is lower than value, otherwise returns false.

> **Note:** ZILF supports DLESS? in all versions.

**History:** Zapf syntax: DLESS?, Inform syntax: dec_chk

---

### DO
**Usage:** `<DO (name start end [step]) [(END expressions ...)] expressions ...>`

Z-code built-in function that executes a loop, behaving as a cross between a Pascal-style "for" statement and a C-style "for" statement.

Pascal-style "for" statements loop over a range of values:
<DO (I 1 10) ...>
<DO (J 10 1 -1) ...>

C-style "for" statements initialize some state, then mutate it and repeat until a condition becomes true (note: the condition is reversed from C, the loop exits when it becomes true):
<DO (I <FIRST? .OBJ> <NOT .I> <NEXT? .I>) ...>

The behavior of DO depends on the syntax used for each part. If the third value inside the parens is a complex FORM -- meaning one that isn't a simple LVAL or GVAL, like '.MAX' is -- it's assumed to be a "C-style" exit condition, otherwise it's assumed to be a "Pascal-style" upper/lower bound. Likewise, the optional fourth value is treated as either a C-style mutator or a Pascal-style step size.

---

### ERASE
**Usage:** `<ERASE value>`

Z-code built-in function that erases from the current cursor position. This functions behavior is dependent on the supported version.

Versions 4 and 5: if the value is 1, erase from the current cursor position to the end of its line in the current window. If the value is anything other than 1, do nothing.  

Version 6: if the value is 1, erase from the current cursor position to the end of its line in the current window. If not, erase the given number of pixels minus one across from the cursor (clipped to stay inside the right margin). The cursor does not move.

> **Note:** ZILF supports ERASE in versions 4-.

**History:** Zapf syntax: ERASE, Inform syntax: erase_line

---

### F?
**Usage:** `<F? expression>`

Z-code built-in predicate that tests is expression evaluates to false.

> **Note:** ZILF supports F? in all versions.

---

### FCLEAR
**Usage:** `<FCLEAR object flag>`

Z-code built-in function that removes flag from object.

> **Note:** ZILF supports FCLEAR in all versions.

**History:** Zapf syntax: FCLEAR, Inform syntax: clear_attr

---

### FIRST?
**Usage:** `<FIRST? object>`

Z-code built-in function that returns the first object inside (contained) in the object. Returns 0 (false) if no object exists.

> **Note:** ZILF supports FIRST? in all versions.

**History:** Zapf syntax: FIRST?, Inform syntax: get_child

---

### FONT
**Usage:** `Version 5: <FONT number>, Version 6-: <FONT number [window-number]>`

Z-code built-in function that Sets current font to number. Returns old fonts number. If the font number is not available 0, return false.

The following numbers map to font types.
1 := Normal font
3 := Character graphics font (see section 16 in the Z-Machine Standards Document).
4 := Monospace (fixed-pitch) font

> **Note:** ZILF supports FONT in versions 5-.

**History:** Zapf syntax: FONT, Inform syntax: set_font

---

### FSET
**Usage:** `<FSET object flag>`

Z-code built-in function adds flag to object.

> **Note:** ZILF supports FSET in all versions.

**History:** Zapf syntax: FSET, Inform syntax: set_attr

---

### FSET?
**Usage:** `<FSET? object flag>`

Z-code built-in predicate that tests if the flag is set on the object.

> **Note:** ZILF supports FSET? in all versions.

**History:** Zapf syntax: FSET?, Inform syntax: test_attr

---

### FSTACK
**Usage:** `<FSTACK number [stack]>`

Removes number of items from system stack or given stack (table).

> **Note:** ZILF supports FSTACK in versions 6-.

**History:** Zapf syntax: FSTACK, Inform syntax: pop / pop_stack

---

### G=?
**Usage:** `<G=? value1 value2>`

MDL and Z-code predicate that returns true if value1 is greater than or equal to value2, otherwise false.

---

### G?
**Usage:** `<G? value1 value2>`

MDL built-in predicate that returns true if value1 is greater than value2, otherwise the predicate returns false.

> **Note:** 'G' means "is greater than."

---

### GET
**Usage:** `<GET table offset>`

Z-code built-in function that returns WORD-record (2 bytes) stored at offset. Note that table is an address in memory so the WORD that is returned is at table+offset*2. It is legal to use, for example, 0 as an address to retrieve information from the header. 

Also see BACK, GETB, PUT, PUTB and REST.

> **Note:** ZILF supports GET in all versions.

**History:** Zapf syntax: GET, Inform syntax: loadw

---

### GETB
**Usage:** `<GETB table offset>`

ZIL library function (<GETB table index>) and Z-code built-in (<GETB table offset>) that returns the 1-byte record stored at the given byte offset (usable both outside and inside ROUTINEs). Note that table is an address in memory so the BYTE that is returned is at table+offset. It is legal to use, for example, 0 as an address to retrieve information from the header. 

Also see BACK, GET, PUT, PUTB and REST.

> **Note:** ZILF supports GETB in all versions.

**History:** Zapf syntax: GETB, Inform syntax: loadb

---

### GETP
**Usage:** `<GETP object property>`

Z-code built-in function that gets property from the object. Returns default value if property is not declared in the object.

> **Note:** ZILF supports GETP in all versions.

**History:** Zapf syntax: GETP, Inform syntax: get_prop

---

### GETPT
**Usage:** `<GETPT object property>`

Z-code built-in that gets property address from object. Returns 0 (false) if property is not declared in the object.

> **Note:** ZILF supports GETPT in all versions.

**History:** Zapf syntax: GETPT, Inform syntax: get_prop_addr

---

### GRTR?
**Usage:** `<GRTR? Value1 value2>`

**Alternative Usage:** `<G? value1 value2>`

Predicate. Returns true if value1 is greater than value2, otherwise false.

> **Note:** ZILF supports GRTR? in all versions.

**History:** Zapf syntax: GRTR?, Inform syntax: jg

---

### GVAL
**Usage:** `<GVAL atom>`

**Alternative Usage:** `,atom`

MDL built-in function that gets the value of the global atom.

> **Note:** Typically used in its alternate form ",atom".

---

### HLIGHT
**Usage:** `<HLIGHT style>`

Set text to style. It is possible to combine styles.

* 0 = Normal 
* 1 = Inverse 
* 2 = Bold 
* 4 = Italic 
* 8 = Monospace

> **Note:** ZILF supports HLIGHT in versions 4-.

**History:** Zapf syntax: HLIGHT, Inform syntax: set_text_style

---

### IFFLAG
**Usage:** `<IFFLAG (condition body ...) ...>`

ZIL library function that returns the result as soon as any body is evaluated. If no body is evaluated, the function returns FALSE. Each condition is either:

* A STRING naming a compilation flag, to evaluate the corresponding body if the flag’s value is true. 
* An ATOM whose PNAME names a compilation flag, to evaluate the corresponding body if the flag’s value is true.
* A FORM, to evaluate the FORM after replacing any element ATOMs whose PNAMEs name compilation flags with the flag values, and then evaluate the corresponding body if the result is true.
* Any other value, to evaluate the corresponding body immediately.

> **Note:** As a consequence of the evaluation conditions (rules), undefined compilation flags are effectively TRUE.

---

### IGRTR?
**Usage:** `<IGRTR? name value>`

Predicate. Increase variable (signed) name with 1 and returns true if variable name is greater than value, otherwise returns false.

> **Note:** ZILF supports IGRTR? in all versions.

**History:** Zapf syntax: IGRTR?, Inform syntax: inc_chk

---

### IN?
**Usage:** `<IN? object1 object2>`

Z-code built-in predicate that returns true if object1 is in object2 (object1 has object2 as parent),otherwise false.

> **Note:** ZILF supports IN? in all versions.

**History:** Zapf syntax: IN?, Inform syntax: jin

---

### INC
**Usage:** `<INC name>`

Z-code built-in function that increments name by 1, which is signed, such that -1 increments to 0.

> **Note:** ZILF supports INC in all versions.

**History:** Zapf syntax: INC, Inform syntax: inc

---

### INPUT
**Usage:** `<INPUT 1 [time] [routine]>`

Z-code built-in function that  reads a single character from the keyboard. Calls routine every time*0.1 s. If routine returns true input is aborted.

> **Note:** ZILF supports INPUT in versions 4-.

**History:** Zapf syntax: INPUT, Inform syntax: read_char

---

### INTBL?
**Usage:** `<INTBL? value table length [rec-spec]>  ;  "Version 5, 7-"` | `<INTBL? value table length>   ;  "Version 4, 6"`

Z-code built-in predicate that that returns the address of value if value is in the table table of the length length, otherwise 0. 

In version 5, 7 and 8 the rec-spec describes the field where bit 7 is set for words and clear for bytes, rest defines the length of the field.

> **Note:** ZILF supports INTBL? in versions 4-.

**History:** Zapf syntax: INTBL?, Inform syntax: scan_table

---

### IRESTORE
**Usage:** `<IRESTORE>`

Z-code built-in function that restores game state saved to memory by ISAVE (undo).

> **Note:** ZILF supports IRESTORE in versions 5-.

**History:** Zapf syntax: IRESTORE, Inform syntax: restore_undo

---

### ISAVE
**Usage:** `<ISAVE>`

Z-code built-in function that saves the game state to memory that later can be restored by IRESTORE (undo). Returns 0 if ISAVE fails, returns 1 if it is successful, and returns -1 if the interpreter does not handle undo.

> **Note:** ZILF supports ISAVE in versions 5-.

**History:** Zapf syntax: ISAVE, Inform syntax: save_undo

---

### ITABLE
**Usage:** `<ITABLE [specifier] count [(flags...)] defaults ...>`

Defines a table of count elements filled with default values: either zeros or, if the default list is specified, the specified list of values repeated until the table is full.

The optional specifier may be the atoms NONE, BYTE, or WORD. BYTE and WORD turn on the length marker (element 0 in the table contains the length of the table) and also set its form. This can also be done with the flags (see TABLE about flags).

> **Note:** TABLE is a ZIL-specific structure that can be used both outside and inside ROUTINES.

---

### L=?
**Usage:** `<L=? value1 value2>`

MDL and Z-code predicate that returns true if value1 is less than or equal to value2, otherwise false.

---

### L?
**Usage:** `<L? value1 value2>`

MDL built-in predicate that returns true if value1 is lower than value2 otherwise false.

> **Note:** L means less than.

---

### LESS?
**Usage:** `<LESS? Value1 value2>`

**Alternative Usage:** `<L? value1 value2>`

Predicate. Returns true if value1 is less than value2, otherwise false.

> **Note:** ZILF supports LESS? in all versions.

**History:** Zapf syntax: LESS?, Inform syntax: jl

---

### LEX
**Usage:** `<LEX text parse [dictionary] [flag]>`

Z-code built-in function that parses the text into parse. See READ for more info about parsing. The game dictionary is used if not a dictionary table (LTABLE) is supplied. If the length of the dictionary is negative, the dictionary can be unsorted. If the flag is set (true), unrecognized words are not written to parse but their slot is left unmodified. This makes it possible to run LEX against different dictionaries serially. Also see READ.

> **Note:** ZILF supports LEX in versions 4-.

**History:** Zapf syntax: LEX, Inform syntax: tokenise

---

### LOC
**Usage:** `<LOC object>`

Z-code built-in function that returns parent to object.

> **Note:** ZILF supports LOC in all versions.

**History:** Zapf syntax: LOC, Inform syntax: get_parent

---

### LOWCORE
**Usage:** `<LOWCORE field-spec [new-value]>`

Z-code built-in function that reads and in some cases writes to the header information fields.

> **Note:** Valid field-spec symbols (Appendix B): ZVERSION, ZORKID/RELEASEID, ENDLOD, START, VOCAB, OBJECT, GLOBALS, PURBOT, FLAGS, SERIAL, SERI1, SERI2, FWORDS, PLENTH, PCHKSUM, INTWRD, INTID, INTVER, SCRWRD, SCRV, SCRH, HWRD, VWRD, FWRD, LMRG/FOFF, RMRG/SOFF, CLRWRD, TCHARS, CRCNT, TWID, CRFUNC/STDREV, CHRSET, EXTAB, and extended header fields MSLOCX, MSLOCY, MSETBL/UNITBL, MSEDIR/FLAGS3, MSEINV/TRUFGC, MSEVRB/TRUBGC, MSEWRD, BUTTON, JOYSTICK, BSTAT, JSTAT.

---

### LOWCORE-TABLE
**Usage:** `<LOWCORE-TABLE field-spec length routine>`

Z-code built-in function that reads the length number of bytes from field-spec and calls routine between each byte.

> **Note:** See LOWCORE and Appendix B of the ZILF Reference Guide for valid header field-spec symbols.

---

### LSH
**Usage:** `<LSH number places>`

MDL built-in function that is a bitwise shift, shifting number left when places is positive and right if it is negative. When right shifting, the sign is not preserved (0 is always shifted in). For example.

1000 0000 0000 1010  -->  0100 0000 0000 0101

---

### LTABLE
**Usage:** `<LTABLE [(flags ...)] values ...>`

Z-code built-in function that Defines a table containing the specified values and with the LENGTH flag.

> **Note:** See TABLE for more information about LENGTH and other flags.

---

### LVAL
**Usage:** `<LVAL name>`

**Alternative Usage:** `.name`

MDL built-in function (<LVAL atom [environment]>) that gets the local value of atom in the optional or current environment.

Z-code built-in function (<LVAL name>) that gets the value of local variable name inside a ROUTINE.

> **Note:** LVAL is more often used in its short for, which is .name.

---

### MAP-CONTENTS
**Usage:** `<MAP-CONTENTS (name [next] object) [(END expressions ...)] expressions ...>`

Z-code built-in function that loops over all objects that have an object as parent (all children to object). For each iteration name is assigned the current child-object and next the child-object that will be name in the next iteration (0 if the current name is the last child).

For each iteration the expressions are evaluated and, if supplied, the (END expressions...) is evaluated last after all iterations.

---

### MAP-DIRECTIONS
**Usage:** `<MAP-DIRECTIONS (name pt room)  [(END expressions ...)] expressions ...>`

Z-code built-in function that loops over all defined directions in a room. For each iteration name is assigned the current direction and pt is the property for this direction.

For each iteration the expressions are evaluated and, if supplied, the (END expressions...) is evaluated last after all iterations.

---

### MARGIN
**Usage:** `<MARGIN left right [window-number]>`

Z-code built-in function that sets the left and right margin (in pixels) of the given window-number. If no window-number is specified, MARGIN sets margins in window-number 0.

> **Note:** ZILF supports MARGIN in versions 6-.

**History:** Zapf syntax: MARGIN, Inform syntax: set_margins

---

### MENU
**Usage:** `<MENU number table>`

Z-code built-in function that controls menu 3- (not menu 0-2, they are system menus). The table is a LTABLE of LTABLE. Item 1 being the menu name. Item 2- are the entries.

> **Note:** ZILF supports MENU in versions 6-.

**History:** Zapf syntax: MENU, Inform syntax: make_menu

---

### MOD
**Usage:** `<MOD number1 number2>`

MDL built-in function that divides 32-bit FIX number1 by non-zero number2 and returns the remainder.

Z-code built-in function that returns the remainder of 16-bit signed division (number2 must be non-zero).

> **Note:** ZILF supports MOD in all versions.

**History:** Zapf syntax: MOD, Inform syntax: mod

---

### MOUSE-INFO
**Usage:** `<MOUSE-INFO table>`

Reads mouse information into table. The table is 4 WORDS (2 bytes) long.

* 0 is Y coordinate
* 1 is X coordinate
* 2 is Button bits (host dependent)
* 3 is Menu (number * 256 + entry)

> **Note:** ZILF supports MOUSE-INFO in versions 6-.

**History:** Zapf syntax: MOUSE-INFO, Inform syntax: read_mouse

---

### MOUSE-LIMIT
**Usage:** `<MOUSE-LIMIT window-number>`

Restricts mouse movement to window-number. If window-number is -1 all restrictions are removed. 1 is the default window-number.

> **Note:** ZILF supports MOUSE-LIMIT in versions 6-.

**History:** Zapf syntax: MOUSE-LIMIT, Inform syntax: mouse_window

---

### MOVE
**Usage:** `<MOVE object1 object2>`

Move object1 to be the first child of object2. Children of object1 move with it.

> **Note:** ZILF supports MOVE in all versions.

**History:** Zapf syntax: MOVE, Inform syntax: insert_obj

---

### N==?
**Usage:** `<N==? value1 value2>`

MDL and Z-code predicate that returns false if value1 and value2 are the same object, otherwise true. Opposite of ==?.

---

### N=?
**Usage:** `<N=? value1 value2>`

MDL and Z-code predicate that returns false if value1 and value2 are structurally equal (or equal to any subsequent argument in Z-code), otherwise true. Opposite of =?.

---

### NEXT?
**Usage:** `<NEXT? object>`

Returns object after object in object-list (sibling). Returns 0 (false) if no object exists.

> **Note:** ZILF supports NEXT? in all versions.

**History:** Zapf syntax: NEXT?, Inform syntax: get_sibling

---

### NEXTP
**Usage:** `<NEXTP object property>`

Returns the property that comes after property on the object. Returns 0 if there are no more properties after property. If property is 0 then NEXTP returns first property on object.

> **Note:** ZILF supports NEXTP in all versions.

**History:** Zapf syntax: NEXTP, Inform syntax: get_next_prop

---

### NOT
**Usage:** `<NOT value>`

MDL built-in function (<NOT value>) that returns true if value is #FALSE (<>), otherwise false (0 is truthy in MDL).

Z-code built-in function (<NOT expression>) that returns boolean NOT (1 if expression is 0, otherwise 0).

> **Note:** This is a boolean (logical) "not."

---

### OR
**Usage:** `<OR expressions...>`

MDL built-in function that is a boolean OR. Requires that one of the expressions evaluates to true to return true. Exits on the first expression that evaluates to true (rest of expressions are not evaluated).

> **Note:** Outside a routine (MDL), OR returns #FALSE if all expressions are false, or the value of the first non-false expression (0 is truthy). Inside a routine (Z-code), 0 is false, so OR returns 0 if all expressions are false or the value of the first non-zero expression.

---

### ORB
**Usage:** `<ORB numbers ...>`

MDL built-in function that performs a bitwise OR.

---

### ORIGINAL?
**Usage:** `<ORIGINAL?>`

Predicate that tests if the game disc is an original. Almost all modern interpreters always return true.

> **Note:** ZILF supports ORIGINAL? in versions 5-.

**History:** Zapf syntax: ORIGINAL?, Inform syntax: piracy

---

### PICINF
**Usage:** `<PICINF picture-number table>`

Z-code built-in function that Writes picture data from picture-number into table. Word 0 of table holds picture width and word 1 holds picture height. Then follows the picture data. If picture-number is 0, the number of available pictures is written into word 0 of table and release number of picture file is written into word 1.

> **Note:** ZILF currently supports PICINF in versions 6-. (Note: the ZILF Reference Guide example has a typo calling PICINFO instead of PICINF.)

**History:** Zapf syntax: PICINF, Inform syntax: picture_data

---

### PICSET
**Usage:** `<PICSET table>`

Z-code built-in function that gives the interpreter a table of picture numbers that the interpreter can then unpack from disc and cache in memory.

> **Note:** ZILF currently supports PICSET in versions 6-.

**History:** Zapf syntax: PICSET, Inform syntax: picture_table

---

### PLTABLE
**Usage:** `<PLTABLE [flags ...] values ...>`

ZIL library function that defines a table containing the specified values and with the PURE and LENGTH flag (see TABLE about LENGTH, PURE and other flags).

> **Note:** TABLE is a ZIL-specific structure that can be used both outside and inside ROUTINES.

---

### POP
**Usage:** `<POP [stack]>`

Z-code built-in function used inside ROUTINE that pops a value from a stack. If no stack is given, a value is popped from the game stack.

> **Note:** ZILF currently supports POP in versions 6-.

**History:** Zapf syntax: POP, Inform syntax: pull

---

### PRINT
**Usage:** `<PRINT value [channel]>`

MDL built-in function that prints a CRLF, the evaluated representation of value, and a space to channel, returning the evaluated value.

Z-code built-in function (print_paddr) that prints a packed string from high memory pointed to by string.

> **Note:** PRINT is just like PRIN1, except that it first prints a CRLF, then the evaluated representation of value and lastly a space.

---

### PRINTB
**Usage:** `<PRINTB string>`

Prints the unpacked-string from the dynamic or static memory (referenced by an unpacked address) that is pointed to by string. String can be a direct address, a local or global variable, or come from the stack.

> **Note:** ZILF supports PRINTB in all versions.

**History:** Zapf syntax: PRINTB, Inform syntax: print_addr

---

### PRINTC
**Usage:** `<PRINTC character>`

Print ASCII character.

> **Note:** ZILF supports PRINTC in all versions.

**History:** Zapf syntax: PRINTC, Inform syntax: print_char

---

### PRINTD
**Usage:** `<PRINTD object>`

Print description of object.

> **Note:** ZILF supports PRINTD in all versions.

**History:** Zapf syntax: PRINTD, Inform syntax: print_obj

---

### PRINTF
**Usage:** `<PRINTF table>`

Print a formatted table. Each line starts with a WORD that is the number of characters that follows. Last byte in each line is 0.

> **Note:** ZILF supports PRINTF in versions 6-.

**History:** Zapf syntax: PRINTF, Inform syntax: print_form

---

### PRINTI
**Usage:** `<PRINTI string>`

Print in-line string. The string is stored in-line with the code, immediately following the instruction.

> **Note:** ZILF supports PRINTI in all versions.

**History:** Zapf syntax: PRINTI, Inform syntax: print

---

### PRINTN
**Usage:** `<PRINTN number>`

Print number.

> **Note:** ZILF supports PRINTN in all versions.

**History:** Zapf syntax: PRINTN, Inform syntax: print_num

---

### PRINTR
**Usage:** `<PRINTR string>`

The same as PRINTI with the addition that PRINTR prints the string and then executes a CRLF followed by a RTRUE.

> **Note:** ZILF supports PRINTR in all versions.

**History:** Zapf syntax: PRINTR, Inform syntax: print_ret

---

### PRINTT
**Usage:** `<PRINTT table width [height] [skip]>`

Print table (string) in rectangle defined by width and height. Default height is 1. If skip is given then that number of characters is skipped between lines.

> **Note:** ZILF supports PRINTT in versions 5-.

**History:** Zapf syntax: PRINTT, Inform syntax: print_table

---

### PRINTU
**Usage:** `<PRINTU number>`

Print unicode-character number.

> **Note:** ZILF supports PRINTU in versions 5-.

**History:** Zapf syntax: PRINTU, Inform syntax: print_unicode

---

### PROG
**Usage:** `<PROG [activation] (bindings ...) [decl] expressions ...>`

MDL built-in function that defines a program block with its own set of bindings. PROG is similar to BIND and REPEAT but unlike BIND it creates a default activation (like REPEAT) at the start of the block and doesn't have an automatic AGAIN at the end of the block (like REPEAT). It is possible to name an atom to the activation but it is not necessary. AGAIN and RETURN inside a PROG-block will start the block over or return from the block.

The decl is used to specify the valid TYPE of the variables. In its simplest form decl is formatted like: #DECL ((X) FIX), meaning that X must be of the TYPE FIX. For more information on how to format the decl see GDECL.

> **Note:** In Z-code (inside a ROUTINE), DO-FUNNY-RETURN? controls whether <RETURN value> exits the enclosing ROUTINE (when true, default in V5+) or the PROG block (when false, default in V3-4). Bare <RETURN> always exits the PROG block. Also see AGAIN, BIND, REPEAT and RETURN.

---

### PTABLE
**Usage:** `<PTABLE [(flags ...)] values ...>`

ZIL library function that defines a table containing the specified values and with the PURE flag (see TABLE about PURE and other flags).

> **Note:** TABLE is a ZIL-specific structure that can be used both outside and inside ROUTINES.

---

### PTSIZE
**Usage:** `<PTSIZE property-value>`

Z-code built-in function that gets the property size in bytes at property-address.

> **Note:** ZILF supports PTSIZE in all versions.

**History:** Zapf syntax: PTSIZE, Inform syntax: get_prop_len

---

### PUSH
**Usage:** `<PUSH value>`

Z-code built-in function that pushes value on the game stack.

> **Note:** ZILF supports PUSH in all versions.

**History:** Zapf syntax: PUSH, Inform syntax: push

---

### PUT
**Usage:** `<PUT table offset value>`

MDL built-in function (<PUT structure index new-value>) that sets the element at 1-based index in structure to new-value.

Z-code built-in function (<PUT table offset value>) that puts a 16-bit WORD value in the table at 0-based word position offset. Actual address is table-address+offset*2. Note that table can be a byte-address in dynamic memory. 

Also see BACK, GET, GETB, PUTB and REST.

> **Note:** ZILF supports PUT in all versions.

**History:** Zapf syntax: PUT, Inform syntax: storew

---

### PUTB
**Usage:** `<PUTB table offset value>`

ZIL library function (<PUTB table index new-value>) and Z-code built-in (<PUTB table offset value>) that writes a 1-byte value into table at the given byte offset (usable both outside and inside ROUTINEs). The actual address is table-address+offset. Note that table can be a byte-address in dynamic memory.

Also see BACK, GET, GETB, PUT and REST.

> **Note:** ZILF supports PUTB in all versions.

**History:** Zapf syntax: PUTB, Inform syntax: storeb

---

### PUTP
**Usage:** `<PUTP object property value>`

Z-code built-in function that puts value into property on the object.

> **Note:** ZILF supports PUTP in all versions.

**History:** Zapf syntax: PUTP, Inform syntax: put_prop

---

### QUIT
**Usage:** `<QUIT [exit-code]>`

**Alternative Usage:** `<QUIT>`

MDL built-in function (<QUIT [exit-code]>) that exits ZILF interpreter mode and returns to the operating system with exit-code.

Z-code built-in function (<QUIT>) that immediately halts Z-machine game execution (takes no arguments).

> **Note:** ZILF supports QUIT in all versions.

**History:** Zapf syntax: QUIT, Inform syntax: quit

---

### RANDOM
**Usage:** `<RANDOM range>`

Z-code built-in function that returns a random number between 1 and range. If range is negative the randomizer is reseeded with -range (absolute value of range).

> **Note:** ZILF supports RANDOM in all versions.

**History:** Zapf syntax: RANDOM, Inform syntax: random

---

### READ
**Usage:** `<READ text [parse] [time] [routine]>  ;  "Versions 5-"`

**Alternative Usage:** `<READ text parse [time] [routine]>  ;  "Version 4"`

Read text from the keyboard and parse it. Result is stored in two byte-tables. Byte 0 in text must contain the max-size of the buffer and if parse is supplied, byte 0 of it must contain a max number of words that will be parsed.

In version 5-, byte 1 should be 0 before READ begins, otherwise READ appends characters starting from value in byte 1.

After READ, text contains:

Version 1 - 4,

* Byte 0, Max number of chars read into the buffer
* Byte 1-, The typed chars all converted to lowercase 

Version 5 -,

* Byte 0, Max number of chars read into the buffer
* Byte 1, Actual number of chars read into the buffer 
* Byte 2-, The typed chars all converted to lowercase

`parse` contains: 

* Byte 0, Max number of words parsed
* Byte 1, Actual number of words parsed
* Byte 2-3, Address to first word in dictionary (0 if word is not in it)
* Byte 4, Length of first word
* Byte 5, Start position (in text) of first word
* Byte 6-9, Second word

> **Note:** `<READ text parse>`  ;  Versions 1-3

**History:** Zapf syntax: READ, Inform syntax: aread / sread

---

### REMOVE
**Usage:** `<REMOVE object>`

MDL built-in function (<REMOVE pname oblist> or <REMOVE atom>) that removes an ATOM from an OBLIST.

Z-code built-in function (<REMOVE object>) that detaches object from its parent object. To reattach it, see MOVE.

> **Note:** ZILF supports REMOVE in all versions.

**History:** Zapf syntax: REMOVE, Inform syntax: remove_obj

---

### REPEAT
**Usage:** `<REPEAT [activation] (bindings ...) [decl] expressions ...>`

MDL built-in function that  defines a program block with its own set of bindings. REPEAT is similar to BIND and PROG but unlike BIND it creates a default activation (like PROG) at the start of the block but unlike PROG it also has an automatic AGAIN at the end of the block. It is possible to name an atom to the activation but it is not necessary. A REPEAT-block repeatedly executes expressions until it encounters a RETURN statement that will exit the block. 

The decl is used to specify the valid TYPE of the variables. In its simplest form decl is formatted like: #DECL ((X) FIX), meaning that X must be of the TYPE FIX. For more information on how to format the decl see GDECL.

> **Note:** In Z-code (inside a ROUTINE), DO-FUNNY-RETURN? controls whether <RETURN value> exits the enclosing ROUTINE (when true, default in V5+) or the REPEAT block (when false, default in V3-4). Bare <RETURN> always exits the REPEAT block. Also see AGAIN, BIND, PROG and RETURN.

---

### REST
**Usage:** `<REST structure [count]>`

MDL built-in function (<REST structure [count]>) that returns structure without its first count elements (default 1).

Z-code built-in function (<REST table [bytes]>) that returns a table address advanced by bytes (default 1). Note that this is not a copy of the structure, it is pointing to the same structure with another starting element. 

structure must be an object that STRUCTURED? evaluates to true.

> **Note:** Note that TABLE is not a structure.
>
> Also see BACK, LENGTH, NTH, PUT, SUBSTRUC and TOP.

---

### RESTART
**Usage:** `<RESTART>`

Restarts the game. No questions asked. The only things that survive a restart are bit 0 and bit 1 of Flags 2 in the header (setting for transcribing and monospace).

> **Note:** ZILF supports RESTART in all versions.

**History:** Zapf syntax: RESTART, Inform syntax: restart

---

### RESTORE
**Usage:** `<RESTORE>  ;  "Versions 1-4"`

**Alternative Usage:** `<RESTORE [table] [bytes] [filename]> ; "Versions 5-"`

RESTORE a game to a previously saved state. All questions about filename and path are asked by the interpreter.

* If `RESTORE` fails, game execution continues with the next statement after RESTORE.
* If `RESTORE` is successful, game execution continues from where the SAVE was issued (SAVE returns 2 in this case).

See The Inform Designer’s Manual (ch. §42, p. 319) and The Z-machine Standards Document for a description about how to SAVE and RESTORE auxiliary files.

> **Note:** ZILF supports RESTORE in all versions.

**History:** Zapf syntax: RESTORE, Inform syntax: restore

---

### RETURN
**Usage:** `<RETURN [value] [activation]>`

MDL built-in function that  returns value from program-block defined by activation. True is returned if no value is specified. If activation is not specified RETURN will exit the current defined program-block where an automatic activation was created (PROG and REPEAT creates automatic activations, BIND does not).

In practice RETURN exits the current program-block and returns value  to the outer program-block defined by BIND (needs activation), PROG or REPEAT.

> **Note:** In Z-code (inside a ROUTINE, Zapf: RETURN, Inform: ret), <RETURN [value] [activation]> returns 1 (true) if no value is given, or exits the specified/enclosing block; when DO-FUNNY-RETURN? is true (default V5+), <RETURN value> without an activation exits the ROUTINE. See AGAIN, BIND, DO, PROG and REPEAT.

---

### RFALSE
**Usage:** `<RFALSE>`

Z-code built-in function that  always exits routine and returns false (0). Note that this differs from RETURN that can both exit program blocks and routines.

> **Note:** ZILF supports RFALSE in all versions.

**History:** Zapf syntax: RFALSE, Inform syntax: rfalse

---

### RFATAL
**Usage:** `<RFATAL>`

Z-code built-in function that always exits routine and returns FATAL-VALUE (2). Note that this differs from RETURN that can both exit program blocks and routines.

---

### RSTACK
**Usage:** `<RSTACK>`

Z-code built-in function that pops value from the game stack and returns that value.

> **Note:** ZILF supports RSTACK in all versions.

**History:** Zapf syntax: RSTACK, Inform syntax: ret_popped

---

### RTRUE
**Usage:** `<RTRUE>`

Z-code built-in function that always exits routine and returns true (1). Note that this differs from RETURN that can both exit program blocks and routines.

> **Note:** ZILF supports RTRUE in all versions.

**History:** Zapf syntax: RTRUE, Inform syntax: rtrue

---

### SAVE
**Usage:** `<SAVE>  ;  Versions 1-4,` | `<SAVE [table] [bytes] [filename]>  ;  Versions 5-`

Z-code built-in function that saves a game state that later can be restored. All questions about filename and path are asked by the interpreter. 

SAVE returns 0 if SAVE fails and 1 if it is successful. 

SAVE also can return 2. That means this is a continuation from a successful RESTORE.

See RESTORE on code example on SAVE and RESTORE.

See The Inform Designer’s Manual (ch. §42, p. 319) and The Z-machine Standards Document for a description about how to SAVE and RESTORE auxiliary files.

> **Note:** ZILF supports SAVE in all versions.

**History:** Zapf syntax: SAVE, Inform syntax: save

---

### SCREEN
**Usage:** `<SCREEN window-number>`

Z-code built-in function that selects window-number for text output. Note that in versions 3-5 only the lower screen (window-number = 0) has text-buffering and word-wrap.

> **Note:** ZILF supports SCREEN in versions 3-.

**History:** Zapf syntax: SCREEN, Inform syntax: set_window

---

### SCROLL
**Usage:** `<SCROLL window-number pixels>`

Z-code built-in function that scrolls window-number up (pixels is positive) or down (pixels is negative) by the number of supplied pixels. New lines are empty (background color).

> **Note:** ZILF supports SCROLL in versions 6-.

**History:** Zapf syntax: SCROLL, Inform syntax: scroll_window

---

### SET
**Usage:** `MDL: <SET atom value [environment]>,` | `Zapf: <SET name value>`

MDL built-in function that asigns a value to the local atom. It is possible to supply an environment for SET. See EVAL for more about the environment.

Z-code built-in function that stores value in local variable name.

> **Note:** ZILF supports SET in all versions.

**History:** Zapf syntax: SET, Inform syntax: store

---

### SETG
**Usage:** `MDL: <SETG atom value>,` | `Zapf: <SETG name value>`

MDL built-in function that assigns a value to the global atom. If an atom is already assigned a value, it is changed.

Z-code built-in function that Store value in global variable name. The name variable must be declared with GLOBAL outside the ROUTINE.

> **Note:** ZILF supports SETG in all versions.

**History:** Zapf syntax: SETG, Inform syntax: store

---

### SHIFT
**Usage:** `<SHIFT number places>`

**Alternative Usage:** `<LSH number places>`

Bitwise shift. Shift number left when places is positive and right if it is negative. When right shifting the sign is not preserved (0 is always shifted in).

1000 0000 0000 1010  -->  0100 0000 0000 0101

Also see ASH.

> **Note:** ZILF supports SHIFT in versions 5-.

**History:** Zapf syntax: SHIFT, Inform syntax: log_shift

---

### SOUND
**Usage:** `<SOUND number [effect] [volume]>  ;  "Versions 3-4",` | `<SOUND number [effect] [volrep] [routine]>  ;  "Versions 5-"`

Z-code built-in  that plays sound number (1 = high-pitch beep, 2 = low-pitch beep and 3- is user defined). 

Valid entries for effect are 1 = prepare, 2 = start, 3 = stop and 4 = finished with. 

The volrep is calculated as 256 * repetitions + volume. Repetitions can be 0-255 (255 = infinite) and volume 1-8, 255 (1 =  quiet, 8 = loud, 255 = loudest possible. Note that repetitions only are valid from version 5 onward. For version 5 and later a repetition equal to 0 is considered illegal but it’s suggested that interpreters should treat this as a request to play the sound once. 

If routine is supplied it is called after sound is finished. 

See The Inform Designer’s Manual (ch. §42, p. 315-316 and ch. §43) and The Z-machine Standards Document for a description about how to include sound in games.

> **Note:** ZILF supports SOUND in versions 3-.

**History:** Zapf syntax: SOUND, Inform syntax: sound_effect

---

### SPLIT
**Usage:** `<SPLIT number>`

Z-code built-in function that splits the screen  in two parts with the upper part having number rows. If number is 0 the screen is unsplit.The upper screen is window-number 1 and the lower screen is window-number 0.

See SCREEN for example on how to use SPLIT.

> **Note:** ZILF supports SPLIT in versions 3-.

**History:** Zapf syntax: SPLIT, Inform syntax: split_window

---

### T?
**Usage:** `<T? expression>`

Predicate. Test if expression evaluates to true ( not 0).

---

### TABLE
**Usage:** `<TABLE [(flags ...)] values ...>`

ZIL library function that defines a table containing the specified values. The following flags control the table format.

*   WORD causes the elements to be 2-byte words. This is the default.

*  BYTE causes the elements to be single bytes.

*  LEXV  causes the elements to be 4-byte records. If default values are given to ITABLE with this flag, they will be split into groups of three: the first compiled as a word, the next two compiled as bytes. The table is also prefixed with a byte indicating the number of records, followed by a zero byte.

*  STRING causes the elements to be single bytes and also changes the initializer format. This flag may not be used with ITABLE. When this flag is given, any values given as strings will be compiled as a series of individual ASCII characters, rather than as string addresses.

The following flags alter the table without changing its basic format:

*  LENGTH  causes a length marker to be written at the beginning of the table, indicating the number of elements that follow. The length marker is a byte if BYTE or STRING are also given; otherwise the length marker is a WORD. This flag is ignored if LEXV is given.

*  PURE causes the table to be compiled into static memory (ROM).

The flag LENGTH is implied in LTABLE and PLTABLE. The flag PURE is implied in PTABLE and PLTABLE.

> **Note:** TABLE is a ZIL-specific structure that can be used both outside and inside ROUTINES.

---

### TELL
**Usage:** `<TELL token-commands ...>`

Print formatted text to screen. There is a set built-in tokens that can be replaced with TELL-TOKENS or expanded with ADD-TELL-TOKENS.

The built-in tokens are:

| Pattern | Form | Description |
|---|---|---|
| (CR CRLF) | `<CRLF>` | Print CR |
| D * | `<PRINTD .X>` | Print object-description |
| N * | `<PRINTN .X>` | Print number |
| C * | `<PRINTC .X>` | Print character |
| B * | `<PRINTB .X>` | Print unpacked-string |

---

### THROW
**Usage:** `<THROW value stack-frame>`

Z-code built-in function that is used with CATCH. THROW sets the stack to stack-frame and returns value (the result is that execution returns from the routine where the stack-frame was "caught" with value as the routines return value. Also see CATCH.

> **Note:** ZILF supports THROW in versions 5-.

**History:** Zapf syntax: THROW, Inform syntax: throw

---

### USL
**Usage:** `<USL>`

Z-code built-in function that updates the status line. This command is only recognized in version 3.

> **Note:** ZILF supports USL in version 3.

**History:** Zapf syntax: USL, Inform syntax: show_status

---

### VALUE
**Usage:** `MDL: <VALUE atom [environment]>,` | `Zapf: <VALUE name/number>`

MDL built-in function that returns the value of an atom. If  the atom has an LVAL then the LVAL is returned, otherwise the GVAL of the atom is returned. It is possible to supply an environment for VALUE. See EVAL for more about the environment.

Z-code built-in function that loads name/number. Note that this command is mostly redundant and rarely used.

> **Note:** ZILF supports VALUE in all versions.

**History:** Zapf syntax: VALUE, Inform syntax: load

---

### VERIFY
**Usage:** `<VERIFY>`

Z-code built-in function that returns true if sum($0040:PLENTH (byte 26-27 in header)) MOD $10000 = PCHKSUM (byte 28-29 in header), otherwise false.

> **Note:** ZILF supports VERIFY in all versions.

**History:** Zapf syntax: VERIFY, Inform syntax: verify

---

### VERSION?
**Usage:** `<VERSION? (version-spec body ...) ...>`

ZIL library predicate that tells the compiler to use different code-blocks depending on the setting of VERSION. 

The version-spec can be:
* 3 (ZIP) 
* 4 (EZIP) 
* 5 (XZIIP) 
* 6 (YZIP) 
* 7 
* 8 
* ELSE/T

---

### WINATTR
**Usage:** `<WINATTR window-number flags operation>`

Change flags for `window-number`.

The `flags` are:

| Bit | Definition |
|---|---|
| 0 | Keep text inside margin |
| 1 | Scroll when reaching bottom |
| 2 | Copy text to stream 2 (printer) |
| 3 | Buffer text and word-wrap |

The `operations` are:

| Operation | Definition |
|---|---|
| 0 | Set to `flags` |
| 1 | Set bits supplied (BOR) |
| 2 | Clear bits supplied |
| 3 | Reverse bits supplied |

> **Note:** ZILF supports WINATTR in versions 6-.

**History:** Zapf syntax: WINATTR, Inform syntax: window_style

---

### WINGET
**Usage:** `<WINGET window-number property>`

Z-code built-in function that reads property on window-number.

> **Note:** ZILF supports WINGET in versions 6-.

**History:** Zapf syntax: WINGET, Inform syntax: get_wind_prop

---

### WINPOS
**Usage:** `<WINPOS window-number row column>`

Z-code built-in function that moves window-number to position row column (pixels). (1, 1) is in the top left corner.

> **Note:** ZILF supports WINPOS in versions 6-.

**History:** Zapf syntax: WINPOS, Inform syntax: move_window

---

### WINPUT
**Usage:** `<WINPUT window-number property value>`

Z-code built-in function that writes value to property window-number.

> **Note:** ZILF supports WINPUT in versions 6-.

**History:** Zapf syntax: WINPUT, Inform syntax: put_wind_prop

---

### WINSIZE
**Usage:** `<WINSIZE window-number height width>`

Z-code built-in function that changes window-number size.

> **Note:** ZILF supports WINSIZE in versions 6-.

**History:** Zapf syntax: WINSIZE, Inform syntax: window_size

---

### XPUSH
**Usage:** `<XPUSH value stack>`

Z-code built-in function that pushes value on the stack.

> **Note:** ZILF supports XPUSH in versions 6-.

**History:** Zapf syntax: XPUSH, Inform syntax: push_stack

---

### ZWSTR
**Usage:** `<ZWSTR src-table length offset dest-table>`

Z-code built-in function that encodes length characters starting at offset from ZSCII word zscii-text and stores result in 6-byte Z-encoded dest-table.

> **Note:** ZILF supports ZWSTR in versions 5-.

**History:** Zapf syntax: ZWSTR, Inform syntax: encode_text

---