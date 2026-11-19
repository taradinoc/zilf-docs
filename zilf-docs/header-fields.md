[← Back to Main Index](./index.md)

# Appendix B: Z-Machine Header Fields

Z-machine ordinary and extended header field-spec symbols used with LOWCORE and LOWCORE-TABLE.

---

## Ordinary Header Fields
*Standard 64-byte Z-machine header fields (bytes 0-55) accessible via LOWCORE and LOWCORE-TABLE.*

### HdrCHRSET
**Usage:** `CHRSET`

Bytes 52-53 (Ver 5-, R): Alphabet table byte address, or 0 for default ZSCII alphabet.

---

### HdrCLRWRD
**Usage:** `CLRWRD`

Bytes 44-45 (Ver 5-, R): Default background color (byte 44) and default foreground color (byte 45).

---

### HdrCRCNT
**Usage:** `CRCNT`

Bytes 48-49 (Ver 5, R/W): Version 5 header field at bytes 48-49.

---

### HdrCRFUNC
**Usage:** `CRFUNC`

**Alternative Usage:** `STDREV`

Bytes 50-51 (Ver 1-, R/W): Standard revision number.

---

### HdrENDLOD
**Usage:** `ENDLOD`

Bytes 4-5 (Ver 1-, R): Base of high memory (byte address).

---

### HdrEXTAB
**Usage:** `EXTAB`

Bytes 54-55 (Ver 5-, R): Header extension table byte address.

---

### HdrFLAGS
**Usage:** `FLAGS`

Bytes 16-17 (Flags 2, R/W): Bit 0 transcripting (V1-, R/W), Bit 1 force monospace (V3-, R/W), Bit 2 redraw request (V6-, R/W), Bit 3 pictures (V5-, R), Bit 4 UNDO (V5-, R; V3 Lurking Horror sound), Bit 5 mouse (V5-, R), Bit 6 colors (V5-, R), Bit 7 sound (V5-, R), Bit 8 menu (V6, R).

---

### HdrFWORDS
**Usage:** `FWORDS`

Bytes 24-25 (Ver 2-, R): Byte address of the abbreviations (frequent words) table.

---

### HdrFWRD
**Usage:** `FWRD`

Bytes 38-39 (Ver 5-, R): Font width and height in units (V5: byte 38 width, byte 39 height; V6+: byte 38 height, byte 39 width).

---

### HdrGLOBALS
**Usage:** `GLOBALS`

Bytes 12-13 (Ver 1-, R): Byte address of the global variables table.

---

### HdrHWRD
**Usage:** `HWRD`

Bytes 34-35 (Ver 5-, R): Screen width in units.

---

### HdrINTID
**Usage:** `INTID`

Byte 30 (Ver 4-, R): Interpreter number.

---

### HdrINTVER
**Usage:** `INTVER`

Byte 31 (Ver 4-, R): Interpreter version.

---

### HdrINTWRD
**Usage:** `INTWRD`

Bytes 30-31 (Ver 4-, R): Interpreter number and version word.

---

### HdrLMRG
**Usage:** `LMRG`

**Alternative Usage:** `FOFF`

Bytes 40-41 (Ver 5-, R): Routines offset divided by 8.

---

### HdrOBJECT
**Usage:** `OBJECT`

Bytes 10-11 (Ver 1-, R): Byte address of the object table.

---

### HdrPCHKSUM
**Usage:** `PCHKSUM`

Bytes 28-29 (Ver 3-, R): File checksum verified by VERIFY.

---

### HdrPLENTH
**Usage:** `PLENTH`

Bytes 26-27 (Ver 3-, R): Length of story file (scaled by version).

---

### HdrPURBOT
**Usage:** `PURBOT`

Bytes 14-15 (Ver 1-, R): Base of static memory (byte address).

---

### HdrRMRG
**Usage:** `RMRG`

**Alternative Usage:** `SOFF`

Bytes 42-43 (Ver 5-, R): Static strings offset divided by 8.

---

### HdrSCRH
**Usage:** `SCRH`

Byte 33 (Ver 4-, R): Screen width in characters.

---

