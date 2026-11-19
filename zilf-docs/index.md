# ZILF Language Reference
**Scheme:** ZILF Reference Scheme

Welcome to the ZILF Reference Guide. Select a concept below to view detailed documentation.

| Concept | Description |
| :--- | :--- |
| **[Language Fundamentals](./language-fundamentals.md)** | Primitive/derived data types (`ATOM`, `FIX`, `LIST`, `TABLE`) and lexical/evaluation rules (`%`, `%%`, `OBLIST`s, segments). |
| **[Core Functions](./core-functions.md)** | Fundamental MDL built-in functions and ZIL library functions (`EVAL`, `ROUTINE`, `DEFSTRUCT`). |
| **[Z-Code Built-ins](./z-code-built-ins.md)** | Z-machine instructions used inside `ROUTINE` (`POP`, `TELL`, `DO`). |
| **[Object System](./object-system.md)** | Entities (`OBJECT`, `ROOM`), properties (`DESC`, `SYNONYM`), and state flags (`LIGHTBIT`, `OPENBIT`, `TAKEBIT`). |
| **[Parser System](./parser-system.md)** | Directives for vocabulary/syntax (`VOC`, `SYNTAX`, `SYNONYM`), search flags (`HAVE`, `TAKE`), and Appendix D internal parser tables. |
| **[Z-Machine OP-Codes](./z-machine-opcodes.md)** | Appendix A: Low-level Z-machine opcodes without direct ZIL equivalents (`CALL`, `ICALL`, `JUMP`). |
| **[Z-Machine Header Fields](./header-fields.md)** | Appendix B: Ordinary and extended Z-machine header `field-spec` symbols for `LOWCORE` and `LOWCORE-TABLE`. |
| **[Reserved Symbols](./reserved-symbols.md)** | Appendix C: Compiler-reserved constants, globals, locals, and flags (`REDEFINE`, `NEW-PARSER?`, `DO-FUNNY-RETURNS?`). |

---

## Coding Cookbook
For practical implementation patterns, consult the cookbook:
* **[View the Cookbook](./cookbook.md)** – A collection of code examples extracted directly from the ZILF ontology.

Copyright (C) 2026 ZILF Contributors. Permission is granted to copy, distribute and/or modify this document under 
the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software 
Foundation; with no Invariant Sections, no Front- Cover Texts, and no Back-Cover Texts. A copy of the license is 
included in the section entitled "GNU Free Documentation License".
