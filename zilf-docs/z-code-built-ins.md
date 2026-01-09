[← Back to Main Index](./index.md)

# Z-Code Built-ins
---

### POP
**Usage:** `<POP [stack]>`

Z-code built-in function used inside ROUTINE that pops a value from a stack.

> **Note:** If no stack is given, a value is popped from the game stack.

**History:** POP is a valid opcode for all versions but ZILF only recognizes POP for Version 6. Inform used the PUSH opcode instead of POP because Inform featured an RFATAL macro, which was usually defined as <PUSH 2> <RSTACK>.

---