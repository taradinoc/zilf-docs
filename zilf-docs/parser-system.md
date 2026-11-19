[← Back to Main Index](./index.md)

# Parser System
---

### ADD-WORD
**Usage:** `<ADD-WORD atom-or-string [part-of-speech] [value] [flags]>`

ZIL parser library function (used with NEW-PARSER? T) that adds a word to the vocabulary with optional part-of-speech, value, and flags.

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

**Alternative Usage:** `<SYNTAX verb [prep1] [OBJECT] [(FIND flag-name)]` | `[(search-flags ...)] [prep2] [OBJECT]` | `[(FIND flag-name)] [(search-flags ...)]` | `= action-routine-name [preaction-routine-name]>`

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

### VOC
**Usage:** `<VOC string [part-of-speech]>`

ZIL parser library function that  inserts the string in the game vocabulary (dictionary). Normally there is no need to define the vocabulary with VOC, the vocabulary is automatically updated with words when you define ROOMs, OBJECTs, SYNTAX, etc.

What follows below is a description of the vocabulary when you use the standard parser library. The vocabulary description for the new parser (<SETG NEW-PARSER? T>) is in ADD-WORD.

The part-of-speech can be one of the following:

part-of-speech, Value, Description
<>, 0, None
BUZZ, 4, Buzz-word
PREP, 8, Preposition
DIR, 16, Direction
ADJ or ADJECTIVE, 32, Adjective
VERB, 64, Verb
NOUN or OBJECT, 128, Noun

The vocabulary then occupies 7 or 9 bytes, depending on version, per entry distributed as follows.

Version 3
Bytes 0-3, Word up to 6 Z-characters (5 bit)
Byte 4, PoS
Byte 5, Value
Byte 6, V2

Version 4-
Bytes 0-5, Word up to 9 Z-characters (5 bit)
Byte 6, PoS
Byte 7, V1
Byte 8, V2

For PoS, Byte 6 (or byte 4) contains the part-of-speech value (as above) plus if  the word is defined as a first part-of-speech in the first 2 bytes.

- 0, None
- 1, Verb first
- 2, Adjective first
- 3, Direction first

For V1, Byte 7 (or byte 5) contains the words value (id). Each part-of-speech can have 255 (65535 for NOUNs) unique words (synonyms have the same value as parent).

For V2, Byte 8 is used for NOUNs (V1 & V2 gives 2 bytes, 1-65535 OBJECTs).

The different part-of-speech and first definitions have all global values defined as:

- P1?OBJECT    0 
- P1?VERB    1 
- P1?ADJECTIVE   2 
- P1?DIRECTION   3 
- PS?BUZZ-WORD   4 
- PS?PREPOSITION   8 
- PS?DIRECTION  16 
- PS?ADJECTIVE  32 
- PS?VERB   64 
- PS?OBJECT  128

---

## Syntax Search & Scope Flags
*Search scope and behavior flags used in SYNTAX definitions.*

### FlagADJACENT
**Usage:** `ADJACENT`

Version 6 new-parser SYNTAX search flag (value 192) searching adjacent rooms/locations.

---

### FlagALL
**Usage:** `ALL`

Version 6 new-parser SYNTAX search flag (value 15 = ROOM + CARRIED) searching both the room and inventory.

---

### FlagCARRIED
**Usage:** `CARRIED`

SYNTAX scope flag to search inside open containers in the player's inventory.

---

### FlagEVERYWHERE
**Usage:** `EVERYWHERE`

Version 6 new-parser SYNTAX search flag (value 128) allowing an object to be matched anywhere in the game.

---

### FlagHAVE
**Usage:** `HAVE`

SYNTAX search flag requiring the object to be in the player's inventory.

---

### FlagHELD
**Usage:** `HELD`

SYNTAX scope flag to search in the player's top-level inventory.

---

### FlagINROOM
**Usage:** `IN-ROOM`

SYNTAX scope flag to search inside containers on the ground.

---

### FlagKLUDGEBIT
**Usage:** `KLUDGEBIT`

Special FIND bit used when a SYNTAX line ends with a preposition and has no indirect object.

---

### FlagMANY
**Usage:** `MANY`

SYNTAX search flag allowing multiple objects with the verb.

---

### FlagMOBY
**Usage:** `MOBY`

Version 6 new-parser SYNTAX search flag (value 128, synonym for EVERYWHERE) matching objects regardless of location.

---

### FlagNEWSFLAGS
**Usage:** `NEW-SFLAGS`

GVAL table used to define custom search flags in Version 6 new parser games.

---

### FlagOFFGROUND
**Usage:** `OFF-GROUND`

Version 6 new-parser SYNTAX search bit (value 2, implicit component of ROOM/IN-ROOM; not explicitly defined in NEW-SFLAGS).

---

### FlagONGROUND
**Usage:** `ON-GROUND`

SYNTAX scope flag to search on the ground at top-level.

---

