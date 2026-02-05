[← Back to Main Index](./index.md)

# Core Functions
---

### ASCII
**Usage:** `<ASCII {number | character}>`

MDL built-in function that converts a number to a character or a character to a number.

---

### ATOM
**Usage:** `<ATOM pname>`

MDL built-in that returns a newly created ATOM with pname (string). The ATOM is not on any OBLIST and therefore has the trailer !-#FALSE () attached to it.

---

### AVALUE
**Usage:** `<AVALUE asoc>`

MDL built-in function that returns the value part from an asoc entry, of TYPE ASOC, in the ASSOCIATION chain.

> **Note:** See ASSOCIATIONS, GETPROP, INDICATOR, ITEM, NEXT and PUTPROP.

---

### BEGIN-SEGMENT
**Usage:** `<BEGIN-SEGMENT value>`

ZIL library function that groups code and data into segments of memory outside the main game memory. BEGIN-SEGMENT pairs with END-SEGMENT.

> **Note:** ZILF ignores this and always returns FALSE.

**History:** Having been used in a few InfoCom projects, BEGIN-SEGMENT was notably used in The Abyss, an unreleased interactive fiction game written by Bob Bates for Infocom under historical source code for the game, entitled The Abyss Source Code Collection.

---

### DEFAULT-DEFINITION
**Usage:** `<DEFAULT-DEFINITION name body ...>`

ZIL library function that defines a “replaceable” block with the given name.  

If neither DELAY-DEFINITION nor REPLACE-DEFINITION was previously called for the given name, then the body is evaluated, and this function returns the result of evaluating the last element of the body. 

If the block was replaced (via REPLACE-DEFINITION), the replacement body supplied earlier is used instead. 

If the block was delayed (via DELAY-DEFINITION), the body is ignored, and this function returns FALSE.

> **Note:** It is possible to do the same by setting REDEFINE to true. This actually makes it possible to change ALL definitions (it is the last one that becomes the one actually compiled). 

See DELAY-DEFINITION and REPLACE-DEFINITION.

---

### DEFAULTS-DEFINED
**Usage:** `<DEFAULTS-DEFINED>`

ZIL library function.

> **Note:** ZILF ignores this and always returns FALSE.

---

### DEFINE
**Usage:** `<DEFINE name [activation] arg-list [decl] expressions ...>`

MDL built-in function that  assigns the global variable name with a FUNCTION. See FUNCTION for an explanation of activation, arg-list, decl and expressions.

> **Note:** <DEFINE name ...> is equivalent to <SETG name #FUNCTION ...> with the exception that DEFINE protects from overwriting a name with a new FUNCTION (this behaviour can be changed by setting REDEFINE to true, instead of false).

---

### DEFINE-GLOBALS
**Usage:** `<DEFINE-GLOBALS group-name (atom-or-adecl [{BYTE | WORD}] [initializer]) ...>`

ZIL library function that defines a set of macros that can be used for global storage in Z-code, similar to global variables. 

Each atom-or-adecl becomes the name of a new macro which can be called with no arguments (to read the global value) or one argument (to write it). The optional initializer sets the initial value, as in GLOBAL. BYTE or WORD can be specified to set the global’s size; WORD is the default.

> **Note:** ZILF ignores the group-name.  

See FUNNY-GLOBALS? for a more convenient way to bypass the Z-machine’s global variable limit. (In fact, ZILF implements DEFINE-GLOBALS by turning on FUNNY-GLOBALS? and defining a global variable for each macro.)

---

### DEFINITIONS
**Usage:** `<DEFINITIONS package-name>`

MDL package system that is exactly the same as PACKAGE except that there is no internal OBLIST with DEFINITIONS, 

See END-DEFINITIONS, INCLUDE, INCLUDE-WHEN, PACKAGE and RENTRY.

> **Note:** To activate a package-name INCLUDE or INCLUDE-WHEN is used.

---

### DEFMAC
**Usage:** `<DEFMAC name [activation] arg-list [decl] expressions ...>`

MDL built-in function that  has the same syntax as DEFINE, but defines a MACRO instead of a FUNCTION. A MACRO is evaluated two times, the first evaluation inserts the arguments in the MACRO and creates an object that is evaluated during the second evaluation. The first evaluation is done at “top-level”, in other words during compilation. EXPAND is used to perform the first evaluation.

> **Note:** Note that two identical calls to a MACRO always generate the same result from the first evaluation.

---

### DELAY-DEFINITION
**Usage:** `<DELAY-DEFINITION name>`

