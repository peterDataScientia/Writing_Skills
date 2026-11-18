---
name: research-timeline-design
description: Create reproducible, publication-ready scientific research timelines and Gantt charts using validated CSV data and Matplotlib. Use for proposal, dissertation, and project work-plan graphics.
---

# Research Timeline Design

## Purpose
Generate beautiful, clear, reproducible Gantt charts from a source CSV. Applies to any research domain. Do not guess dates or treat proposed timelines as official deadlines.

## Input contract
The schedule must contain `Task`, `StartMonthIndex` (zero-based), and `DurationMonths` (positive integer). Provide first calendar month (`YYYY-MM`) and total number of months. Reject missing values, non-integers, negative starts, durations below one, and activities extending beyond the display. When updating one activity, preserve all others.

## Approved visual system
- Matplotlib, aligned with the approved scientific figure settings used by Figentra: DejaVu Sans, 12 pt bold activity/month labels, visible left and top axis lines at 2 pt, outward 6 pt major ticks, no minor ticks.
- Landscape canvas expanded when necessary to keep long activity labels readable. Use generous left margin; verify no clipping after rendering.
- White background, very pale blue alternating month panels, subtle separators, bright yet academic navy-blue/teal rounded bars, minimal shadow.
- No chart title, footnote, notes, legend, completion percentages, invented milestones, or decorative gradients unless specifically requested. Put figure caption outside the chart.
- Exports: PNG at 600 dpi, PDF, and SVG. One script must generate all formats from the same input data.
- Scientific integrity: colors/style cannot change activity timing or meaning; do not invent progress or statuses.

## Reproducible workflow
1. Read the schedule and previous user decisions. Keep every constraint not explicitly changed.
2. Validate the CSV columns, month indices, and duration bounds. Construct calendar labels from `YYYY-MM`, crossing year boundaries correctly.
3. Draw tasks in CSV order from top to bottom, month columns, visible axes, and properly scaled rounded bars.
4. Use the approved palette and export all formats from one Matplotlib figure.
5. Open the PNG and inspect months, axis visibility, legibility, bar endpoints, and clipped labels. Correct layout and rerun if necessary.
6. Supply the Python script and editable CSV alongside all output figures. State whether dates are proposed or institutionally approved outside the figure.

## Command
```bash
python -m pip install matplotlib pandas
python plot_research_timeline.py --csv example_schedule.csv --start 2026-10 --months 6 --out research_timeline
```

Expected: `research_timeline.png`, `research_timeline.pdf`, `research_timeline.svg`.

## Example schedule (not universal)
The bundled October 2026–March 2027 six-month BRD4 dissertation schedule has proposal development Oct–Nov; literature review Oct–Feb; dataset preparation Oct–Nov; QSAR development Nov–Dec; FDA-approved drug screening Dec; experimental validation Jan–Feb; analysis/writing/submission Jan–Mar. These are planning values, not independently certified regulatory deadlines.

## Quality assurance
- [ ] Every period matches the input schedule
- [ ] All six month labels correct, without overlap
- [ ] Visible X and Y axes, bold labels and appropriate tick widths
- [ ] Title, notes and legend absent unless requested
- [ ] All bars visible; no clipped task names
- [ ] PNG, PDF, SVG exported from the same validated inputs
- [ ] CSV and source script included for reproducibility

## Companion files
- `plot_research_timeline.py`: standalone command-line implementation.
- `example_schedule.csv`: editable sample data.
