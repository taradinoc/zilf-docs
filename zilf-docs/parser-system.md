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

---

### VERB-SYNONYM
**Usage:** `<VERB-SYNONYM original synonyms ...>`

ZIL parser library function that creates one or more synonyms to the original verb.

> **Note:** ZILF treats VERB-SYNONYM as an alias to SYNONYM.

---