---
name: scientific-introduction-writing
version: 2.0.0
status: evidence-expanded-training-guide
purpose: Evidence-grounded drafting and auditing of scientific manuscript introductions
---

# Scientific Introduction Writing Skill

## 1. Mission
Write an Introduction that constructs a defensible scientific argument from established knowledge to a precise unresolved question and a justified study objective. Do not merely summarize background or list papers. This is a reusable writing instruction file, not a model-weight update.

## 2. Training provenance and limits
Foundational exemplars:
- Xie et al. (2026), *npj Science of Food*, DOI: 10.1038/s41538-026-00731-9. Original foodomics research: functional food context -> tatsoi chemistry -> integrated analytical approaches -> growth-stage gap -> study scope.
- Jasna et al. (2026), *Molecular Biology Reports*, DOI: 10.1007/s11033-026-12727-5. Rheumatoid arthritis review: pathogenesis and therapeutic limitations -> herbal multi-target complexity -> network pharmacology -> review scope. Its extended search-method description in the Introduction is not a universal model.

Expanded with ten open-access Q1 original-research introductions, including eight from Nature Communications (2024–2025) and two from Bioinformatics (2025). Full introductions were read and compared for paragraph progression, literature synthesis, citation function, specific gaps, and weaknesses. See companion file `STAGE3_TEN_Q1_INTRODUCTIONS_AUDIT.md` for the DOI list and analysis. These are structural exemplars, not proof of universal best practice. Underlying cited references have not all been independently checked. The guide must be tested on a real manuscript.

Additional general guidance: Springer Nature's manuscript-writing guidance stresses relevant, balanced literature, clear questions and aims, and concise background. See https://www.springernature.com/la/authors/campaigns/writing-a-manuscript/introduction-methods-materials and https://link.springer.com/article/10.1007/s40828-022-00160-7 . Target-journal instructions take precedence.

## 3. Required inputs before drafting
Collect manuscript type, title/research question, target journal if known, verified key findings and methods, existing introduction, source literature or reference library, and author constraints. If evidence is absent, label it as missing; do not invent citations, datasets, prior-study findings, or novelty.

## 4. Core reasoning sequence (not a mandatory paragraph template)
1. Identify the exact scientific problem and why it matters to the intended readership.
2. State the relevant established evidence, with appropriate citations.
3. Synthesize previous studies by agreement, contrast, scope, methods, or evidence quality rather than presenting an annotated bibliography.
4. Specify what remains unresolved and show how that conclusion follows from the cited evidence.
5. Explain the consequence of the uncertainty and why the present study design can address it.
6. End with a precise aim/question and a short, accurate description of the approach where appropriate.

Paragraph count and order are flexible. For this author's usual manuscripts, start with six coherent paragraphs unless the target journal or research argument requires a different structure. Never pad to reach a count.

## 5. Paragraph and sentence-level rules
- Give each paragraph one distinct argumentative job and a clear connection to the previous paragraph.
- For each sentence ask: What new evidence, distinction, inference, or transition does this add?
- Remove textbook definitions and tangential facts unless needed for the research question.
- Use 'however', 'therefore', 'although', and 'consequently' only when the claimed logical relationship holds.
- Avoid repeating 'important', 'promising', 'powerful', 'novel', or 'further studies are needed' without specific justification.
- Do not place a broad health or therapeutic claim after a computational result without qualifying the level of evidence.
- Avoid first-person plural (we/our/us) and defensive or self-congratulatory language.
- Avoid dangling hyphens/dashes and end-of-line word hyphenation in final layout.
- Prefer precise scientific nouns and verbs over promotional adjectives.

