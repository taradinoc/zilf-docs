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

### BIND
**Usage:** `<BIND [activation] (bindings ...) [decl] expressions ...>`

MDL built-in function that defines a program block with its own set of bindings. BIND is similar to PROG and REPEAT but BIND doesn't create a default activation (like PROG and REPEAT) at the start of the block and doesn't have an automatic AGAIN at the end of the block (like REPEAT). If an activation is needed it must be specified. AGAIN and RETURN without specified activation inside a BIND-block will start over or return from the closest surrounding activation within the current function.

The decl is used to specify the valid TYPE of the variables. In its simplest form decl is formatted like: #DECL ((X) FIX), meaning that X must be of the TYPE FIX. For more information on how to format the decl see GDECL. 

Also see AGAIN, PROG, REPEAT and RETURN for more details how to control program flow.

---

### BLOAT
**Usage:** `<BLOAT>`

MDL built-in function that is used in MDL to temporarily expand available storage space to avoid unnecessary garbage collection when loading large files.

> **Note:** ZILF ignores this and always returns FALSE.

---

### BLOCK
**Usage:** `<BLOCK (oblist ...)>`

MDL built-in function that  pushes current binding of the local ATOM OBLIST and rebinds it with the LIST of oblist supplied as argument and returns the new <LVAL OBLIST>. Usually you want <ROOT> as the last oblist in LIST. <ENDBLOCK> then restores the local ATOM OBLIST to its previous value.

---

### BOUND?
**Usage:** `<BOUND? atom [environment]>`

MDL bulit-in predicate that returns true if the atom ever had a local value in the environment.

If no environment is supplied, the environment defaults to current scope. See EVAL for more about the environment.

---

### BYTE
**Usage:** `<BYTE number>`

**Alternative Usage:** `<CHTYPE number BYTE>`

ZIL library function that changes number of TYPE to #BYTE.

> **Note:** #BYTE number is alternative (MDL built-in) syntax.

---

### CHECK-VERSION?
**Usage:** `<CHECK-VERSION? version-spec>`

ZIL library predicate that  returns TRUE if current setting of VERSION is version-spec. Valid values for version-spec are ZIP, EZIP, XZIP, YZIP and the values 3-8.

---

### CHECKPOINT
**Usage:** `<CHECKPOINT>`

ZIL library function.

> **Note:** ZILF ignores this and always returns FALSE.

---

### CHRSET
**Usage:** `<CHRSET alphabet-number {string | character | number | byte} ...>`

ZIL library function that can be used in version 5+ to replace one or more of the standard character alphabets. The ZSCII alphabet table is divided up in three blocks of 26 characters each, totaling 78 characters.

The default layout is:

 Z-char 6789abcdef0123456789abcdef

current

A0      abcdefghijklmnopqrstuvwxyz

A1      ABCDEFGHIJKLMNOPQRSTUVWXYZ

A2       ^0123456789.,!?_#'"/\-:()

Text is then encoded into 2-byte words with 5-bits per character. The left-over bit is always 0 except on the last word where it is 1 to indicate that this is the last 2-byte word in the text.

--first byte-------   --second byte---

7    6 5 4 3 2  1 0   7 6 5  4 3 2 1 0

bit  --first--  --second---  --third--

Initially the A0 is the current alphabet. The characters 2, 3, 4 and 5 change alphabet according to this table:

(Z-char N)    from A0      from A1      from A2

(Z-char 2)      A1               A2               A0

(Z-char 3)      A2               A0               A1

(Z-char 4)      A1               A2               A0

(Z-char 5)      A2               A0               A1

Characters 2 and 3 change the alphabet for the next character (“shift”) and characters 4 and 5 change the alphabet permanently (“shift lock”).

> **Note:** CHARSET changes one character in one alphabet or changes an alphabet altogether.

---

### CLOSE
**Usage:** `<CLOSE channel>`

MDL built-in function that closes the channel opened by OPEN and returns the channel.

> **Note:** See READSTRING for and example of CLOSE.

---

### COMPILATION-FLAG
**Usage:** `<COMPILATION-FLAG atom-or-string [value]>`

ZIL library function that defines a COMPILATION-FLAG named atom-or-string initialized to value. If no value is supplied it defaults to TRUE. The name of the flag can either be an ATOM or a STRING whose text becomes the ATOM. 

The flag can then be read by COMPILATION-FLAG-VALUE or used as a condition in 
IFFLAG.

> **Note:** A call to COMPILATION-FLAG with an already defined ATOM changes the value of the ATOM.

---

### COMPILATION-FLAG-DEFAULT
**Usage:** `<COMPILATION-FLAG-DEFAULT atom-or-string value>`

ZIL library function that defines a COMPILATION-FLAG named atom-or-string initialized to value. If no value is supplied it defaults to TRUE. The name of the flag can either be an ATOM or a STRING whose text becomes the ATOM. 

The flag can then be read by COMPILATION-FLAG-VALUE or used as a condition in IFFLAG.

> **Note:** A call to COMPILATION-FLAG-DEFAULT with an already defined ATOM doesn't change the value of the ATOM.

---

### COMPILATION-FLAG-VALUE
**Usage:** `<COMPILATION-FLAG-VALUE atom-or-string>`

ZIL library function that returns the value of the COMPILATION-FLAG atom-or-string. If no atom-or-string is defined it returns FALSE.

---

### COMPILING?
**Usage:** `<COMPILING?>`

ZIL library function that is presumably  used in the MDL environment to determine if the game is compiled with ZILCH or running in the interpreter.

> **Note:** ZILF ignores this and always returns TRUE.

---

### CONS
**Usage:** `<CONS first list>`

MDL built-in function that adds first to the front of list, without copying list, and returns the resulting LIST. References to list are not affected.

> **Note:** CONS means "construct".

---

### CONSTANT
**Usage:** `<CONSTANT atom value>`

ZIL library function that defines an atom with value that will never be changed. The atom can is accessed inside a ROUTINE with GVAL (or ,) just like a GLOBAL atom. Defining a CONSTANT instead of a GLOBAL when possible can be vital information the compiler can use for optimization.

> **Note:** MSETG is an alias for CONSTANT.

---

### CRLF
**Usage:** `<CRLF [channel]>`

MDL built-in function that prints a carriage-return and a line-feed to channel (default for channel is <LVAL OUTCHAN>; the console). CRLF returns true.

---

### DECL-CHECK
**Usage:** `<DECL-CHECK boolean>`

MDL built-in function that turns off or on type declaration checking. It is initially on.

---

### DECL?
**Usage:** `<DECL? value pattern>`

