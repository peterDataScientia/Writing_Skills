# GFigure Skills — Approved Publication Figure Standard

**Version:** 1.0.0  
**Approved:** 31 October 2026  
**Reference implementation:** `JBU_HPU_45_Figure3_StackedFraction_EXECUTED.ipynb`  
**Scope:** Publication-grade scientific charts, with the approved JBU–HPU four-figure suite as the visual reference. The figures are created with Matplotlib in a **GraphPad Prism-inspired** style; do **not** claim they were produced in proprietary GraphPad Prism.

## 1. Design objective

Produce clean, legible, high-contrast scientific figures that remain clear when reduced for manuscript publication. Prefer a white background, strong text, high-visibility data colors, consistent visual encoding, minimal legend clutter, and faithful scientific reporting. Maintain the approved style consistently across all panels without altering data or computations for cosmetic purposes.

## 2. Approved configuration

The following values are the approved baseline. Expose them in **one configurable cell/object**, rather than hardcoding inconsistent styles across figures.

```python
FIGURE_SETTINGS = {
    'preset': 'Publication',
    'axisTitlePt': 15,
    'tickLabelPt': 12,
    'legendPt': 11,
    'axisWidthPt': 2.0,
    'markerSize': 7,  # marker diameter, points
    'majorTicks': True,
    'minorTicks': False,
    'boldHighContrast': True,
    'equalityLine': True,
    'equalityLineLegend': False,
    'palette': 'Bright high contrast',
    'exports': 'PDF + SVG + PNG',
}
```

- **Axis labels:** 15 pt, bold, near-black, descriptive but concise; never clipped.
- **Tick labels:** 12 pt, bold, near-black. Use major ticks only.
- **Axes and major tick line widths:** **2.0 pt**. Outward major ticks, approximately 6 pt length. Show left and bottom spines; hide top and right.
- **Legends:** 11 pt, bold, high contrast, preferably unboxed, placed without overlapping points or being cut off.
- **Markers:** approximately 7 pt diameter, clear dark outlines, with consistent study-group colors and distinct shapes where appropriate.
- **Background:** pure white; avoid gridlines, unnecessary boxes, and excessive decoration.
- **Export:** PDF and SVG vectors plus 600 DPI PNG, keeping fonts and graphics sharp. Use tight bounding boxes and sufficient margins.

### Approved color palette

| Purpose | Hex | Note |
|---|---|---|
| Near-black labels / outlines | `#080F1D` | All axes, text, marker borders |
| Bright blue | `#0866DD` | Odake observations; selected sensitivity results |
| Bright orange-red | `#F04C28` | Other studies |
| Bright teal-green | `#00A878` | Tang observations |
| Dark slate reference lines | `#38445C` | Dashed comparison/reference lines |
| Background | `#FFFFFF` | White |

Use distinct **shape + color** for group identification in scatter plots so groups remain interpretable even when color differentiation is limited.

## 3. Axis labels, units, and mathematical notation

1. **Units must appear in square brackets, not parentheses**, e.g., `Jack bean urease IC₅₀ [µM]`, `H. pylori urease IC₅₀ [µM]`.
2. Use proper mathematical subscripts (e.g., `IC₅₀`, `log₁₀`) and avoid plain `IC50` in final rendered artwork.
3. When a ratio is explicitly requested as a fraction, render a **vertically stacked numerator/denominator inside square brackets**, not a simple inline slash.
4. For the approved Figure 3, the X-axis is arranged across two lines as:

   **Pooled** \(\left[\dfrac{\mathrm{HPU}_{IC_{50}}}{\mathrm{JBU}_{IC_{50}}}\right]\)  
   **after excluding each study**

   Position and line spacing must keep the full fraction, brackets and second line visibly within the exported figure. Matplotlib may use two text objects to render the stacked math cleanly. Avoid cramped labels or text extending off the page.
5. Long labels may wrap to two clear lines without removing the user-approved information. Do not change a label's meaning while shortening it.
6. **Scientific caveat:** Source study Odake et al. (1994) reported `I₅₀`, whereas other publications report `IC₅₀`. The **approved figure convention** displays `IC₅₀` consistently. This must never be mistaken for proof that the source publications used interchangeable terminology. Preserve original endpoint names in source-data provenance and state any harmonization in the manuscript Methods/caption. Do not silently convert or remeasure observations.

## 4. Study citations on categorical axes

- Axis rows representing **studies** are cited consistently as `First author (Year)`, `First author & Second author (Year)` for exactly two authors, or `First author et al. (Year)` for three or more authors, subject to journal style.
- Confirm **full author lists** against the original source metadata before assigning the format; do not guess the number of authors.
- Never use a compound name such as `Coptisine (2018)` in place of an author-year study citation.
- Keep internal stable identifiers (`study_id`, e.g., `Coptisine_2018`) for merging/provenance; use a separate display-label field (e.g., `study_label`) for the charts and human-readable CSVs.
- The approved dataset uses the following display mapping:

