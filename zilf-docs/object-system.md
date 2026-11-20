[← Back to Main Index](./index.md)

# Object System
**Parent Concept:** Object System

Entities (`OBJECT`, `ROOM`), properties (`DESC`, `SYNONYM`), state flags (`LIGHTBIT`, `OPENBIT`, `TAKEBIT`), special locations, and action arguments.

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

### ROOM
**Usage:** `<ROOM name (property value ...) ...>`

ZIL library function that creates a room-object with the internal objectname, name. After the name follows LISTs of properties for the ROOM and the values for each property. Which properties that define up a ROOM is determined by the parser and it’s possible to add new properties with PROPDEF as long as the parser is modified to support the new property. Usually the below properties are understood by the parser and the properties IN (or LOC), DESC and FLAGS are required, the others are optional.

*  IN or LOC is a required property. The value is always ROOMS for ROOM-objects.

*  DESC is a required property. The short description text of the ROOM. This is the text that is, for example, printed in the statusbar.

*  FLAGS is a required property. This lists all the flagbits that are set on this ROOM.

*  LDESC is an optional property. The long description of the ROOM. This is the text that is printed, for example, the first time the player visits the ROOM.

*  (dir ...) is an optional property.  List a direction, dir and where it leads. There is 5  
   different types of EXITS:

    *  UEXIT (“unconditional exit”). The syntax is (dir TO room-name). If  the player moves in this direction he is moved unconditionally to room-name.

    *  NEXIT (“non-exit”). The syntax is (dir "text-why-not"). The text-why-not is printed when the player tries to move in this direction. Use this only if you want a different text than the standard message, typically something like "You can’t move in that direction!".

    *  CEXIT (“conditional exit”). The syntax is (dir TO room-name IF gval [ELSE "text-why-not"]). This moves the player if the global value, gval, is TRUE. The ELSE-part is optional and the standard message is printed if it is not supplied.

    *  DEXIT (“door-exit”). The syntax is (dir TO room-name IF door-name IS OPEN). This is a special case of CEXIT that moves the player to room-name if the door-name has the OPENBIT set.

    *  FEXIT (“function-exit”). The syntax is (dir PER routine-name). This moves the player to the ROOM returned by the ROUTINE, routine-name. If the routine returns FALSE it is presumed that the routine has printed an appropriate message.

*  GLOBAL is an optional property. This is a LIST of all the OBJECTs that is IN the LOCAL-GLOBALS that are accessible from this ROOM. This could, for example, be a door that is accessible from two different ROOMs.

*  THINGS is an optional property. This creates one or more simple “pseudo-objects”. Each object has three parts: a LIST of adjectives (FALSE if none), a LIST of nouns and the name of the action-routine to call when this object is accessed. In early Infocom games this property was called PSEUDO and had a slightly different syntax.

*  ACTION is an optional property. The syntax is (ACTION routine-name). This ROUTINE takes one argument, by convention call RARG (“room-argument”), and is called more than once during a turn with different values to RARG. 

    *  M-BEG, the routine-name is called with this value to RARG before any OBJECTs or verb action-routines.  

    *  M-END, the routine-name is called with this value to RARG after any OBJECTs or verb action-routines.

    *  M-LOOK, the routine-name is called with this value to RARG when the player LOOKs.

    *  M-ENTER, the routine-name is called with this value to RARG when the player enters the ROOM (before any room description).

> **Note:** Note that ROOMs can just as easily be created with OBJECT as long as they are (IN ROOMS).
>
> See Learning ZIL, Steve E. Meretzky and ZIL Course, Marc S. Blank for more on properties, flagbits and how to write and design games.

---

## Object Properties

### PropAction
**Usage:** `ACTION`

Action routine associated with an OBJECT or ROOM.

---

### PropAdjective
**Usage:** `ADJECTIVE`

A list of adjectives the parser accepts to identify a specific object.

---

### PropCapacity
**Usage:** `CAPACITY`

Container capacity of an OBJECT.

---

### PropCexit
**Usage:** `CEXIT`

Conditional room exit: (dir TO room-name IF gval [ELSE 'text-why-not']).

---

### PropContfcn
**Usage:** `CONTFCN`

Routine called on a container when objects inside it are handled.

---

### PropDesc
**Usage:** `DESC`

A short string used to name the object in game output.

---

### PropDescfcn
**Usage:** `DESCFCN`

Routine that handles custom description printing for an OBJECT.

---

### PropDexit
**Usage:** `DEXIT`

Door room exit: (dir TO room-name IF door-name IS OPEN).

---

### PropFdesc
**Usage:** `FDESC`

First description text used to describe an OBJECT until it is picked up.

---

### PropFexit
**Usage:** `FEXIT`

Function room exit: (dir PER routine-name).

---

### PropGlobal
**Usage:** `GLOBAL`

List of LOCAL-GLOBALS objects accessible from a ROOM.