MDL built-in predicate that returns TRUE if value checks against pattern, otherwise FALSE. For the format of the pattern, see GDECL.

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

### DEFINE-SEGMENT
**Usage:** `<DEFINE-SEGMENT>`

ZIL library function.

> **Note:** ZILF ignores this an always returns false.

---

### DEFINE20
**Usage:** `<DEFINE20 name [activation] arg-list [decl] expressions ...>`

ZIL library function that  is an alias for DEFINE except that it isn’t affected by MDL-ZIL mode: it always defines an MDL function.

> **Note:** DEFINE20 (and SETG20) are used in "MDL-ZIL"-files, where routines are defined with DEFINE - 42 - instead of ROUTINE, global variables are created with SETG instead of GLOBAL, etc. Presumably that was a way to run the games in MDL during development to avoid recompiling them. SETG20 and DEFINE20 are aliases for the MDL versions of SETG and DEFINE.

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

### ENTRY
**Usage:** `<ENTRY atoms ...>`

MDL package system that creates/moves one or more ATOMs to the external OBLIST in a PACKAGE. ENTRY is only valid inside a PACKAGE, if it's used outside an error is raised.

> **Note:** See PACKAGE, RENTRY, USE, USE-WHEN.

---

### EQVB
**Usage:** `<EQVB numbers ...>`

MDL built-in function that evaluates bitwise equivalence (inverse of exclusive “or”).

> **Note:** EQVB uses 32-bit.

---

### ERROR
**Usage:** `<ERROR values ...>`

MDL built-in function that raises an error ([error MDL0001]) and listing values as resources. The values are usually a text explaining the error, offending ATOM, routine where it occurred and last any other information.

---

### EVAL
**Usage:** `<EVAL value [environment]>`

MDL built-in function that evaluates value (usually a FORM created by FORM or QUOTE).

> **Note:** It is possible to supply an environment for EVAL. This tells EVAL from which environment. EVAL should take variable bindings. See The MDL Programming Language, chap. 9.7 for more about the environment.

---

### EVAL-IN-SEGMENT
**Usage:** `<EVAL-IN-SEGMENT dummy1 value[dummy2]>`

ZIL library function that calls EVAL on the value and returns its result.

> **Note:** When ZILF calls EVAL, it ignores dummy1 and the optional dummy2

---

### EVALTYPE
**Usage:** `<EVALTYPE atom [handler]>`

MDL built-in function that tells the TYPE atom how it should be evaluated by EVAL. If EVALTYPE is called without a handler then the currently active handler is returned. If there is no active handler, FALSE is returned.

> **Note:** Note that it is possible to replace the handler with a new handler, even on the predefined TYPEs. See APPLYTYPE, NEWTYPE and PRINTTYPE.

---

### EXPAND
**Usage:** `<EXPAND value>`

MDL built-in function that performs the first EVAL of the value. In case the value is a MACRO only the first EVAL is done.

---

### FILE-LENGTH
**Usage:** `<FILE-LENGTH channel>`

MDL built-in function that returns the size, in bytes, of the file on channel. FILE-LENGTH returns FALSE if the file is closed.

---

### FLOAD
**Usage:** `<FLOAD filename>`

MDL built-in function.

> **Note:** ZILF ignores all but the first argument and treats FLOAD as an alias to INSERT-FILE.

---

### FORM
**Usage:** `<FORM values ...>`

MDL built-in function that creates a FORM without evaluating it. This is analogous to LIST and VECTOR but with "<>" instead of "()" or "[]". In many cases it is possible to use QUOTE to achieve the same result.

---

### FREQUENT-WORDS?
**Usage:** `<FREQUENT-WORDS?>`

ZIL library predicate.

> **Note:** ZILF ignores this and always returns FALSE. Frequent words table is built by ZAPF instead.

---

### FUNNY-GLOBALS?
**Usage:** `<FUNNY-GLOBALS? [boolean]>`

When enabled, this ZIL library predicate lets the game define more than the usual 240 global variables.

If needed, ZILF will move the extra variables into a table (GLOBAL-VARS-TABLE) and generate table instructions to access them (PUT and GET, or in the case of BYTE globals created with DEFINE-GLOBALS, PUTB and GETB).

> **Note:** This translation is mostly transparent to game source code, but it can’t be used for global variables that are ever referenced indirectly by number. ZILF uses a simple heuristic to try to identify those variables and reserve “real” global variable slots for them.

---

### G?
**Usage:** `<G? value1 value2>`

**Alternative Usage:** `<G=? value1 value2>`

MDL built-in predicate that returns true if value1 is greater than value2, otherwise the predicate returns false.

> **Note:** 'G' means "is greater than."

---

### GASSIGNED?
**Usage:** `<GASSIGNED? Atom>`

MDL built-in predicate that returns true if atom has a GVAL (global value).

---

### GBOUND?
**Usage:** `<GBOUND? atom>`

MDL built-in predicate that returns true if the atom ever had a global value.

---

### GC
**Usage:** `<GC>`

MDL built-in function that causes garbage collection.

> **Note:** In ZILF, GC ignores all arguments and always returns true. ZILF relies on the garbage collection in the NET framework and only implements this for compatibility.

---

### GC-MON
**Usage:** `<GC-MON>`

MDL built-in function.

> **Note:** ZILF ignores this and always returns FALSE.

---

### GET-DECL
**Usage:** `<GET-DECL item>`

MDL built-in function that returns the pattern defined to the item. It returns FALSE if no item exists.

> **Note:** See DECL?, GDECL and PUT-DECL for more on declaration patterns.

---

### GETPROP
**Usage:** `<GETPROP item indicator [default-value]>`

MDL built-in returns the property-value stored under indicator on item. If no value can be found GETPROP returns the default-value or FALSE if no default-value is given.

> **Note:** See ASSOCIATIONS, AVALUE, INDICATOR, ITEM, NEXT and PUTPROP.

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

### GROW
**Usage:** `<GROW vector end beginning>`

MDL built-in function that expands the vector with end and/or beginning number of elements to respectively end of the vector.  Only non-negative values for end and beginning are valid. The new elements have FALSE as an initial value.

> **Note:** If elements are added to the beginning of a vector all old references to that vector have to use TOP or BACK to access the new elements.

---

### GUNASSIGN
**Usage:** `<GUNASSIGN atom>`

MDL built-in function that unassigns global atom.

---

### GVAL
**Usage:** `<GVAL atom>`

**Alternative Usage:** `,atom`

MDL built-in function that gets the value of the global atom.

> **Note:** Typically used in its alternate form ",atom".

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

### ILIST
**Usage:** `<ILIST count [init]>`

