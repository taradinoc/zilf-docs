[← Back to Main Index](./index.md)

# Z-Code Built-ins
---

### BACK
**Usage:** `<BACK table [bytes]>`

Z-code built-in function that returns table with address moved bytes back. If the count moves past the start of the table no error is raised. Default value for bytes is 1. 

Note that this is not a copy of the table, it is pointing to the same table with another starting address. Also see GET, GETB, PUT, PUTB and REST.

---

### BCOM
**Usage:** `<BCOM value>`

Z-code built-in function that is a bitwise NOT, reversing all bits in the WORD value (16 bits).

> **Note:** ZILF supports BCOM in all versions.

**History:** Zapf syntax: BCOM, Inform syntax: not

---

### BTST
**Usage:** `<BTST value1 value2>`

Z-code built-in predicate that performs a binary test that evaluates to true if all value2 bits are set in value1. Could be expressed as <=? <BAND value1 value2> value2>.

> **Note:** ZILF supports BTST in all versions.

**History:** Zapf syntax: BTST, Inform syntax: test

---

### BUFOUT
**Usage:** `<BUFOUT value>`

Z-code built-in flag that controls if output is buffered (to enable proper word-wrap). value can be true or false.

> **Note:** ZILF supports BUFOUT in versions 4-.

**History:** Zapf syntax: BUFOUT, Inform syntax: buffer_mode

---

### CATCH
**Usage:** `<CATCH>`

Used in conjunction with THROW, this Z-code built-in function returns the current state of the stack (the "stack frame"). Also see THROW.

> **Note:** ZILF supports CATCH in versions 5-.

**History:** Zapf syntax: CATCH, Inform syntax: catch

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

### IN?
**Usage:** `<IN? object1 object2>`

Z-code built-in predicate that returns true if object1 is in object2 (object1 has object2 as parent),otherwise false.

> **Note:** ZILF supports IN? in all versions.

**History:** Zapf syntax: IN?, Inform syntax: jin

---

### INC
**Usage:** `<INC name>`

Z-code built-in function that increments name by 1, which is signed, such that -1 increments to 0.

> **Note:** ZILF supports INC in all versions.

**History:** Zapf syntax: INC, Inform syntax: inc

---

### INPUT
**Usage:** `<INPUT 1 [time] [routine]>`

Z-code built-in function that  reads a single character from the keyboard. Calls routine every time*0.1 s. If routine returns true input is aborted.

> **Note:** ZILF supports INPUT in versions 4-.

**History:** Zapf syntax: INPUT, Inform syntax: read_char

---

### INTBL?
**Usage:** `<INTBL? value table length [rec-spec]>  ;  "Version 5, 7-"
<INTBL? value table length>   ;  "Version 4, 6"`

Z-code built-in predicate that that returns the address of value if value is in the table table of the length length, otherwise 0. 

In version 5, 7 and 8 the rec-spec describes the field where bit 7 is set for words and clear for bytes, rest defines the length of the field.

> **Note:** ZILF supports INTBL? in versions 4-.

**History:** Zapf syntax: INTBL?, Inform syntax: scan_table

---

### IRESTORE
**Usage:** `<IRESTORE>`

Z-code built-in function that restores game state saved to memory by ISAVE (undo).

> **Note:** ZILF supports IRESTORE in versions 5-.

**History:** Zapf syntax: IRESTORE, Inform syntax: restore_undo

---

### ISAVE
**Usage:** `<ISAVE>`

Z-code built-in function that saves the game state to memory that later can be restored by IRESTORE (undo). Returns 0 if ISAVE fails, returns 1 if it is successful, and returns -1 if the interpreter does not handle undo.

> **Note:** ZILF supports ISAVE in versions 5-.

**History:** Zapf syntax: ISAVE, Inform syntax: save_undo

---

### LEX
**Usage:** `<LEX text parse [dictionary] [flag]>`

Z-code built-in function that parses the text into parse. See READ for more info about parsing. The game dictionary is used if not a dictionary table (LTABLE) is supplied. If the length of the dictionary is negative, the dictionary can be unsorted. If the flag is set (true), unrecognized words are not written to parse but their slot is left unmodified. This makes it possible to run LEX against different dictionaries serially. Also see READ.

