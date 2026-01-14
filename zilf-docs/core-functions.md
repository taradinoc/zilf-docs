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

### END-SEGMENT
**Usage:** `<END-SEGMENT>`

ZIL library function that terminates the current code and data group, returning to main game memory. END-SEGMENT pairs with BEGIN-SEGMENT.

> **Note:** ZILF ignores this and always returns FALSE.

**History:** Having been used in a few InfoCom projects, BEGIN-SEGMENT was notably used in The Abyss, an unreleased interactive fiction game written by Bob Bates for Infocom under historical source code for the game, entitled The Abyss Source Code Collection.

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

---

### QUOTE
**Usage:** `<QUOTE value>`

MDL built-in function that returns unevaluated value.

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
**Usage:** `<SET atom value [environment]>`

MDL built-in function that asigns a value to the local atom.

> **Note:** It is possible to supply an environment for SET. See EVAL for more about the environment.

---

### SETG
**Usage:** `<SETG atom value>`

MDL built-in function that assigns a value to the global atom. If an atom is already assigned a value, it is changed.

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
**Usage:** `<VALUE atom [environment]>`

MDL built-in function that returns the value of an atom. If  the atom has an LVAL then the LVAL is returned, otherwise the GVAL of the atom is returned.

> **Note:** It is possible to supply an environment for VALUE. See EVAL for more about the environment.

---