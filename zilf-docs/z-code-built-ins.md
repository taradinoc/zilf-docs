[← Back to Main Index](./index.md)

# Z-Code Built-ins
---

### PICINF
**Usage:** `<PICINF picture-number table>`

Z-code built-in function that Writes picture data from picture-number into table. Word 0 of table holds picture width and word 1 holds picture height. Then follows the picture data. If picture-number is 0, the number of available pictures is written into word 0 of table and release number of picture file is written into word 1.

> **Note:** ZILF currently supports PICSET in V6.

**History:** Zapf syntax: PICINF, Inform syntax: picture_data

---

### PICSET
**Usage:** `<PICSET table>`

Z-code built-in function that gives the interpreter a table of picture numbers that the interpreter can then unpack from disc and cache in memory.

> **Note:** ZILF currently supports PICSET in V6.

**History:** Zapf syntax: PICSET, Inform syntax: picture_table

---

### POP
**Usage:** `<POP [stack]>`

Z-code built-in function used inside ROUTINE that pops a value from a stack. If no stack is given, a value is popped from the game stack.

> **Note:** ZILF currently supports POP in V6.

**History:** Zapf syntax: POP, Inform syntax: pull

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

> **Note:** ZILF supports POP in all versions.

**History:** Zapf syntax: PUT, Inform syntax: storew

---

### REMOVE
**Usage:** `<REMOVE object>`

Z-code built-in function that removes object from parent. To reattach it to another object, see MOVE.

> **Note:** ZILF supports REMOVE in all versions.

**History:** Zapf syntax: REMOVE, Inform syntax: remove_obj

---