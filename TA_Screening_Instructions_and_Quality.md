# Title-and-Abstract Screening: Instructions and Quality Assurance

**Document type:** Operational standard operating procedure (SOP) and quality-control checklist  
**Project:** *Drug Repurposing for BRD4: A Scoping Review of Screening Strategies and Experimental Evidence*  
**Version:** 1.0 | **Prepared:** 5 November 2026 | **Status:** Proposed for author-team approval; not a record of completed human screening

## 1. Purpose and boundary of title-and-abstract screening

The purpose of title-and-abstract (T&A) screening is to decide **whether a record should progress to full-text eligibility assessment** using prespecified criteria. It is **not** final study inclusion, quality appraisal, extraction of potency values, or validation of a pharmacological mechanism.

The fundamental asymmetry is:

- **YES / Retain:** The title or abstract provides a plausible basis for eligibility.
- **MAYBE / Retain:** Eligibility cannot be reliably established *or ruled out* from the available title, abstract, and permitted bibliographic metadata. A missing fact is not evidence of ineligibility.
- **NO / Exclude:** The available information **affirmatively demonstrates** that a prespecified exclusion rule applies, or that an essential inclusion criterion is not met. Record a precise, supportable reason.

Both **YES** and **MAYBE** proceed to full-text assessment. The operative goal is **high sensitivity without indiscriminate retention**: avoid false exclusions while excluding records that are demonstrably outside scope.

## 2. Review-specific question, concept, and units of analysis

**Core question:** What evidence has been reported for compounds investigated through BRD4-directed drug-repurposing strategies, from candidate identification to biochemical characterization, cellular evaluation, and translational investigation?

**Relevant concept:** A compound previously characterized for a non-BRD4 pharmacological or biological purpose, subsequently investigated for BRD4/BET activity. The review maps strategies and reported evidence, including computational-only studies. A previously marketed or FDA-approved status is **not required**; however, prior identity, purpose, and evidence should ultimately be verifiable.

Distinguish the following:

1. **Molecular-target repurposing:** Prior non-BRD4 pharmacology -> BRD4/BET interrogation. Potentially eligible.
2. **Disease-indication repurposing:** A compound *already developed as a BET/BRD4 inhibitor* applied to a new disease. **Not sufficient by itself**.
3. **De novo BRD4 discovery/optimization:** Molecules created or optimized for BRD4 without previous independent pharmacological characterization. Outside the central repurposing scope.
4. **Linked follow-up:** A subsequent experiment on the same repurposed compound can contribute evidence, even when it is not a new discovery campaign; retain when it plausibly reports relevant BRD4 evidence, then link publications at full text.

Use separate levels of counting: **retrieved record**, **publication/report**, **unique compound**, and **discovery campaign**. They are not interchangeable.

## 3. Prespecified T&A eligibility guidance (proposed)

### Potential inclusion at T&A

Retain when the record plausibly reports:

- Identification or testing of previously characterized drugs, pharmacologically active compounds, or repurposing libraries against BRD4 or BET proteins, provided BRD4 relevance is plausible.
- Computational, pharmacophore, docking, ML, biochemical, biophysical, structural, cellular, in-vivo, or clinical investigation **connected to BRD4-directed repurposing**. Do **not** require wet-lab validation at this stage.
- Evidence on a relevant compound following its initial BRD4 discovery, including mechanistic or translational follow-up.
- A BET-family screen where the abstract does not specify the individual BET protein tested, provided BRD4 involvement remains plausible.
- Conference abstracts, preprints, or nonstandard reports with potentially relevant original evidence; verify source status and overlap later.

### Defensible exclusion at T&A

Exclude **only when clear from title/abstract**:

- Exclusively novel compounds synthesized/developed as BRD4 inhibitors, with no plausible pre-existing independent pharmacological context.
- A known BET/BRD4 inhibitor used for a new disease, **without any newly investigated non-BRD4-to-BRD4 repurposing relationship or relevant linked evidence**.
- BRD4 is mentioned solely as a downstream expression marker, pathway association, or generic network target, without credible direct BRD4/BET candidate investigation.
- Research exclusively about another target with no plausible BRD4/BET relevance.
- Clearly non-primary publications (e.g., a review, editorial, news item) **if the protocol excludes them as included evidence**; tag useful reviews separately for reference chasing.
- Clearly irrelevant materials that do not address compounds or BRD4/BET-directed screening/activity.