### HdrSCRV
**Usage:** `SCRV`

Byte 32 (Ver 4-, R): Screen height in lines (255 = infinite).

---

### HdrSCRWRD
**Usage:** `SCRWRD`

Bytes 32-33 (Ver 4-, R): Screen height and width word.

---

### HdrSERI1
**Usage:** `SERI1`

Bytes 20-21 (Ver 3-, R): Serial number MM-part.

---

### HdrSERI2
**Usage:** `SERI2`

Bytes 22-23 (Ver 3-, R): Serial number DD-part.

---

### HdrSERIAL
**Usage:** `SERIAL`

Bytes 18-19 (Ver 3-, R): Serial number YY-part (start of 6-byte ASCII serial number).

---

### HdrSTART
**Usage:** `START`

Bytes 6-7 (Ver 1-5/6, R): Initial program counter byte address (V1-5) or packed address of initial main routine (V6).

---

### HdrTCHARS
**Usage:** `TCHARS`

Bytes 46-47 (Ver 5-, R): Byte address of terminating characters table.

---

### HdrTWID
**Usage:** `TWID`

Bytes 48-49 (Ver 6-, R): Total width in pixels of text sent to output stream 3.

---

### HdrVOCAB
**Usage:** `VOCAB`

Bytes 8-9 (Ver 1-, R): Byte address of the dictionary (vocabulary table).

---

### HdrVWRD
**Usage:** `VWRD`

Bytes 36-37 (Ver 5-, R): Screen height in units.

---

### HdrZORKID
**Usage:** `ZORKID`

**Alternative Usage:** `RELEASEID`

Bytes 2-3 (Ver 1-, R): Release number word (traditionally 11 bits masked with *3777* in Infocom games).

---

### HdrZVERSION
**Usage:** `ZVERSION`

Bytes 0-1 (Ver 1-, R): Byte 0 is the Z-machine version number; Byte 1 is Flags 1 (V1-3: status line type, split disc, Tandy bit, status line unavailable, screen-splitting, proportional font; V4+: colors, pictures, bold, italic, monospace, sound, timed input).

---

## Extended Header Fields
*Header extension table fields (Version 5+, pointed to by EXTAB) accessible via LOWCORE.*

### HdrBSTAT
**Usage:** `BSTAT`

Extended header bytes 20-21 (Ver 5-, R/W): Extended header button status field.

---

### HdrBUTTON
**Usage:** `BUTTON`

Extended header bytes 16-17 (Ver 5-, R/W): Extended header button state field.

---

### HdrJOYSTICK
**Usage:** `JOYSTICK`

Extended header bytes 18-19 (Ver 5-, R/W): Extended header joystick field.

---

### HdrJSTAT
**Usage:** `JSTAT`

Extended header bytes 22-23 (Ver 5-, R/W): Extended header joystick status field.

---

### HdrMSEDIR
**Usage:** `MSEDIR`

**Alternative Usage:** `FLAGS3`

Extended header bytes 8-9 (Ver 5-, R/W): Flags 3 (Bit 0: game wants to use transparency).

---

### HdrMSEINV
**Usage:** `MSEINV`

**Alternative Usage:** `TRUFGC`

Extended header bytes 10-11 (Ver 5-, R/W): True default foreground colour.

---

### HdrMSETBL
**Usage:** `MSETBL`

**Alternative Usage:** `UNITBL`

Extended header bytes 6-7 (Ver 5-, R/W): Unicode translation table address (optional).

---

### HdrMSEVRB
**Usage:** `MSEVRB`

**Alternative Usage:** `TRUBGC`

Extended header bytes 12-13 (Ver 5-, R/W): True default background colour.

---

### HdrMSEWRD
**Usage:** `MSEWRD`

Extended header bytes 14-15 (Ver 5-, R/W): Extended header mouse word.

---

### HdrMSLOCX
**Usage:** `MSLOCX`

Extended header bytes 2-3 (Ver 5-, R): X-coordinate of mouse after a click.

---

### HdrMSLOCY
**Usage:** `MSLOCY`

Extended header bytes 4-5 (Ver 5-, R): Y-coordinate of mouse after a click.

---