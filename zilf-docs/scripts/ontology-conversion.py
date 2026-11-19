# Title: ZILF Ontology Conversion Python Script
# Author: Robert Gervais (kaoticgreen)
# Description: This script converts the ZILF ontology to documentation markdown files.
# Dependencies: rdflib
# Script usage: python ontology-conversion.py
# Questions: Please join the ZILF Community Discord server if there are questions about the docs.

from pathlib import Path
from rdflib import Graph, Namespace, SKOS

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
    """Helper to get a deterministically sorted list of literal values."""
    return sorted(str(v) for v in graph.objects(subject, predicate))


def format_zil_code(code_str):
    """Wraps ZIL code in a markdown block."""
    if not code_str:
        return ""
    return f"```zil\n{code_str}\n```"


def format_inline_usage(usage_str):
    """Formats single or multi-line usage strings safely for inline backticks."""
    lines = [line.strip() for line in usage_str.splitlines() if line.strip()]
    return " | ".join(f"`{line}`" for line in lines)


def format_blockquote(prefix, text):
    """Formats single or multi-line notes as a valid Markdown blockquote."""
    raw_lines = text.splitlines()
    if not raw_lines:
        return ""
    formatted = [f"> {prefix} {raw_lines[0]}"]
    for line in raw_lines[1:]:
        formatted.append(f"> {line}" if line.strip() else ">")
    return "\n".join(formatted)


def write_file(filename, content):
    """Writes content to the output directory."""
    out_path = OUTPUT_DIR / filename
    print(f"Writing ZILF: {out_path}")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)


def get_sorted_children(g, parent, exclude=None):
    """Returns sorted subjects with skos:broader pointing to parent, excluding sub-containers."""
    exclude_set = set(exclude) if exclude else set()
    subjects = [s for s in g.subjects(SKOS.broader, parent) if s not in exclude_set]
    subjects.sort(key=lambda s: s.split("/")[-1])
    return subjects


def append_concept_documentation(g, subj, lines):
    """Helper to append standard documentation fields to the line list."""
    name = subj.split("/")[-1]
    usage = get_literal(g, subj, SKOS.prefLabel)
    alt_usages = get_literals(g, subj, SKOS.altLabel)

    definition = get_literal(g, subj, SKOS.definition)
    note = get_literal(g, subj, SKOS.editorialNote)
    history = get_literal(g, subj, SKOS.historyNote)

    lines.append(f"\n### {name}")

    # Standard Usage
    if usage:
        lines.append(f"**Usage:** {format_inline_usage(usage)}\n")

    # Alternative Usage (supports multiple skos:altLabel triples)
    if alt_usages:
        formatted_alts = " | ".join(format_inline_usage(a) for a in alt_usages)
        lines.append(f"**Alternative Usage:** {formatted_alts}\n")

    if definition:
        lines.append(f"{definition}\n")
    if note:
        lines.append(f"{format_blockquote('**Note:**', note)}\n")
    if history:
        lines.append(f"**History:** {history}\n")
    lines.append("---")