Do **not** exclude merely because the abstract lacks: an FDA-approval claim, IC50, clinical outcomes, target engagement, prior-use details, a specific domain name (BD1/BD2), or experimental validation.

**Borderline classes needing a fixed protocol rule, not case-by-case intuition:** dietary phytochemicals, endogenous metabolites, natural products, excipients/solvents, partial BET-family-only reports, PROTAC/degrader studies, and non-drug screening libraries. Record as MAYBE pending eligibility-rule resolution when uncertainty could change inclusion.

## 4. Decision algorithm: apply to each record

1. **Identity check:** Read the complete title and abstract, publication type, and source identifiers. Do not infer from the title alone when an abstract exists.
2. **Topic check:** Is BRD4/BET investigation at least plausible? If explicitly absent or unrelated, NO; if unclear, MAYBE.
3. **Repurposing check:** Is there a previously characterized compound, prior non-BRD4 activity, or a library plausibly containing such compounds? Clear YES if supported; MAYBE when unspecified; NO only if exclusively novel BRD4-directed development is explicit.
4. **Evidence check:** Are computational-only studies included? **Yes.** Do not equate a docking score with experimentally verified inhibition.
5. **Report-type check:** Is this original evidence, possible follow-up, review for citation chasing, conference abstract, or linked preprint? Record its type. Do not double-count versions.
6. **Decision:** Choose exactly one of `YES`, `MAYBE`, `NO`.
7. **Reason:** For NO, cite the **specific criterion and title/abstract evidence**. For MAYBE, state the **missing information to verify at full text**. For YES, state the inclusion signal without overstating results.
8. **Link flag (independent field):** `possible_follow_up`, `possible_preprint_version`, `conference_to_article_link`, or blank. **Never use “linked follow-up” as a fourth T&A eligibility decision.**

### Worked examples

| Abstract signal | T&A decision | Basis |
|---|---|---|
| Existing antibiotic newly evaluated for BRD4/BET activity | YES | Clear target-directed repurposing signal |
| Previously developed kinase inhibitors tested against BET bromodomains | YES | Prior non-BET pharmacology plus BET testing |
| BRD4 virtual screening of a library with unspecified provenance | MAYBE | Prior pharmacological characterization is not resolved |
| Drug-library BRD4 screen with no wet-lab assays | YES/MAYBE | Computational-only evidence is permitted; provenance determines confidence |
| Explicitly designed and synthesized new BRD4 inhibitors only | NO | De novo discovery rather than repurposing |
| JQ1 administered for a different disease with no new repurposing discovery | NO | Known BET inhibitor repurposed by indication only |
| BET-family binding with specific BET paralog unspecified | MAYBE | Verify BRD4-specific or family-wide results |
| Direct BRD2-only study, explicit absence of BRD4 experiments | NO or MAYBE per *pre-agreed* BET-family inclusion boundary | Avoid silently changing the scope |
| No abstract, ambiguous title | MAYBE | Missing information is not an exclusion criterion |
| Published nitroxoline follow-up reporting BRD4-linked evidence | YES with follow-up flag | Retain publication; link to discovery campaign later |

## 5. Pilot calibration and human reviewer independence

1. Freeze a versioned master dataset and eligibility guide before pilot screening.
2. Draw a **reproducible random pilot sample**; JBI describes a framework using 25 records, all reviewers working independently, discussion of discrepancies, revision of guidance, and at least **75% agreement** before routine screening. A 100-record pilot is permissible as a project decision; use a recorded random seed and sampling frame.
3. Each **actual human reviewer** makes an independent decision without seeing other reviewers' votes.
4. Compare decisions only after independent completion; discuss divergences and ambiguous rules; document any protocol amendment and date.
5. Repeat calibration if decisions reveal major misunderstanding or inadequate agreement. Agreement alone is not proof of high-quality screening, particularly with highly imbalanced exclusions.
6. Define who screens each record and how conflicts are resolved **before screening**. Prefer two independent human reviewers per record and a third human adjudicator or consensus discussion; JBI describes other options when duplicate screening is not feasible, which must be prespecified and transparently reported.
7. **AI outputs are AI-assisted triage, not independent human-author votes**. Multiple prompts/passes by one model are correlated and must not be represented as separate human screeners or used to claim human inter-rater reliability.

**Project status warning:** The earlier AI triage of 1,445 BRD4 records and AI pilot assessments are **not** finalized three-author screening or consensus. They can guide audit and prioritization but must not be silently promoted into final PRISMA counts.

## 6. Minimum screening ledger (one row per deduplicated record)