ZIL library function that tells ZILF that a REPLACE-DEFINITION for name should be expected thus the DEFAULT-DEFINITION never is evaluated for the name. This means that REPLACE-DEFINITION can appear after the DEFAULT-DEFINITION.

DELAY-DEFINITION also means that the body of REPLACE-DEFINITION will be evaluated at the place of REPLACE-DEFINITION. 

See DEFAULT-DEFINITION and REPLACE-DEFINITION.

---

### EMPTY?
**Usage:** `<EMPTY? structure>`

MDL built-in predicate that returns true if structure contains no elements, otherwise false.

> **Note:** structure must be an object that STRUCTURED? evaluates to true.

---

### END-DEFINITIONS
**Usage:** `<END-DEFINITIONS>`

MDL package system that is an alias of ENDBLOCK.

> **Note:** See DEFINITIONS.

---

### END-SEGMENT
**Usage:** `<END-SEGMENT>`

ZIL library function that terminates the current code and data group, returning to main game memory. END-SEGMENT pairs with BEGIN-SEGMENT.

> **Note:** ZILF ignores this and always returns FALSE.

**History:** Having been used in a few InfoCom projects, BEGIN-SEGMENT was notably used in The Abyss, an unreleased interactive fiction game written by Bob Bates for Infocom under historical source code for the game, entitled The Abyss Source Code Collection.

---

### ENDBLOCK
**Usage:** `<ENDBLOCK>`

MDL built-in function that  pops back, rebinds and returns the local ATOM OBLIST to the state it had before the call to BLOCK. ENDBLOCK without previous BLOCK (or PACKAGE, DEFINITIONS, etc) results in an error.

---

### ENDLOAD
**Usage:** `<ENDLOAD>`

ZIL library function.

> **Note:** ZILF ignores this and always returns FALSE.

---

### ENDPACKAGE
**Usage:** `<ENDPACKAGE>`

MDL package system that is an alias to ENDBLOCK.

> **Note:** See PACKAGE.

---

### ENDSECTION
**Usage:** `<ENDSECTION>`

MDL package system that is an alias to ENDBLOCK.

> **Note:** See DEFINITIONS.

---

### EVAL
**Usage:** `<EVAL value [environment]>`

MDL built-in function that evaluates value (usually a FORM created by FORM or QUOTE).

> **Note:** It is possible to supply an environment for EVAL. This tells EVAL from which environment. EVAL should take variable bindings. See The MDL Programming Language, chap. 9.7 for more about the environment.

---

### GLOBAL
**Usage:** `<GLOBAL atom default-value [decl] [size]>`

ZIL library function that declares a global variable atom, which can laater be used inside a ROUTINE. The variable is initialized with default-value.

> **Note:** ZILF ignores the DECL because DECL is checked in code that runs at compile time (i.e. MDL code); however, there is no type checking for compiled code inside routines, at runtime or compile time.

For example, the following:
<GDECL (BAR) FIX> T
<SETG BAR "fsdf">

Outputs this error: 
[error MDL0206] <stdin>:1: expected GVAL of BAR to match DECL FIX, but got "fdsf"

---

### OR
**Usage:** `<OR expressions...>`

MDL built-in function that is a boolean OR. Requires that one of the expressions evaluates to true to return true. Exits on the first expression that evaluates to true (rest of expressions are not evaluated).

> **Note:** Because false is its own TYPE outside a routine OR returns #FALSE if all expressions are false or the value of the first true expression.

---

### OR?
**Usage:** `<OR? Expressions ...>`

MDL built-in function that returns the same result as OR with the difference that all exressions are evaluated.

> **Note:** <OR? <=? 1 2> <=? 1 1>>  ; True 
 <OR? <=? 1 1> <SET X 2>> ;  X is set to 2 because all expressions are evaluated

---

### PICFILE
**Usage:** `<PICFILE>`

ZIL library function that is a compiler directive used to associate a graphics resource file with a game, and Infocom's version of PICFILE translates to a ZAP .PICFILE directive.

> **Note:** The current version of ZILF ignores PICFILE and always returns FALSE because modern interpreters do not support Infocom's graphics format. The next release of ZILF will bundle images into Blorb files (without ZAPF).

---

### PNAME
**Usage:** `<PNAME atom>`

MDL built-in function for "printed name", which returns a newly created string copy of the atom's pname.

> **Note:** PNAME never prints an ATOMs trailers, unlike UNPARSE, and is therefore quicker.

---

### PRIMTYPE
**Usage:** `<PRIMTYPE value>`

MDL built-in function that evaluates to the primitive type of value.

