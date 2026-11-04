---
name: structure-skills
version: "1.0.0"
description: >-
  Evidence-first RDKit workflow for chemically correct, publication-quality
  2D molecular structure comparisons, aligned core/scaffold highlighting,
  substituent mapping, and structure–activity relationship figures.
triggers:
  - draw molecular structures
  - highlight shared scaffold
  - compare chemical structures
  - make RDKit publication figures
  - create chemical structure/SAR panels
  - improve molecular depiction quality
language: English for technical instructions; follow the user's language in discussion
---

# Structure Skills — Chemically Accurate, Publication-Quality RDKit Figures

## 1. Mission

Produce scientific molecular drawings that communicate **real structural relationships**, not visually appealing but chemically unreliable graphics. Use original chemical structures and a deliberately defined scaffold, verify every highlighted bond, align molecules consistently, and export clean vector figures suited to medicinal chemistry manuscripts.

**Non-negotiable:** RDKit generates the chemical structures. Do not use generative image tools to redraw molecular connectivity, recreate bond diagrams, place functional groups, or invent stereochemistry.

## 2. Lessons learned from the camptothecin comparison

The source case involves SN-38, (S)-10-hydroxycamptothecin (10-HCPT), irinotecan, topotecan, and belotecan.

Previous presentation errors to avoid:

1. Highlighting every matched *atom* produced distracting circles/dots across the molecules.
2. Restricting the common framework to ring bonds omitted shared exocyclic carbonyl bonds and other conserved groups.
3. Treating an automatically generated maximum common substructure (MCS) as the chemically intended pharmacophore/scaffold without inspecting the atom map.
4. Using independently generated orientations made substituent positions difficult to compare.
5. Shrinking chemically dense structures or using low-resolution raster exports impaired readability.
6. Treating vendor SMILES with unspecified stereochemistry as publication-verified configurations.
7. Overstating uniformity: the aromatic 10-hydroxyl is **not** present in every member of this five-compound group. Likewise, verify individual substituent identities from the actual structures rather than copying verbal descriptions.

Important chemical distinction: camptothecin has a conserved pentacyclic framework, a quinolinone carbonyl and an E-ring **lactone carbonyl**. Do not describe all carbonyls as ketones; distinguish chemical functionalities accurately. The C20 hydroxyl and C20 ethyl substituent may be part of the deliberately extended shared motif if verified across every selected structure. An extended shared motif is **not automatically identical** to a Bemis–Murcko scaffold.

## 3. Source and structure integrity

Before drawing, create a structure manifest with:

- Preferred compound name, source and source URL/accession.
- Original SMILES or SDF, and standardized parent SMILES.
- RDKit canonical isomeric SMILES and molecular formula.
- InChIKey when possible, including stereochemical and protonation notes.
- Salt/counterion handling (record original form; never silently switch analytical identity).
- Explicit versus unspecified tetrahedral and double-bond stereochemistry.
- Whether each figure depicts neutral parent, charged form, or experimentally administered salt.

Run RDKit parsing/sanitization checks. Inspect potentially inconsistent structures manually against authoritative chemical identifiers and, where relevant, source publications. Do not infer chirality from a compound's trade name. If source structures conflict, resolve the discrepancy before publication or label it explicitly.

**Source-of-truth hierarchy:** primary chemical structure from experimentally published record or curated authoritative source > verified database SDF/isomeric SMILES > vendor structure with documented caveats. Automated 2D depiction cannot repair incorrect starting chemistry.

## 4. Define the core before highlighting

Decide which of the following is intended:

- **Ring scaffold:** common ring system and its ring bonds.
- **Bemis–Murcko scaffold:** ring systems and linkers produced by `rdkit.Chem.Scaffolds.MurckoScaffold`; exocyclic functional groups may be removed.
- **Extended conserved chemical framework:** manually approved ring system plus specified conserved exocyclic features (e.g., carbonyl groups and C20 substituents).
- **MCS:** algorithmic shared atom/bond graph, useful as a starting hypothesis but not necessarily the desired chemical scaffold.