MDL built-in function that returns a LIST with count items all set to init.

> **Note:** ILIST means "implicit" or "iterated" list.

---

### IMAGE
**Usage:** `<IMAGE ch [channel]>`

MDL built-in function that prints the actual raw character with number ch to channel. No extra characters are ever printed.

> **Note:** IMAGE returns ch.

---

### INCLUDE
**Usage:** `<INCLUDE package-name ...>`

MDL package system that activates one or many package-names and makes its content available in the current OBLIST-path. In practice INCLUDE copies the OBLIST package-name and adds it last to the local OBLIST (<LVAL OBLIST>). This means that all ATOMs on the DEFINITIONS OBLIST becomes available in current environment. 

If the package-name is not available in the current environment, INCLUDE tries to load “package-name.zil” from the current path.

> **Note:** INCLUDE only works together with DEFINITIONS and if the definition of the package-name is missing from the environment or no file is found containing that definition is found, an error is raised. 

See DEFINITIONS and INCLUDE-WHEN.

---

### INCLUDE-WHEN
**Usage:** `<INCLUDE-WHEN condition package-name ...>`

MDL package system that only activates the package-name if the condition evaluates to TRUE.

> **Note:** INCLUDE-WHEN is mostly like INCLUDE.

See DEFINITIONS and INCLUDE.

---

### INDENT-TO
**Usage:** `<INDENT-TO position [channel]>`

ZIL library function that places the cursor at the position on channel. Default value for the channel is .OUTCHAN (the console).

---

### INDEX
**Usage:** `<INDEX offset>`

MDL built-in function that returns the index-part of an OFFSET.

---

### INDICATOR
**Usage:** `<INDICATOR asoc>`

MDL built-in function that returns the indicator part from an asoc entry, of TYPE ASOC, in the ASSOCIATION chain.

> **Note:** See ASSOCIATIONS, AVALUE, GETPROP, ITEM, NEXT and PUTPROP.

---

### INSERT
**Usage:** `<INSERT atom | pname oblist>`

MDL built-in function that creates an ATOM with the pname and inserts it into oblist. INSERT returns the newly created ATOM (or raises an error if the ATOM already was on the oblist). First argument can also be an atom but this ATOM can not be on any OBLIST and therefore must be newly created by ATOM or recently REMOVE.
 
INSERT requires that you specify oblist, if you want to create an ATOM on the standard OBLIST, usually <1 .OBLIST>, you can use <PARSE string> instead.

> **Note:** Note that you also can use trailers to both create the ATOM and the OBLIST (or one of them). atom!-oblist inserts the atom on the oblist and if one of them or both don’t exist, they are created.

---

### INSERT-FILE
**Usage:** `<INSERT-FILE filename>`

ZIL library function that inserts a file with filename at this point. If extension is omitted, ".zil" is assumed.

The filename can have an absolute or relative path. If no path is given, the compiler looks in the current library and the libraries specified to the compiler with the -ip switch.

> **Note:** Note that path is specified like in Linux (forward slashes etc.) and uppercase/lowercase can be significant, depending on the host system.

ZILF ignores all but the first argument.

---

### ISTRING
**Usage:** `<ISTRING count [init]>`

MDL built-in function that returns a STRING with count items all set to init (character).

> **Note:** ISTRING is "implicit" or "iterated".

---

### ITEM
**Usage:** `<ITEM asoc>`

MDL built-in function that returns the item part from an asoc entry, of TYPE ASOC, in the ASSOCIATION chain.

> **Note:** See ASSOCIATIONS, AVALUE, GETPROP, INDICATOR, NEXT and PUTPROP.

---

### IVECTOR
**Usage:** `<IVECTOR count [init]>`

MDL built-in function that returns a VECTOR with count items all set to init.

> **Note:** IVECTOR means "implicit" or "iterated" vector.

---

### L?
**Usage:** `<L? value1 value2>`

**Alternative Usage:** `<L=? value1 value2>`

MDL built-in predicate that returns true if value1 is lower or equal than value2 otherwise false.

> **Note:** L means less than.

---

### LANGUAGE
**Usage:** `<LANGUAGE name [escape-char] [change-chrset]>`

ZIL library setting that changes how text is encoded in two ways: it lets you write language-specific characters in ZIL source code by adding a prefix to ASCII characters, and it changes the Z-machine alphabet to encode them more efficiently. 

If change-chrset is false, the Z-machine character set won’t be changed, so the language setting will only affect how source code is read.

> **Note:** The escape-char is !\% by default, meaning that language-specific characters may be used in strings or atoms by adding a percent sign prefix (e.g. %s for ß).

The name may be GERMAN, or DEFAULT to stick with classic ZSCII. GERMAN is defined as follows:

*  Alphabet 0: abcdefghiklmnoprstuwzäöü., 
*  Alphabet 1: ABCDEFGHIKLMNOPRSTUWZjqvxy 
*  Alphabet 2: 0123456789!?'-:()JÄÖÜß«» 
*  Special characters:  ä(%a), ö(%o), ü(%u), ß(%s), Ä(%A), Ö(%O), Ü(%U), «(%<), »(%>)

---

### LEGAL?
**Usage:** `<LEGAL? value>`

MDL built-in predicate  that returns TRUE if portion of the stack value occupies is still active, otherwise FALSE. Although LEGAL? works for all TYPEs, it’s only useful for those TYPEs that live on the stack, like TUPLE, activation and environment, all other types always return TRUE.

---

### LENGTH
**Usage:** `<LENGTH structure>`

MDL built-in function that returns the number of elements in structure. structure must be an object that STRUCTURED? evaluates to true.

> **Note:** Note that TABLE is not a structure. Also see BACK, NTH, PUT, REST, SUBSTRUC and TOP.

---

### LENGTH?
**Usage:** `<LENGTH? structure limit>`

MDL built-in predicate that returns false if LENGTH of structure is greater than limit, otherwise true (it actually returns LENGTH of structure).

> **Note:** LENGTH? answers the question: "is LENGTH of structure less or equal to limit?"

---

### LIST
**Usage:** `<LIST values ...>`

**Alternative Usage:** `(values ...)`

MDL built-in function that returns a list of containing values.

> **Note:** A list is a collection of items where each item has a pointer to the next item in the collection. This makes it easy to add and insert items in lists but a list is always forward looking. See more about LIST structure in The MDL Programming Language, Appendix 1.

---

### LONG-WORDS?
**Usage:** `<LONG-WORDS? [boolean]>`

ZIL library predicate that  tells the compiler whether to generate the CONSTANT LONG-WORDS-TABLE. The boolean defaults to true if omitted.

