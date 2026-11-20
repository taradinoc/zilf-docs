[← Back to Main Index](./index.md)

# Appendix C: Reserved Constants, Globals & Locals

Compiler-reserved constants, global variables (GVALs), local variables (LVALs), compilation flags, and file flags recognized by ZILF.

---

### FlagNEWSFLAGS
**Usage:** `NEW-SFLAGS`

GVAL table used to define custom search flags in Version 6 new parser games.

---

### ResActions
**Usage:** `ACTIONS`

Reserved GVAL pointing to the compiler-generated table of verb action-routine packed addresses.

---

### ResCRLFCharacter
**Usage:** `CRLF-CHARACTER`

Reserved GVAL (default: |) specifying the character interpreted as a newline inside ZIL strings.

---

### ResCleanStack
**Usage:** `CLEAN-STACK?`

FILE-FLAGS and ROUTINE-FLAGS flag instructing ZILF to emit extra instructions to clear unneeded values from the Z-machine stack, preventing stack overflow at runtime.

---

### ResDoFunnyReturns
**Usage:** `DO-FUNNY-RETURNS?`

**Alternative Usage:** `DO-FUNNY-RETURN?`

Reserved GVAL (default: <> in V3-4, T in V5-) controlling whether <RETURN value> inside PROG/REPEAT exits the enclosing ROUTINE.

---

### ResFalseValue
**Usage:** `FALSE-VALUE`

Reserved CONSTANT (default: 0) representing the runtime Z-machine false return value.

---

### ResFatalValue
**Usage:** `FATAL-VALUE`

Reserved CONSTANT (default: 2) returned by RFATAL.

---

### ResGlobalVarsTable
**Usage:** `GLOBAL-VARS-TABLE`

Compiler-generated table used when FUNNY-GLOBALS? (or DEFINE-GLOBALS) is enabled to store global variables beyond the Z-machine's 240-global limit.

---

### ResInZilch
**Usage:** `IN-ZILCH`

Reserved COMPILATION-FLAG (default: <>) indicating ZILCH/compiler context.

---

### ResInitial
**Usage:** `INITIAL`

Predefined OBLIST (<1 .OBLIST> by default) that starts empty and stores user-created ATOMs.

---

### ResLastObject
**Usage:** `LAST-OBJECT`

Reserved CONSTANT automatically set by the compiler to the object number of the last object.

---

### ResLongWordsTable
**Usage:** `LONG-WORDS-TABLE`

Compiler-generated CONSTANT table created when LONG-WORDS? is enabled, mapping truncated vocabulary word pointers (exceeding 6 Z-chars in V3 or 9 in V4+) to their full printed strings.

---

### ResMdlZil
**Usage:** `MDL-ZIL?`

FILE-FLAGS flag instructing ZILF to treat top-level SETG as GLOBAL and DEFINE as ROUTINE (while SETG20 and DEFINE20 retain MDL semantics).

---

### ResNewParser
**Usage:** `NEW-PARSER?`

Reserved GVAL (undefined by default); set via <SETG NEW-PARSER? T> to enable the Version 6 new parser vocabulary/syntax format.

---

### ResOblist
**Usage:** `OBLIST`

Predefined LVAL (.OBLIST) holding the ordered LIST of OBLISTs searched when resolving ATOM names (initially INITIAL followed by ROOT); rebound by BLOCK, PACKAGE, DEFINITIONS, USE, and INCLUDE.

---

### ResOutchan
**Usage:** `OUTCHAN`

Predefined LVAL (.OUTCHAN) holding the default output CHANNEL (the console) used by PRIN1, PRINC, PRINT, CRLF, INDENT-TO, M-HPOS, and PRINT-MANY.

---

### ResPackageOblist
**Usage:** `PACKAGE (OBLIST)`

Predefined OBLIST storing external package OBLISTs created by PACKAGE and DEFINITIONS. ZILF predefines three empty compatibility packages on it: NEWSTRUC, ZIL, and ZILCH.

---

### ResPreactions
**Usage:** `PREACTIONS`

Reserved GVAL pointing to the compiler-generated table of verb preaction-routine packed addresses.

---

### ResPrepositions
**Usage:** `PREPOSITIONS`

Compiler-defined constant pointing to the preposition lookup table (mapping vocabulary addresses to preposition numbers).

---

### ResPreserveSpaces
**Usage:** `PRESERVE-SPACES?`

Reserved GVAL (default: <>) controlling whether multiple spaces in strings are preserved instead of collapsed.

---

### ResPrmanyCrlf
**Usage:** `PRMANY-CRLF`

Special symbol recognized as an item in PRINT-MANY to print a carriage-return and line-feed (CRLF) at that position.

---

### ResPropspec
**Usage:** `PROPSPEC`

Special PUTPROP indicator (<PUTPROP item PROPSPEC [function]>) that registers a compile-time handler function invoked whenever item appears as a property inside an OBJECT definition.

---

### ResRedefine
**Usage:** `REDEFINE`

Reserved LVAL (default: <>); when set to T, allows redefining existing FUNCTIONs, ROUTINEs, and other definitions without error.

---

### ResRootOblist
**Usage:** `ROOT (OBLIST)`

Predefined OBLIST (<2 .OBLIST> by default, returned by <ROOT>) containing all built-in SUBRs, FSUBRs, and core symbols such as OBLIST, DEFAULT, and T. Targeted directly by empty trailer syntax (atom!-).

---

### ResSentenceEnds
**Usage:** `SENTENCE-ENDS?`

Reserved FILE-FLAG (Version 6) instructing the compiler to treat two spaces after a period or question mark as a sentence end in TELL.

---

### ResVerbs
**Usage:** `VERBS`

Reserved GVAL pointing to the compiler-generated table of verb syntax pointers.

---

### ResZapToSourceDirectory
**Usage:** `ZAP-TO-SOURCE-DIRECTORY?`

FILE-FLAGS flag from historical ZILCH controlling output directory placement; ignored by ZILF.

---