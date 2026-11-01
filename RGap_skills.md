---
name: rgap-skills
version: "1.1.0"
description: >-
  Evidence-first skill for discovering, testing, writing, and critically reviewing
  scientific research gaps and research justifications. Optimized for original
  research in chemistry, QSAR, cheminformatics, molecular modeling, medicinal
  chemistry, computational drug discovery, and scientific software, while
  transferable to other fields. Insists on reading primary literature, identifying
  what evidence cannot yet establish, and matching the study design and claims
  to the unresolved question.
triggers:
  - identify a research gap
  - establish scientific novelty
  - assess manuscript introduction
  - evaluate research justification
  - develop research questions or hypotheses
  - compare previous studies with proposed research
  - write or revise the final introduction paragraphs
  - critique computational drug discovery studies
language: English for scientific outputs; follow the user's language when discussing the work
status: Authorized reference skill, built from the staged 90-paper research-gap reading exercise
---

# RGap Skills — Evidence-Based Scientific Research Gap Discovery and Writing

## 1. Mission

Find **a defensible scientific problem**, not merely an unoccupied combination of methods. Read published original research critically; reconstruct how earlier findings lead to unresolved uncertainty; determine what new evidence is needed; and write a precise, publication-grade rationale that the proposed study can genuinely address.

**Core reasoning sequence:**

> Established evidence → precise unresolved question → why the uncertainty matters → plausible explanation or testable question → evidence-generating study design → proportionate contribution.

This is a *logic of justification*, not a mandatory five-sentence or five-paragraph writing template. Scientific prose must remain natural, concise, and specific to the literature. The method is learned from a staged discussion of 90 original papers across QSAR, cheminformatics, molecular generation, docking, ADMET, virtual screening, and experimentally anchored inhibitor discovery. The 90-paper discussion is a training context, **not** an independently verified systematic corpus, quality assessment, or license to cite every paper without rechecking it.

### Success criteria

A competent research-gap assessment can answer the following without hand-waving:

1. **Exactly what do earlier studies establish?** Refer to actual results, populations, assays, tasks, conditions, and limitations.
2. **What specific conclusion is not warranted by those results?** Explain why the available evidence is insufficient, inconsistent, confounded, restricted, or unsuitable for the intended decision.
3. **Why does the unresolved point matter?** Link it to biological interpretation, a scientific hypothesis, model validity, medicinal chemistry decisions, experimental feasibility, or translation.
4. **What will the proposed work discriminate, test, measure, or establish?** Give a testable question, meaningful comparison, or falsifiable expectation.
5. **Could the proposed methods actually answer the question?** Check data adequacy, relevant controls, validation level, and scope.
6. **What will remain unresolved even if the study succeeds?** Draw an evidence boundary around the conclusion.

If any answer is unsupported, **do not manufacture a novelty claim**. Label the point *hypothesized*, *needs verification*, or *not yet feasible*.

## 2. Non-negotiable rules

- **Primary-source first.** Read original research papers, not only abstracts, review summaries, search snippets, citation titles, or authors' promotional claims. Reviews help map a field but usually do not replace original evidence.
- **Full-text reading means full-text reading.** Before claiming to have read a paper completely, access and inspect its Introduction, Methods, Results, Discussion, figures/tables and stated limitations. Inspect supplementary methods/results when the key inference depends on them. Record when material is inaccessible. An abstract-only paper is not a full-text-read paper.
- **Separate author claims from independent appraisal.** Write, for example, “the authors claim X; their design directly establishes Y; Z remains untested.” Publication does not guarantee a strong or valid gap.
- **No novelty by absence alone.** “No QSAR model for target X,” “no docking + MD study,” and “no scaffold split” are descriptions of method coverage. They become defensible gaps only when connected to a consequential scientific question with adequate evidence and feasibility.
- **Do not use a missing method as the problem statement.** The problem may be assay-dependent measurements, nonadditive SAR, poor target engagement, unreliable predicted binding, conflicting experimental outcomes, uncertain selectivity, or an inappropriate benchmark. The method is a response.
- **No fabricated citations, quotes, statistics, negative results, datasets, DOI details, or novelty assertions.** Verify bibliographic metadata and read the cited section. Prefer exact original primary references that support the clause.
- **No premature “first,” “never,” or “no studies.”** Broad absence claims require a clearly scoped and up-to-date search. Prefer “existing studies have primarily focused on …, whereas … remains insufficiently resolved,” only if the cited set genuinely supports that contrast.
- **Do not force a strong gap.** A valid outcome is “the question has already been answered,” “evidence is too thin,” “data cannot support a reliable test,” or “the method combination is incremental.”
- **Proportion claims to validation.** A retrospective split does not prove prospective clinical value. A docking score does not establish binding affinity. MD does not prove allostery. A generated SMILES does not establish synthesis, potency, selectivity, target engagement, ADMET performance, or efficacy.
- **Do not mislabel the article type.** A critical narrative review does not become a systematic review without systematic search, eligibility, selection and synthesis methodology. The gap required for a review is an unanswered **synthesis or interpretation** question, not merely a missing review title.
- **Respect the user's authorization.** Do not create, edit, post, or submit manuscripts, evidence matrices, datasets, or derived artifacts beyond what was requested. Discuss and preview first when the user has reserved approval.

## 3. Definitions that must not be confused

