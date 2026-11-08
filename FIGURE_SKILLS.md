# FIGURE_SKILLS.md — General-Purpose Figure Design, Production, and Quality Assurance

**Version:** 2.0.0  
**Scope:** Reusable across research articles, theses, technical reports, presentations, dashboards, education, business, and other figure-producing workflows.  
**Status:** General-purpose skill; no project-, software-, discipline-, or journal-specific settings are mandatory unless specified by the task.

## 1. Purpose and operating principle

Create clear, accurate, accessible, reproducible, publication- or presentation-ready visual figures. The figure must serve the communication objective and preserve the truth of its source material. Choose a visual encoding based on the data, audience, and intended medium, rather than applying one chart template to every problem.

**Core rule:** Understand the question → inspect the evidence → select an appropriate visual form → produce → inspect → revise → export → obtain approval where required.

Never assume that a high-resolution file is automatically a high-quality figure. Do not invent measurements, citations, statistical significance, uncertainty, or results.

## 2. Intake: determine the figure's requirements

Before drawing, identify (or infer conservatively where the task permits):
- **Purpose:** comparison, distribution, trend, correlation, composition, geography, workflow, mechanism, image annotation, conceptual illustration, or other.
- **Source:** measured/observed data, model outputs, derived statistics, validated diagrams, user-provided assets, or explicitly requested illustration.
- **Audience and use:** journal, presentation, poster, web, print, accessibility requirements.
- **Figure type:** plot, multipanel plot, diagram, flowchart, map, annotated image, schematic, infographic.
- **Output:** preview only, PNG, PDF, SVG, editable source, or other requested format.
- **Constraints:** target size, fonts, margins, color palette, caption, journal specifications, author-approved style.
- **Verification state:** source data available, analysis complete, provisional, missing.
- **Author's approval state:** draft vs approved.

Do not ask unnecessary clarifying questions if there is enough information to make a useful first draft. Do not silently treat an incomplete analysis as complete.

## 3. Evidence, provenance, and statistical integrity

1. Use the actual authorized source data or material. Clearly mark synthetic/example data as **illustrative**; never present it as real results.
2. Validate variable definitions, units, missingness, inclusion/exclusion rules, sample counts, grouping, and identifiers.
3. Compute summaries programmatically where possible; keep computations reproducible. Retain original data and a traceable file manifest.
4. Label statistical quantities correctly: SD ≠ SEM ≠ confidence interval ≠ prediction interval. Define error bars and sample sizes in caption/legend.
5. Keep scientific comparisons equivalent: same units, evaluation split, time window, measurement protocol, or explicitly flag differences.
6. For repeated/paired observations, connect only genuinely matched observations. Preserve paired identifiers; do not imply pairing where none exists.
7. Never conceal inconvenient observations, crop away outliers without disclosure, manipulate axes to exaggerate effects, or imply causation from correlation.
8. Do not report significance symbols/p-values unless the corresponding analyses were actually performed.
9. Distinguish training, validation, test/holdout, independent external validation, predicted values, and experimentally measured outcomes.
10. Where data and claims disagree, report the discrepancy instead of silently editing either.

## 4. Choose the appropriate visual encoding

| Communication need | Good default options | Common mistakes |
|---|---|---|
| Compare categories | Dot plot, interval plot, bar chart where justified | Bars hiding sample variability |
| Show individual observations | Scatter/strip/swarm/dot plot | Showing only aggregated means |
| Compare paired observations | Paired dot/line plot | Connecting unrelated subjects/folds |
| Show distributions | Histogram, density, ECDF, violin, boxplot plus points | Overinterpreting boxplots with very small n |
| Show trends/time series | Line chart with actual time order; uncertainty band if supported | Treating nominal categories as continuous time |
| Show relationships | Scatterplot with appropriate fit/identity line | Unsupported regression or causal claims |
| Show parts of a whole | Stacked bars, proportion chart | Unreadable slices and misleading totals |
| Show matrices | Heatmap with readable legend and perceptually sensible scale | Rainbow palettes, undocumented normalization |
| Show networks/workflows | Node-link diagram, flowchart with unambiguous direction | Excessive crossing arrows and tiny labels |
| Show mechanisms/structures | Labeled schematic, technical drawing, precise annotation | Aesthetic but scientifically inaccurate geometry |
| Show spatial variation | Map with scale/projection/source and legend | Ambiguous location or ungrounded positions |
| Show image evidence | Image panel with scale bar and honest enhancements | Unmarked montage and selective image alteration |

