[← Back to Main Index](./index.md)

# Object System
**Parent Concept:** Object System

Entities (`OBJECT`), properties (`DESC`, `SYNONYM`), and state flags (`ONBIT`, `TAKEBIT`).

---

### OBJECT
The base entity definition.

---

## Object Properties

### ADJECTIVE
**Usage:** ADJECTIVE

A list of adjectives the parser accepts to identify a specific object.

### DESC
**Usage:** DESC

A short string used to name the object in game output.

### SYNONYM
**Usage:** SYNONYM

A list of nouns the parser accepts for this object.

---

## Flags
*A collection of boolean bits (flags) that define the state or behavior of an object.*

### ONBIT
**Usage:** ONBIT

Flag indicating that a light-source object is currently providing light.

### TAKEBIT
**Usage:** TAKEBIT

Flag indicating that an object can be picked up by the player.