| Concept | Meaning | Example | What it does **not** prove |
|---|---|---|---|
| Topic | Broad scientific area | HPSE1 inhibitor discovery | That a research gap exists |
| Underexplored target | Relatively few studies or ligands | Limited activity records for a kinase | That modeling is feasible or novel |
| Method gap | Technique or configuration not yet used | No published target-specific 3D-QSAR identified | That a meaningful biological question exists |
| Evidence gap | Existing studies cannot establish a needed conclusion | Potency measures differ between assays | That any proposed analysis can fix it |
| Mechanistic gap | An important causal or structural explanation remains uncertain | Binding-site water rearrangement may influence SAR | That docking/MD alone proves causation |
| Measurement gap | Available labels or methods cannot consistently measure the construct | Mixing biochemical IC50 and cellular EC50 | That standardized labels can be recovered |
| Evaluation gap | A benchmark cannot reliably answer the real task | In-domain test performance mistaken for unseen-scaffold performance | That a novel model is needed |
| Translational gap | Success in one evidence level has not been demonstrated at the next | Biochemical inhibition without cellular target engagement | That a computational study can validate therapeutic activity |
| Research question | The unresolved point framed to investigate | Does assay context account for potency disagreement? | A predetermined favorable answer |
| Hypothesis | A testable explanation or directional claim | Assay-specific terms will explain measurable between-study variance | That the hypothesis is already established |
| Objective | Work to be done | Quantify heterogeneity; evaluate held-out assays | Novelty by itself |
| Contribution | New, bounded result or insight | Estimates of transferability under defined conditions | Universal validity |

**Decision rule:** Prior to drafting the gap paragraph, write separate one-sentence versions of the *scientific problem*, *evidence limitation*, *consequence*, and *intended test*. If these sentences all merely list software or algorithms, return to the literature.

## 4. Classify the real form of the gap

The classification helps diagnose scientific reasoning; do not insert these labels mechanically into the manuscript.

| Gap mechanism | Question to investigate | Evidence required |
|---|---|---|
| **Unresolved explanation** | What causes the observed failure or relationship? | Prior observation; at least two plausible explanations; discriminating test |
| **Conflicting findings** | Why do studies disagree? | Comparable endpoints, assays, contexts and uncertainty analysis |
| **Untested field assumption** | Does a widely assumed relationship hold? | Evidence of actual use of the assumption; direct falsification test |
| **Limit of existing solution** | Under which conditions does an accepted solution fail? | Specific prior method, measured limitation, fair alternative |
| **Measurement/assay mismatch** | Is the signal comparable across experiments? | Assay metadata, endpoints, censoring, controls, replicate information |
| **Evaluation invalidity** | Is reported performance relevant to intended use? | Split protocol, leakage audit, representative data, application scenario |
| **Mathematical/representation mismatch** | What information is intrinsically lost or distorted? | Counterexample or formal argument; representational comparison |
| **Biological/mechanistic ambiguity** | Does an association reflect the intended target/process? | Orthogonal biochemical, cellular, genetic, structural or kinetic evidence |
| **Knowledge-to-decision mismatch** | Can current evidence support a medicinal chemistry choice? | Explicit decision, uncertainty, experimental consequence |
| **Practical/operational barrier** | What prevents the established method from being usable? | Reproducibility, accessibility, cost/compute, scale and meaningful tests |
| **Missing integration of complementary evidence** | Does combining modalities resolve a particular limitation? | Clear insufficiency of each source; ablations; controls for added complexity |
| **Translational disconnect** | Is a surrogate endpoint predictive of a downstream outcome? | Paired upstream/downstream data, comparability, uncertainty, controls |
| **Missing critical synthesis (review)** | What cross-study conclusion remains obscured? | Overlapping primary studies with inconsistent assumptions/findings, not just a vacant review title |

**Prefer:** gaps that establish a concrete failure, conflict, assumption, measurement issue, or decision bottleneck.

**Treat cautiously:** gaps whose only rationale is combining X + Y + Z, adding an algorithm, increasing dataset size, or targeting a “dark” protein. Those may be useful engineering work, but the contribution must be stated accurately.

## 5. Full-text reading protocol for EACH original paper

Do not read only to collect papers that agree with a preferred project. Seek disconfirming studies.

**Identity and access**

- Confirm title, authors, year, journal, DOI, version, correction/retraction status if relevant.
- Record source and access level: full HTML, PDF, full text plus supplementary files, or abstract only.
- If access is limited, label the limitation and exclude the paper from the fully read set.

**Introduction**

1. Record the specific problem or phenomenon used to open the argument.
2. Identify the *named prior studies* and what each actually contributed; capture their evidence rather than only their citations.
3. Find the precise contrast or tension: what is already possible versus what cannot yet be established.
4. Note how the author transitions: *However* is optional; the reasoning itself must establish the gap.
5. Rewrite the paper's gap in one neutral sentence, without copying its promotional language.
6. Record its research question, hypothesis, and stated intended contribution separately.

**Methods**

7. Identify dataset origins, units, endpoints, eligibility rules, exclusions, assay conditions, and preprocessing.
8. Identify controls, baselines, splits, external validation, ablations, statistics and any prospective experiments.
9. Ask what alternative explanation or source of bias the design fails to control.

**Results and figures/tables**

10. Locate the results that *directly test* the proposed gap; do not substitute headline accuracy.
11. Record negative, null, inconsistent, or sensitivity findings, including statistical uncertainty.
12. Distinguish observed facts from model-derived interpretations.

