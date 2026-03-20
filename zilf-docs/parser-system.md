[← Back to Main Index](./index.md)

# Parser System
---

### ADJ-SYNONYM
**Usage:** `<ADJ-SYNONYM original synonyms ...>`

ZIL parser library function that creates one or more synonyms to the original adjective. ZILF treats ADJ-SYNONYM as an alias to SYNONYM.

> **Note:** Note that due to the way words, especially adjectives and nouns, are stored in the vocabulary synonyms for adjectives only work in version 3 (ZIP) games.

---

### BIT-SYNONYM
**Usage:** `<BIT-SYNONYM first synonyms ...>`

ZIL parser library function that creates synonyms to flag-bits.

---

### BUZZ
**Usage:** `<BUZZ atoms ...>`

ZIL parser library function that creates words in the vocabulary with the part-of-speech BUZZ.

> **Note:** These are words that can be ignored by the parser or have special handling in the parser.

---

### DIR-SYNONYM
**Usage:** `<DIR-SYNONYM original synonyms ...>`

ZIL parser library function that creates one or more synonyms to the original direction.

> **Note:** ZILF treats DIR-SYNONYM as an alias to SYNONYM.

---

### DIRECTIONS
**Usage:** `<DIRECTIONS atoms ...>`

ZIL parser library function that creates words in the vocabulary with the part-of-speech DIRECTION.

> **Note:** DIRECTIONS are often defined in the parser and the order is usually tightly tied to the parser. Be careful if you change these. You can use DIR-SYNONYM if you, for example, want to add FORE, AFT, PORT and STARBOARD.

---

### NEW-ADD-WORD
**Usage:** `<NEW-ADD-WORD atom-or-string [type] [value] [flags]>`

ZIL parser library function that is an alias to ADD-WORD.

---

### PREP-SYNONYM
**Usage:** `<PREP-SYNONYM original synonyms ...>`

ZIL parser library function that creates one or more synonyms to the original preposition.

> **Note:** ZILF treats PREP-SYNONYM as an alias to SYNONYM.

---

### SYNONYM
**Usage:** `<SYNONYM original synonyms ...>`

ZIL parser library function that creates one or more synonyms to the original verb, adjective, preposition or direction. Instead of  SYNONYM it is also possible to use VERB-SYNONYM, ADJ-SYNONYM, PREP-SYNONYM and DIR-SYNONYM for verbs, adjectives, prepositions and directions respectively, ZILF handles them all like aliases to SYNONYM.

> **Note:** Note that due to the way words, especially adjectives and nouns,  are stored in the vocabulary synonyms for adjectives only work in version 3 (ZIP) games.

---

### SYNTAX
**Usage:** `SYNTAX`

**Alternative Usage:** `<SYNTAX verb [prep1] [OBJECT] [(FIND flag-name)]
    [(search-flags ...)] [prep2] [OBJECT]
    [(FIND flag-name)] [(search-flags ...)]
        = action-routine-name [preaction-routine-name]>`

ZIL parser library function that  defines a verb-phrase and specifies which action-routine-name should be called when an input matches this verb-phrase. A SYNTAX must contain a verb and an action-routine-name. Optionally it can contain one direct noun-phrase, the first token OBJECT, and one indirect noun-phrase, the second token OBJECT. Each noun-phrase can also have a corresponding preposition, prep1 and prep2 respectively.

The noun-phrases can have FIND and search, search-flags, conditions defined. The token FIND means that the OBJECT must have the flag-name bit set. If there is only one OBJECT in the scope that meets the FIND condition the parser makes a GWIM (“Get what I mean”). For example if there is only one door in the room with the DOORBIT set an OPEN assumes that you mean that door.

One special case of FIND is when there is no indirect OBJECT but the SYNTAX ends with a preposition. In these cases a special bit, KLUDGEBIT (or ROOMBIT), is used so that the player can type sentences like “turn machine on” (<SYNTAX TURN OBJECT (FIND DEVICEBIT) ON OBJECT (FIND KLUDGEBIT) = V-TURN-ON>).

The search-flags HAVE, MANY and TAKE define the following rules for the OBJECT:

*  HAVE indicates that the OBJECT must be in the player’s inventory (or inside open containers in  the player’s inventory). If the OBJECT is not in the inventory the parser fails and prints something like “You don’t have the x,”.

*  MANY indicates that is possible to use multiple OBJECTs with this verb.

*  TAKE indicates that if the OBJECT is not in  the player’s inventory but takeble the parser attempts to take the OBJECT, an so called implicit take is performed, before  
continuing (the OBJECT is moved to the player’s inventory and the parser prints something like “[Taken.]”).

The search-flags CARRIED, HELD, IN-ROOM and ON-GROUND can be seen as hints to the parser where to first look for the OBJECT. These flags define the scope for the search. Note that these flags are only hints to the parser and if the OBJECT is not in the defined scope the parser continues the search in the other scopes before it fails. The default value for scope is that all flags are set. 

*  CARRIED means to search  for the OBJECT inside open containers in the player’s inventory.

*  HELD means to search for the OBJECT in the player’s inventory at top-level (not inside other containers).

*  IN-ROOM means to search for the OBJECT inside containers on the ground.

*  ON-GROUND means to search for the OBJECT on the ground at the top-level.

Finally after the token = (equal-sign) there is one or two ROUTINE-names specified, action-routine-name and preaction-routine-name (optional). By convention these handlers are usually named V-verb and PRE-verb, respectively.

The preaction-routine-name is fired before the OBJECTs action-routine and the 
action-routine-name is fired after the OBJECTs action-routine. The preaction is usually 
used to check the prerequisites for the verb, for example that you have a weapon before attacking something so you don’t have to check that in every attackable OBJECTs action-routine. The action-routine-name is usually used to handle response when the OBJECTs action-routine fails.

Each occurrence of an action-routine-name together with an optional preaction-routine-name must always have the same pattern (same action-routine-name can’t exist with different preaction-routine-names).

> **Note:** It is possible to replace the search-flags with the GVAL NEW-SFLAGS. This is used with the new parser in Arthur, Shogun and Zork Zero where the search-flags ALL, ROOM, HELD, CARRIED, IN-ROOM, ON-GROUND, EVERYWHERE, MOBY and ADJACENT are defined.

---

### VERB-SYNONYM
**Usage:** `<VERB-SYNONYM original synonyms ...>`

ZIL parser library function that creates one or more synonyms to the original verb.

> **Note:** ZILF treats VERB-SYNONYM as an alias to SYNONYM.

---