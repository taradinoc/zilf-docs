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

### ResInZilch
**Usage:** `IN-ZILCH`

Reserved COMPILATION-FLAG (default: <>) indicating ZILCH/compiler context.

---

### ResLastObject
**Usage:** `LAST-OBJECT`

Reserved CONSTANT automatically set by the compiler to the object number of the last object.

---

### ResNewParser
**Usage:** `NEW-PARSER?`

Reserved GVAL (undefined by default); set via <SETG NEW-PARSER? T> to enable the Version 6 new parser vocabulary/syntax format.

---

### ResPreactions
**Usage:** `PREACTIONS`

Reserved GVAL pointing to the compiler-generated table of verb preaction-routine packed addresses.

---

### ResPreserveSpaces
**Usage:** `PRESERVE-SPACES?`

Reserved GVAL (default: <>) controlling whether multiple spaces in strings are preserved instead of collapsed.

---

### ResRedefine
**Usage:** `REDEFINE`

Reserved LVAL (default: <>); when set to T, allows redefining existing FUNCTIONs, ROUTINEs, and other definitions without error.

---

### ResSentenceEnds
**Usage:** `SENTENCE-ENDS?`

Reserved FILE-FLAG (Version 6) instructing the compiler to treat two spaces after a period or question mark as a sentence end in TELL.

---

### ResVerbs
**Usage:** `VERBS`

Reserved GVAL pointing to the compiler-generated table of verb syntax pointers.

---