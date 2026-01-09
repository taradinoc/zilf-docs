# Title: ZILF Ontology Conversion Python Script
# Author: Robert Gervais (kaoticgreen)
# Description: This script converts the ZILF ontology to documentation markdown files.
# Dependencies: rdflib
# Script usage: python ontology-conversion.py
# Questions: Please join the ZILF Community Discord server if there are questions about the docs.

import os
from pathlib import Path
from rdflib import Graph, Namespace, RDF, SKOS, Literal

# --- Configuration ---
SCRIPT_DIR = Path(__file__).parent
ONTOLOGY_FILE = SCRIPT_DIR.parent.parent / "zilf-ontology" / "ZILF_Ontology.ttl"
OUTPUT_DIR = SCRIPT_DIR.parent

# Define Namespace
ZILF = Namespace("http://example.org/zilf/")

def load_ontology():
    """Parses the Turtle file."""
    print(f"Loading ontology from: {ONTOLOGY_FILE}")
    g = Graph()
    g.parse(ONTOLOGY_FILE, format="ttl")
    return g

def get_literal(graph, subject, predicate):
    """Helper to get a single literal value as string."""
    val = graph.value(subject, predicate)
    return str(val) if val else None

def get_literals(graph, subject, predicate):
    """Helper to get a list of literal values."""
    return [str(v) for v in graph.objects(subject, predicate)]

def format_zil_code(code_str):
    """Wraps ZIL code in a markdown block."""
    if not code_str:
        return ""
    return f"```zil\n{code_str}\n```"

def write_file(filename, content):
    """Writes content to the output directory."""
    out_path = OUTPUT_DIR / filename
    print(f"Writing ZILF: {out_path}")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

def append_concept_documentation(g, subj, lines):
    """Helper to append standard documentation fields to the line list."""
    name = subj.split('/')[-1]
    usage = get_literal(g, subj, SKOS.prefLabel)
    definition = get_literal(g, subj, SKOS.definition)
    note = get_literal(g, subj, SKOS.editorialNote)
    history = get_literal(g, subj, SKOS.historyNote)
    
    lines.append(f"\n### {name}")
    if usage: lines.append(f"**Usage:** `{usage}`\n")
    if definition: lines.append(f"{definition}\n")
    if note: lines.append(f"> **Note:** {note}\n")
    if history: lines.append(f"**History:** {history}\n")
    lines.append("---")

def generate_index_md():
    """Writes the approved landing page (index.md)."""
    content = """# ZILF Language Reference
**Scheme:** ZILF Reference Scheme

Welcome to the ZILF Reference Guide. Select a concept below to view detailed documentation.

| Concept | Description |
| :--- | :--- |
| **[Core Functions](./core-functions.md)** | Fundamental MDL built-in functions and ZIL library functions (`EVAL`, `ROUTINE`). |
| **[Z-Code Built-ins](./z-code-built-ins.md)** | Z-machine instructions used inside ROUTINE (`POP`). |
| **[Object System](./object-system.md)** | Entities (`OBJECT`), properties (`DESC`), and state flags (`ONBIT`, `TAKEBIT`). |
| **[Parser System](./parser-system.md)** | Directives for syntax (`SYNTAX`) and synonym definitions (`SYNONYM`). |

---

## Coding Cookbook
For practical implementation patterns, consult the cookbook:
* **[View the Cookbook](./cookbook.md)** – A collection of code examples extracted directly from the ZILF ontology.

Copyright (C) 2026 ZILF Contributors. Permission is granted to copy, distribute and/or modify this document under 
the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software 
Foundation; with no Invariant Sections, no Front- Cover Texts, and no Back-Cover Texts. A copy of the license is 
included in the section entitled "GNU Free Documentation License".
"""
    write_file("index.md", content)

def generate_core_functions(g):
    """Generates core-functions.md."""
    lines = ["[← Back to Main Index](./index.md)", "", "# Core Functions", "---"]
    subjects = list(g.subjects(SKOS.broader, ZILF.CoreFunctions))
    subjects.sort(key=lambda s: s.split('/')[-1])

    for subj in subjects:
        append_concept_documentation(g, subj, lines)
        
    write_file("core-functions.md", "\n".join(lines))

def generate_z_code_built_ins(g):
    """Generates z-code-built-ins.md for ROUTINE instructions like POP."""
    lines = ["[← Back to Main Index](./index.md)", "", "# Z-Code Built-ins", "---"]
    subjects = list(g.subjects(SKOS.broader, ZILF.ZCodeBuiltIns))
    subjects.sort(key=lambda s: s.split('/')[-1])

    for subj in subjects:
        append_concept_documentation(g, subj, lines)
        
    write_file("z-code-built-ins.md", "\n".join(lines))

def generate_object_system(g):
    """Generates object-system.md."""
    lines = [
        "[← Back to Main Index](./index.md)",
        "",
        "# Object System",
        "**Parent Concept:** Object System",
        "",
        "Entities (`OBJECT`), properties (`DESC`, `SYNONYM`), and state flags (`ONBIT`, `TAKEBIT`).",
        "",
        "---"
    ]

    # 1. Base Object
    if (ZILF.OBJECT, RDF.type, None) in g:
         lines.append("\n### OBJECT")
         lines.append("The base entity definition.\n\n---")

    # 2. Properties
    lines.append("\n## Object Properties")
    props = list(g.subjects(SKOS.broader, ZILF.ObjectProperties))
    if ZILF.PropFlags in props: props.remove(ZILF.PropFlags)
    props.sort(key=lambda s: s.split('/')[-1])

    for p in props:
        append_concept_documentation(g, p, lines)

    # 3. Flags
    lines.append("\n## Flags")
    lines.append("*A collection of boolean bits (flags) that define the state or behavior of an object.*")
    
    flags = list(g.subjects(SKOS.broader, ZILF.PropFlags))
    flags.sort(key=lambda s: s.split('/')[-1])

    for f in flags:
        append_concept_documentation(g, f, lines)

    write_file("object-system.md", "\n".join(lines))

def generate_parser_system(g):
    """Generates parser-system.md."""
    lines = ["[← Back to Main Index](./index.md)", "", "# Parser System", "---"]
    concepts = list(g.subjects(SKOS.broader, ZILF.ParserSystem))
    concepts.sort(key=lambda s: s.split('/')[-1])

    for c in concepts:
        append_concept_documentation(g, c, lines)
        
    write_file("parser-system.md", "\n".join(lines))

def generate_cookbook(g):
    """Generates cookbook.md by pulling all skos:example entries."""
    lines = ["[← Back to Main Index](./index.md)", "", "# ZILF Cookbook", "---"]
    subjects_with_examples = sorted(list(set(g.subjects(SKOS.example, None))), key=lambda s: s.split('/')[-1])

    for subj in subjects_with_examples:
        name = subj.split('/')[-1]
        examples = get_literals(g, subj, SKOS.example)
        if examples:
            lines.append(f"\n### {name}")
            for ex in examples:
                lines.append(format_zil_code(ex))
            lines.append("")
            
    write_file("cookbook.md", "\n".join(lines))

def main():
    if not ONTOLOGY_FILE.exists():
        print(f"Error: ZILF ontology file not found at {ONTOLOGY_FILE}")
        return

    g = load_ontology()
    generate_index_md()
    generate_core_functions(g)
    generate_z_code_built_ins(g)
    generate_object_system(g)
    generate_parser_system(g)
    generate_cookbook(g)
    print("\nZILF documentation generation complete!")

if __name__ == "__main__":
    main()