| Internal study ID | Displayed author–year label |
|---|---|
| `Odake_1994` | Odake et al. (1994) |
| `Yu_2015` | Yu et al. (2015) |
| `Mo_2015` | Mo et al. (2015) |
| `Tan_2017` | Tan et al. (2017) |
| `Zhou_2017` | Zhou et al. (2017) |
| `Coptisine_2018` | Li et al. (2018) |
| `Mohammed_2022` | Mohammed et al. (2022) |
| `Sanguinarine_2022` | Lu et al. (2022) |
| `Quercetin_2025` | Li et al. (2025) |
| `Lu_2025` | Lu et al. (2025) |
| `Tang_2025` | Tang et al. (2025) |
| `Zhao_2026` | Zhao et al. (2026) |

This mapping is specific to the approved dataset; **do not generalize it to unrelated projects**.

## 5. Approved JBU–HPU figure designs

### Figure 1 — Paired urease inhibition concentrations

- X-axis: `Jack bean urease IC₅₀ [µM]`.
- Y-axis: `H. pylori urease IC₅₀ [µM]`.
- Use equal log-scale domains, major ticks only, visible high-contrast markers.
- **Keep the dashed 1:1 equality line on the plot, but exclude its entry from the legend.**
- Figure 1 legend **exactly**:
  - `Odake et al. (1994) [29]` — bright-blue circle.
  - `Other studies [14]` — orange-red diamond.
  - `Tang et al. (2025) [2]` — teal-green triangle.
- Numbers in **square brackets** denote paired observations; publication years remain in **parentheses**.
- Retain the Spearman annotation (\(\rho\) and \(n\)); keep it inside a clear location without obscuring points or lines.

### Figure 2 — Study-level ratios

- Display one dot per study against the within-study geometric mean HPU/JBU ratio on a log X-axis.
- Use first-author–year Y-axis labels, ordered by the study estimate.
- Include a separately aligned `n` column listing number of paired observations per study.
- Retain the vertical reference line at ratio 1, without implying that it is a confidence interval.
- Do not fabricate standard errors or confidence intervals for single-pair studies.

### Figure 3 — Leave-one-study-out sensitivity

- Each Y-axis row names the **study excluded** from the re-analysis, **not the study whose own ratio is plotted**.
- Use the approved vertically stacked fraction and square brackets in the X-axis label (Section 3).
- Show the complete-data pooled estimate (~0.512) and ratio=1 as separate dashed reference lines, with concise labels.
- Show ratio values in a separate aligned right-hand column rather than allowing them to overlap markers.
- Distinguish removal of the dominant Odake study, whose exclusion raises the compound-weighted ratio to ~1.322.
- These are **descriptive sensitivity estimates**, not per-study confidence intervals.

### Figure 4 — Within-study log-ratio distributions

- Show every observed log₁₀(HPU/JBU concentration ratio) as an individual dot, grouped by first-author–year study labels.
- If necessary, apply small seeded/reproducible jitter only to separate overlapping points; **jitter must not change the numeric X-values**.
- Black short bars mark within-study mean log-ratio for groups with at least 2 observations, not confidence intervals.
- Use a compact legend distinguishing `Individual paired measurement` from `Mean (studies with n ≥ 2)`.
- Preserve the zero-reference line and major ticks; do not introduce minor ticks.

## 6. Numerical integrity and manuscript reporting

- Source figures derive from **45 paired observations across 12 studies**; 29 observations are from Odake et al. (1994).
- Treat statistical outputs as **read-only** during stylistic changes. For example, the approved analysis has Spearman \(\rho\) ≈ **0.792**, compound-weighted geometric HPU/JBU ratio ≈ **0.512**, and excluding Odake ≈ **1.322**.
- Never substitute a different weighting scheme, change sample sizes, adjust or invent uncertainties, or change endpoints merely to improve appearance.
- Keep the underlying verified source data, analysis and human-readable study labels consistent across figures, CSV files, and notebook.
- The legacy PRISMA flow is **not automatically updated** to 12 studies; study-selection records require separate reconciliation before that flow is finalized.
- The figures describe experimental associations and heterogeneity; do not claim out-of-study predictive validation from a pooled correlation alone.

## 7. Reproducibility / release checklist

Before presenting a new version:

- [ ] Run **all notebook cells** in order, without errors.
- [ ] Ensure `FIGURE_SETTINGS` is a single visible control block for the full figure suite.
- [ ] Inspect **all four full-resolution figures**, including axis labels, brackets, reference lines, legends, and spacing.
- [ ] Verify the approved colors, bold fonts, major-only ticks, 2.0 pt axes/ticks, and no clipped annotations.
- [ ] Figure 1: exact author–year legend with `[29]`, `[14]`, `[2]`; 1:1 line visible but not in legend.
- [ ] Figure 3: stacked HPU/JBU fraction enclosed by square brackets, visible in full.
- [ ] Export **PDF + SVG + PNG (600 DPI)** for each figure.
- [ ] Confirm numeric CSV/statistical outputs are unchanged against the previous approved analysis when only styling changed.
- [ ] Display the figures **directly in chat** for visual approval; do not substitute search images, placeholder components, or download links for previews.
- [ ] Never claim a figure is generated in GraphPad Prism when it was created in Matplotlib.

## 8. Approval and change control

These specifications are the **user-approved baseline** for the 31 October 2026 JBU–HPU figure suite. For future research projects, reuse the **visual standards**, not the JBU–HPU data, colors-to-study mappings, or scientific claims. Respect later explicit user changes while preserving all scientific and citation integrity checks.