> **Note:** LONG-WORDS-TABLE contains an entry for each vocab word whose length exceeds the maximum word length for the selected Z-machine version (6 Z-characters for V3, or 9 Z-characters for V4+). The table is prefixed by the number of entries, and each entry consists of a word pointer followed by a string giving the printed form of the word.

---

### LOOKUP
**Usage:** `<LOOKUP string oblist>`

MDL built-in function that returns the ATOM with PNAME string from oblist. It returns FALSE if no ATOM is found.

---

### LPARSE
**Usage:** `<LPARSE text [10] [lookup-oblist]>`

MDL built-in function that  is just like PARSE with the exception that LPARSE returns a LIST of all the expressions in the text.

> **Note:** LPARSE means "list parse." ZILF requires that the second argument is 10 if a lookup-oblist is given.

---

### LSH
**Usage:** `<LSH number places>`

MDL built-in function that is a bitwise shift, shifting number left when places is positive and right if it is negative. When right shifting, the sign is not preserved (0 is always shifted in). For example.

1000 0000 0000 1010  -->  0100 0000 0000 0101

---

### M-HPOS
**Usage:** `<M-HPOS channel>`

ZIL library function that returns the current horizontal cursor position on channel.

---

### MAKE-GVAL
**Usage:** `<MAKE-GVAL atom>`

ZIL library function that returns the atom as GVAL (,atom).

---

### MAPF
**Usage:** `<MAPF finalf applicable structs ...>`

MDL built-in function that  traverses over all structs one element at a time until one of the structs is out of elements and calls the function applicable with the elements. In other words, the first iteration takes the first element from each of the structs and calls applicable, the second iteration takes the second element from each of the structs and calls applicable, and so on until one of the structs doesn't have any more elements. The intermediate results from each call to applicable is stored in a TUPLE. 

The finalf can either be a FUNCTION or <> (FALSE). If it is FALSE the TUPLE with the intermediate result  is thrown away, otherwise finalf is called with the TUPLE. 

MAPF returns the result from finalf. If finalf is FALSE, MAPF returns the result from the last call to applicable. If applicable never was called (one of the structs was empty) MAPF returns FALSE.

One special case is if only finalf and applicable are given. In this case applicable is called indefinitely with no arguments until a MAPLEAVE or MAPSTOP is invoked. finalf is called if MAPSTOP is used to leave the iteration.

> **Note:** MAPF means "map first."

---

### MAPLEAVE
**Usage:** `<MAPLEAVE [value]>`

MDL built-in function that leaves the MAPF or the MAPR immediately and makes the MAPF or the MAPR return the value (TRUE by default). This means that an eventual finalf in the MAPF or the MAPR never will be invoked.

---

### MAPR
**Usage:** `<MAPR finalf applicable structs ...>`

MDL built-in function that works the same as MAPF but instead of sending one element at a time to applicable it sends the REST of the structs, starting with <REST struct 0>. In other words, the first iteration takes REST 0 from each of the structs and calls applicable, the second iteration takes REST 1 from each of the structs and calls applicable, and so on until one of the structs doesn't have any more elements. The intermediate results from each call to applicable is stored in a TUPLE. 

The finalf can either be a FUNCTION or <> (FALSE). If it is FALSE the TUPLE with the 
intermediate result  is thrown away, otherwise finalf is called with the TUPLE.  

MAPR returns the result from finalf. If finalf is FALSE, MAPR returns the result from the last call to applicable. If applicable never was called (one of the structs was empty) MAPR returns FALSE. 

One special case is if only finalf and applicable are given. In this case applicable is called indefinitely with no arguments until a MAPLEAVE or MAPSTOP is invoked. finalf is called if MAPSTOP is used to leave the iteration.

> **Note:** MAPR means "map rest."

---

### MAPRET
**Usage:** `<MAPRET [value] ...>`

MDL built-in function that leaves the current iteration of the MAPF or the MAPR and adds the specified values to the TUPLE of arguments used when the finalf is called. If no values are specified nothing is added to the TUPLE in this iteration.

> **Note:** Note that the MAPF or the MAPR continues to run through the iterations until one of the structs is out of elements.

---

### MAPSTOP
**Usage:** `<MAPSTOP [value] ...>`

MDL built-in function, which is similar to MAPRET, however, after it adds the values to the TUPLE of arguments, it directly calls finalf and aborts all remaining iterations.

---

### MAX
**Usage:** `<MAX numbers ...>`

MDL built-in function that returns the maximum number among numbers.

---

### MEMBER
**Usage:** `<MEMBER item structure>`

MDL built-in function that  iterates through structure and returns <REST structure i>, where i is the index of the first element in structure that is =? with item.

MEMBER returns false if the item is not found.

---

### MEMQ
**Usage:** `<MEMQ item structure>`

MDL built-in function that iterates through structure and returns <REST structure i>, here i is the index of the first element in structure that is ==? with item.

MEMQ returns false if the item is not found.

> **Note:** MEMQ means "member quick."

---

### MIN
**Usage:** `<MIN numbers ...>`

MDL built-in function that returns the minimum number among numbers.

---

### MOBLIST
**Usage:** `<MOBLIST name>`

MDL built-in function that creates and returns a new empty OBLIST named name. If an OBLIST with the name already exists the existing one is returned instead.

> **Note:** MOBLIST means "make oblist."

---

### MSETG
**Usage:** `<MSETG atom value>`

ZIL library function that defines an atom with value that will never be changed. The atom can is accessed inside a ROUTINE with GVAL (or ,) just like a GLOBAL atom. Defining a MSETG (CONSTANT) instead of a GLOBAL when possible can be vital information the compiler can use for optimization.

> **Note:** MSETG means "manifest set global," which is an alias for CONSTANT.

---

### NEVER-ZAP-TO-SOURCE-DIRECTORY?
**Usage:** `<NEVER-ZAP-TO-SOURCE-DIRECTORY?>`

ZIL library predicate.

> **Note:** ZILF ignores this and always returns FALSE.

---

### NEWTYPE
**Usage:** `<NEWTYPE name primtype-atom [decl]>`