---

### PropIn
**Usage:** `IN`

**Alternative Usage:** `LOC`

Initial location (parent object or room) of an OBJECT or ROOM.

---

### PropLdesc
**Usage:** `LDESC`

Long description text of an OBJECT on the ground or of a ROOM.

---

### PropNexit
**Usage:** `NEXIT`

Non-exit message in a room: (dir 'text-why-not').

---

### PropSize
**Usage:** `SIZE`

Size/weight of an OBJECT for inventory handling.

---

### PropSynonym
**Usage:** `SYNONYM`

A list of nouns the parser accepts for this object.

---

### PropThings
**Usage:** `THINGS`

**Alternative Usage:** `PSEUDO`

Defines simple pseudo-objects (adjectives, nouns, action-routine) in a ROOM.

---

### PropUexit
**Usage:** `UEXIT`

Unconditional room exit: (dir TO room-name).

---

### PropValue
**Usage:** `VALUE`

Scoring value of an OBJECT.

---

## Flags
*A collection of boolean bits (flags) that define the state or behavior of an object.*

### BitCont
**Usage:** `CONTBIT`

Object flag indicating that an object is a container (commonly used with FIND CONTBIT in SYNTAX).

---

### BitDevice
**Usage:** `DEVICEBIT`

Object flag indicating that an object is a switchable device (commonly used with FIND DEVICEBIT in SYNTAX).

---

### BitDoor
**Usage:** `DOORBIT`

Object flag indicating that an object is a door (commonly used with FIND DOORBIT in SYNTAX).

---

### BitLight
**Usage:** `LIGHTBIT`

Object or room flag indicating that a room is lit or an object can provide light.

---

### BitNdungeon
**Usage:** `NDUNGEONBIT`

Room flag shown in ZILF Reference Guide room examples (indicating a non-dungeon room).

---

### BitOn
**Usage:** `ONBIT`

Flag indicating that a light-source object is currently providing light.

> **Note:** Traditional ZIL/zillib light-state flag; not explicitly listed in the ZILF Reference Guide (which uses LIGHTBIT).

---

### BitOpen
**Usage:** `OPENBIT`

Object flag indicating that a container or door is currently open.

---

### BitPerson
**Usage:** `PERSONBIT`

Object flag indicating that an object is a person/NPC (commonly used with FIND PERSONBIT in SYNTAX).

---

### BitRoom
**Usage:** `ROOMBIT`

Special flag sometimes used in place of KLUDGEBIT when a SYNTAX line ends with a preposition.

---

### BitSurface
**Usage:** `SURFACEBIT`

Object flag indicating that an object is a supporter/surface (commonly used with FIND SURFACEBIT in SYNTAX).

---

### BitTake
**Usage:** `TAKEBIT`

Flag indicating that an object can be picked up by the player.

---

## Special Object Locations
*Special parent container objects used in (IN ...) or (LOC ...) clauses to organize rooms and globally or conditionally in-scope objects.*

### LocGenericObjects
**Usage:** `GENERIC-OBJECTS`

Special parent location for abstract or conceptual objects rather than physical items (for example, the murder or the new will in Infocom's Deadline).

---

### LocGlobalObjects
**Usage:** `GLOBAL-OBJECTS`

Special parent location for objects that the player can refer to from anywhere in the game.

---

### LocLocalGlobals
**Usage:** `LOCAL-GLOBALS`

Special parent location for objects (such as doors or scenery shared across rooms) that are in scope only in ROOMs listing them in their (GLOBAL ...) property. Recognized by ORDER-OBJECTS? for ROOMS-AND-LGS-FIRST.

---

### LocROOMS
**Usage:** `ROOMS`

Special parent container object holding all ROOM objects via (IN ROOMS) or (LOC ROOMS). Also recognized by ORDER-OBJECTS? to identify rooms.

---

## Room & Description Action Arguments
*Message constants passed as arguments to ROOM ACTION routines (RARG) and OBJECT DESCFCN routines.*

### ArgMBEG
**Usage:** `M-BEG`

Room ACTION argument (RARG) passed before any object or verb action routines execute during a turn.

---

### ArgMEND
**Usage:** `M-END`

Room ACTION argument (RARG) passed after object and verb action routines complete during a turn.

---

### ArgMENTER
**Usage:** `M-ENTER`

Room ACTION argument (RARG) passed when the player enters a ROOM, before its room description is printed.

---

### ArgMLOOK
**Usage:** `M-LOOK`

Room ACTION argument (RARG) passed when the player executes LOOK to print a custom room description.

---

### ArgMOBJDESC
**Usage:** `M-OBJDESC`

DESCFCN routine argument instructing the routine to print the object's custom description.

---

### ArgMOBJDESCQ
**Usage:** `M-OBJDESC?`

DESCFCN routine argument querying whether the object uses a custom description; returning FALSE falls back to standard FDESC/LDESC output.

---