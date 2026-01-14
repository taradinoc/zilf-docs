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