## 6. Citation integrity
- Every nontrivial factual, mechanistic, numerical, historical, or previous-study claim must have appropriate support.
- Cite the original study when discussing its actual findings; use reviews for synthesis and context where suitable.
- Never fabricate DOI, author, year, study outcome, or citation number.
- Distinguish verified source claims, reasonable interpretation, and hypotheses.
- Check whether a cited paper actually supports the adjacent clause, not merely the paragraph topic.
- Represent conflicting findings fairly; do not selectively cite only supporting studies.
- If source PDFs are supplied, read relevant sections and inspect tables/figures where needed before asserting details.
- If sources are missing, insert [SOURCE REQUIRED] in a working draft rather than inventing references.

## 7. Research-gap test
A gap must specify: (a) known evidence, (b) precise missing knowledge or unresolved contradiction, (c) why it matters, and (d) how the present study addresses it. 'Few studies exist', 'no study has used method X', or 'to the best of our knowledge' alone are insufficient. A new combination of methods is not automatically scientific novelty.

## 8. Manuscript-type adaptation
### Original experimental research
Prioritize measured phenomena, experimental context, unresolved mechanism/comparison, and testable aim.
### QSAR / cheminformatics / molecular modeling
Specify endpoint provenance, chemical domain, assay heterogeneity, validation strategy, and the precise predictive or mechanistic uncertainty relevant to the actual study. Do not present docking scores as binding affinities or computational predictions as biological proof.
### Critical narrative review
Establish the contested scientific question, major evidence streams, tensions and limitations, and the evaluative scope. Do not impose PRISMA, systematic-review screening, or a search-flow diagram unless the manuscript truly uses that design.

## 9. Drafting workflow
A. Read the full supplied manuscript context and target-journal instructions.
B. Build an evidence map: claim | supporting source | evidence type | uncertainty | intended paragraph.
C. Create a one-sentence argument map for each proposed paragraph.
D. Draft continuous prose with citations only where supported.
E. Perform sentence-by-sentence dependency and redundancy review.
F. Check gap-to-objective alignment and ensure methods/claims reflect work actually done.
G. Audit citations against the source literature.
H. Read the Introduction aloud for coherence, concision and scientific tone.
I. Present the draft with an audit of unresolved evidence issues, not invented certainty.

## 10. Quality-control rubric (100 points)
- Scientific problem and relevance: 15
- Accuracy and depth of evidence synthesis: 20
- Logical paragraph/sentence progression: 15
- Specificity and defensibility of gap: 20
- Alignment of rationale, methods and aims: 15
- Citation integrity: 10
- Concision and journal-appropriate language: 5

Score each dimension only after source checking. A numerical score is a revision aid, not an objective publication probability. Any fabricated citation, invented finding, or materially unsupported novelty claim is an automatic fail regardless of score.

## 11. Red flags and repairs
- Generic opening -> start closer to the actual scientific problem.
- Study-by-study list -> compare what the studies jointly establish and fail to establish.
- Unexplained methodological enthusiasm -> state capabilities and limits.
- Repeated motivation -> assign one distinct role per paragraph.
- Unsupported 'first study' -> replace with a verifiable, bounded gap.
- Abstract-like final paragraph -> end with the question/aim and approach, not a results inventory.
- Overlong search procedure in narrative-review Introduction -> place methods detail where journal conventions require it.

## 12. Output contract
Deliver: (1) a clean Introduction; (2) an evidence/citation audit; (3) a short rationale for the argument structure; (4) clearly flagged claims requiring verification. Do not call a draft publication-ready without a source-level and target-journal audit.

## 13. Future training log
Version 1 is based on two exemplars and general publisher guidance. Next: evaluate 5–10 stronger field-specific introductions; compare their argument patterns; revise rules based on evidence; blind-test on an existing manuscript; record author feedback and version changes.


## 14. Evidence from ten additional Q1 introductions (Version 2)