def generate_index_md():
    """Writes the landing page (index.md) covering all top concepts in ZILF_Scheme."""
    content = """# ZILF Language Reference
**Scheme:** ZILF Reference Scheme

Welcome to the ZILF Reference Guide. Select a concept below to view detailed documentation.

| Concept | Description |
| :--- | :--- |
| **[Language Fundamentals](./language-fundamentals.md)** | Primitive/derived data types (`ATOM`, `FIX`, `LIST`, `TABLE`) and lexical/evaluation rules (`%`, `%%`, `OBLIST`s, segments). |
| **[Core Functions](./core-functions.md)** | Fundamental MDL built-in functions and ZIL library functions (`EVAL`, `ROUTINE`, `DEFSTRUCT`). |
| **[Z-Code Built-ins](./z-code-built-ins.md)** | Z-machine instructions used inside `ROUTINE` (`POP`, `TELL`, `DO`). |
| **[Object System](./object-system.md)** | Entities (`OBJECT`, `ROOM`), properties (`DESC`, `SYNONYM`), and state flags (`LIGHTBIT`, `OPENBIT`, `TAKEBIT`). |
| **[Parser System](./parser-system.md)** | Directives for vocabulary/syntax (`VOC`, `SYNTAX`, `SYNONYM`), search flags (`HAVE`, `TAKE`), and Appendix D internal parser tables. |
| **[Z-Machine OP-Codes](./z-machine-opcodes.md)** | Appendix A: Low-level Z-machine opcodes without direct ZIL equivalents (`CALL`, `ICALL`, `JUMP`). |
| **[Z-Machine Header Fields](./header-fields.md)** | Appendix B: Ordinary and extended Z-machine header `field-spec` symbols for `LOWCORE` and `LOWCORE-TABLE`. |
| **[Reserved Symbols](./reserved-symbols.md)** | Appendix C: Compiler-reserved constants, globals, locals, and flags (`REDEFINE`, `NEW-PARSER?`, `DO-FUNNY-RETURNS?`). |

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


def generate_language_fundamentals(g):
    """Generates language-fundamentals.md (DataTypes and LexicalAndEvaluationRules)."""
    lines = [
        "[← Back to Main Index](./index.md)",
        "",
        "# Language Fundamentals",
        "",
        get_literal(g, ZILF.LanguageFundamentals, SKOS.definition) or "",
        "",
        "---",
    ]

    # 1. Data Types
    data_types = get_sorted_children(g, ZILF.DataTypes)
    if data_types:
        lines.append("\n## Data Types")
        dt_def = get_literal(g, ZILF.DataTypes, SKOS.definition)
        if dt_def:
            lines.append(f"*{dt_def}*")
        for dt in data_types:
            append_concept_documentation(g, dt, lines)

    # 2. Lexical and Evaluation Rules
    lex_rules = get_sorted_children(g, ZILF.LexicalAndEvaluationRules)
    if lex_rules:
        lines.append("\n## Lexical and Evaluation Rules")
        lr_def = get_literal(g, ZILF.LexicalAndEvaluationRules, SKOS.definition)
        if lr_def:
            lines.append(f"*{lr_def}*")
        for lr in lex_rules:
            append_concept_documentation(g, lr, lines)

    write_file("language-fundamentals.md", "\n".join(lines))


def generate_core_functions(g):
    """Generates core-functions.md."""
    lines = ["[← Back to Main Index](./index.md)", "", "# Core Functions", "---"]
    for subj in get_sorted_children(g, ZILF.CoreFunctions):
        append_concept_documentation(g, subj, lines)

    write_file("core-functions.md", "\n".join(lines))


def generate_z_code_built_ins(g):
    """Generates z-code-built-ins.md for ROUTINE instructions."""
    lines = ["[← Back to Main Index](./index.md)", "", "# Z-Code Built-ins", "---"]
    for subj in get_sorted_children(g, ZILF.ZCodeBuiltIns):
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
        "Entities (`OBJECT`, `ROOM`), properties (`DESC`, `SYNONYM`), and state flags (`LIGHTBIT`, `OPENBIT`, `TAKEBIT`).",
        "",
        "---",
    ]

    # 1. Base Entities (OBJECT, ROOM, etc.)
    for ent in get_sorted_children(g, ZILF.ObjectSystem, exclude=[ZILF.ObjectProperties]):
        append_concept_documentation(g, ent, lines)

    # 2. Properties
    lines.append("\n## Object Properties")
    for p in get_sorted_children(g, ZILF.ObjectProperties, exclude=[ZILF.PropFlags]):
        append_concept_documentation(g, p, lines)

    # 3. Flags
    lines.append("\n## Flags")
    flags_def = get_literal(g, ZILF.PropFlags, SKOS.definition)
    if flags_def:
        lines.append(f"*{flags_def}*")
    for f in get_sorted_children(g, ZILF.PropFlags):
        append_concept_documentation(g, f, lines)

    write_file("object-system.md", "\n".join(lines))


def generate_parser_system(g):
    """Generates parser-system.md including SyntaxFlags and Appendix D ParserTables."""
    lines = ["[← Back to Main Index](./index.md)", "", "# Parser System", "---"]

    # 1. Parser Directives (ADD-WORD, BUZZ, DIRECTIONS, SYNONYM, SYNTAX, VOC, etc.)
    for c in get_sorted_children(g, ZILF.ParserSystem, exclude=[ZILF.SyntaxFlags, ZILF.ParserTables]):
        append_concept_documentation(g, c, lines)

    # 2. Syntax Search & Scope Flags (Classic + Version 6 New Parser)
    syntax_flags = get_sorted_children(g, ZILF.SyntaxFlags)
    if syntax_flags:
        lines.append("\n## Syntax Search & Scope Flags")
        sf_def = get_literal(g, ZILF.SyntaxFlags, SKOS.definition)
        if sf_def:
            lines.append(f"*{sf_def}*")
        for sf in syntax_flags:
            append_concept_documentation(g, sf, lines)

    # 3. Appendix D: Internal Parser Tables & New Parser
    parser_tables = get_sorted_children(g, ZILF.ParserTables)
    if parser_tables:
        lines.append("\n## Appendix D: Internal Parser Tables & New Parser")
        pt_def = get_literal(g, ZILF.ParserTables, SKOS.definition)
        if pt_def:
            lines.append(f"*{pt_def}*")
        for pt in parser_tables:
            append_concept_documentation(g, pt, lines)

    write_file("parser-system.md", "\n".join(lines))


def generate_z_machine_opcodes(g):
    """Generates z-machine-opcodes.md (Appendix A)."""
    lines = [
        "[← Back to Main Index](./index.md)",
        "",
        "# Appendix A: Other Z-Machine OP-Codes",
        "",
        get_literal(g, ZILF.ZMachineOpcodes, SKOS.definition) or "",
        "",
        "---",
    ]
    for op in get_sorted_children(g, ZILF.ZMachineOpcodes):
        append_concept_documentation(g, op, lines)

    write_file("z-machine-opcodes.md", "\n".join(lines))


def generate_header_fields(g):
    """Generates header-fields.md (Appendix B: Ordinary & Extended Header Fields)."""
    lines = [
        "[← Back to Main Index](./index.md)",
        "",
        "# Appendix B: Z-Machine Header Fields",
        "",
        get_literal(g, ZILF.HeaderFields, SKOS.definition) or "",
        "",
        "---",
    ]

    # 1. Ordinary Header Fields
    ordinary = get_sorted_children(g, ZILF.OrdinaryHeaderFields)
    if ordinary:
        lines.append("\n## Ordinary Header Fields")
        ord_def = get_literal(g, ZILF.OrdinaryHeaderFields, SKOS.definition)
        if ord_def:
            lines.append(f"*{ord_def}*")
        for field in ordinary:
            append_concept_documentation(g, field, lines)

    # 2. Extended Header Fields
    extended = get_sorted_children(g, ZILF.ExtendedHeaderFields)
    if extended:
        lines.append("\n## Extended Header Fields")
        ext_def = get_literal(g, ZILF.ExtendedHeaderFields, SKOS.definition)
        if ext_def:
            lines.append(f"*{ext_def}*")
        for field in extended:
            append_concept_documentation(g, field, lines)

    write_file("header-fields.md", "\n".join(lines))


def generate_reserved_symbols(g):
    """Generates reserved-symbols.md (Appendix C)."""
    lines = [
        "[← Back to Main Index](./index.md)",
        "",
        "# Appendix C: Reserved Constants, Globals & Locals",
        "",
        get_literal(g, ZILF.ReservedSymbols, SKOS.definition) or "",
        "",
        "---",
    ]
    for sym in get_sorted_children(g, ZILF.ReservedSymbols):
        append_concept_documentation(g, sym, lines)

    write_file("reserved-symbols.md", "\n".join(lines))


def generate_cookbook(g):
    """Generates cookbook.md by pulling all skos:example entries and grouping by category."""
    lines = ["[← Back to Main Index](./index.md)", "", "# ZILF Cookbook", "---"]

    # Collect Language Fundamentals subjects
    fundamentals_subjects = list(g.subjects(SKOS.broader, ZILF.DataTypes))
    fundamentals_subjects.extend(g.subjects(SKOS.broader, ZILF.LexicalAndEvaluationRules))

    # Collect Parser System subjects (including SyntaxFlags and ParserTables)
    parser_subjects = list(g.subjects(SKOS.broader, ZILF.ParserSystem))
    parser_subjects.extend(g.subjects(SKOS.broader, ZILF.SyntaxFlags))
    parser_subjects.extend(g.subjects(SKOS.broader, ZILF.ParserTables))

    # Collect Object System subjects (Entities, Properties, Flags)
    object_system_subjects = list(g.subjects(SKOS.broader, ZILF.ObjectSystem))
    object_system_subjects.extend(g.subjects(SKOS.broader, ZILF.ObjectProperties))
    object_system_subjects.extend(g.subjects(SKOS.broader, ZILF.PropFlags))

    # Collect Header Fields subjects
    header_subjects = list(g.subjects(SKOS.broader, ZILF.OrdinaryHeaderFields))
    header_subjects.extend(g.subjects(SKOS.broader, ZILF.ExtendedHeaderFields))

    categories = {
        "Language Fundamentals": fundamentals_subjects,
        "Core Functions": list(g.subjects(SKOS.broader, ZILF.CoreFunctions)),
        "Z-Code Built-ins": list(g.subjects(SKOS.broader, ZILF.ZCodeBuiltIns)),
        "Parser System": parser_subjects,
        "Object System": object_system_subjects,
        "Z-Machine OP-Codes": list(g.subjects(SKOS.broader, ZILF.ZMachineOpcodes)),
        "Z-Machine Header Fields": header_subjects,
        "Reserved Symbols": list(g.subjects(SKOS.broader, ZILF.ReservedSymbols)),
    }

    processed_subjects = set()

    for cat_name, subjects in categories.items():
        subjects_with_examples = [s for s in set(subjects) if (s, SKOS.example, None) in g]

        if subjects_with_examples:
            lines.append(f"\n## {cat_name}")
            subjects_with_examples.sort(key=lambda s: s.split("/")[-1])

            for subj in subjects_with_examples:
                processed_subjects.add(subj)
                name = subj.split("/")[-1]
                examples = get_literals(g, subj, SKOS.example)

                if examples:
                    lines.append(f"\n### {name}")
                    for ex in examples:
                        lines.append(format_zil_code(ex))
                    lines.append("")

    all_example_subjects = set(g.subjects(SKOS.example, None))
    uncategorized = list(all_example_subjects - processed_subjects)

    if uncategorized:
        lines.append("\n## Uncategorized Examples")
        uncategorized.sort(key=lambda s: s.split("/")[-1])
        for subj in uncategorized:
            name = subj.split("/")[-1]
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
    generate_language_fundamentals(g)
    generate_core_functions(g)
    generate_z_code_built_ins(g)
    generate_object_system(g)
    generate_parser_system(g)
    generate_z_machine_opcodes(g)
    generate_header_fields(g)
    generate_reserved_symbols(g)
    generate_cookbook(g)
    print("\nZILF documentation generation complete!")


if __name__ == "__main__":
    main()
