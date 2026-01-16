[← Back to Main Index](./index.md)

# Z-Code Built-ins
---

### FSET
**Usage:** `<FSET object flag>`

Z-code built-in function adds flag to object.

> **Note:** ZILF supports FSET in all versions.

**History:** Zapf syntax: FSET, Inform syntax: set_attr

---

### FSET?
**Usage:** `<FSET? object flag>`

Z-code built-in predicate that tests if the flag is set on the object.

> **Note:** ZILF supports FSET? in all versions.

**History:** Zapf syntax: FSET?, Inform syntax: test_attr

---

### GET
**Usage:** `<GET table offset>`

Z-code built-in function that returns WORD-record (2 bytes) stored at offset. Note that table is an address in memory so the WORD that is returned is at table+offset*2. It is legal to use, for example, 0 as an address to retrieve information from the header. 

Also see BACK, GETB, PUT, PUTB and REST.

> **Note:** ZILF supports GET in all versions.

**History:** Zapf syntax: GET, Inform syntax: loadw

---

### GETB
**Usage:** `<GETB table offset>`

Z-code built-in that returns BYTE-record (1 byte) stored at offset. Note that table is an address in memory so the BYTE that is returned is at table+offset. It is legal to use, for example, 0 as an address to retrieve information from the header. 

Also see BACK, GET, PUT, PUTB and REST.

> **Note:** ZILF supports GETB in all versions.

**History:** Zapf syntax: GETB, Inform syntax: loadb

---

### GETP
**Usage:** `<GETP object property>`

Z-code built-in function that gets property from the object. Returns default value if property is not declared in the object.

> **Note:** ZILF supports GETP in all versions.

**History:** Zapf syntax: GETP, Inform syntax: get_prop

---

### GETPT
**Usage:** `<GETPT object property>`

Z-code built-in that gets property address from object. Returns 0 (false) if property is not declared in the object.

> **Note:** ZILF supports GETPT in all versions.

**History:** Zapf syntax: GETPT, Inform syntax: get_prop_addr

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

### PUT
**Usage:** `<PUT table offset value>`

Z-code built-in function that puts a 16-bit WORD value in the table at word position offset. Actual address is table-address+offset*2. Note that table can be a byte-address in dynamic memory. 

Also see BACK, GET, GETB, PUTB and REST.

> **Note:** ZILF supports PUT in all versions.

**History:** Zapf syntax: PUT, Inform syntax: storew

---

### PUTB
**Usage:** `<PUTB table offset value>`

Z-code built-in function that puts a byte value in the table at byte position offset. The actual address is table-address+offset. Note that table can be a byte-address in dynamic memory.

Also see BACK, GET, GETB, PUT and REST.

> **Note:** ZILF supports PUTB in all versions.

**History:** Zapf syntax: PUTB, Inform syntax: storeb

---

### PUTP
**Usage:** `<PUTP object property value>`

Z-code built-in function that puts value into property on the object.

> **Note:** ZILF supports PUTP in all versions.

**History:** Zapf syntax: PUTP, Inform syntax: put_prop

---

### RANDOM
**Usage:** `<RANDOM range>`

Z-code built-in function that returns a random number between 1 and range. If range is negative the randomizer is reseeded with -range (absolute value of range).

> **Note:** ZILF supports RANDOM in all versions.

**History:** Zapf syntax: RANDOM, Inform syntax: random

---

### REMOVE
**Usage:** `<REMOVE object>`

Z-code built-in function that removes object from parent. To reattach it to another object, see MOVE.

> **Note:** ZILF supports REMOVE in all versions.

**History:** Zapf syntax: REMOVE, Inform syntax: remove_obj

---