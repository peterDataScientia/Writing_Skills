# Worked case: Evidence-driven scientific argument construction

Source: [CDK introduction v0.0.0.1](CDK_Introduction_v0.0.0.1.md). This is a user-supplied working draft, preserved in full including the editorial verification note. The example demonstrates argument architecture, not independent verification of clinical claims, references, or novelty. Do not treat it as a validated scientific gold standard.

## Paragraph dependency map

| P | Scientific function | Premise established for the next step | Critical check |
|---|---|---|---|
| 1 | Epidemiology, disease progression and heterogeneity | Treatment depends on stage and biological subtype | Verify WHO estimates and staging citations; burden does not justify a kinase target |
| 2 | HR+/HER2− context and oestrogen signalling | Endocrine signalling connects to proliferation and cell-cycle machinery | Verify subtype prevalence and distinguish clinical receptor categories from molecular intrinsic subtypes |
| 3 | CDK biology and mechanism | CDK4/6 and endocrine co-inhibition has biological rationale | Verify CDK family numbering, cyclin regulation and context-specific mechanisms |
| 4 | Current intervention and outcomes | Clinical benefits coexist with progression and resistance | Check MONALEESA-2 population, comparator, endpoint and trial context; progression alone does not identify mechanism |
| 5 | Cyclin E–CDK2 escape mechanism | CDK2 inhibition may address a subset of resistance mechanisms | PALOMA-3 association is not proof of causality; distinguish biomarker association and preclinical intervention |
| 6 | Evolution to CDK2/4/6 inhibition | Residual toxicity motivates questioning whether all three kinases require inhibition | Complete PF-06873600 citations; do not assign all toxicity to CDK6 |
| 7 | Differential CDK4/CDK6 biology | CDK6 sparing with CDK2/4 inhibition becomes a plausible strategy | Distinguish preferential inhibition and complete selectivity; preclinical findings do not guarantee clinical safety |
| 8 | Existing combinations and dual inhibitors | Feasibility already demonstrated; potency/selectivity balance remains a candidate discovery challenge | Verify trial status and abstract findings; Cpd-1308 values are cellular target engagement, not biochemical IC50 |
| 9 | Structural challenge and design rationale | Both intended targets and CDK6 must be assessed jointly | Verify 92% identity definition, alignment and binding-site scope; do not infer selectivity from sequence alone |
| 10 | Kinase profiling and QSAR rationale | Experimental data can support candidate prediction | Verify assay types: kinase binding affinity versus inhibition; distinguish prediction from measurement |
| 11 | Comparative computational literature synthesis | Different selection objectives motivate testing a distinct profile | Verify original papers, scope and recent direct competing approaches; difference alone is not novelty |
| 12 | Research purpose, reliability and boundaries | Target-specific modelling, AD and selectivity screening yield candidates for biochemical evaluation | Quantify potency and selectivity requirements, harmonise endpoints, assess uncertainty and validation |

## Six transferable principles

1. Progressive scientific reasoning: narrow context through supported premises, not keywords.
2. Paragraph dependency: identify each paragraph's role, incoming premise and outgoing implication. Not every introduction must be strictly linear.
3. Evidence functionality: label what each quantitative result demonstrates and what it cannot establish.
4. Strategy evolution: show what an existing intervention achieved, what remains unresolved, and why a new strategy is scientifically plausible.
5. Comparative gap construction: compare target profile, outcome, methods and limitations across directly relevant studies.
6. Methodological emergence: introduce the method when the unresolved question and data requirements make its suitability clear.

## Quantitative evidence audit

| Draft evidence | Argumentative purpose | Boundary |
|---|---|---|
| 2.4 million diagnoses, 694,000 deaths | Disease burden | Verify year/source; not evidence for CDK2/4 |
| 51.4 vs 63.9 months | Existing therapeutic benefit | Overall survival in a specified trial, not resistance rate |
| 7.6 vs 14.1 months | Association with cyclin E1 | Progression-free survival subgroup; not universal causal mechanism |
| Cpd-1308: 123, 24, 521 nM | Unequal CDK2/4 selectivity relative to CDK6 | Ratios 521/123 ≈ 4.2 and 521/24 ≈ 21.7; cellular engagement, preliminary abstract |
| 92% ATP-site identity | Structural conservation challenge | Verify residue definition and source |
| 8,592 compounds | Scope of prior computational work | Dataset size is not evidence of validity or a missing research profile |

## Comparative gap matrix

| Study as described in draft | Primary prioritisation | What it does not establish for this study |
|---|---|---|
| Kaveh et al. (2024) | Multi-CDK structure–activity/selectivity relationships | Whether a CDK2/4 dual, CDK6-sparing screen was directly evaluated |
| Akinnusi et al. (2026) | CDK2-biased activity relative to other CDKs | Joint CDK2 and CDK4 potency with CDK6 sparing |
| Wang et al. (2026) | CDK4/6 dual inhibition | CDK6 sparing with CDK2/4 inhibition |
| Proposed investigation | CDK2/4 potency and comparatively weaker CDK6 activity | Clinical safety, efficacy and experimental activity remain unproven |

This comparison establishes a difference in the described objectives, not an exhaustive literature gap. Search direct dual inhibitors, alternative terminologies, patents, preprints and contemporary studies before claiming novelty. Existing INV-6452 and Cpd-1308 examples rule out treating the pharmacological strategy itself as unprecedented.

## Operational LLM exercise

For a new introduction, produce a paragraph map, identify all missing inferential bridges, assign evidence roles, construct a comparative gap matrix and state a bounded contribution. Distinguish rhetoric quality from evidence quality. If one link fails, revise the chain rather than adding decorative transitions. For this case, the defensible provisional conclusion is candidate prioritisation for subsequent biochemical testing; neither overcoming clinical resistance nor reducing patient toxicity is demonstrated.

## Verification and revision priorities

- Complete and independently check references, including the editorial note in the source.
- Confirm direct prior work and search scope before asserting a research gap.
- Specify assay-matched activity thresholds and target-specific selectivity ratios; account for prediction errors and joint applicability domains.
- Keep the clinical motivation separate from the computational deliverable.
- Preserve the original source as an example, not as a final manuscript.