For a *shared-core figure*, state the definition precisely. If the manuscript wants carbonyls, C20–OH, and C20–ethyl highlighted, include their **actual bonds and atoms** in the chosen template/query after confirming they are identical in all depicted structures.

**Do not use MCS as a substitute for chemical judgment.** If MCS is used, constrain rings appropriately, inspect its SMARTS, check atom/bond counts and verify positions on each derivative. An atom may be conserved but a neighboring substituent or bond order may differ.

## 5. Verify core matches across every molecule

1. Load the reference core as a chemically valid molecule or an explicit SMARTS query.
2. Calculate substructure matches for each molecule.
3. Check that exactly the intended region matches and inspect ambiguous symmetric matches.
4. Compare mapped bond orders, aromaticity, positions and substituent attachment points.
5. Confirm that all requested highlighted **bonds** belong to the matched core.
6. Store core atom indices, bond indices, atom maps, input SMILES and RDKit version in a reproducibility manifest.

A bond of the reference core is mapped to a molecule using the corresponding pair of matched atom indices; avoid mapping bond indices positionally across independent molecules.

If the shared region is not actually present in every molecule, do not force a match or edit a molecule to make the diagram look consistent.

## 6. Consistent 2D alignment

Use a well-formed, correctly oriented 2D reference core and RDKit constrained depiction:

- `rdDepictor.Compute2DCoords(reference)`
- `rdDepictor.GenerateDepictionMatching2DStructure(mol, reference, ...)`

Retain any stereochemical wedges and atom labels. Validate that the alignment preserves chemical integrity. When substituents crowd each other, enlarge panels or choose a better reference orientation rather than rotating each molecule independently.

For a five-compound SAR comparison, prefer a consistent grid (such as three structures on the first row, two on the second), equal molecular scale, adequate whitespace and concise labels.

## 7. Bond-only highlighting: no dots

The manuscript figure should usually use **colored core bonds** (and optionally a very restrained bond-width emphasis), with all noncore bonds black. Avoid filled circles at every conserved atom.

RDKit options:

- `MolDraw2DSVG` for vector output.
- `DrawMolecule(..., highlightAtoms=[], highlightBonds=core_bond_ids, highlightBondColors=...)` where the installed RDKit version supports these signatures.
- Set `MolDrawOptions().fillHighlights = False` when appropriate.
- Set `MolDrawOptions().continuousHighlight = False` or choose a discrete style when continuous backgrounds obscure the chemical line work.
- Explicitly test the selected draw options: RDKit highlighting semantics vary by renderer/options. Inspect the **rendered SVG**, not only the code.

For crisp *colored bond strokes* with no halos or dots, a reliable alternative is drawing normally and using RDKit's bond highlighting/color options confirmed by visual inspection. Do not use atom highlighting merely to force bond colors.

**Minimal conceptual pattern** (requires a verified `mol`, mapped `core_bond_ids`, and corresponding 2D coordinates):

```python
from rdkit.Chem.Draw import rdMolDraw2D

drawer = rdMolDraw2D.MolDraw2DSVG(700, 450)
opts = drawer.drawOptions()
opts.addAtomIndices = False
opts.bondLineWidth = 2.0
opts.fillHighlights = False

drawer.DrawMolecule(
    mol,
    highlightAtoms=[],
    highlightBonds=core_bond_ids,
    highlightBondColors={i: (0.10, 0.39, 0.70) for i in core_bond_ids},
)
drawer.FinishDrawing()
svg = drawer.GetDrawingText()
```

Run a small single-compound visual test before generating the whole grid. If the result has colored blobs, halo strokes or missing carbonyl highlights, change the drawing approach rather than distributing an unsatisfactory figure.

## 8. Publication design standards

