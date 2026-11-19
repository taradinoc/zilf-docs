[← Back to Main Index](./index.md)

# Language Fundamentals

Core ZILF/MDL language fundamentals covering primitive and derived data types, truth semantics, OBLISTs, blocking, read macros, and segments.

---

## Data Types
*Primitive types (ATOM, FIX, LIST, STRING, TABLE, VECTOR) and derived/structured types recognized by ZILF.*

### TypeADECL
**Usage:** `ADECL (Type)`

Annotated declaration binding an identifier or placeholder to a DECL pattern using colon syntax (e.g., X:FIX or *:FIX).

---

### TypeASOC
**Usage:** `ASOC (Type)`

Type representing an entry in the global association chain containing ITEM, INDICATOR, and AVALUE.

---

### TypeATOM
**Usage:** `ATOM (Primitive Type)`

Primitive type representing a named identifier/variable with a print name (PNAME) that can hold both a global value (GVAL) and a local value (LVAL).

---

### TypeBYTE
**Usage:** `BYTE (Type)`

Derived type (PRIMTYPE FIX, 8-bit 0-255) representing a single unsigned byte value, created via <BYTE n> or #BYTE n.

---

### TypeCHANNEL
**Usage:** `CHANNEL (Type)`

Structured type representing an I/O channel (such as .OUTCHAN or a file opened with OPEN).

---

### TypeCHARACTER
**Usage:** `CHARACTER (Type)`

Derived type (PRIMTYPE FIX, 8-bit 0-255) representing a single character, written with !\ prefix (e.g., !\A).

---

### TypeDECL
**Usage:** `DECL (Type)`

Structured type representing a type/structure declaration pattern (e.g., #DECL ((X) FIX)) used for compile-time type checking.

---

### TypeFALSE
**Usage:** `FALSE (Type)`

Derived structured type (PRIMTYPE LIST) representing boolean falsity outside routines, evaluating to an empty form <> (#FALSE ()).

---

### TypeFIX
**Usage:** `FIX (Primitive Type)`

Primitive type representing a 32-bit signed integer (-2147483648 to 2147483647). Supports decimal, octal (*747*), and binary (#2 10110111) literals.

---

### TypeFORM
**Usage:** `FORM (Type)`

Derived structured type (PRIMTYPE LIST) enclosed in angle brackets <...> representing an evaluable expression.

---

### TypeFSUBR
**Usage:** `FSUBR (Type)`

Applicable built-in special form whose arguments are not automatically evaluated before invocation.

---

### TypeFUNCTION
**Usage:** `FUNCTION (Type)`

Derived structured and applicable type (PRIMTYPE LIST) created by FUNCTION or DEFINE.

---

### TypeLIST
**Usage:** `LIST (Primitive Type)`

Primitive type representing a forward-linked list enclosed in parentheses (...). Base PRIMTYPE for FORM, FUNCTION, MACRO, FALSE, DECL, and SEGMENT.

---

### TypeMACRO
**Usage:** `MACRO (Type)`

Derived structured and applicable type (PRIMTYPE LIST) created by DEFMAC; evaluated twice (expansion at compile time, then evaluation of result).

---

### TypeOBLIST
**Usage:** `OBLIST (Type)`

Structured type representing an object list (namespace/symbol table) of ATOMs.

---

### TypeSEGMENT
**Usage:** `SEGMENT (Type)`

Structured type (PRIMTYPE LIST) written !<...> that evaluates to a structure and splices its elements into an enclosing structure.

---

### TypeSPLICE
**Usage:** `SPLICE (Type)`

Structured type used internally when splicing multiple expressions during macro expansion.

---

### TypeSTRING
**Usage:** `STRING (Primitive Type)`

Primitive type representing a contiguous byte array of characters enclosed in double quotes ("...").

---

### TypeSUBR
**Usage:** `SUBR (Type)`

Applicable built-in primitive subroutine whose arguments are evaluated before invocation.

---

### TypeTABLE
**Usage:** `TABLE (Primitive Type)`

ZIL-specific primitive type representing a zero-based contiguous byte or word array without per-element type tags. Not considered STRUCTURED? in MDL.

---

### TypeUVECTOR
**Usage:** `UVECTOR (Type)`

MDL uniform vector type (![... !]) where all elements share a single type. ZILF does not distinguish UVECTOR and treats it as a standard VECTOR.

---

### TypeVECTOR
**Usage:** `VECTOR (Primitive Type)`

Primitive type representing a contiguous array of typed elements enclosed in square brackets [...].

---

## Lexical and Evaluation Rules
*Core ZILF/MDL lexical, scoping, truth-value, and read-time evaluation mechanisms.*

### RuleBlocking
**Usage:** `Dynamic and Static (Lexical) Blocking`

ZILF prevents identifier collisions via dynamic blocking (stack-scoped LVALs in FUNCTION, BIND, PROG, REPEAT) and static/lexical blocking (switching .OBLIST namespaces via BLOCK/ENDBLOCK, PACKAGE, and DEFINITIONS).

---

### RuleOblists
**Usage:** `OBLISTs and !- Trailer Syntax`

OBLISTs are namespaces of ATOMs. ZILF predefines INITIAL (user atoms) and ROOT (built-in primitives), searched via the local LIST .OBLIST. Trailer syntax atom!-oblist disambiguates or creates atoms on a specific oblist (atom!- targets ROOT).

---

### RuleReadMacroDoublePercent
**Usage:** `%% (Read Macro)`

Read-time evaluation macro that immediately passes the following MDL object to EVAL during READ for its side effects, discarding the return value so nothing is inserted into the surrounding expression.

---

### RuleReadMacroPercent
**Usage:** `% (Read Macro)`

Read-time evaluation macro that immediately passes the following MDL object to EVAL during READ and splices the resulting value into the surrounding expression before READ continues.

---

### RuleSegments
**Usage:** `!<...> (Segments)`

Segment syntax (!<function args ...!>, trailing ! optional, also !.LVAL / !,GVAL) that evaluates to a structure and splices its elements directly into an enclosing structure.

---

### RuleTrueFalse
**Usage:** `TRUE and FALSE Semantics`

Outside routines (MDL), FALSE is its own TYPE evaluating to <> (#FALSE ()), and 0 is truthy. Inside routines (Z-code), 0 is FALSE and all non-zero values are TRUE. Consequently, <=? <> 0> is FALSE outside a routine but TRUE inside a routine.

---