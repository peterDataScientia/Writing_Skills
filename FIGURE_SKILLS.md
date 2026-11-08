# FIGURE_SKILLS.md — Publication-Quality Scientific Figures

Version: 1.0.0  
Updated: 2026-11-08  
Scope: Scientific journal figures, especially computational chemistry, QSAR, machine learning, and cheminformatics manuscripts.

## Purpose
Produce publication-quality **data-driven, reproducible** figures suitable for author review and eventual journal submission. Figures must faithfully represent the underlying analysis, be legible after reduction to journal column width, and maintain high contrast. **Never claim that a figure is approved until the author explicitly approves it.**

## Binding user preferences for this workflow
- Prefer **programmatic figures** using Python/Matplotlib or equivalent, not AI image generation. Do not use image generators for scientific plots.
- Use **GraphPad Prism-inspired publication styling**, not a claim of strict equivalence to any particular Prism template.
- **No overall title inside the figure.** Write the formal figure title/caption separately in the manuscript.
- Use a **white background**, with **no decorative backgrounds, gradients, shadows, or gridlines** by default.
- Maintain **high saturation, strong contrast, visibly black and substantial axes, thick tick marks, dark readable typography, visible error bars**, and clearly distinguishable data markers.
- For multipanel figures, label panels **A, B, C, D** clearly and keep spacing sufficient to prevent crowding.
- Keep targets and metrics correctly named (e.g., **BRD4-BD1**, not unspecified BRD4 if the data are BD1-specific).
- Always render and inspect the actual plot at a **manuscript-like display size** before presenting it for approval. Do not ask the author to approve a figure based only on source code.
- **No invented observations.** Do not use illustrative or synthetic values in a figure claimed to show study results.

## 1. Data provenance and analysis integrity
1. Load real, final analysis data from traceable CSV, XLSX, or analysis artifacts.
2. Check source columns, sample sizes, target IDs, algorithm configurations, fold identifiers, and missingness. Verify the number of observations per group.
3. Recompute means, SDs, and statistics from raw fold records when possible. Do not manually type summary metrics if a file supports direct computation.
4. For tuned ML models, label results accurately: **development-validation**, **model-selection**, **fixed-holdout**, or **independent experimental**, as applicable. Do not label selection-fold metrics as independent holdout performance.
5. Apply the same grouping and folds across algorithms only if verified from underlying files. Paired lines must connect the **same fold identifier**, never inferred ordering.
6. Do not mix scores from incompatible datasets, folds, random seeds, or evaluation protocols without explicitly describing that distinction.
7. Preserve all real outliers and replicate points. No smoothing, cropping, shifted data, unreported normalization, or selective omission that changes interpretation.
8. State whether error bars represent SD, SEM, CI, or another quantity; never substitute one for another.

## 2. Layout rules
- Favor a clean, balanced layout. When four panels are required, use a **2 × 2** grid with aligned axes and consistent panel sizes.
- Arrange comparisons logically: e.g., top row R² for EGFR and BRD4-BD1; bottom row RMSE for EGFR and BRD4-BD1.
- Match axis limits **when doing so makes comparisons meaningful**, but do not force misleading scales.
- Avoid overcrowding: sufficient margin between panels, labels, ticks, legend, and data. Move a shared legend below all panels when necessary.
- No *suptitle* or decorative headline. Use concise panel letters and target labels only.
- Keep captions outside the plotted canvas for manuscript typesetting.
- Display units on axis labels (e.g., RMSE (pIC₅₀ units)); show R² as dimensionless.
- Avoid duplicating information already unambiguously presented in the figure or manuscript table.

## 3. GraphPad Prism-inspired high-contrast style
These are **starting specifications**, not universal journal requirements. Verify the actual 100% and reduced-size preview.