### Recurrent successful moves
- **Identify the second-order bottleneck.** More screening throughput is insufficient without ligand-ranking accuracy (Zhou et al., 2024); strong in-domain predictive performance is insufficient under domain shift (Chen & Li, 2025).
- **Synthesize by methodological assumptions.** Compare tokens and molecular graphs (Token-Mol), sequence-only versus structure-only inputs (UAMRL), or graph-augmentation operations (MolFCL). Never write a catalogue merely showing that several models exist.
- **Make research questions discriminative.** State what new comparison, perturbation, assay or benchmark would *differentiate between competing explanations or approaches* (Luttens et al.; Thomas et al.).
- **Define endpoints and evidence levels.** DTI presence, DTA regression, activation/inhibition, IC50, Ki, Kd, molecular generation, and measured cellular phenotypes are different targets of inference (DTIAM; DeepDTAGen). Do not collapse them into one claim.
- **Prioritize chemical utility.** Chemical novelty and experimentally supported activity can be more important scientific contributions than an incremental ML benchmark (Xie et al., 2025).
- **Link method to measurable validation.** Whenever experimental testing is absent, explicitly describe the limits of computational evidence; do not imply a physical binding or drug efficacy claim is confirmed.

### New mandatory argument map
Before drafting, create a 6-column private planning table (or a visible audit when requested): `claim | primary citation and DOI | evidence type | unresolved issue | how current study tests it | paragraph role`. Every major Introduction claim must be supported, bounded or marked `[SOURCE REQUIRED]`.

### Scientific test for gap statements
For each proposed gap, answer:
1. Which prior papers actually studied the question and in what chemical/protein/assay domain?
2. What is known versus merely predicted?
3. What exactly fails or remains uncertain: endpoint consistency, representation chemistry, selectivity, extrapolation, docking physics, or biological validation?
4. What observation in the present study could change the answer?
5. Is the novelty due to scientific knowledge, rigorous evaluation, new data or genuinely enabling method, rather than combining familiar tools?

### Required methodological-claim distinctions
- IC50 is an assay-dependent potency metric, not a universal equilibrium binding affinity. Ki and Kd must also be distinguished.
- A predicted docking pose, docking score, conformational stability, and estimated free energy answer different questions.
- A target predicted by network pharmacology is not an experimentally verified mechanism of action.
- Random-split predictive accuracy, scaffold-split generalization, external validation and prospective experimental validation are distinct evidence levels.
- A medicinal chemistry hypothesis, pharmacophore match, generated structure and biological hit are distinct outputs.

### Avoid patterns visible even in highly ranked journals
- Generic 'AI is transforming drug discovery' openings without immediate domain relevance.
- Extensive paragraph-length lists of algorithm names without a comparison criterion.
- Unsupported statements of model superiority across targets or experimental contexts.
- Vague phrases such as 'for the first time', 'powerful', 'robust' and 'revolutionary' unsupported by bounded comparison.
- Multiple final-Introduction paragraphs reproducing results and performance numbers.
- Using journal status as proof a sentence or citation is scientifically sound.

## 15. Version 2 operational workflow
1. Extract the existing manuscript's actual question, endpoints, dataset, methods, validation and findings. Do not change the scope without permission.
2. Read sufficient original references to support the claim-to-gap path. Separate primary evidence from reviews.
3. Build the evidence matrix described in Section 14.
4. Choose the strongest argument sequence; do not enforce a universal paragraph count. Accommodate the author's usual six-paragraph preference when the sequence supports it.
5. Draft without first-person plural or promotional/defensive language, and with no dangling hyphens.
6. Audit sentence-to-sentence dependency: each sentence must add new evidence, qualification, comparison, inference or necessary transition.
7. Check whether the final stated aim is answerable by the studies actually performed. Avoid prospective promises when only retrospective data exist.
8. Perform a source-level citation check, not just counting citations. Explicitly flag references not individually opened.
9. Apply the existing 100-point rubric and note any automatic failures.
10. For revisions, preserve the author's verified results and chosen thesis; present the revised text and a brief factual change log.

**Provenance:** Stage 3 companion audit: `STAGE3_TEN_Q1_INTRODUCTIONS_AUDIT.md`. Paper list and article links in that file. Version 2 describes observed patterns, not a model weight update or a guarantee of publication acceptance.