Required fields:

```text
master_id
record_title
abstract_text
abstract_availability
doi
pmid
source_databases
publication_type
record_version
protocol_version
reviewer_id
reviewer_type                  # human or AI
screening_pass_id
screening_date
screening_decision             # YES | MAYBE | NO
criterion_code
criterion_specific_reason
supporting_title_abstract_text
uncertainty_to_verify
linked_report_flag
potential_campaign_or_compound_link
human_consensus_decision      # blank until actual decision
consensus_rationale            # blank until actual decision
full_text_retrieval_status
```

Store **individual votes separately** from the final consensus field. Preserve a read-only source dataset, transformations, and version history. Do not overwrite one reviewer's decision with another's.

### Suggested reason codes

- `E01`: Clearly unrelated to BRD4/BET-directed drug investigation.
- `E02`: Explicitly de novo BRD4 inhibitor design without prior non-BRD4 pharmacological context.
- `E03`: Known BRD4/BET inhibitor used for another indication only.
- `E04`: BRD4 is a downstream marker/network mention only, not a directed target study.
- `E05`: Non-primary publication outside prespecified evidence eligibility (retain citation-chasing flag if useful).
- `E06`: Other protocol-defined exclusion, accompanied by concrete evidence.
- `U01`: Candidate provenance unresolved.
- `U02`: BRD4-specific involvement unresolved in BET-family work.
- `U03`: Insufficient title/abstract or missing abstract.
- `U04`: Publication/version or study-type ambiguity.
- `I01`: Previously characterized compound screened/tested for BRD4/BET.
- `I02`: Potentially relevant linked experimental/translational follow-up.

Codes are **project-specific operational labels**, not official JBI classification codes. Avoid generic reasons such as “not relevant,” “no novelty,” “no experimental IC50,” or “no repurposing keyword.”

## 7. Quality-assurance controls

### Before screening

- [ ] Review question and PCC clearly articulated.
- [ ] Eligibility and exclusion criteria versioned and approved.
- [ ] Search records deduplicated, but original identifiers and provenance preserved.
- [ ] Source types/preprint-journal pair handling specified.
- [ ] Abstract-missing protocol explicitly states MAYBE unless exclusion is independently clear.
- [ ] Reviewers trained on borderline examples and blind pilot completed.
- [ ] Conflict resolution and screening responsibilities specified.

### During screening

- [ ] Each NO has an explicit criterion and record-specific evidence.
- [ ] No record is excluded solely because a key fact is *not mentioned*.
- [ ] YES and MAYBE remain eligible for full-text retrieval.
- [ ] Computational-only designs are not automatically excluded.
- [ ] BET-family uncertainty is flagged rather than guessed.
- [ ] Conference abstracts and preprints are not automatically thrown away.
- [ ] Follow-up reports and publication versions are linked, not naively counted as new discovery campaigns.
- [ ] Reviewer identity, human-vs-AI status and dates are accurate.
- [ ] No automated or model-derived labels are presented as an independent human assessment.

### After screening

- [ ] Every unique record has the expected number of human reviewer decisions for the chosen protocol.
- [ ] Each disagreement has an auditable resolution; no silent overwrites.
- [ ] Random stratified audit of NO records emphasizes high-risk false exclusions (BRD4, BET, drug libraries, kinase inhibitors, previously characterized compounds, computational studies, and missing abstracts).
- [ ] Known eligible/benchmark papers are retrieved or explicitly investigated if missed.
- [ ] Reason-code distributions, missing data, identifier conflicts and report-linking are inspected.
- [ ] Final YES + MAYBE + NO totals reconcile exactly to the number screened.
- [ ] PRISMA-ScR counts are calculated from **approved human-reviewed decisions**, not provisional AI triage.
- [ ] Full-text exclusion reasons are documented at the full-text stage; do not conflate them with T&A reasons.

## 8. Quality metrics: how to interpret them

- **Observed agreement:** proportion of records with matching independent reviewer decisions in a pilot. The JBI piloting framework provides **≥75% agreement as a suggested threshold**, *not a guarantee* of correct screening or an absolute law for every review.
- **Cohen's kappa / other agreement measures:** optional diagnostics; prevalence imbalance can alter interpretation. Never treat high agreement as proof that exclusions are valid.
- **False-exclusion audit:** the most important safety check for this review. Re-review a prespecified random and risk-enriched sample of NO decisions and restore wrongly excluded candidates before full-text selection.
- **Benchmark retrieval:** test whether known BRD4 repurposing studies (e.g., nitroxoline, kinase inhibitors, SN-38 and NSAID–BET investigations) have been found and retained or transparently explained.
- **Audit completeness:** zero missing decisions, reason codes, or reviewer provenance for finalized human screening; uncertain records need a specific verification question.
- **Source completeness:** retain explicit counts for missing abstracts and unretrievable full texts, without fabricating abstract text.

