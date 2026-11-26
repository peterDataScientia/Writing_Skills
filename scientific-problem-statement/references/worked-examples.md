# Worked Examples and Anti-patterns

**All stronger examples are teaching constructions, not quotations or verified novelty claims.** Validate against the real literature before publishing.

## Example 1: Novel method ≠ research gap
**Weak:** "Few studies applied deep learning to this target, so deep learning is needed."

**Better:** "Existing models have established predictive feasibility in the studied chemical space. It remains to determine whether predictions retain acceptable error and calibrated uncertainty when evaluated on structurally distinct compounds using an independent test design."

**Why:** Names the specific generalisation question and appropriate evidence. It is only a proposed gap until studies are checked.

## Example 2: Catalogue ≠ synthesis
**Weak:** "Study A used docking. Study B used MD. Study C used QSAR. More work is needed."

**Better:** "Docking and molecular dynamics investigate different structural aspects of ligand binding, whereas QSAR estimates activity from measured endpoints. Agreement among computational scores does not by itself establish biochemical inhibition; the research question must specify which experimental evidence can support the intended inference."

**Why:** Compares inferential targets and avoids equating incompatible endpoints.

## Example 3: Acknowledging previous achievement
**Weak:** "All previously published computational models are unreliable."

**Better:** "Published approaches have demonstrated useful performance under their reported conditions. However, these evaluations cannot alone establish reliability for settings or molecular domains that were not represented in testing."

**Why:** Concedes the supported findings while identifying a bounded limitation.

## Example 4: Timing of available information
**Weak:** "New ML models are required to improve pharmaceutical formulation prediction."

**Better:** "Models that rely on properties measured after formulation preparation answer a different prediction question from models intended to guide decisions before preparation. Matched comparisons can determine the additional predictive information provided by post-preparation measurements under independent evaluation."

**Why:** Defines the decision time and testable informational distinction.

## Example 5: Missing variables and causal overreach
**Weak:** "The model excluded factor X, so the literature is invalid."

**Better:** "If factor X influences the specified outcome under the studied conditions, its omission may change the model's predictions or parameter interpretation. The proposed investigation should test that possibility rather than assume the effect."

**Why:** Distinguishes a hypothesis about an omitted mechanism from proven model failure.

## Example 6: Practical motivation versus scientific problem
**Weak:** "Disease Y is serious, therefore molecular docking should be performed."

**Better:** "Disease burden provides the motivation, but a research problem must identify a specific unanswered molecular, therapeutic or predictive question and demonstrate why current studies cannot resolve it."

**Why:** Disease importance does not automatically confer methodological necessity.

## Final comparison rule
For each stronger sentence, ask: what study would prove it wrong? What evidence is required? Which statement could be claimed now, and which remains provisional?