Select charts because they answer the user's question. Do not mandate specific panel counts or types across unrelated projects.

## 5. Layout and visual hierarchy

- Prioritize the data and core message over decorative elements.
- Use consistent alignment, spacing, panel dimensions, and typography.
- For multipanel figures, use legible panel labels (A, B, C, …) and coherent reading order.
- Allow enough room for ticks, axis labels, annotations, legends, uncertainty bars, and long category names.
- Prefer a clear legend or direct labeling; avoid duplicating both unnecessarily.
- Avoid decorative gradients, shadows, unnecessary 3D effects, or background patterns.
- **Titles are task-dependent.** For journal manuscript figures, prefer a caption outside the figure when requested. For dashboards, presentations, and standalone charts, a concise internal title can be appropriate. Never hardcode “no overall title” as a universal rule.
- Consider the final reduction size (single-column, double-column, slide screen, phone, poster). Inspect at that size, not just enlarged.
- Coordinate axis scales when comparisons benefit from identical limits; otherwise annotate different scales to prevent misleading comparisons.

## 6. Contrast, typography, axes, and mark weight

**High contrast is essential, but style is configurable.** These are starting points for scientific plots, **not mandatory defaults for every visual medium**.

| Element | Print-oriented starting range | Practical requirement |
|---|---|---|
| Axes/spines | ~1.2–2.4 pt; optionally heavier | Clearly visible after reduction |
| Tick marks | ~1.0–2.2 pt; ~4–8 pt long | Dark enough to see; consistent placement |
| Axis labels | ~10–14 pt at design size | Legible, sufficient font weight |
| Tick labels | ~8–12 pt | Legible without clutter |
| Panel labels | ~11–16 pt, often bold | Distinguishable and aligned |
| Markers | ~4–9 pt plus contrasting edge as needed | Individual points discernible |
| Error bars | ~1.2–2.4 pt with legible caps | Visible and not visually deceptive |
| Connecting lines | ~1–2 pt | Sufficient contrast, not dominant |
| Gridlines | None or subtle | Must not compete with data |
| Background | Solid neutral, commonly white | Good contrast with marks and text |

### Contrast audit
When a figure looks **faded**, evaluate **all** of these together:
1. Axis darkness, axis thickness, and tick strength.
2. Tick text weight and actual rendered font (not just nominal size).
3. Marker saturation, marker size, outlines, and opacity.
4. Error-bar contrast and cap thickness.
5. Connecting-line contrast and legibility.
6. Legend readability and distinction of categories.
7. Reduced-size and grayscale appearance.

**Do not treat increased DPI as a fix for weak contrast.** Conversely, excessively thick axes and all-bold labels can overwhelm thin data: achieve balanced visual weight.

### Typography
Use the font family specified by the user, publisher, or brand. Otherwise choose a legible, consistent sans-serif for plots (or an appropriate font for the medium). Use weight hierarchy intentionally: emphasized headings/axis titles, readable ticks and annotations, no gratuitous boldness. Ensure Greek letters, subscripts, mathematical symbols, and non-English scripts render correctly.

## 7. Colors and accessibility

- Use a consistent, accessible palette appropriate to the audience and medium.
- Ensure text/mark contrast against the background.
- Distinguish categories by color **and**, when needed, marker shape, line pattern, label, or position.
- Check grayscale legibility and color-vision accessibility when relevant.
- Use sequential colors for magnitudes, diverging colors for signed deviations around a meaningful center, and categorical colors for groups.
- Avoid low-opacity pale lines on white, high-saturation backgrounds, and rainbow maps without justification.
- Preserve domain color conventions or user preferences when specifically requested.

## 8. Figure-specific technical checks

### Quantitative plots
- Axis direction, intercept, transforms, units, scales, and labels must match the data.
- Recalculate summary values when possible; state uncertainty definitions.
- Show raw points when sample sizes are small and privacy permits.
- Label predictions as predictions, not observations.
- In parity plots, correctly implement any identity line (y = x) and avoid misleading axis disparity.

### Images, micrographs, and photographs
- Preserve provenance and processing history.
- Report scale bars, magnification, acquisition metadata, and treatment details when applicable.
- Apply only scientifically appropriate global adjustments; declare substantial manipulation, composite panels, or selective changes.
- Respect consent, privacy, licensing, and attribution.

### Diagrams and schematics
- Preserve causal direction, order, variable meaning, and mechanistic accuracy.
- Ensure arrows, nodes, legend, labels, and edge crossings are unambiguous.
- When a diagram is conceptual rather than empirically validated, identify it as such.