These quality metrics are for **process evaluation**; they are not outcomes of BRD4 inhibitor effectiveness and should not be conflated with critical appraisal or meta-analysis.

## 9. Red flags and required corrective actions

| Red flag | Corrective action |
|---|---|
| Exclusion justified only as “previous use not reported” | Reclassify as MAYBE pending full-text provenance check |
| Exclusion because study reports docking only | Reconsider: computational-only work is within scope if genuine repurposing is plausible |
| Include because “repurposing” appears in title but compound is already a BET inhibitor | Check whether only the disease indication changed; classify appropriately |
| Multi-target compound accepted with no BRD4-specific findings | Mark MAYBE; verify actual target results at full text |
| Crystal structure, binding, inhibition and cellular phenotype treated as synonyms | Preserve distinct evidence types for later charting |
| Same model generates “three author” votes | Relabel as AI passes; do not report human independence or human consensus |
| Large batch of auto-exclusions has only keyword-based rationales | Audit high-risk negatives; consider re-screening with human reviewers |
| Conference abstract and journal article counted as two discoveries | Link versions/publications to compound and campaign |
| Screening criteria changed midstream without a log | Version criteria; document reason/date and re-evaluate affected records |

## 10. BRD4 project implementation sequence

1. Preserve the **1,445-record master literature dataset** as an immutable input; verify final identifier reconciliation and abstract coverage.
2. Keep the existing 1,445-row AI output as **AI-assisted preliminary triage** only; do not treat its 1,115 suggested NO decisions as final.
3. Have the actual author team approve this guide, including borderline compound classes and BET-family scope.
4. Pilot the same selected sample independently with actual human reviewers, document disagreements and approve the screening rulebook.
5. Conduct formal human-led T&A screening; do not bulk-adopt AI negatives without review.
6. Retain all YES and MAYBE records for full-text retrieval; track linked reports and retrieval failures separately.
7. At full text, verify original non-BRD4 pharmacological purpose, specific BRD4/BET evidence, molecular/compound identity and study design. Make final eligibility judgments there.
8. Chart included evidence by compound, study/publication, assay, BRD4 domain and discovery campaign; separate in-silico predictions from binding, functional inhibition, cellular engagement and disease outcomes.
9. Construct the PRISMA-ScR flow diagram from audited decisions and source counts only.

## 11. Reporting language and research-integrity safeguards

**Permitted description:** “An AI-assisted preliminary title-and-abstract triage was undertaken for workflow support; independent human reviewer selection and consensus were performed separately [only if actually completed].”

**Do not claim:** “Three authors independently screened 1,445 records,” “95% human reviewer agreement,” or “1,115 records were formally excluded,” unless those statements are substantiated by real, documented human screening and adjudication.

If human screening has not been completed, say so. Accuracy in the methods matters more than making the review look finished.

## 12. Primary methodological sources

1. JBI Manual for Evidence Synthesis. **Section 10.2.7: Selecting the evidence** (updated 31 August 2026): https://jbi-global.atlassian.net/wiki/spaces/MANUAL/pages/355862769/10.2.7%20Data%20extraction
2. JBI Manual for Evidence Synthesis. **Section 10.2.7.1: Piloting the selection of studies** (updated 31 August 2026): https://jbi-global-wiki.refined.site/space/MANUAL/2049540102/10.2.7.1%2BPiloting%2Bthe%2Bselection%2Bof%2Bstudies
3. NIH Library. **Screening**: https://www.nihlibrary.nih.gov/services/evidence-synthesis/select-collect-synthesize/screening
4. Cochrane Handbook for Systematic Reviews of Interventions. **Chapter 4: Searching for and selecting studies**: https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04
5. PRISMA Extension for Scoping Reviews (**PRISMA-ScR**): https://www.prisma-statement.org/scoping

**Source distinction:** Sections 1, 5, 7 and 8 adapt JBI, Cochrane, NIH and PRISMA-ScR principles. The BRD4 eligibility tests, codebook, examples, audit flags and implementation sequence are **project-specific operational proposals** requiring author approval, not quotations or mandatory rules from those guidelines.