[← Back to Main Index](./index.md)

# Z-Code Built-ins
---

### ERASE
**Usage:** `<ERASE value>`

Z-code built-in function that erases from the current cursor position. This functions behavior is dependent on the supported version.

Versions 4 and 5: if the value is 1, erase from the current cursor position to the end of its line in the current window. If the value is anything other than 1, do nothing.  

Version 6: if the value is 1, erase from the current cursor position to the end of its line in the current window. If not, erase the given number of pixels minus one across from the cursor (clipped to stay inside the right margin). The cursor does not move.

> **Note:** ZILF supports ERASE in versions 4-.

**History:** Zapf syntax: ERASE, Inform syntax: erase_line

---

### F?
**Usage:** `<F? expression>`

Z-code built-in predicate that tests is expression evaluates to false.

> **Note:** ZILF supports FONT in all versions.

---

### FCLEAR
**Usage:** `<FCLEAR object flag>`

Z-code built-in function that removes flag from object.

> **Note:** ZILF supports FCLEAR in all versions.

**History:** Zapf syntax: FCLEAR, Inform syntax: clear_attr

---

### FIRST?
**Usage:** `<FIRST? object>`

Z-code built-in function that returns the first object inside (contained) in the object. Returns 0 (false) if no object exists.

> **Note:** ZILF supports FIRST? in all versions.

**History:** Zapf syntax: FIRST?, Inform syntax: get_child

---

### FONT
**Usage:** `Version 5: <FONT number>, Version 6-: <FONT number [window-number]>`

Z-code built-in function that Sets current font to number. Returns old fonts number. If the font number is not available 0, return false.

The following numbers map to font types.
1 := Normal font
3 := Character graphics font (see section 16 in the Z-Machine Standards Document).
4 := Monospace (fixed-pitch) font

> **Note:** ZILF supports FONT in versions 5-.

**History:** Zapf syntax: FONT, Inform syntax: set_font

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

> **Note:** ZILF currently supports PICINF in versions 6-.

**History:** Zapf syntax: PICINF, Inform syntax: picture_data

---

### PICSET
**Usage:** `<PICSET table>`

Z-code built-in function that gives the interpreter a table of picture numbers that the interpreter can then unpack from disc and cache in memory.

> **Note:** ZILF currently supports PICSET in versions 6-.

**History:** Zapf syntax: PICSET, Inform syntax: picture_table

---

### POP
**Usage:** `<POP [stack]>`

Z-code built-in function used inside ROUTINE that pops a value from a stack. If no stack is given, a value is popped from the game stack.

> **Note:** ZILF currently supports POP in versions 6-.

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

### QUIT
**Usage:** `<QUIT [exit-code]>`

MDL built-in function that exits ZILF (interpreter mode) and returns to the operating system with exit-code.

> **Note:** ZILF supports QUIT in all versions.

**History:** Zapf syntax: QUIT, Inform syntax: quit

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

### RFALSE
**Usage:** `<RFALSE>`

Z-code built-in function that  always exits routine and returns false (0). Note that this differs from RETURN that can both exit program blocks and routines.

> **Note:** ZILF supports RFALSE in all versions.

**History:** Zapf syntax: RFALSE, Inform syntax: rfalse

---

### RFATAL
**Usage:** `<RFATAL>`

Z-code built-in function that always exits routine and returns FATAL-VALUE (2). Note that this differs from RETURN that can both exit program blocks and routines.

---

### RSTACK
**Usage:** `<RSTACK>`

Z-code built-in function that pops value from the game stack and returns that value.

> **Note:** ZILF supports RSTACK in all versions.

**History:** Zapf syntax: RSTACK, Inform syntax: ret_popped

---

### RTRUE
**Usage:** `<RTRUE>`

Z-code built-in function that always exits routine and returns true (1). Note that this differs from RETURN that can both exit program blocks and routines.

> **Note:** ZILF supports RTRUE in all versions.

**History:** Zapf syntax: RTRUE, Inform syntax: rtrue

---

### SAVE
**Usage:** `<SAVE>  ;  Versions 1-4, 
<SAVE [table] [bytes] [filename]>  ;  Versions 5-`

Z-code built-in function that saves a game state that later can be restored. All questions about filename and path are asked by the interpreter. 

SAVE returns 0 if SAVE fails and 1 if it is successful. 

SAVE also can return 2. That means this is a continuation from a successful RESTORE.

See RESTORE on code example on SAVE and RESTORE.

See The Inform Designer’s Manual (ch. §42, p. 319) and The Z-machine Standards Document for a description about how to SAVE and RESTORE auxiliary files.

> **Note:** ZILF supports SAVE in all versions.

**History:** Zapf syntax: SAVE, Inform syntax: save

---

### SCREEN
**Usage:** `<SCREEN window-number>`

Z-code built-in function that selects window-number for text output. Note that in versions 3-5 only the lower screen (window-number = 0) has text-buffering and word-wrap.

> **Note:** ZILF supports SCREEN in versions 3-.

**History:** Zapf syntax: SCREEN, Inform syntax: set_window

---

### SCROLL
**Usage:** `<SCROLL window-number pixels>`

Z-code built-in function that scrolls window-number up (pixels is positive) or down (pixels is negative) by the number of supplied pixels. New lines are empty (background color).

> **Note:** ZILF supports SCROLL in versions 6-.

**History:** Zapf syntax: SCROLL, Inform syntax: scroll_window

---

### SET
**Usage:** `MDL: <SET atom value [environment]>,
Zapf: <SET name value>`

MDL built-in function that asigns a value to the local atom. It is possible to supply an environment for SET. See EVAL for more about the environment.

Z-code built-in function that stores value in local variable name.

> **Note:** ZILF supports SET in all versions.

**History:** Zapf syntax: SET, Inform syntax: store

---

### SETG
**Usage:** `MDL: <SETG atom value>,
Zapf: <SETG name value>`

MDL built-in function that assigns a value to the global atom. If an atom is already assigned a value, it is changed.

Z-code built-in function that Store value in global variable name. The name variable must be declared with GLOBAL outside the ROUTINE.

> **Note:** ZILF supports SETG in all versions.

**History:** Zapf syntax: SETG, Inform syntax: store

---