### Maps
- Use grounded geography and appropriate scale, projection, labels, legend, and source attribution.
- Do not fabricate coordinates, routes, or travel times.

## 9. Reproducibility and tool selection

- For data-driven charts, prefer reliable programmatic plotting (e.g., Matplotlib, Plotly, R/ggplot2) or user-selected software. Save scripts/configurations when possible.
- For editable diagrams, use native vector/diagram formats or source code where appropriate.
- For illustration tasks, use the requested medium while keeping data visualization distinct from decorative imagery.
- **Do not use generative image tools to fabricate or replace scientific data plots.** For purely illustrative figures, use generation only where the user explicitly requests an image or illustrative component and the task permits it.
- Track input data paths, processing steps, plot parameters, font/color configuration, versions, and output filenames.

## 10. Export and delivery

Choose formats based on publisher and user requirements:
- **SVG/PDF/EPS or other vector format** for crisp scalable lines and text when supported.
- **PNG/TIFF** for high-resolution raster output; 300–600 DPI may be appropriate for many journal workflows, but always check specific submission requirements.
- **Editable native source** where requested and feasible.
- Prefer lossless export, correct aspect ratio, embedded fonts when appropriate, and no clipped labels.
- Verify that exports really exist, open, and match the preview. Inspect text rendering, transparency, line weights, and resolution.
- Avoid promising “editable” if the chosen format is merely a flattened image; SVG editability depends on how text and graphics are encoded.
- Include a separate caption when applicable; the caption should describe the plotted variables, groups, panels, units, statistics, and abbreviations.
- Never distribute font files.

## 11. Quality assurance checklist

- [ ] Figure type fits the communication objective.
- [ ] Source data/visual material verified; values, groups, units, and counts correct.
- [ ] No invented results, unsupported statistics, or misleading omissions.
- [ ] Appropriate encodings, axis limits, transformations, and uncertainty labels.
- [ ] High-contrast axes, marks, text, and connecting lines **at final display size**.
- [ ] Colors and symbol differences remain interpretable in grayscale/accessible contexts.
- [ ] Panel labels, categories, legend, and annotations readable without collisions.
- [ ] Text hierarchy appropriate to medium; no unwanted titles.
- [ ] Correct target/project-specific terms only where relevant.
- [ ] Figure caption separate or internal according to requirements.
- [ ] Exports validated: no cropping, missing glyphs, transparency issues, or invisible marks.
- [ ] Reproducible source and provenance available where appropriate.
- [ ] Approval status accurate; **draft is not final unless the author approves**.

## 12. Revision protocol

1. Interpret feedback as a concrete visual or analytical requirement, not as a request to redraw unrelated content.
2. Keep source data and analysis fixed unless the user authorizes a methodological change.
3. Revise the deficient properties in combination when necessary: e.g., “too faint” can require axes, tick labels, dots, lines, and error bars to change together.
4. Re-render and inspect at intended print/display dimensions.
5. Show the **actual revised figure** and verified export links.
6. Preserve iteration history or versions when useful.
7. Never assert approval until it is explicitly given.

## 13. Configuration template (adapt per task)

```yaml
figure:
  purpose: comparison
  medium: journal         # journal | thesis | slide | poster | web | report | other
  size: publisher_or_user_defined
  title_inside_figure: false  # true for standalone presentations where useful
  panel_layout: auto
  background: white
  font_family: user_or_publisher_preference
  font_weight: readable_hierarchy
  palette: accessible_high_contrast
  axes:
    width_pt: 1.8        # adjust after print-size preview
    color: "#000000"
  ticks:
    width_pt: 1.5
    length_pt: 6
  grid: false
  error_bars: show_if_supported
  data_points: preserve_all_eligible
  exports: [png, pdf, svg]
  raster_dpi: 600        # subject to publisher specifications
  caption: separate
  approval: pending
```

The configuration is a **starting preset**, never a rigid requirement. Apply domain-specific requirements **only within the relevant project or figure brief**, not in this general-purpose skill.

## 14. What this skill must never do

- Declare a particular project, target, algorithm, dataset, palette, chart layout, or named software style mandatory everywhere.
- Replace real data with illustrative values without labeling them.
- Confuse graphic polish with analytical validity.
- Turn a user's design critique into a new unrelated figure.
- Conceal incomplete analyses or claim experiments were performed without evidence.
- Claim that approval has been granted when it has not.