MDL built-in function that creates a new TYPE with the name, name and the same PRIMTYPE as primtype-atom. It returns the new TYPE. The name must be unique (<VALID-TYPE? name> is FALSE> otherwise NEWTYPE results in an error.

> **Note:** It is possible to specify a decl (see GDECL) for the new TYPE that is enforced when CHTYPE.

See APPLYTYPE, EVALTYPE and PRINTTYPE.

---

### NEXT
**Usage:** `<NEXT asoc>`

MDL built-in function that returns the next asoc entry, of TYPE ASOC, in the ASSOCIATION chain. If there are no more entries then FALSE is returned.

> **Note:** See ASSOCIATIONS, AVALUE, GETPROP, INDICATOR, ITEM and PUTPROP.

---

### NOT
**Usage:** `<NOT value>`

MDL built-in function that returns true if value is false (#FALSE <>), otherwise NOT returns false.

> **Note:** This is a boolean (logical) "not."

---

### NTH
**Usage:** `<NTH structure index>`

**Alternative Usage:** `<index structure>`

MDL built-in function that returns the element at index in structure. Valid values for index are between 1 and \<LENGTH structure\>. structure must be an object that STRUCTURED? evaluates to TRUE. NTH can also be abbreviated as <index structure>.

> **Note:** Note that TABLE is not a structure.

Also see BACK, LENGTH, PUT, REST, SUBSTRUC and TOP.

---

### OBLIST?
**Usage:** `<OBLIST? atom>`

MDL built-in predicate that returns the OBLIST that contains the atom. If the atom is not in any OBLIST it returns FALSE.

---

### OFFSET
**Usage:** `<OFFSET index structure-decl [value-decl]>`

MDL built-in function that creates an OFFSET TYPE that is used with NTH and PUT to check that an element at index in the structure follows the specified pattern, structure-decl and value-decl.

The index is an integer and the structure-decl follow the normal rules for a decl (see GDECL). Because the OFFSET only specifies the decl for one element in the structure it is possible to split the decl in two parts where structure-decl specifies the structure and value-decl is the decl for this specific element.

> **Note:** Note that in ZILF can OFFSET only be used with NTH and PUT in the form <index-or-offset structure> and <index-or-offset structure value> respectively. 

GET-DECL and PUT-DECL can be used to examine and change the decl of the OFFSET and INDEX returns the index of an OFFSET.

---

### OPEN
**Usage:** `<OPEN "READ" path>`

MDL built-in function that opens the file at path for input.

> **Note:** The second argument must always be "READ" in ZILF and the path is specified like in Linux (forward slashes etc.) and uppercase/lowercase can be significant, depending on the host system.

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

### ORB
**Usage:** `<ORB numbers ...>`

MDL built-in function that performs a bitwise OR.

---

### ORDER-FLAGS?
**Usage:** `<ORDER-FLAGS? LAST objects ...>`

Belonging to the ZIL library, each of the objects is an atom naming a flag, as seen in the (FLAGS ...) clause of an OBJECTdefinition.

The only ordering allowed is LAST, which causes the named flags to be added to the list of “flags requiring high numbers”, which are assigned the highest flag numbers so they may be distinguished from zero. Flags mentioned in the (FIND ...) clause of SYNTAX definitions are already added to this list by default.

---

### ORDER-OBJECTS?
**Usage:** `<ORDER-OBJECTS? atom>`

Belonging to the ZIL library, this controls the order in which object numbers are assigned to objects.

By default, if ORDER-OBJECTS? is not used, object numbers are assigned in reverse mention order. That is, the first object defined is given the highest number, and any other objects mentioned in its definition are given the next highest numbers (in order), whether or not those objects are explicitly defined later.

The atom is one of the following:

*  DEFINED, to assign numbers to all explicitly defined objects in the order of their definitions (starting at 1), then to all other mentioned objects in the order of their mentions.

*  ROOMS-FIRST, which is the same as DEFINED, except that numbers are assigned to rooms before non-rooms, so room numbers can be packed into a byte array (assuming there are less than 256 of them).

*  ROOMS-LAST, which is the same as DEFINED, except that numbers are assigned to non-rooms before rooms.

*  ROOMS-AND-LGS-FIRST, which is the same as ROOMS-FIRST, except that numbers are assigned to rooms and local globals before the remaining objects.

For the purpose of object ordering, “rooms” include all objects defined with ROOM (instead of OBJECT) as well as all objects whose initial LOC is an object named ROOMS. “Local globals” includes all objects whose initial LOC is an object named LOCAL-GLOBALS.

> **Note:** Note that there are two ways the compiler can learn about an object: some objects are explicitly “defined” using ROOM or OBJECT, whereas the existence of others is merely implied when the objects are “mentioned” as part of another object’s definition (in a LOC or direction property).

---

### ORDER-TREE?
**Usage:** `<ORDER-TREE? atom>`

ZIL library function that controls the initial layout of the Z-machine object tree.

The object tree is defined by three fields on each object, named in the Z-Machine Standards Document as “parent”, “child”, and “sibling”, which are read by the ZIL functions LOC, FIRST?, and NEXT?. Each object’s parent field is specified by the (LOC …) clause in the object definition, but the compiler has discretion to set the child and sibling fields as long as the tree remains well-formed.

The atom must be REVERSE-DEFINED to force objects to be linked in the reverse order of their definitions. That is, the child of an object X is the last object in the source code whose definition contains (LOC X); the sibling of that child is the next to last object in the source code that contains (LOC X); and so on.

By default, if ORDER-TREE? is not used, the order is the same as REVERSE-DEFINED except for the first defined child, which remains the first object linked. That is, the child of an object X is the first object in the source code whose definition contains (LOC X); the sibling of that child is the last object that contains (LOC X); the sibling of that child in turn is the next to last object that contains (LOC X); and so on.

---

### PACKAGE
**Usage:** `<PACKAGE package-name>`

MDL package system that defines a group of ATOMs (i.e. variables and functions) with the package-name for potential later inclusion (via USE or USE-WHEN) in the project. A PACKAGE is often used to functionally group together library functions that can have a usage over many projects.

Internally an OBLIST named PACKAGE is used in conjunction with BLOCK and ENDBLOCK. When you define a PACKAGE the following is happening:

1.  An external OBLIST, package-name, is created and added to the OBLIST PACKAGE (e.g. FOO!-PACKAGE).

2.  An internal OBLIST, Ipackage-name, is created and added to the OBLIST package-name (e.g. IFOO!-FOO!-PACKAGE).

3.  A BLOCK is started with the OBLISTs (in this order) Ipackage-name, package-name and <ROOT> (e.g. IFOO, FOO, <ROOT>).

This means that every ATOM that is created inside the PACKAGE ends up on the internal OBLIST first. If ENTRY is used the ATOM is created/moved to the external OBLIST and finally RENTRY creates/moves the ATOM to the ROOT OBLIST.

The PACKAGE definition is ended by END-PACKAGE (in fact an ENDBLOCK) which restores the OBLISTs to the state they had before the PACKAGE definition began.

When you decide to use a package by USE or USE-WHEN the OBLIST package-name is copied and added last to the local OBLIST (<LVAL OBLIST>). This means that all ATOMs on the external package OBLIST becomes available in current environment.

> **Note:** Note that a PACKAGE can be defined additive (i.e. multiple PACKAGE definitions with the same package-name is added together to one PACKAGE). ZILF has three packages predefined in <MOBLIST PACKAGE>; NEWSTRUC, ZIL and ZILCH. They are all empty and are only there for compatibility (all ATOMs in these packages are already in ZILF).

See DEFINITIONS, ENDPACKAGE, ENTRY, RENTRY, USE and USE-WHEN.

---

### PARSE
**Usage:** `<PARSE text [10] [lookup-oblist]>`

MDL built-in function that takes a string, text, and returns the first MDL object encountered in it. If lookup-oblist is supplied, PARSE looks for potential ATOMs on this OBLIST. If no lookup-oblist is supplied, .OBLIST is used.

> **Note:** ZILF requires that the second argument is 10 if a lookup-oblist is supplied.

---

### PICFILE
**Usage:** `<PICFILE>`

ZIL library function that is a compiler directive used to associate a graphics resource file with a game, and Infocom's version of PICFILE translates to a ZAP .PICFILE directive.

> **Note:** The current version of ZILF ignores PICFILE and always returns FALSE because modern interpreters do not support Infocom's graphics format. The next release of ZILF will bundle images into Blorb files (without ZAPF).

---

### PLTABLE
**Usage:** `<PLTABLE [flags ...] values ...>`

ZIL library function that defines a table containing the specified values and with the PURE and LENGTH flag (see TABLE about LENGTH, PURE and other flags).

> **Note:** TABLE is a ZIL-specific structure that can be used both outside and inside ROUTINES.

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

### PRINT-MANY
**Usage:** `<PRINT-MANY channel printer items ...>`

ZIL library function that prints multiple items to channel with the printer. The printer is usually PRINT, PRINC or PRIN1 but could actually be any FUNCTION that takes one argument. The printer is called repeatedly with one item at a time until the list of items is exhausted.

> **Note:** If PRMANY-CRLF is given as an item, a CRLF is printed at that position.

---

### PRINTTYPE
**Usage:** `<PRINTTYPE atom [handler]>`

MDL built-in function that tells the TYPE atom how it should be printed (PRIN1-style). If PRINTTYPE is called without a handler then the currently active handler is returned. If there is no active handler, FALSE is returned.

> **Note:** Note that it is possible to replace the handler with a new handler, even on the predefined TYPEs.

See APPLYTYPE, EVALTYPE and NEWTYPE.

---

### PROG
**Usage:** `<PROG [activation] (bindings ...) [decl] expressions ...>`

MDL built-in function that defines a program block with its own set of bindings. PROG is similar to BIND and REPEAT but unlike BIND it creates a default activation (like REPEAT) at the start of the block and doesn't have an automatic AGAIN at the end of the block (like REPEAT). It is possible to name an atom to the activation but it is not necessary. AGAIN and RETURN inside a PROG-block will start the block over or return from the block.

The decl is used to specify the valid TYPE of the variables. In its simplest form decl is formatted like: #DECL ((X) FIX), meaning that X must be of the TYPE FIX. For more information on how to format the decl see GDECL.

> **Note:** Also see AGAIN, BIND, REPEAT and RETURN for more details how to control program flow.

---

### PROPDEF
**Usage:** `<PROPDEF atom default-value [spec-patterns ...]>`

ZIL library function that defines a property, atom, with a default-value for OBJECTs (and ROOMs). The default-value is the value that GETP will return if the property is not defined for the given OBJECT.

For the more complex properties it is possible to define a spec-pattern according to (atom|DIR ["MANY"|"OPT"] [phrase] var:type ... [form-len] ["MANY"] <fnc-size var>|(const value)| (ptr <fnc-size var>) ...) ...

The spec-pattern consists of two parts divided by an equal sign. The left side is the pattern and the right side is the rules on how to store the property.

*  atom|DIR is the property. DIR is a special case that is used for DIRECTIONS.

*  "MANY" means that the pattern of var:type repeats itself. If "MANY" is defined on the left side of the equal sign there must be a matching on the right side.

*  "OPT" means that the pattern after is optional.

*  [phrase] can be tokens like IF, ELSE, TO.

*  var:type is a variable name, var, and its type. Usually FIX, STRING or ROOM.

*  form-len is the length (records) of the form. The form-len is optional and can also be given as <>.

*  <fnc-size var> can be a call with var to either BYTE, WORD, STRING, OBJECT, ROOM, GLOBAL, NOUN, ADJ, or VOC. This stores var or derivative of var and adds to the vocabulary and/or creates a GVAL.

*  (ptr <fnc-size var>) creates a GVAL, ptr, that contains the address-pointer relative to the property.

*  (const value) creates a CONSTANT, name, containing value.

---

### PTABLE
**Usage:** `<PTABLE [(flags ...)] values ...>`

ZIL library function that defines a table containing the specified values and with the PURE flag (see TABLE about PURE and other flags).

> **Note:** TABLE is a ZIL-specific structure that can be used both outside and inside ROUTINES.

---

### PUT-DECL
**Usage:** `<PUT-DECL item pattern>`

MDL built-in function that  defines an alias, item, for a pattern. See DECL?, GDECL and GET-DECL for more on declaration patterns.

---

### PUT-PURE-HERE
**Usage:** `<PUT-PURE-HERE>`

ZIL library function.

> **Note:** ZILF ignores this and always returns FALSE.

---

### PUTPROP
**Usage:** `<PUTPROP item indicator [value]>`

MDL built-in function that stores value as an association on the item under the indicator and returns the item. If no value is specified PUTPROP returns the value and then clears the association.

> **Note:** In ZILF, there is a special indicator, PROPSPEC, that has a special meaning inside OBJECTs. A PROPSPEC property is defined: <PUTPROP item PROPSPEC [function]>

When an item defined in this way is used in an OBJECT, the function is invoked during the compilation with the LIST (containing the item) as an argument. The return value from the function must be a LIST and it is stored as value under PROPSPEC on the item. If no function is specified the PROPSPEC for the item is cleared. See examples below. 

See ASSOCIATIONS, AVALUE, GETPROP, INDICATOR, ITEM and NEXT.

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

**Alternative Usage:** `'value`

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

### REST
**Usage:** `<REST structure [count]>`

MDL built-in function that returns structure without its first count elements (count is default 1). Note that this is not a copy of the structure, it is pointing to the same structure with another starting element. 

structure must be an object that STRUCTURED? evaluates to true.

> **Note:** Note that TABLE is not a structure.

Also see BACK, LENGTH, NTH, PUT, SUBSTRUC and TOP.

---

### RETURN
**Usage:** `<RETURN [value] [activation]>`

MDL built-in function that  returns value from program-block defined by activation. True is returned if no value is specified. If activation is not specified RETURN will exit the current defined program-block where an automatic activation was created (PROG and REPEAT creates automatic activations, BIND does not).

In practice RETURN exits the current program-block and returns value  to the outer program-block defined by BIND (needs activation), PROG or REPEAT.

> **Note:** See AGAIN, BIND, PROG and REPEAT for more examples of using RETURN and details how to control program flow.

---

### ROOM
**Usage:** `<ROOM name (property value ...) ...>`

ZIL library function that creates a room-object with the internal objectname, name. After the name follows LISTs of properties for the ROOM and the values for each property. Which properties that define up a ROOM is determined by the parser and it’s possible to add new properties with PROPDEF as long as the parser is modified to support the new property. Usually the below properties are understood by the parser and the properties IN (or LOC), DESC and FLAGS are required, the others are optional.

*  IN or LOC is a required property. The value is always ROOMS for ROOM-objects.

*  DESC is a required property. The short description text of the ROOM. This is the text that is, for example, printed in the statusbar.

*  FLAGS is a required property. This lists all the flagbits that are set on this ROOM.

*  LDESC is an optional property. The long description of the ROOM. This is the text that is printed, for example, the first time the player visits the ROOM.

*  (dir ...) is an optional property.  List a direction, dir and where it leads. There is 5  
   different types of EXITS:

    *  UEXIT (“unconditional exit”). The syntax is (dir TO room-name). If  the player moves in this direction he is moved unconditionally to room-name.

    *  NEXIT (“non-exit”). The syntax is (dir "text-why-not"). The text-why-not is printed when the player tries to move in this direction. Use this only if you want a different text than the standard message, typically something like "You can’t move in that direction!".

    *  CEXIT (“conditional exit”). The syntax is (dir TO room-name IF gval [ELSE "text-why-not"]). This moves the player if the global value, gval, is TRUE. The ELSE-part is optional and the standard message is printed if it is not supplied.

    *  DEXIT (“door-exit”). The syntax is (dir TO room-name IF door-name IS OPEN). This is a special case of CEXIT that moves the player to room-name if the door-name has the OPENBIT set.

    *  FEXIT (“function-exit”). The syntax is (dir PER routine-name). This moves the player to the ROOM returned by the ROUTINE, routine-name. If the routine returns FALSE it is presumed that the routine has printed an appropriate message.

*  GLOBAL is an optional property. This is a LIST of all the OBJECTs that is IN the LOCAL-GLOBALS that are accessible from this ROOM. This could, for example, be a door that is accessible from two different ROOMs.

*  THINGS is an optional property. This creates one or more simple “pseudo-objects”. Each object has three parts: a LIST of adjectives (FALSE if none), a LIST of nouns and the name of the action-routine to call when this object is accessed. In early Infocom games this property was called PSEUDO and had a slightly different syntax.

*  ACTION is an optional property. The syntax is (ACTION routine-name). This ROUTINE takes one argument, by convention call RARG (“room-argument”), and is called more than once during a turn with different values to RARG. 

    *  M-BEG, the routine-name is called with this value to RARG before any OBJECTs or verb action-routines.  

    *  M-END, the routine-name is called with this value to RARG after any OBJECTs or verb action-routines.

    *  M-LOOK, the routine-name is called with this value to RARG when the player LOOKs.

    *  M-ENTER, the routine-name is called with this value to RARG when the player enters the ROOM (before any room description).

> **Note:** Note that ROOMs can just as easily be created with OBJECT as long as they are (IN ROOMS).

See Learning ZIL, Steve E. Meretzky and ZIL Course, Marc S. Blank for more on properties, flagbits and how to write and design games.

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

### ROUTINE-FLAGS
**Usage:** `<ROUTINE-FLAGS CLEAN-STACK?>`

ZIL library function that sets flags to control how ZILF should compile. To clear, call FILE-FLAGS without any flags.

The flags are:

*  CLEAN-STACK?  which tells the compiler to generate extra code to remove unneeded values from the stack. Without it, the compiler will generate smaller code in some cases, at the risk of potentially causing stack overflow at runtime.

---

### SET
**Usage:** `MDL: <SET atom value [environment]>,
Zapf: <SET name value>`

MDL built-in function that asigns a value to the local atom. It is possible to supply an environment for SET. See EVAL for more about the environment.

Z-code built-in function that stores value in local variable name.

> **Note:** ZILF supports SET in all versions.

**History:** Zapf syntax: SET, Inform syntax: store

---

### SET-DEFSTRUCT-FILE-DEFAULTS
**Usage:** `<SET-DEFSTRUCT-FILE-DEFAULTS args ...>`

MDL built-in function that is used to change the default behaviour of the struct-option and the field-option tokens in DEFSTRUCT.

The newly defined defaults are only active in the same file as they were defined. If a file is loaded via, for example, FLOAD or INSERT-FILE the defaults are the built-in defaults inside these files.

The tokens that can have changed default behaviour are:

*  'CONSTRUCTOR replaces the default constructor (MAKE-).

*  'INIT-ARGS replaces the init arguments to the base-type. This is empty by default.

*  'NODECL, use 'NODECL, to get 'NODECL by default.

*  ‘NOTYPE,  use 'NOTYPE, to get 'NOTYPE by default.

*  'NTH, the default ATOM for this is NTH. Change to other with ('NTH MY-NTH).

*  'PUT, the default ATOM for this is PUT. Change to other with ('PUT MY-PUT).