**Discussion and limitations**

13. Inspect whether the authors return to the original unresolved problem.
14. Note which parts were answered, partially answered, contradicted, or untouched.
15. Record their caveats, assumptions, applicability limits, and future directions; do not automatically convert a future-work sentence into our novelty claim.

**Reading record — minimum schema**

```text
Paper ID:
Full citation + verified DOI:
Full-text access status:
Scientific setting (target, endpoint, biological context):
Prior studies specifically contrasted:
Established observations, with exact evidence:
Gap claimed by the authors:
Independently reconstructed unresolved question:
Why it matters:
Competing explanation(s)/assumptions:
Methods capable of testing it:
Decisive result(s) and quantitative evidence:
Weaknesses, confounders, missing controls:
What was established:
What remains unresolved:
Transferable lesson for research-gap writing:
Citation/location within original article:
```

**Rule for completion:** A paper is not recorded as “fully read” unless its Introduction, Methods, Results, Discussion/Conclusion and decisive tables/figures have been inspected. If not, record the sections not seen. Reading several abstracts does not count as reading several full papers.

## 6. Build a literature evidence map BEFORE choosing a gap

For a candidate topic, create an evidence matrix with one row per distinct original study (not one row per citation in a review). Recommended columns:

| Study | Question / hypothesis | Data and conditions | Actual result | Claimed limitation | Independent limitation | Implication for proposed question | Confidence |
|---|---|---|---|---|---|---|---|
| [Verified source] | [Specific] | [N, assay, units, structures, model, context] | [Finding + uncertainty] | [Author's own] | [Your audit] | [Supported / contradicts / narrows] | [High / medium / low] |

Then build a **claim–evidence ledger**:

| Proposed manuscript claim | Supporting original study and result | Contrary or qualifying evidence | Claim strength | Action |
|---|---|---|---|---|
| “Potency is assay-dependent” | [Same-chemical, different-assay comparisons] | [Assays with consistent measurements] | Qualified | Specify which assays/conditions |
| “Scaffold generalization is unknown” | [Actual split protocol and scope] | [Independent scaffold test if one exists] | Conditional | Search latest evaluation papers |
| “No study has done X” | [Search strategy with coverage and dates] | [Any discovered contrary paper] | High-risk | Prefer narrower statement or remove |

### Search discipline

- Search target synonyms, biological nomenclature, alternate assay names, chemotypes, benchmark names, technique synonyms, patents and supplementary information where relevant.
- Search the **proposed research question**, not just the target name plus “QSAR.” Search for papers whose results could already answer the question using different terminology or methods.
- Include foundational studies and genuinely recent original studies; date-stamp the search.
- Use backward and forward citation tracing to find preceding evidence and direct successors.
- Examine relevant negative studies, benchmark criticisms, independent replications and contradictory findings.
- For absence/priority claims, document databases and search queries used and the date. Do not imply systematic coverage when the process was narrative.
- When the dataset is finite, perform an actual feasibility audit before proposing a modeling project: distinct structures, comparable endpoints, assay identity, censoring, chemical diversity, replicates, train/test constraints and paired data where needed.
- If source verification fails, say so. Never cite an abstract as if detailed results or supplementary validation were checked.

## 7. The research-gap reasoning engine

Apply these tests in order. If a test fails, return to the preceding evidence rather than repairing the prose cosmetically.

### Gate A — Established knowledge

State the strongest defensible version of what previous research has achieved. Give authors credit. Name results and relevant boundaries.

**Bad:** “Current QSAR approaches are inaccurate.”

**Better:** “Prior QSAR models predict potency within the chemical series and assay conditions represented in their evaluation; whether this carries across the particular assay or chemical change of interest is a separate question.”

The “better” sentence is an illustrative reasoning pattern, **not a factual assertion about any target** until verified.

### Gate B — Demonstrable unresolved uncertainty

Write the gap as **a missing inference**, not a missing action:

- “It remains uncertain whether X predicts Y under condition Z.”
- “The reported difference could reflect A or B; existing experiments do not distinguish them.”
- “Existing validation estimates in-domain performance, whereas the intended use requires performance on unseen C.”
- “The available assay labels do not isolate target-specific activity from D.”

Only use a formulation supported by the evidence map. Qualify scope (target, chemical series, assay, species, endpoint, time, population).

### Gate C — Scientific consequence

Ask: *If the uncertainty is not resolved, what interpretation or decision remains unreliable?*

Illustrative consequences include misranking molecules, conflating assay signal with target engagement, attributing potency to the wrong mechanism, falsely estimating an activity-cliff effect, overinterpreting docking, or allocating experimental resources to artifacts.

The consequence must be specific to the research, not just “drug discovery is costly” or “more accurate models are urgently needed.”

### Gate D — Discriminating question or hypothesis

Prefer questions able to distinguish at least two interpretations, define useful boundary conditions, or estimate a meaningful effect. Examples of **question forms**, not pre-established gaps:

- “To what extent does assay identity explain the between-study variation of matched-compound potency estimates?”
- “Does removing protocol-induced effects change the relative ranking of docking approaches?”
- “Can a structure-based hydration hypothesis explain experimentally observed substituent-specific potency changes?”
- “Do models identify genuine activity cliffs after controlling near-duplicate leakage and assay similarity?”

A question is weak if almost any set of positive model scores can be called a solution.

### Gate E — Study-design adequacy

Map each claim to a decisive test:

| Intended claim | Minimum meaningful evidence (examples, not universal mandates) |
|---|---|
| Predictive improvement | Relevant held-out evaluation; fair baselines; leakage control; confidence intervals; error analysis |
| Improved scaffold transfer | Unseen-scaffold partition with sufficient diverse scaffolds; multiple seeds; baseline and applicability analysis |
| Assay transferability | Multiple comparable assays; shared molecules or matched series; assay metadata; heterogeneity and error modeling |
| Novel target selectivity | Paired experiments for the target and counter-target(s); same chemical identity; relevant assays |
| Binding mechanism | Structural or kinetic evidence with discriminating controls; MD/docking are hypotheses unless validated |
| Biochemical-to-cellular translation | Matched biochemical/cellular data; target engagement, permeability and off-target confounders considered |
| Activity-cliff predictability | Leak-resistant split, explicit cliff definitions, assay/label quality, nearest-neighbor controls |
| Better drug-like lead | Evidence across potency, selectivity, exposure, developability and relevant cellular/experimental assays |
| De novo design effectiveness | Chemical validity and diversity **plus** suitable structure/activity validation; prospective synthesis/testing if biological claims are made |
| Scientific software utility | Working reproducible tool, verified outputs, meaningful scientific use cases, comparison to existing tools; do not infer novelty from UI alone |
| Narrative review contribution | New critical synthesis of unresolved interpretive questions, with cross-study evidence and clear boundaries |

If an intended claim lacks a credible test, **reduce the claim or redesign the study**. Never compensate with stronger rhetoric.

## 8. How to WRITE the gap in an Introduction

### Paragraph-level reasoning, not a rigid template

A compelling Introduction typically moves through these functions (the number and length of paragraphs vary by journal and study):

1. **Scientific setting:** Introduce the relevant biological, chemical, analytical, or computational problem with focused evidence.
2. **What has been accomplished:** Synthesize closely related original studies, including what their actual findings established. Avoid list-of-paper summaries.
3. **The precise unresolved issue:** Show the contradiction, limitation, untested assumption, information deficit, measurement weakness or evidence mismatch that remains *after* those successes.
4. **Why it matters:** Explain the scientific or decision consequence, not just the importance of the disease/field.
5. **Proposed question and response:** Describe what the present work tests, controls or compares, and why that design can produce missing evidence. End with a narrowly stated contribution; do not preview conclusions as proven before the study.

**Writing technique:** Every significant contrast must have identifiable references on both sides where possible. “Although” and “however” are transitions, not evidence. Prefer synthesis (“Studies consistently found X under A, whereas studies using B obtained Y”) over citation dumping (“A did X; B did Y; C did Z”).

### Publication-grade language rules

- Use exact scientific nouns: *assay-specific IC50*, *congeneric series*, *inter-assay heterogeneity*, *prospective inhibition*, *target engagement*, *unseen-scaffold evaluation*, *receptor conformational ensemble*.
- Make the claim as narrow as needed. State *where* and *for whom* a limitation applies.
- Attribute known findings accurately; separate observation from explanation.
- Avoid inflated adjectives (*groundbreaking*, *revolutionary*, *critical gap*, *unprecedented*) unless evidence supports the magnitude.
- Avoid recurrent teaching-language closers (“This study will significantly contribute to drug discovery”). State the actual scientific contribution instead.
- Avoid first-person plural when the manuscript style prefers impersonal construction: “This study evaluates…,” “The analysis tests…,” rather than repetitive “We…” sentences.
- Avoid repetitive back-to-back *However*, *Nevertheless*, *Furthermore* and one-sentence paragraphs.
- Use formal continuous prose; no tables, bullet points, meta commentary or “research gap” subheading in the manuscript unless the journal/author explicitly needs them.
- Maintain citation proximity: the reference must support the specific claim, not just the general paragraph topic.
- Do not end sentences or lines with decorative hyphens or dashes. Use clear punctuation.

### The “removal test”

Delete the sentence “No study has combined X and Y.” Does the rationale still make scientific sense? If not, the gap was likely built on method novelty rather than a scientific need.

### The “opposite-result test”

Would an unfavorable or null result still answer a scientific question? If **yes**, the question is likely well formed. If only increased accuracy, more predicted hits, or better docking scores count as success, the problem may be promotional rather than hypothesis-driven.

### The “scientific boundary test”

After reading the proposed final paragraph, ask which claim requires biochemical experiments, which requires cellular target engagement, and which is only supported in silico. Rewrite any sentence that silently crosses these levels.

## 9. Before-and-after EXAMPLES (illustrative; not claims about an actual target)

### Example A — QSAR modeling

**Weak gap:**

> Although many studies have used random forest, none has combined XGBoost with molecular dynamics for kinase X. Therefore, this study develops a novel computational pipeline.

**Evidence-dependent stronger logic:**

> Previous studies have established relationships between chemical structure and kinase X inhibition within the chemical series represented in their training data [verified primary citations]. Their evaluations, however, do not establish whether the inferred relationships persist across the specific assay conditions and chemical-series boundaries relevant to lead prioritization [verified methods and results]. Because changes in assay context can alter apparent potency, model predictions may conflate transferable SAR with assay-dependent variation. The proposed analysis therefore tests whether compound- and assay-level information explain variation in matched potency measurements and whether prediction errors remain stable in held-out chemical series and assays.

**Necessary caveat:** Do not use this example unless *paired assays, comparable endpoints and sufficiently diverse chemical series* actually exist. This wording is not a shortcut to a research gap.

### Example B — Structure-based drug design

**Weak gap:**

> Docking and MD have not been performed together on protein Y; thus, the first integrated study is presented.

**Evidence-dependent stronger logic:**

> Experimental analogue series show potency changes that are not explained by the contacts visible in the available static complex structures [specific compounds and original structural/biochemical results]. This leaves uncertain whether a defined hydration or conformational change contributes to the observed SAR. A structure-informed perturbation analysis, evaluated against available analogue potency and ideally new discriminating experiments, can test whether the proposed structural mechanism accounts for those differences.

**Boundary:** Docking plus MD may *generate or support a mechanistic hypothesis*; they do not independently prove causal ligand binding, potency or allosteric mechanism.

### Example C — Computational critical review

**Weak gap:**

> No comprehensive computational review has been published on protein Z.

**Evidence-dependent stronger logic:**

> Recent studies on protein Z have used differing receptor structures, protonation assumptions, biochemical endpoints and evaluation criteria [original studies]. These differences complicate comparison of predicted binding modes and the interpretation of reported inhibitor rankings. A critical narrative synthesis can therefore evaluate which conclusions remain robust across assumptions, where predictions diverge from experimental evidence, and which methodological decisions have the greatest consequence for future validation.

**Boundary:** The review cannot establish new biological causation merely by combining publications. A genuine review contribution needs an evidence-based critical synthesis, not a catalog of software.

## 10. Research-gap evaluation by study type

### QSAR / cheminformatics / ML

Check assay provenance, target identity, endpoint units and censoring, salts/stereochemistry/duplicates, chemical-series effects, cliffs, label errors, data leakage, retrospective versus prospective validation, variance across splits, applicability domain, model calibration, and whether evaluation reflects the intended use. A complicated model does not compensate for an incoherent dataset.

### Molecular docking / MD / free-energy modeling

Check receptor state, experimental structure support, protonation/tautomeric state, flexible loops, cofactors, water treatment, redocking controls, replicate simulations, convergence, energy-function limitations and orthogonal validation. Interpret contacts, docking scores and trajectories at the correct evidentiary level.

### Molecular generation / optimization

Ask whether design is driven by an accurate predictor, whether generated compounds leave its applicability domain, how reward hacking is controlled, and whether synthetic and biological constraints are independently validated. A large generated library is not itself a discovery.

### Target-specific drug discovery

Check whether enough experimentally characterized ligands exist, whether inhibitors are selective, whether assays distinguish desired mechanism, whether paired cellular outcomes exist, and what knowledge is actually missing. Lack of target-specific ML papers alone is not enough.

### Software / application notes

Contrast precise shortcomings of existing tools with scientifically meaningful functionality, reproducibility, validated output correctness, user accessibility and real scientific use. Claims of “first platform,” “user-friendly,” or “multipage” do not establish a scientific contribution without comparators and demonstrations.

### Critical narrative reviews

Identify a substantive interpretation problem crossing multiple studies: inconsistent results, conflicting hypotheses, overlooked evidence, unsupported translational inferences or incompatible measurements. Review authors must not describe a review as systematic/scoping unless they actually used and report the relevant methods.

## 11. How to evaluate the strength of an alleged research gap

Use these **six gates**, each assessed 0–3. This is an internal decision aid, not a validated bibliometric scale and not an automatic publication predictor.

| Dimension | 0 — Missing | 1 — Weak | 2 — Credible | 3 — Strong |
|---|---|---|---|---|
| Prior evidence | No original studies | General citations | Relevant originals summarized | Results, scope and limits triangulated |
| Unresolved question | Only missing method | Vague unknown | Specific unknown | Specific, discriminating, potentially falsifiable |
| Consequence | Generic importance | Speculative | Plausible and relevant | Directly affects interpretation/decision |
| Distinctness | Already answered | Minor variation | Narrow new evidence | New inference or resolution of meaningful contradiction |
| Feasibility | Data/controls absent | Major unverified assumptions | Test seems feasible | Data, comparisons and controls verified |
| Claim–evidence fit | Unsupported leap | Partial mismatch | Mostly aligned | Results can directly answer stated question |

**Operational judgment:**

- Any **0** in prior evidence, unresolved question, feasibility or claim–evidence fit is a **stop**: do not declare a defensible gap.
- Several **1s** indicate *provisional or incremental* contribution; investigate or narrow it.
- A 2 or 3 in every dimension supports developing a proposal, not claiming that novelty has already been established.
- Review editor/journal fit, quality of the proposed data and practical effort separately. Do not mistake this rubric for journal acceptance prediction.

## 12. Mandatory adversarial review (attempt to disprove the gap)

Before finalizing, answer these questions:

1. Which single existing study most threatens this novelty claim, and why?
2. Could the same scientific question have already been answered under a different term, endpoint or target family?
3. Are seemingly conflicting findings actually based on incomparable assays, populations or chemical classes?
4. Does the proposed hypothesis rely on an unverified dataset size, ligand structure, protein structure or paired activity measurement?
5. Is the claimed scientific insight indistinguishable from benchmarking one more algorithm?
6. Could the intended results emerge from label leakage, inappropriate splitting, assay artifacts or favorable selection of examples?
7. If the method succeeds in silico, what biological or chemical conclusion is still unproven?
8. If the method fails, would the finding still be informative, and does the design support that interpretation?
9. Is the supposed gap a generic limitation that almost every study in the field has, without a context-specific rationale?
10. Is the research contribution incremental, strong methodological, explanatory, experimental, or translational? Describe it without hype.

If these questions reveal a decisive counterexample or lack of feasible data, state that openly rather than rewriting the gap to conceal it.

## 13. Standard output modes

### MODE A — Learn how published authors construct gaps

Produce a paper-by-paper critical reading report:

1. Verified full citation and access status.
2. Established literature explicitly discussed in the Introduction.
3. Exact unresolved issue reconstructed in neutral prose.
4. Scientific consequence and question/hypothesis.
5. Methods/results that address it, including negative evidence.
6. Whether the authors **resolved**, **partly resolved**, or **did not resolve** their claimed gap.
7. One transferable writing principle and one caution.

Do not force each paper to earn a “strong” rating. Mark abstract-only papers honestly and do not count them as fully read.

### MODE B — Audit a proposed research topic

Return, in order:

- The precise candidate scientific question.
- What is already established (primary studies with results).
- Strongest evidence **against** its novelty.
- Remaining uncertainty, with carefully bounded scope.
- Why that uncertainty matters.
- Required data and feasibility audit.
- Testable design and decisive comparisons.
- Claim level that the design could legitimately support.
- Verdict: **defensible**, **promising but unverified**, **incremental**, **already addressed**, or **not currently feasible**.

Do not invent a title as a substitute for this audit. Offer a title only if requested or once the problem is justified.

### MODE C — Draft or revise manuscript Introduction

- Ask for and inspect the existing manuscript or research brief when available; do not invent earlier results or citations.
- Prepare a **claim–citation map** privately or as a separate audit if requested.
- Draft cohesive, journal-appropriate paragraphs that synthesize original evidence instead of enumerating software.
- Respect requested style, length and organization; if the user requests six paragraphs, use six meaningful paragraphs rather than six boilerplate functions.
- The final part should progress naturally from established evidence to a precisely scoped limitation, consequence, and direct objective/hypothesis.
- After drafting, perform the novelty, causal inference, study-design and citation audit.
- Distinguish a polished draft from factually verified literature claims; flag unresolved sources before the text is deemed submission-ready.

### MODE D — Critique a written gap

Provide:

- Exact problematic statement or paragraph location.
- Why its inference is unsupported, redundant, broad or untestable.
- The primary evidence needed to strengthen it.
- A revised version **only if requested**.
- Which parts of the original argument should be retained because they are well supported.

Avoid turning every critique into a redesign of the study. If the user asks for assessment only, give assessment only.

## 14. Examples anchored in published original papers

These **selected examples** are learning anchors. They are paraphrased summaries of how the scientific justification works, not passages to copy or universal claims that the gap remains open today. Bibliographic links below were checked against publisher pages when this skill was prepared.

| Original paper | What its Introduction makes problematic | How the study responds | Transferable lesson |
|---|---|---|---|
| Nelen et al. (2025), *Matched pairs demonstrate robustness against inter-assay variability* | Absolute cross-assay measurements differ; relative matched-pair consistency is assumed but needs quantification | Measures matched-pair agreement under different curation levels | Test an assumption already used in the field |
| Abe, Miyao & Bajorath (2026), *Accurate prediction of activity cliff compounds based on bioactivity profiles depends on assay nearest neighbor relationships* | Apparently high activity-cliff prediction performance may rely on leakage or closely related profile assays | Leak-controlled analysis, including failures and nearest-assay explanations | Negative outcomes and confound diagnosis can be valuable results |
| Wang et al. (2026), *Molecular embedding-based algorithm selection in protein-ligand docking* | Selection gains may reflect protocol-induced solver-rank changes rather than representation quality | Cross-benchmark, cross-protocol and ablation analysis | Distinguish competing explanations for a performance gain |
| Jeoung et al. (2026), *A novel approach for enhancing the potency of kinase inhibitors using topological water networks* | Existing hydration analysis leaves open how cooperative water information should guide ligand growth | Topological water network-guided fragment growth with synthesis and activity evidence | Build a new question naturally on earlier progress; follow it with relevant validation |
| Huber & Pollmann (2026), *Count your bits: fingerprint benchmarking to assess broad chemical space representation* | “Molecular similarity” varies with fingerprint, bit encoding and task | Broad fingerprint and similarity benchmark | Question the measurement, not only the predictive model |
| Onawole, Blaskovich & Zuegg (2026), *Framework for evaluating explainable AI in antimicrobial drug discovery* | Plausible explanations are not necessarily faithful or chemically useful | Cross-model XAI evaluation against chemically meaningful criteria | Differentiate prediction accuracy from explanation validity |
| Yap et al. (2026), *ScrambleBench* | Inconsistent generative-model metrics obscure practical comparison | Shared tests of diversity, pose realism and hit generation; identifies remaining evaluation limitations | Benchmark claims must be task-relevant and acknowledge their own blind spots |
| Truong et al. (2026), *Enhancing virtual screening of cystathionine β-synthase inhibitors* | Understudied CBS lacks a strong target-specific screening comparison | Curates data and benchmarks target-specific models versus multiple existing approaches | Combine the biological need with a direct, measurable methodological question; audit assumed negatives |
| Song et al. (2025), *Cycle-configuration descriptors* | Existing graph descriptors fail on explicit non-isomorphic structural cases | Introduces descriptors that represent previously indistinguishable configurations | A counterexample can establish a mathematical gap precisely |
| Zavadskaya et al. (2025), *Integrating QSAR modelling with reinforcement learning for Syk inhibitor discovery* | New structurally distinct Syk candidates are sought despite known inhibitors | Generates candidates with predicted properties | Contrast computational candidate generation with unproven therapeutic claims |

### Verified reading-anchor references

1. Nelen, J., et al. (2025). *Matched pairs demonstrate robustness against inter-assay variability*. **Journal of Cheminformatics**. https://doi.org/10.1186/s13321-025-00956-y
2. Abe, R., Miyao, T., & Bajorath, J. (2026). *Accurate prediction of activity cliff compounds based on bioactivity profiles depends on assay nearest neighbor relationships*. **Journal of Cheminformatics**. https://doi.org/10.1186/s13321-026-01210-9
3. Wang, J. B., et al. (2026). *Molecular embedding-based algorithm selection in protein-ligand docking*. **Journal of Cheminformatics**. https://doi.org/10.1186/s13321-026-01168-8
4. Jeoung, R. G., et al. (2026). *A novel approach for enhancing the potency of kinase inhibitors using topological water networks*. **Journal of Cheminformatics**. https://doi.org/10.1186/s13321-026-01188-4
5. Huber, F., & Pollmann, J. (2026). *Count your bits: fingerprint benchmarking to assess broad chemical space representation*. **Journal of Cheminformatics**. https://doi.org/10.1186/s13321-026-01245-y
6. Onawole, A. T., Blaskovich, M. A. T., & Zuegg, J. (2026). *Framework for evaluating explainable AI in antimicrobial drug discovery*. **Journal of Cheminformatics**. https://doi.org/10.1186/s13321-026-01200-x
7. Yap, V., et al. (2026). *ScrambleBench: a workflow for comparative assessment of structure-based de novo generative models*. **Journal of Cheminformatics**. https://doi.org/10.1186/s13321-026-01254-x
8. Truong, C.-M., et al. (2026). *Enhancing virtual screening of cystathionine β-synthase inhibitors: benchmarking target-specific machine-learning scoring functions against state-of-the-art AI docking and co-folding approaches*. **Journal of Cheminformatics**. https://doi.org/10.1186/s13321-026-01262-x
9. Song, B., et al. (2025). *Cycle-configuration descriptors: a novel graph-theoretic approach to enhancing molecular inference*. **Journal of Cheminformatics**. https://doi.org/10.1186/s13321-025-01042-z
10. Zavadskaya, M., et al. (2025). *Integrating QSAR modelling with reinforcement learning for Syk inhibitor discovery*. **Journal of Cheminformatics**. https://doi.org/10.1186/s13321-025-00998-2

These references illustrate different styles of scientific justification. They are not the reference list for a user's new manuscript unless they are topically relevant to its actual claims.

## 15. Final mandatory quality-control checklist

Before presenting research-gap writing as ready to use, verify:

- [ ] All cited studies are real, relevant, and bibliographically correct.
- [ ] Full-text access limitations are identified honestly.
- [ ] The strongest previous achievements are acknowledged accurately.
- [ ] The stated gap is a specific **inference, conflict, assumption, measurement or decision problem**.
- [ ] Contradictory and newer relevant studies were searched, not screened out for convenience.
- [ ] The gap is not simply a new target-method combination.
- [ ] Why the unresolved point matters is concrete and not generic disease burden.
- [ ] The study question is answerable, potentially falsifiable, or capable of resolving a meaningful comparison.
- [ ] Experimental/computational data, baselines and validation are sufficient for the question.
- [ ] No claims exceed the level of evidence supplied by Methods and Results.
- [ ] Causal and mechanistic language is reserved for evidence that warrants it.
- [ ] Citations support their immediately adjacent claims.
- [ ] The text reads as natural scientific prose rather than a checklist or methods catalog.
- [ ] No “first,” “none,” “never” or “underexplored” claim is made without checking its scope.
- [ ] The uncertainty and contribution have been stated at the appropriate level of confidence.
- [ ] The text follows the user's requested length, journal conventions, authorial voice and approval boundaries.

## 16. Operational instruction to the AI using this skill

When the user asks to identify a gap, **do not immediately supply research titles**. First reconstruct what is known from verified original papers, identify the strongest unresolved question and perform the adversarial/feasibility tests. If source coverage is limited, report a *candidate* gap with what must be checked. Do not mistake a high model score, a new application of software, an underexplored target, or a “no one has done this” search result for scientific novelty.

When the user asks how established authors write gaps, **read full original papers and analyze their actual reasoning**, including how the Methods/Results answer (or fail to answer) the gap. Preserve negative results and weak examples as learning material; published papers vary in gap-writing quality.

When the user asks for manuscript prose, produce concise, publication-grade, citation-supported paragraphs with a defensible claim–evidence chain. If the proposed study cannot resolve the advertised problem, say so and narrow the claim **before** writing persuasive prose.

**Final governing principle:**

> A genuine research gap is the specific conclusion that existing evidence cannot yet justify, together with a scientific reason why that missing conclusion matters and a feasible plan to obtain the evidence needed to test it.

---

## 17. Case study: Mtulo et al. — statin-analog Introduction and gap–question alignment

**Source read:** Mtulo, Y. B., et al., *Computational Evaluation of Statin Analogs Targeting HMG-CoA Reductase for Coronary Artery Disease Treatment*, *ChemistryOpen*, 15, e202500533, DOI: 10.1002/open.202500533. Case-study observations refer specifically to its Introduction (PDF pp. 1–2); the Methods/Results are used only to check whether the proposed response matches the claim.

### 17.1 Reconstruct the authors' argument before judging it

The Introduction progresses from (1) cardiovascular disease burden, (2) coronary artery disease and its consequences, (3) prevention and pharmacological limitations, (4) statins, HMG-CoA reductase and limitations, (5) a claimed distinction between previously modified statin derivatives and structurally distinct analogs, to (6) ADMET, docking, MD and free-energy landscape (FEL) analysis as the proposed study. This is an **observed architecture**, not a six-paragraph template that must be reproduced in other manuscripts.

The paper's *claimed* gap is that the potential of structurally distinct statin analogs has been relatively overlooked compared with minor structural modifications. The authors suggest that analogs preserving a relevant pharmacophore while changing peripheral substituents could have different stability and therapeutic profiles. The proposed work investigates selected compounds and their predicted binding/dynamical behavior.

### 17.2 What the example teaches — and what it does not prove

**Transferable strength:** The authors seek a *chemical distinction and scientific consequence* rather than relying entirely on an allegedly missing software method. They connect molecule class, a target/mechanism, and a potential property of interest. The methods then appear as instruments of investigation, not the sole source of the research gap.

**Evidentiary limitation:** The Introduction does not substantiate the scope of the “largely overlooked” claim through a close comparison of named, directly relevant original investigations. Publication of a novelty claim does not make the claim independently verified. Before borrowing this reasoning, establish which analog classes, structures, assays, and prior studies actually exist; avoid assuming that “derivatives” and “analogs” are mutually exclusive scientific categories without an operational chemical definition.

**Alignment limitation:** The identified literature gap concerns analog exploration and potential improvement of therapeutic properties, whereas the final objective places particular weight on enzyme conformational stabilization and mechanistic insight. The bridge between these requires an explicit, testable question, such as whether the selected substitutions are associated with distinguishable binding modes or dynamics *under an appropriate comparator design*. Merely producing additional docking and MD outputs does not settle efficacy, safety, or clinical benefit.

**Claim-boundary lesson:** Docking scores, RMSD/RMSF changes, hydrogen-bond persistence and FEL basins can describe modeled interactions and conformational sampling under the simulation conditions. Alone, they cannot establish superior inhibitory potency, mechanism of inhibition, physiological target engagement, or therapeutic effectiveness. Stronger claims require suitable controls and orthogonal biochemical/experimental evidence. A lower protein RMSD is **not** a universal proxy for better inhibition.

### 17.3 Mandatory 'gap-to-answer bridge' before drafting the final Introduction paragraph

For each proposed study, write one precise answer to each question:

1. **What exactly did previous original studies establish?** Identify the study, chemical series, biological system, comparator, measured endpoint, and limitations relevant to the new question.
2. **Which specific inference is still unsupported?** Describe the missing comparison, unexplained difference, inconsistent outcome, uncertain transferability, or inadequately tested mechanism; not just “few studies.”
3. **Why is this uncertainty consequential?** State what prediction, design decision, interpretation, or biological explanation cannot currently be made reliably.
4. **Which planned measurement would discriminate between competing explanations?** Explicitly link each method to an answerable question and a baseline/control.
5. **What claim can the resulting evidence actually support?** Distinguish computational structural behavior, experimental activity, selectivity, safety, and therapeutic efficacy.

Reject or narrow the candidate gap when the answer to (4) cannot resolve (2), or when the intended conclusion in (5) exceeds what the design measures.

### 17.4 Concrete writing guardrails learned from the case

- Do not treat **disease burden** as a substitute for the *target-level scientific question*. It supplies context but not the unresolved mechanism, comparison, or evidence limitation.
- Do not treat a **plausible chemical distinction** as proof of a literature gap. Verify and define the distinction against the published compounds and experiments.
- Do not import **“underexplored,” “largely overlooked,” or “novel”** without showing the relevant prior evidence and search limits.
- Do not mistake **many analytical stages** for a stronger scientific argument; the pivotal question must remain visible even if the method list is deleted.
- Do not confuse **stability of the modeled complex** with potency or clinical efficacy; different endpoints support different statements.
- Do not force this paper's paragraph count or sequence onto unrelated research topics. Transfer its useful *argument function*, while correcting the weaknesses identified above.

### 17.5 Decision test illustrated by the case

**Weak justification:** “No study has combined ADMET, blind docking, 200 ns MD and FEL for these statin analogs.”

**Better *candidate* scientific framing (not a verified novelty claim):** “For a defined set of statin-related chemical series, it remains to be established whether specific peripheral modifications alter the modeled binding modes and conformational dynamics of HMG-CoA reductase relative to appropriate reference compounds.” This statement must still be checked against the real literature and matched to a design that can make the comparison.

**Key lesson for the skill:** Published Introductions are training examples, not authorities on their own novelty. Extract their chain of justification, test the weakest link, and enforce precise alignment among **literature evidence → unresolved question → comparison/measurement → warranted conclusion**.