| Element | Preferred starting point |
|---|---|
| Figure background | Pure white (#FFFFFF) |
| Axes (left and bottom) | Solid black, **2.6–3.1 pt** |
| Top/right spines | Hidden unless scientifically needed |
| Tick marks | Black, outward, **2.3–2.8 pt**, length **7–9 pt** |
| Tick labels | Black, high contrast, **11–13 pt**, medium/bold when needed |
| Axis titles | Black, **14–16 pt**, semibold/bold |
| Panel letters | Black, **15–18 pt**, bold |
| Panel target labels | Black, **14–16 pt**, bold |
| Data markers | Solid, saturated; **7–10 pt** diameter with black edges (~1–1.4 pt) |
| Error bars | Colored/dark, **2.4–3.2 pt**, clear caps |
| Connecting lines | Visible slate/dark gray, **1.5–2.1 pt**, NOT near-white or very pale |
| Legend | High-contrast black text and full-saturation marks, without frame |
| Grid | None by default |
| Overall title | **None** |

Important: Increasing axis widths alone does not solve faintness. Evaluate **text weight, tick brightness, point fill, marker edge, error bar contrast, connecting-line opacity, and printed-scale visibility together**. If a trace is still washed out, strengthen it rather than repeatedly exporting the same look.

### Color and accessibility
- Use a consistent **dark blue, saturated red-orange, strong teal-green, deep navy/slate** for the four model identities, or the author-approved palette. Colors must remain distinct in grayscale where practical by using distinct marker symbols.
- Do not rely on color alone: combine color with clear labels, shapes, or line styles.
- Check grayscale and small-size readability; colorblind-safe palettes are preferable when practicable.
- No transparency that causes thin lines or data to disappear on white.

## 4. Font discipline
- Use a consistent **Arial/Helvetica-like sans serif** (or another approved installed scientific font).
- Axis titles and panel labels: bold enough to remain legible, without unnecessarily heavy typography.
- Tick numbers and model names: regular or medium by default, but **increase to medium/bold if contrast at print size requires it**.
- Do not let visual style override readability. Consistent proportions matter more than a named font.
- Embed fonts in PDF if supported and use SVG with editable text where feasible; do not distribute font files.

## 5. Selecting chart types
- **Five repeated scaffold validation splits:** favor individual fold points plus **mean ± SD**; optionally link corresponding folds with discernible lines **only when pairs truly match**. State paired connection logic in the caption.
- Use boxplots cautiously with only five folds; show all raw points if boxplots are chosen.
- Parity charts: experimental versus predicted pIC₅₀; include a correctly drawn y=x reference line, identify dataset as holdout or development, and do not imply prospective experimental confirmation.
- Y-randomization: show the randomized-R² distribution and the true model R² reference separately for each target. State number of permutations and tested model settings; old hyperparameter randomization does not automatically validate updated selected models.
- Dual-target screening: plot EGFR versus BRD4-BD1 predicted pIC₅₀, label candidate drugs sparingly, and draw cutoffs only if they were prespecified and justified.
- Avoid ROC curves for continuous-pIC₅₀ regression unless a distinct, declared binary task was evaluated.
- Never make 3D charts solely for aesthetics.

## 6. Output requirements
- Save and provide **PNG at 600 DPI**, **vector PDF**, and **editable SVG** whenever technically possible.
- Use `bbox_inches="tight"` or appropriate layout controls without cropping labels or error bars.
- Preserve aspect ratio and font size at final intended journal print width; do not mistake 600 DPI for visual quality.
- Keep the plotting script and input-data manifest with each final figure, including source filenames, parameters, software version, random seed/fold mapping, and generated outputs.
- Use transparent SVG/PDF text only as required; preserve true vector lines and symbols.
- Check saved PNG and rendered PDF/SVG for clipped text, lost glyphs (R², pIC₅₀), line weights, and differences from interactive preview.

## 7. Figure quality-control checklist
Before presenting the candidate figure, verify:
- [ ] Source data and all numerical aggregates validated against source files
- [ ] Correct target names, algorithms, split definitions, and model configurations
- [ ] No fabricated points, no misleading omissions or axis transformations
- [ ] No overall plot title
- [ ] All axes solid black and thick enough at manuscript print scale
- [ ] Tick marks black, prominent and sharp
- [ ] Tick numbers and labels crisp, sufficiently weighted and dark
- [ ] Points saturated and visibly outlined
- [ ] Error bars clearly visible and correctly labeled
- [ ] Connecting lines clearly visible, without overpowering observations
- [ ] Panels uncluttered and accurately labeled A–D
- [ ] Legend legible and not obscuring data
- [ ] PNG 600 DPI plus vector PDF and SVG exported and inspected
- [ ] Figure caption drafted separately
- [ ] Figure described as **draft/pending author approval**, unless approved

## 8. Iteration protocol for author feedback
1. Ask which *specific visible property* is deficient only when the author has not specified it.
2. Implement requested improvements in the **same plot from the same data**, not an unrelated replacement.
3. For complaints such as “faded/washed out,” **prioritize axes, tick labels, colored points, error bars, paired-line contrast, and font weights together**. Do not respond only by changing the DPI.
4. For complaints such as “fonts are not Prism-like,” adjust font family, actual weight, relative hierarchy and sizing; do not use decorative headings.
5. Present a fresh preview and verified file links.
6. **Do not declare approval or move on to the next figure without explicit author sign-off.**

## 9. Example: EGFR–BRD4 four-model comparison
- Use **optimized SVR, RF and XGBoost and best-tested MLP** only when their underlying fold-level runs are verified as compatible; otherwise label comparisons carefully.
- Four panels: **A EGFR R², B BRD4-BD1 R², C EGFR RMSE, D BRD4-BD1 RMSE**.
- Model labels: SVR, RF, XGBoost, MLP.
- Show five original scaffold validation fold points per algorithm, a prominent mean diamond and SD whiskers, and paired fold lines with enough contrast.
- No overall title; leave full manuscript figure caption outside.
- This layout and styling remain **subject to author approval**.

## 10. General scientific-writing safeguards
- Do not imply that a computational prediction is experimentally validated.
- Do not use “robustness proven” when only one Y-randomization fold or one model configuration has been tested.
- A publication-ready style is not evidence of reproducibility: source code, accurate labels, and underlying analysis remain essential.
- Follow specific target-journal artwork specifications when they supersede stylistic defaults.