*  'START-OFFSET, the default value is 1. Change with ('START-OFFSET value).

> **Note:** If SET-DEFSTRUCT-FILE-DEFAULTS is called without any arguments the built-in default behaviour is restored.

See DEFSTRUCT for more on user defined structures.

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

### SORT
**Usage:** `<SORT predicate vector [record-size] [key-offset] [vector [record-size]  ...]>`

MDL built-in function that can sort a VECTOR (or TUPLE). The predicate can either be <> or a FUNCTION that takes two keys and returns TRUE if the two records are correctly sorted and FALSE if they are incorrectly sorted. For example ,G? will sort keys in ascending order and ,L? will sort keys in descending order. If the predicate is <> the keys must be of the same TYPE and the vector will be sorted in ascending order.

The record-size is the length of each record (default value is 1) and the key-offset is the 
offset in the record to the value to use as the sort key (default value is 0).

If additional vectors are supplied all vectors can have their own record length but each vector must have the same number of records. Records in the additional vectors are interchanged based on how the main vector is sorted.

SORT returns the first sorted vector.

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

### STRUCTURED?
**Usage:** `<STRUCTURED? value>`

MDL bulit-in predicate that returns true if value is of a structured TYPE. The structured TYPEs are:

*  CHANNEL

*  DECL