- White background; no ornamental banners, shadows, gradients, decorative cards or unnecessary tables inside the chemical structure panel.
- Clean black skeletal bonds and atom labels; one consistent, restrained highlight color.
- Align all five core structures to the same 2D template and maintain visually comparable scale.
- Provide clear compound names beneath each structure. Use a separate concise legend: “Blue bonds denote the conserved [explicitly defined] framework.”
- Draw no invented R groups, impossible valences, unmatched heteroatoms or fabricated ring closures.
- Avoid crowding at tertiary amines, lactones and bridged/substituted ring positions.
- Prefer **SVG** (editable vector through standard graphics software); export a high-resolution PNG (300–600 dpi at the intended print dimensions) if required.
- Include a neutral figure caption outside the artwork; avoid embedding unverified potency values.
- For journal submission, check the journal's artwork requirements and print-size legibility rather than assuming all SVG or PNG files are acceptable.
- Keep descriptive labels readable when the final figure is reduced to single- or double-column width.

## 9. Scientific interpretation boundaries

A shared highlighted core shows **chemical conservation**, not shared potency, mechanism, target selectivity, pharmacokinetics or direct binding. Tanimoto similarity depends on the molecular representation, fingerprint settings, structure standardization and stereochemistry treatment.

Distinguish:
- Experimental reference compounds (e.g., BRD4 activities measured for SN-38 and 10-HCPT).
- QSAR-predicted candidates (e.g., irinotecan, topotecan and belotecan).
- Exact molecule matches versus scaffold relatives or fingerprint neighbors.

Do not interpret a conserved ring system as proof of a conserved ligand–protein interaction. Never infer BRD4 binding from the color-highlighted structure figure itself.

## 10. Mandatory visual and chemical QA

Complete this checklist **before** claiming that a figure is publication-ready:

- [ ] Structures imported from verified source SMILES/SDF, with salt and stereochemical notes.
- [ ] Molecules sanitize and pass formula/charge/valence checks.
- [ ] Intended scaffold defined chemically and documented, not guessed from MCS.
- [ ] Core match and bond mapping verified separately for every compound.
- [ ] Conserved exocyclic carbonyl groups are included if the chosen definition requires them.
- [ ] Conserved C20–OH and C20–ethyl groups included only if checked across all structures.
- [ ] Variable 10-position OH and other variable substituents remain unhighlighted.
- [ ] No atom-index dots, colored discs, unreadable halos or distorted chemical bonds.
- [ ] All molecules aligned with a single 2D reference scaffold.
- [ ] Stereochemical wedges retained where source stereo is known; undefined stereochemistry labeled.
- [ ] No collisions, cropped side chains, tiny atom labels or inconsistent structure scales.
- [ ] Full-size SVG inspected and high-resolution PNG inspected at intended manuscript size.
- [ ] Caption defines the highlighted region exactly.
- [ ] Source manifest and executable RDKit script retained for reproducibility.

If any check fails, report the figure as a **draft**, fix it, and rerender. Do not label visually inspected but chemically unverified files “publication-quality.”

## 11. Deliverables

For a user-requested scaffold comparison, deliver:

1. Publication-style **SVG** and high-resolution **PNG** of aligned structures.
2. A small input/source manifest with chemical identifiers and stereochemical coverage.
3. The executed RDKit script (not a hypothetical recipe).
4. A concise legend and figure caption defining highlighted bonds and noting any structural uncertainty.

Avoid unsolicited docking, AI-generated molecular drawings, lengthy infographics, or research-gap analysis when the request is only for a structural figure.

## 12. Reference documentation

- RDKit documentation: https://www.rdkit.org/docs/
- RDKit Cookbook: https://www.rdkit.org/docs/Cookbook.html
- RDKit Python API, drawing: https://www.rdkit.org/docs/source/rdkit.Chem.Draw.rdMolDraw2D.html
- RDKit Python API, depiction: https://www.rdkit.org/docs/source/rdkit.Chem.rdDepictor.html
- RDKit Python API, MCS: https://www.rdkit.org/docs/source/rdkit.Chem.rdFMCS.html
- RDKit Murcko scaffolds: https://www.rdkit.org/docs/source/rdkit.Chem.Scaffolds.MurckoScaffold.html

**Governing principle:** Scientific structural accuracy first; interpretable visual comparison second; publication polish third. An attractive drawing with incorrect bond mapping is not a usable research figure.