> **Note:** ZILF supports LEX in versions 4-.

**History:** Zapf syntax: LEX, Inform syntax: tokenise

---

### LOC
**Usage:** `<LOC object>`

Z-code built-in function that returns parent to object.

> **Note:** ZILF supports LOC in all versions.

**History:** Zapf syntax: LOC, Inform syntax: get_parent

---

### LOWCORE
**Usage:** `<LOWCORE field-spec [new-value]>`

Z-code built-in function that reads and in some cases writes to the header information fields.

> **Note:** TODO: Valid values for field-spec to be listed in a separate document to be linked from this note.

---

### LOWCORE-TABLE
**Usage:** `<LOWCORE-TABLE field-spec length routine>`

Z-code built-in function that reads the length number of bytes from field-spec and calls routine between each byte.

> **Note:** TODO: Valid values for field-spec to be listed in a separate document to be linked from this note.

---

### LTABLE
**Usage:** `<LTABLE [(flags ...)] values ...>`

Z-code built-in function that Defines a table containing the specified values and with the LENGTH flag.

> **Note:** See TABLE for more information about LENGTH and other flags.

---

### LVAL
**Usage:** `<LVAL name>`

**Alternative Usage:** `.name`

Z-code built-in function that gets the value of local variable name.

> **Note:** LVAL is more often used in its short for, which is .name.

---

### MAP-CONTENTS
**Usage:** `<MAP-CONTENTS (name [next] object) [(END expressions ...)] expressions ...>`

Z-code built-in function that loops over all objects that have an object as parent (all children to object). For each iteration name is assigned the current child-object and next the child-object that will be name in the next iteration (0 if the current name is the last child).

For each iteration the expressions are evaluated and, if supplied, the (END expressions...) is evaluated last after all iterations.

---

### MAP-DIRECTIONS
**Usage:** `<MAP-DIRECTIONS (name pt room)  [(END expressions ...)] expressions ...>`

Z-code built-in function that loops over all defined directions in a room. For each iteration name is assigned the current direction and pt is the property for this direction.

For each iteration the expressions are evaluated and, if supplied, the (END expressions...) is evaluated last after all iterations.

---

### MARGIN
**Usage:** `<MARGIN left right [window-number]>`

Z-code built-in function that sets the left and right margin (in pixels) of the given window-number. If no window-number is specified, MARGIN sets margins in window-number 0.

> **Note:** ZILF supports MARGIN in versions 6-.

**History:** Zapf syntax: MARGIN, Inform syntax: set_margins

---

### MENU
**Usage:** `<MENU number table>`

Z-code built-in function that controls menu 3- (not menu 0-2, they are system menus). The table is a LTABLE of LTABLE. Item 1 being the menu name. Item 2- are the entries.

> **Note:** ZILF supports MENU in versions 6-.

**History:** Zapf syntax: MENU, Inform syntax: make_menu

---

### MOD
**Usage:** `<MOD number1 number2>`

Z-code built-in function that Returns remainder of 16-bit signed division. number2 is not allowed to be 0 ("Division by zero").

> **Note:** ZILF supports MOD in all versions.

**History:** Zapf syntax: MOD, Inform syntax: mod

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

### SOUND
**Usage:** `<SOUND number [effect] [volume]>  ;  "Versions 3-4",
<SOUND number [effect] [volrep] [routine]>  ;  "Versions 5-"`

Z-code built-in  that plays sound number (1 = high-pitch beep, 2 = low-pitch beep and 3- is user defined). 

Valid entries for effect are 1 = prepare, 2 = start, 3 = stop and 4 = finished with. 