*  FALSE

*  FORM

*  FUNCTION

*  LIST

*  MACRO

*  OBLIST

*  SEGMENT

*  SPLICE

*  STRING

*  VECTOR

---

### SUBSTRUC
**Usage:** `<SUBSTRUC structure-from [rest] [amount] [structure-to]>`

MDL built-in function that copies an amount number of elements, starting at rest, from structure-from. The result is copied into structure-to, if supplied, otherwise a new structure is returned.

Default value for rest is 0 and default value for amount is LENGTH – rest (in other words, copies from rest to end of structure-from).

structure-from must be of PRIMTYPE LIST, VECTOR or STRING and structure-to must be of the same PRIMTYPE as struture-from and have enough room for the SUBSTRUC to fit.

Also see BACK, LENGTH, NTH, PUT, REST and TOP.

---

### SUPPRESS-WARNINGS?
**Usage:** `<SUPPRESS-WARNINGS? all | none | codes ...>`

ZILF compiler directive that tells the compiler how to treat warnings. NONE is the default.

*  ALL suppresses all warnings.

*  NONE doesn't suppress any warnings.

*  codes suppresses listet warning codes.

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

### TELL-TOKENS
**Usage:** `<TELL-TOKENS {pattern form} ...>`

ZIL library function that replaces current TELL-TOKENS with the specified list of pattern and form. These can then be used in TELL. See ADD-TELL-TOKEN for a description of pattern and form.

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