> **Note:** The primitive types are  ATOM, FIX, LIST, STRING, TABLE and VECTOR.

---

### PRIN1
**Usage:** `<PRIN1 value [channel]>`

MDL built-in function that prints the evaluated representation of value to channel (default for channel is <LVAL OUTCHAN> - the console). PRIN1 also returns the evaluated representation of value.

---

### PRINC
**Usage:** `<PRINC value [channel]>`

MDL built-in function that returns the evaluated representation of value.

> **Note:** PRINC is just like PRIN1, except for STRING and CHARACTER where surrounding double quote (") and initial !\ is suppressed.

---

### PRINT
**Usage:** `<PRINT value [channel]>`

MDL built-in function that returns the evaluated representation of value.

> **Note:** PRINT is just like PRIN1, except that it first prints a CRLF, then the evaluated representation of value and lastly a space.

---

### PTABLE
**Usage:** `<PTABLE [(flags ...)] values ...>`

ZIL library function that defines a table containing the specified values and with the PURE flag (see TABLE about PURE and other flags).

> **Note:** TABLE is a ZIL-specific structure that can be used both outside and inside ROUTINES.

---

### PUTREST
**Usage:** `<PUTREST list new-rest>`

MDL built-in function that replaces the REST of list with new-rest and returns list. In other words, list is assigned the first element of list and then all the elements from new-rest. 

Note that this actually changes the list.

---

### QUIT
**Usage:** `<QUIT [exit-code]>`

MDL built-in function that exits ZILF (interpreter mode) and returns to the operating system with exit-code.

> **Note:** ZILF supports QUIT in all versions.

**History:** Zapf syntax: QUIT, Inform syntax: quit

---

### QUOTE
**Usage:** `<QUOTE value>`

MDL built-in function that returns unevaluated value.

---

### READSTRING
**Usage:** `<READSTRING buffer-str channel [max-length-or-stop-chars]>`

MDL built-in function that reads bytes from the channel into buffer-str and returns the number of bytes read into buffer-str. The buffer-str needs to have room for the input. For each call to READSTRING it either reads bytes to fill up the buffer-str or until max-length-or-stop-chars is reached. The max-length-or-stop-chars can be a FIX number of bytes or a STRING that halts input.

> **Note:** READSTRING returns the actual number of bytes read and returns 0 when the EOF is reached.

---

### RENTRY
**Usage:** `<RENTRY atoms ...>`

MDL built-in function that creates/moves one or more ATOMs to <ROOT> in a PACKAGE or DEFINITION. RENTRY is only valid inside a PACKAGE or DEFINITION, if it's used outside an error is raised.

> **Note:** See DEFINITIONS, ENTRY, INCLUDE, INCLUDE-WHEN, PACKAGE, USE, USE-WHEN.

---

### REPEAT
**Usage:** `<REPEAT [activation] (bindings ...) [decl] expressions ...>`

MDL built-in function that  defines a program block with its own set of bindings. REPEAT is similar to BIND and PROG but unlike BIND it creates a default activation (like PROG) at the start of the block but unlike PROG it also has an automatic AGAIN at the end of the block. It is possible to name an atom to the activation but it is not necessary. A REPEAT-block repeatedly executes expressions until it encounters a RETURN statement that will exit the block. 

The decl is used to specify the valid TYPE of the variables. In its simplest form decl is formatted like: #DECL ((X) FIX), meaning that X must be of the TYPE FIX. For more information on how to format the decl see GDECL.

> **Note:** Also see AGAIN, BIND, PROG and RETURN for more details on how to control program flow.

---

### REPLACE-DEFINITION
**Usage:** `<REPLACE-DEFINITION name body ...>`

ZIL library function that  tells the compiler this block of code defined by name should replace a later  DEFAULT-DEFINITION block of code with the same name. 

This is usually used when there is a library that is inserted (like "parser.zil") where some definitions are possible to override.

> **Note:** Note that the REPLACE-DEFINITION is required to appear before the DEFAULT-DEFINITION. It is possible to do the same by setting REDEFINE to true. This actually makes it possible to change ALL definitions (it is the last one that becomes the one actually compiled).

See DEFAULT-DEFINITION and REPLACE-DEFINITION.

---

### ROOT
**Usage:** `<ROOT>`

MDL built-in function that returns the OBLIST containing names of primitives (the same as <2 .OBLIST>).

> **Note:** Initially contains all predefined SUBRs or FSUBRs, as well as OBLIST, DEFAULT, T, etc.

---

### ROUTINE
**Usage:** `<ROUTINE name [activation-atom] arg-list body ...>`

ZIL library function that is the central building block of a ZIL-program. Inside the ROUTINE it is only possible to use the reduced instruction set that can be executed on the Z-machine. It is the instructions inside the ROUTINEs that are compiled to the actual ZIP-program.

> **Note:** ROUTINE defines a program block with its own set of bindings. It is possible to specify an activation-atom to use as an argument to control the RETURN statement inside the ROUTINE. 

The arg-list is formatted the same way as FUNCTION, but the legal tokens is reduced to these:

Arguments: The required arguments for this ROUTINE. The arguments are bound to local variables inside this ROUTINE. 

"OPT": The optional arguments for this ROUTINE. The arguments are bound to local variables inside this ROUTINE and can be defined with a default value. "OPTIONAL" is an alias for "OPT".

"AUX": Followed by any number of ATOMs that becomes local variables inside this ROUTINE and can be defined with a default value. "EXTRA" is a alias for "AUX". 

"NAME": Followed by an ATOM that becomes the activation-atom for this ROUTINE. This is equivalent to naming the activation-atom  before the arg-list. "ACT" is an alias for "NAME". 

Default values for "OPT" and "AUX" are defined by a two-element LIST whose first element is the ATOM and the second element it is assigned to.

<ROUTINE TEST ("AUX" (X 1) (Y 2)) <+ .X .Y>>  Means that the local variables X and Y are initially assigned 1 and 2. After the arg-list follows the ZIL-instructions that makes up the body of the ROUTINE.

---

### SET
**Usage:** `MDL: <SET atom value [environment]>,
Zapf: <SET name value>`

MDL built-in function that asigns a value to the local atom. It is possible to supply an environment for SET. See EVAL for more about the environment.

Z-code built-in function that stores value in local variable name.

> **Note:** ZILF supports SET in all versions.

**History:** Zapf syntax: SET, Inform syntax: store

---

### SETG
**Usage:** `MDL: <SETG atom value>,
Zapf: <SETG name value>`

MDL built-in function that assigns a value to the global atom. If an atom is already assigned a value, it is changed.

Z-code built-in function that Store value in global variable name. The name variable must be declared with GLOBAL outside the ROUTINE.

> **Note:** ZILF supports SETG in all versions.

**History:** Zapf syntax: SETG, Inform syntax: store

---

### SETG20
**Usage:** `<SETG20 atom value>`

ZIL library function that assigs a value to the global atom. If an atom is already assigned a value, it is changed. SETG20 is an alias for SETG.

---

### SPNAME
**Usage:** `<SPNAME atom>`

MDL built-in function for "shared printed name", which should return the same string of the atom's pname that is in its OBLIST (i.e. pointing to the same storage and therefore not able to change or modify).

> **Note:** ZILF treats SPNAME as an alias to PNAME and returns a string copy of the atom’s pname.

---

### STRING
**Usage:** `<STRING values ...>`

MDL built-in function that returns a concatenated string of all values. values can be character or string.

> **Note:** A string is a block of contiguous bytes where each byte holds a character. See more about STRING  structure in The MDL Programming Language, Appendix 1.

---

### TIME
**Usage:** `<TIME>`

MDL built-in function that is used for measuring CPU execution time, typically used for debugging ZILCH.

> **Note:** ZILF ignores this and always returns 1, because modern IDE's offer different methods of debugging ZILCH.

---

### TOP
**Usage:** `<TOP array>`

MDL built-in function that returns array with all elements put back in  array. TOP only works on the structures VECTOR or STRING (arrays) and not on a LIST (a LIST is only pointing forward).

> **Note:** The returned array is not a copy but pointing to the same array with another starting element. Also see BACK, NTH, PUT, REST and SUBSTRUC.

---

### VALID-TYPE?
**Usage:** `<VALID-TYPE? atom>`

MDL build-in function that returns the TYPE if the atom is a valid name of a TYPE (the atom name is in ALLTYPES), otherwise FALSE.

---

### VALUE
**Usage:** `MDL: <VALUE atom [environment]>, 
Zapf: <VALUE name/number>`

MDL built-in function that returns the value of an atom. If  the atom has an LVAL then the LVAL is returned, otherwise the GVAL of the atom is returned. It is possible to supply an environment for VALUE. See EVAL for more about the environment.

Z-code built-in function that loads name/number. Note that this command is mostly redundant and rarely used.

> **Note:** ZILF supports VALUE in all versions.

**History:** Zapf syntax: VALUE, Inform syntax: load

---