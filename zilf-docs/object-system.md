[← Back to Main Index](./index.md)

# Object System
**Parent Concept:** Object System

Entities (`OBJECT`), properties (`DESC`, `SYNONYM`), and state flags (`ONBIT`, `TAKEBIT`).

---

### OBJECT
**Usage:** `<OBJECT name (property values ...) ...>`

ZIL library function that creates an object with the internal objectname, name. After the name follows LISTs of properties for the OBJECT and the values for each property. Which properties that define up a OBJECT is determined by the parser and it’s possible to add new properties with PROPDEF as long as the parser is modified to support the new property. Below is a list of common properties.

*  IN or LOC is the OBJECTs initial location. This could, for example, be a ROOM, another OBJECT (container) or the player (in its inventory). There are a couple of special locations like GLOBAL-OBJECTS for OBJECTs that the player can refer to everywhere, LOCAL-GLOBALS for OBJECTs the player can refer to in ROOMs that define this OBJECT in its GLOBAL list and GENERIC-OBJECTS for OBJECTs that are concepts more than objects (for example the murder or the new will in Deadline).

*  SYNONYMS lists all the nouns that can be used to refer to the OBJECT.

*  ADJECTIVE lists all the adjectives that can be used to refer to the OBJECT.

* DESC is the short description text of the OBJECT. This is the text that is, for example, printed in the players inventory.

*  FLAGS lists all the flagbits that are set on this OBJECT.

*  FDESC means "first description," and it is the text that is used to describe the OBJECT until it is touched (picked up).

*  LDESC means "long description," and it is the text that is used to describe the OBJECT, when it is on the ground, after it is touched.

*  GLOBAL is an optional property. This is a LIST of all the OBJECTs that is IN the LOCAL-GLOBALS that are accessible from this ROOM. This could, for example, be a door that is accessible from two different ROOMs.

*  THINGS is an optional property.  This creates one or more simple “pseudo-objects”. Each object has three parts: a LIST of adjectives (FALSE if none), a LIST of nouns and the name of the action-routine to call when this object is accessed. In early Infocom games this property was called PSEUDO and had a slightly different syntax.

*  ACTION is defined as (ACTION routine-name). This is the OBJECTs action-routine. For OBJECTs action-routines there is no argument. SIZE  Size of OBJECT (for inventory handling).

*  SiZE is the size of OBJECT (for inventory handling).

*  VALUE is the value of OBJECT (for scoring purposes).

*  DESCFCN  is used to define a function to handle the OBJECTs description. It is called with an argument, ARG, that can be M-OBJDESC? or M-OBJDESC. If the routine returns FALSE during the M-OBJDESC? call, the OBJECT defaults to standard descriptions with FDESC and LDESC, otherwise the description is handled during the M-OBJDESC call.

*  CAPACITY is the capacity of the OBJECT if it is a container.

*  CONTFCN is a routine that is called on the container when OBJECTs inside the container are handled (used raretly).

> **Note:** See Learning ZIL, Steve E. Meretzky and ZIL Course, Marc S. Blank for more on properties, flagbits and how to write and design games.

---

## Object Properties

### PropAdjective
**Usage:** `ADJECTIVE`

A list of adjectives the parser accepts to identify a specific object.

---

### PropDesc
**Usage:** `DESC`

A short string used to name the object in game output.

---

### PropSynonym
**Usage:** `SYNONYM`

A list of nouns the parser accepts for this object.

---

## Flags
*A collection of boolean bits (flags) that define the state or behavior of an object.*

### BitOn
**Usage:** `ONBIT`

Flag indicating that a light-source object is currently providing light.

---

### BitTake
**Usage:** `TAKEBIT`

Flag indicating that an object can be picked up by the player.

---