### TUPLE
**Usage:** `<TUPLE values ...>`

MDL built-in function that is just like a VECTOR with the only difference that a TUPLE should live on the control stack. The advantage of a TUPLE over a VECTOR is that a TUPLE doesn't need to be garbage collected, the disadvantage is that a TUPLE only lives during the execution of the function where it was declared. It is only valid to declare a TUPLE in the "AUX" or "OPTIONAL" part of a functions definition or as a "TUPLE" in a functions definition.

> **Note:** In ZILF, TUPLE is treated as an alias to VECTOR. 

A TUPLE defined in the "AUX" or "OPT" is just like a VECTOR. A "TUPLE" definition makes it possible to have a variable number of arguments to a FUNCTION.

---

### TYPE
**Usage:** `<TYPE value>`

MDL built-in function that evaluates to the type of value. See also ALLTYPES.

---

### TYPE?
**Usage:** `<TYPE? value type-1 ... type-N>`

MDL built-in predicate that evaluates to type-i only if <==? type-i > is true. It is faster and gives more information than OR-ing tests for each TYPE. If the test fails for all type-i’s, TYPE? returns #FALSE ().

---

### TYPEPRIM
**Usage:** `<TYPEPRIM type>`

MDL built-in function that evaluates to the primitive type of type. The primitive types are  ATOM, FIX, LIST, STRING, TABLE and VECTOR.

---

### UNASSIGN
**Usage:** `<UNASSIGN atom [environment]>`

MDL built-in function that unassigns the global atom.

> **Note:** It is possible to supply an environment for the ASSIGNED? predicate. See EVAL for more about the environment.

---

### UNPARSE
**Usage:** `<UNPARSE value>`

MDL built-in function that returns a STRING representation of value. Unlike PNAME, UNPASE prints an ATOMs trailers if required.

---

### USE
**Usage:** `<USE package-name ...>`

MDL package system that  activates one or many package-names and makes its content available in the current OBLIST-path. In practice USE copies the OBLIST package-name and adds it last to the local OBLIST (<LVAL OBLIST>). This means that all ATOMs on the external package OBLIST becomes available in current environment. 

If the package-name is not available in the current environment, USE tries to load 
“package-name.zil” from the current path.

> **Note:** USE only works together with PACKAGE and if the definition of the package-name is missing from the environment or no file is found containing that definition is found, an error is raised.

See PACKAGE and USE-WHEN.

---

### USE-WHEN
**Usage:** `<USE-WHEN condition package-name ...>`

MDL package system that is exactly like USE but only activates the package-name if the condition evaluates to TRUE.

> **Note:** See PACKAGE and USE.

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

### VECTOR
**Usage:** `<VECTOR values ...>`

**Alternative Usage:** `[values ...]`

MDL built-in function that  returns a VECTOR of containing values.

A VECTOR is a collection of items that occupies a continuous block of memory. This makes it easy to traverse a VECTOR both forward and backward but costly to add or insert items in the VECTOR. See more about VECTOR structure in The MDL Programming Language, Appendix 1.

> **Note:** Note that in MDL there is another type of vector, UVECTOR (uniform vector). In an UVECTOR every item is of the same TYPE which makes an UVECTOR more space efficient. ZILF does not support UVECTOR but treats short form definitions of an UVECTOR as a ordinary VECTOR  (![1 2 3!] --> [1 2 3]).

---

### VERSION
**Usage:** `<VERSION {ZIP | EZIP | XZIP | YZIP | number} [TIME]>`

ZIL library function that tells the compiler which Z-machine version that this program is targeting.

Version 3 or ZIP
*  Version 3 (file extension *.z3). Almost all classical Infocom games are in this version. You are limited to 255 objects (rooms+items) and the game can't be bigger than 128K.

Version 4 or EZIP
*  Version 4 (file extension *.z4). Infocom's "plus" games – AMFV, Bureaucracy, Nord and Bert... and Trinity. This format supports 65535 objects and a game size up to 256K.

Version 5 or XZIP
*  Version 5 (file extension *.z5). Infocom's Beyond Zork, Border Zone, Sherlock and the Solid Gold versions of older games. This version adds things like UNDO, COLOR and timed input. This format supports 65535 objects and a game size up to 256K.

Version 6 or YZIP
*  Version 6 (file extension *.z6). Infocom's Arthur, Journey, Shogun and Zork Zero. This version primarily adds graphics. This version supports game size up to 512K.

Version 7
*  Version 7 (file extension *.z7). Post Infocom version. This version supports game size up to 512K. Rarely used version that is superseded by version 8.

Version 8
*  Version 8 (file extension *.z8). Post Infocom version. This version supports game size up to 512K.

> **Note:** In version ZIP the status line is drawn by the interpreter and the argument TIME specifies that the status line should display hh:mm instead of score and moves. Global variable 2, usually SCORE, holds the hour-part and global variable 3, usually MOVES, holds the minute-part.

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