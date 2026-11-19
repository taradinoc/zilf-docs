[← Back to Main Index](./index.md)

# Appendix A: Other Z-Machine OP-Codes

Z-machine opcodes without direct ZIL function equivalents, used internally by the compiler to invoke routines and control the program counter.

---

### OpCALL
**Usage:** `CALL`

**Alternative Usage:** `call_vs`

Calls routine with 0 to 3 arguments and stores the resulting return value (the only call instruction in Version 3). Calling address 0 does nothing and returns false.

**History:** Zapf syntax: CALL, Inform syntax: call_vs

---

### OpCALL1
**Usage:** `CALL1`

**Alternative Usage:** `call_1s`

Executes routine() and stores resulting return value.

**History:** Zapf syntax: CALL1, Inform syntax: call_1s

---

### OpCALL2
**Usage:** `CALL2`

**Alternative Usage:** `call_2s`

Executes routine(arg1) and stores resulting return value.

**History:** Zapf syntax: CALL2, Inform syntax: call_2s

---

### OpICALL
**Usage:** `ICALL`

**Alternative Usage:** `call_vn`

Like CALL, calls routine with 0 to 3 arguments and discards the result.

**History:** Zapf syntax: ICALL, Inform syntax: call_vn

---

### OpICALL1
**Usage:** `ICALL1`

**Alternative Usage:** `call_1n`

Executes routine() and discards the result.

**History:** Zapf syntax: ICALL1, Inform syntax: call_1n

---

### OpICALL2
**Usage:** `ICALL2`

**Alternative Usage:** `call_2n`

Executes routine(arg1) and discards the result.

**History:** Zapf syntax: ICALL2, Inform syntax: call_2n

---

### OpIXCALL
**Usage:** `IXCALL`

**Alternative Usage:** `call_vn2`

Calls routine with a variable number (0 to 7) of arguments using an extra operand-type byte, discarding the result.

**History:** Zapf syntax: IXCALL, Inform syntax: call_vn2

---

### OpJUMP
**Usage:** `JUMP`

**Alternative Usage:** `jump`

Unconditional jump to a given label using a 2-byte signed offset applied to the program counter.

**History:** Zapf syntax: JUMP, Inform syntax: jump

---

### OpNOOP
**Usage:** `NOOP`

**Alternative Usage:** `nop`

No-operation instruction (never emitted in Infocom story files; likely originally intended as a breakpoint).

**History:** Zapf syntax: NOOP, Inform syntax: nop

---

### OpXCALL
**Usage:** `XCALL`

**Alternative Usage:** `call_vs2`

Like IXCALL, calls routine with 0 to 7 arguments and stores the resulting return value.

**History:** Zapf syntax: XCALL, Inform syntax: call_vs2

---