The volrep is calculated as 256 * repetitions + volume. Repetitions can be 0-255 (255 = infinite) and volume 1-8, 255 (1 =  quiet, 8 = loud, 255 = loudest possible. Note that repetitions only are valid from version 5 onward. For version 5 and later a repetition equal to 0 is considered illegal but it’s suggested that interpreters should treat this as a request to play the sound once. 

If routine is supplied it is called after sound is finished. 

See The Inform Designer’s Manual (ch. §42, p. 315-316 and ch. §43) and The Z-machine Standards Document for a description about how to include sound in games.

> **Note:** ZILF supports SOUND in versions 3-.

**History:** Zapf syntax: SOUND, Inform syntax: sound_effect

---

### SPLIT
**Usage:** `<SPLIT number>`

Z-code built-in function that splits the screen  in two parts with the upper part having number rows. If number is 0 the screen is unsplit.The upper screen is window-number 1 and the lower screen is window-number 0.

See SCREEN for example on how to use SPLIT.

> **Note:** ZILF supports SPLIT in versions 3-.

**History:** Zapf syntax: SPLIT, Inform syntax: split_window

---

### THROW
**Usage:** `<THROW value stack-frame>`

Z-code built-in function that is used with CATCH. THROW sets the stack to stack-frame and returns value (the result is that execution returns from the routine where the stack-frame was "caught" with value as the routines return value. Also see CATCH.

> **Note:** ZILF supports THROW in versions 5-.

**History:** Zapf syntax: THROW, Inform syntax: throw

---

### USL
**Usage:** `<USL>`

Z-code built-in function that updates the status line. This command is only recognized in version 3.

> **Note:** ZILF supports USL in version 3.

**History:** Zapf syntax: USL, Inform syntax: show_status

---

### VALUE
**Usage:** `MDL: <VALUE atom [environment]>, 
Zapf: <VALUE name/number>`

MDL built-in function that returns the value of an atom. If  the atom has an LVAL then the LVAL is returned, otherwise the GVAL of the atom is returned. It is possible to supply an environment for VALUE. See EVAL for more about the environment.

Z-code built-in function that loads name/number. Note that this command is mostly redundant and rarely used.

> **Note:** ZILF supports VALUE in all versions.

**History:** Zapf syntax: VALUE, Inform syntax: load

---

### VERIFY
**Usage:** `<VERIFY>`

Z-code built-in function that returns true if sum($0040:PLENTH (byte 26-27 in header)) MOD $10000 = PCHKSUM (byte 28-29 in header), otherwise false.

> **Note:** ZILF supports VERIFY in all versions.

**History:** Zapf syntax: VERIFY, Inform syntax: verify

---

### WINGET
**Usage:** `<WINGET window-number property>`

Z-code built-in function that reads property on window-number.

> **Note:** ZILF supports WINGET in versions 6-.

**History:** Zapf syntax: WINGET, Inform syntax: get_wind_prop

---

### WINPOS
**Usage:** `<WINPOS window-number row column>`

Z-code built-in function that moves window-number to position row column (pixels). (1, 1) is in the top left corner.

> **Note:** ZILF supports WINPOS in versions 6-.

**History:** Zapf syntax: WINPOS, Inform syntax: move_window

---

### WINPUT
**Usage:** `<WINPUT window-number property value>`

Z-code built-in function that writes value to property window-number.

> **Note:** ZILF supports WINPUT in versions 6-.

**History:** Zapf syntax: WINPUT, Inform syntax: put_wind_prop

---

### WINSIZE
**Usage:** `<WINSIZE window-number height width>`

Z-code built-in function that changes window-number size.

> **Note:** ZILF supports WINSIZE in versions 6-.

**History:** Zapf syntax: WINSIZE, Inform syntax: window_size

---

### XPUSH
**Usage:** `<XPUSH value stack>`

Z-code built-in function that pushes value on the stack.

> **Note:** ZILF supports XPUSH in versions 6-.

**History:** Zapf syntax: XPUSH, Inform syntax: push_stack

---

### ZWSTR
**Usage:** `<ZWSTR src-table length offset dest-table>`

Z-code built-in function that encodes length characters starting at offset from ZSCII word zscii-text and stores result in 6-byte Z-encoded dest-table.

> **Note:** ZILF supports ZWSTR in versions 5-.

**History:** Zapf syntax: ZWSTR, Inform syntax: encode_text

---