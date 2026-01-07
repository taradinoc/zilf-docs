# Title: ZILF Ontology Conversion Python Script
# Author: Robert Gervais (kaoticgreen)
# Description: This script is used to convert the ZILF ontology to documentation markdown files.
# Dependencies: rdflib
# Required environment setup: pip install rdflib
# Script usage: python ontology-conversion.py
# Questions: Please join the ZILF Discord community if there are questions about the docs.

import os
from pathlib import Path
from rdflib import Graph, Namespace, RDF, SKOS, Literal

# --- Configuration ---
# Define paths relative to this script: ~/zilf-docs/scripts/ontology-conversion.py
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

def generate_index_md():
    """Writes the approved landing page (index.md)."""
    # TODO: Link to outside docs as this matures.
    content = """# ZILF Language Reference
**Scheme:** ZILF Reference Scheme

Welcome to the ZILF Reference Guide. Select a concept below to view detailed documentation.

| Concept | Description |
| :--- | :--- |
| **[Core Functions](./core-functions.md)** | Fundamental MDL built-in functions and ZIL library functions (`EVAL`, `ROUTINE`, `PRINT`). |
| **[Object System](./object-system.md)** | Entities (`OBJECT`), properties (`DESC`, `SYNONYM`), and state flags (`ONBIT`, `TAKEBIT`). |
| **[Parser System](./parser-system.md)** | Directives for syntax (`SYNTAX`) and verb definitions (`VERB`). |

---

## Coding Cookbook
For practical implementation patterns, consult the cookbook:
* **[View the Cookbook](./cookbook.md)** – A collection of code examples (`ROUTINE`, `PUTREST`, `EVAL`) extracted directly from the ZILF ontology.

Copyright (C) 2020-2023 Henrik Åsman 
Copying and distribution of this file, with or without modification, are permitted in any medium 
without royalty provided the copyright notice and this notice are preserved. This file is offered as-is, 
without any warranty.
"""
    write_file("index.md", content)

def generate_core_functions(g):
    """Generates core-functions.md."""
    lines = [
        "[← Back to Main Index](./index.md)",
        "",
        "# Core Functions",
        "**Parent Concept:** Core Functions",
        "",
        "Fundamental MDL built-in functions and ZIL library functions.",
        "",
        "---"
    ]
    
    subjects = list(g.subjects(SKOS.broader, ZILF.CoreFunctions))
    subjects.sort(key=lambda s: s.split('/')[-1])

    for subj in subjects:
        name = subj.split('/')[-1]
        usage = get_literal(g, subj, SKOS.prefLabel)
        definition = get_literal(g, subj, SKOS.definition)
        note = get_literal(g, subj, SKOS.editorialNote)
        
        lines.append(f"\n### {name}")
        if usage:
            lines.append(f"**Usage:** `{usage}`\n")
        
        if definition:
            lines.append(f"{definition}\n")
            
        if note:
            lines.append(f"> **Note:** {note}\n")
            
        lines.append("---")
        
    write_file("core-functions.md", "\n".join(lines))

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
         lines.append("The base entity definition.")
         lines.append("\n---")

    # 2. Properties
    lines.append("\n## Object Properties")
    props = list(g.subjects(SKOS.broader, ZILF.ObjectProperties))
    if ZILF.PropFlags in props:
        props.remove(ZILF.PropFlags)
    props.sort(key=lambda s: s.split('/')[-1])

    for p in props:
        name = p.split('/')[-1].replace("Prop", "").upper()
        label = get_literal(g, p, SKOS.prefLabel) or name
        definition = get_literal(g, p, SKOS.definition)
        
        lines.append(f"\n### {label}")
        lines.append(f"**Usage:** {label}\n")
        if definition:
            lines.append(f"{definition}")

    # 3. Flags
    lines.append("\n---")
    lines.append("\n## Flags")
    lines.append("*A collection of boolean bits (flags) that define the state or behavior of an object.*")
    
    flags = list(g.subjects(SKOS.broader, ZILF.PropFlags))
    flags.sort(key=lambda s: s.split('/')[-1])

    for f in flags:
        label = get_literal(g, f, SKOS.prefLabel)
        definition = get_literal(g, f, SKOS.definition)
        
        lines.append(f"\n### {label}")
        lines.append(f"**Usage:** {label}\n")
        if definition:
            lines.append(f"{definition}")

    write_file("object-system.md", "\n".join(lines))

def generate_parser_system(g):
    """Generates parser-system.md."""
    lines = [
        "[← Back to Main Index](./index.md)",
        "",
        "# Parser System",
        "**Parent Concept:** Parser System",
        "",
        "Directives for syntax (`SYNTAX`) and verb definitions (`VERB`).",
        "",
        "---"
    ]
    
    concepts = list(g.subjects(SKOS.broader, ZILF.ParserSystem))
    concepts.sort(key=lambda s: s.split('/')[-1])

    for c in concepts:
        label = get_literal(g, c, SKOS.prefLabel)
        definition = get_literal(g, c, SKOS.definition)
        
        lines.append(f"\n### {label}")
        lines.append(f"**Usage:** {label}\n")
        if definition:
            lines.append(f"{definition}")
        else:
            lines.append("*(No definition provided in ontology)*")
        lines.append("\n---")

    write_file("parser-system.md", "\n".join(lines))

def generate_cookbook(g):
    """Generates cookbook.md."""
    lines = [
        "[← Back to Main Index](./index.md)",
        "",
        "# ZILF Cookbook",
        "**Reference:** `skos:example` data from ZILF Reference Scheme",
        "",
        "A collection of code examples extracted directly from the ZILF ontology.",
        "",
        "---"
    ]

    subjects_with_examples = []
    for s, o in g.subject_objects(SKOS.example):
        subjects_with_examples.append(s)
    
    subjects_with_examples = sorted(list(set(subjects_with_examples)), key=lambda s: s.split('/')[-1])

    for subj in subjects_with_examples:
        name = subj.split('/')[-1]
        examples = get_literals(g, subj, SKOS.example)
        
        if examples:
            lines.append(f"\n### {name}")
            for ex in examples:
                lines.append(format_zil_code(ex))
            lines.append("")

    write_file("cookbook.md", "\n".join(lines))

def write_file(filename, content):
    """Writes content to the output directory."""
    out_path = OUTPUT_DIR / filename
    print(f"Writing ZILF: {out_path}")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    if not ONTOLOGY_FILE.exists():
        print(f"Error: ZILF ontology file not found at {ONTOLOGY_FILE}")
        return

    g = load_ontology()
    
    generate_index_md()
    generate_core_functions(g)
    generate_object_system(g)
    generate_parser_system(g)
    generate_cookbook(g)
    print("\nZILF documentation generation complete!")

if __name__ == "__main__":
    main()