### FlagPOCKETS
**Usage:** `POCKETS`

Version 6 new-parser SYNTAX search bit (value 8, implicit component of CARRIED; not explicitly defined in NEW-SFLAGS).

---

### FlagROOM
**Usage:** `ROOM`

Version 6 new-parser SYNTAX search flag (value 3 = ON-GROUND + OFF-GROUND) searching the current room.

---

### FlagTAKE
**Usage:** `TAKE`

SYNTAX search flag instructing the parser to attempt an implicit take if the object is not held.

---

## Appendix D: Internal Parser Tables & New Parser
*Internal Z-machine dictionary, verb, syntax, action, preaction, and preposition table layouts, compiler vocabulary flags, and the Version 6 new parser architecture.*

### FlagOneBytePartsOfSpeech
**Usage:** `ONE-BYTE-PARTS-OF-SPEECH`

Compilation flag in the new parser controlling whether CLASSIFICATION-NUMBER occupies 1 byte (9-byte entry, e.g. Zork Zero) or 2 bytes (10-byte entry, e.g. Shogun/Arthur).

---

### FlagWordFlagsInTable
**Usage:** `WORD-FLAGS-IN-TABLE`

Compilation flag (default true in new parser) storing word flags in WORD-FLAG-TABLE instead of inline in each VWORD entry.

---

### FnTERMINALS
**Usage:** `TERMINALS`

Game-defined function in the new parser that assigns part-of-speech CLASSIFICATION-NUMBER values and ordering (packing IDs that exceed 1 or 2 bytes with the high bit set).

---

### NewParserArchitecture
**Usage:** `Version 6 New Parser (NEW-PARSER?)`

Infocom Version 6 parser format (used in Arthur, Shogun, Zork Zero, Abyss, Milliways) replacing standard vocabulary/syntax tables with VWORD, VERB-DATA, WORD-FLAG-TABLE, and NEW-SFLAGS.

---

### StructVWORD
**Usage:** `VWORD`

DEFSTRUCT required by the new parser describing vocabulary entries (LEXICAL-WORD, SEMANTIC-STUFF, optional FLAGS, CLASSIFICATION-NUMBER).

---

### StructVerbData
**Usage:** `VERB-DATA`

DEFSTRUCT required by the new parser describing 8-byte verb dispatch entries (0-object action, preposition, 1-object syntax table, 2-object syntax table).

---

### TableActions
**Usage:** `Actions Table`

Pointer table accessible via ACTIONS holding packed addresses of verb action routines indexed by ACTION.

---

### TablePreactions
**Usage:** `Preactions Table`

Pointer table accessible via PREACTIONS holding packed addresses of verb preaction routines indexed by ACTION.

---

### TablePrepositions
**Usage:** `Prepositions Table`

Lookup table accessible via PREPOSITIONS mapping vocabulary addresses to preposition numbers (4 bytes per entry, or 3 bytes when COMPACT-VOCABULARY? is set).

---

### TableSyntax
**Usage:** `Syntax Table`

Table of verb syntax lines (8 bytes per line by default: NOBJ, PREP1, PREP2, FIND1, FIND2, OPTS1, OPTS2, ACTION; or 2/4/7 bytes when COMPACT-SYNTAXES? is set). Each verb defines an ST?<VERB> constant.

---

### TableVerbs
**Usage:** `Verbs Table`

Pointer table accessible via VERBS mapping verb numbers (starting at 255 downwards) to the start of each verb's syntax lines.

---

### TableVocabulary
**Usage:** `Vocabulary Table`

Dictionary table located at header VOCAB: break characters, entry count, and 7-byte (V1-3) or 9-byte (V4+) entries containing Z-characters plus PoS, V1, and V2 bytes. Each word defines a W?<WORD> constant.

---

### TableWordFlagTable
**Usage:** `WORD-FLAG-TABLE`

GVAL table created when WORD-FLAGS-IN-TABLE is true, storing pairs of vocabulary word pointers and word flags (FIRST-PERSON, PLURAL-FLAG, SECOND-PERSON, THIRD-PERSON, PRESENT-TENSE, PAST-TENSE, FUTURE-TENSE, POSSESSIVE, THING-PNF, DONT-ORPHAN, DEFAULT-OBJECT).

---

### VarCompactSyntaxes
**Usage:** `COMPACT-SYNTAXES?`

Global flag enabling variable-length compact syntax table entries (2, 4, or 7 bytes depending on NOBJ).

---

### VarCompactVocabulary
**Usage:** `COMPACT-VOCABULARY?`

Global flag that removes extra byte V2 from vocabulary entries (shrinking preposition table entries to 3 bytes) and frees nouns, buzzwords, and prepositions from the part-of-speech limit.

---

### VarNewVoc
**Usage:** `NEW-VOC?`

Global flag that frees nouns from the standard 2-part-of-speech limit so a word can simultaneously be an adjective, noun, and verb.

---