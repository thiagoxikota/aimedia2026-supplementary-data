# Survey Analysis: Specification Literacy and Prompt Strategy

Descriptive analysis of participant survey responses (n=6). Due to the small sample size, findings are reported as observed patterns rather than statistically tested correlations. All scales are 1–5 unless noted.

**Note on P4:** P4 described their intended approach but did not submit an actual prompt. This respondent was excluded from the main paper's convergence analysis (Group A, n=5) because no AI output could be generated. P4's survey responses are included here for completeness, as they provide insight into prompt strategy awareness. References to "the five designers" in the main paper correspond to P1, P2, P3, P5, and P6.

---

## 1. Participant Overview

| ID | Exp. (yr) | Domain | Operational exp. | AI fam. | Figma Make fam. | Words (exact) | Words (approx)\* | Strategy |
|----|-----------|--------|-------------------|---------|-----------------|---------------|------------------|----------|
| P1 | 7 | SaaS | Prior projects | 4 | 3 | 95 | ~120 | Minimal extraction |
| P2 | 4 | E-commerce | Prior projects | 3 | 2 | 297 | ~350 | Contextual specification |
| P3 | 3.2 | Web apps | Regular work | 5 | 1 | 2100 | ~2500 | Exhaustive specification |
| P4\*\* | 7 | Consulting | Prior projects | 3 | 4 | 38 | ~40 | Meta-description |
| P5 | 4 | Landing pages | None | 1 | 1 | 235 | ~200 | AI-delegated |
| P6 | 3.5 | Apps/websites | Prior projects | 3 | 3 | 427 | ~500 | Structural specification |

\* Approximate values as reported in the main paper (Table 5). Exact counts computed from verbatim prompt text.

\*\* P4 did not submit an actual prompt and was excluded from the main paper's convergence analysis (see note above).

**Means (all 6):** Experience 4.8 yr, AI familiarity 3.2, Figma Make familiarity 2.3, Difficulty 2.5, Confidence 3.3, Pattern avoidance 2.8. **Means (5 analyzed, excl. P4):** Experience 4.3 yr, AI familiarity 3.2, Figma Make familiarity 2.0, Difficulty 2.2, Confidence 3.2, Pattern avoidance 3.2.

---

## 2. Prompt Strategy Taxonomy

Six distinct strategies emerged from the prompts, ordered by increasing specification depth:

| Strategy | Participant | Description |
|----------|-------------|-------------|
| **Meta-description** | P4 | Described what they would write, not the prompt itself. Recognized the task would take ~1h. |
| **Minimal extraction** | P1 | Extracted key data points from the brief. Short, focused on content rather than structure. |
| **AI-delegated** | P5 | Used ChatGPT to generate the prompt. Moderate detail, generic structure. |
| **Contextual specification** | P2 | Added usage context, UX guidelines, visual style, and expected deliverables beyond the brief. |
| **Structural specification** | P6 | Numbered sections defining layout, column structure, component specs, and interaction behaviors. |
| **Exhaustive specification** | P3 | Role-playing persona, complete design system (hex colors, typography), component micro-specs, anti-patterns, resilience states, content tone. |

---

## 3. Key Patterns

### 3.1 Specification Literacy Gradient

A clear gradient of specification depth is observable across participants. We define *specification literacy* as the demonstrated ability to translate design intent into machine-readable specifications that constrain AI output toward a specific structural outcome.

**Low specification literacy (P5):**
- Lowest AI familiarity (1) and Figma Make familiarity (1)
- Delegated prompt construction to another AI tool (ChatGPT)
- Lowest confidence in structural differentiation (1)
- No deliberate pattern avoidance (1)
- The resulting prompt reads as a generic UX requirements document

**Medium specification literacy (P1, P2, P6):**
- Moderate AI familiarity (3–4)
- Wrote their own prompts with varying levels of structural detail
- Moderate-to-high confidence in differentiation (3–4)
- Moderate pattern avoidance (3–4)
- Prompts range from minimal data extraction to structured layout specifications

**High specification literacy (P3):**
- Highest AI familiarity (5)
- Wrote the most detailed prompt (~2100 words) with explicit anti-patterns
- High confidence (4) and highest pattern avoidance (5)
- Incorporated pre-tested prompt structures from prior experiments
- Only participant to write in English (potentially strategic for AI tool performance)
- Only participant to specify what the AI should *not* do (anti-patterns)

**Notable outlier (P4):**
- Highest Figma Make familiarity (4) but did not write a prompt
- Recognized the task would require ~1h of work — suggesting awareness of specification depth needed
- Reported highest difficulty (4) despite most tool-specific experience
- Pattern avoidance = 1, but noted in comments: "I wouldn't have thought about avoiding conventional patterns in the prompt itself — interesting"
- Represents a case where domain expertise and tool familiarity exist without prompt-level specification literacy

### 3.2 AI Familiarity and Prompt Sophistication

| AI fam. | Participant | Prompt strategy | Word count |
|---------|-------------|-----------------|------------|
| 5 | P3 | Exhaustive specification | ~2100 |
| 4 | P1 | Minimal extraction | 95 |
| 3 | P2, P4, P6 | Contextual / Meta / Structural | 38–427 |
| 1 | P5 | AI-delegated | 235 |

Higher AI familiarity correlates with more sophisticated prompting strategies, with the notable exception of P1 (high familiarity, minimal prompt). P1's high confidence (4) despite a short prompt may indicate tacit knowledge about what matters in prompts — or overconfidence in minimal specification.

### 3.3 Pattern Avoidance and Confidence

| Pattern avoidance | Confidence | Participants |
|-------------------|------------|--------------|
| 5 | 4 | P3 |
| 4 | 3 | P2 |
| 3 | 4 | P1, P6 |
| 1 | 4 | P4 |
| 1 | 1 | P5 |

Pattern avoidance and confidence in structural differentiation show a positive association, with P5 anchoring the low end (1, 1) and P3 anchoring the high end (5, 4). P4 is an outlier: high confidence (4) with no pattern avoidance (1), suggesting confidence in their design process rather than in prompt-level differentiation.

### 3.4 Difficulty Perception

| Difficulty | AI fam. | Figma Make fam. | Participant |
|------------|---------|-----------------|-------------|
| 1 | 4 | 3 | P1 |
| 2 | 5 | 1 | P3 |
| 2 | 3 | 3 | P6 |
| 3 | 3 | 2 | P2 |
| 3 | 1 | 1 | P5 |
| 4 | 3 | 4 | P4 |

P4 (most experienced with Figma Make, familiarity=4) reported the highest difficulty (4). This may reflect a calibration effect: deeper familiarity with the tool reveals the gap between design intent and what a single prompt can communicate. Conversely, P1 (difficulty=1) wrote the shortest prompt — low perceived difficulty may correlate with less awareness of specification possibilities.

### 3.5 The Double-Delegation Pattern

P5 used ChatGPT to construct a prompt for Figma Make — a two-stage AI pipeline where neither stage involves direct human specification of design structure. This creates a potential *double-homogenization* risk: the meta-prompt tool produces generic requirements, which the design tool then interprets through its own default patterns. P5's self-reported confidence of 1 aligns with this interpretation.

### 3.6 Experience Does Not Equal Specification Literacy

Professional experience (years) shows no clear association with prompt sophistication:

- P4 (7 years, consulting): meta-description only, pattern avoidance = 1
- P1 (7 years, SaaS): minimal 95-word prompt
- P3 (3.2 years, web apps): most sophisticated 2100-word prompt, highest pattern avoidance

This supports the paper's framing of specification literacy as a distinct competency from design expertise — one that may be more related to AI tool familiarity and deliberate practice with prompt engineering.

---

## 4. Qualitative Observations

### Anti-Pattern Specification as a Differentiator

Only P3 included explicit anti-patterns in their prompt:

> "No oversized hero section / No decorative illustrations / No generic analytics cards / No soft crypto/AI gradient look / No glassmorphism-heavy aesthetic / No dribbblized concept UI that ignores function"

This strategy — telling the AI what *not* to produce — may be a key mechanism by which specification literacy moderates homogenization. Rather than only specifying desired features (which all participants did to varying degrees), P3 also constrained the solution space by excluding common AI-generated patterns.

### Metacognitive Awareness

P4's comment ("I wouldn't have thought about avoiding conventional patterns in the prompt itself — interesting") reveals that the survey instrument itself surfaced a gap in their mental model. This suggests specification literacy includes a metacognitive component: awareness that AI tools have default structural tendencies that can be deliberately countered through prompt design.

### Pragmatic Convention Choice

P6 explicitly chose to maintain conventional dashboard patterns for usability reasons, innovating on prioritization logic rather than layout. This represents a deliberate, informed choice — distinct from P5's unconscious acceptance of conventions. Both scored pattern avoidance = 1–3, but for qualitatively different reasons.

---

## 5. Implications for the Main Paper

These patterns support the paper's central thesis that specification literacy moderates homogenization in GenAI-assisted interface design:

1. **A specification literacy gradient exists** — Participants demonstrate clearly differentiated levels of ability to translate design intent into AI-constraining specifications.

2. **Higher specification literacy correlates with higher confidence in structural differentiation** — Those who write more detailed, structured prompts believe their outputs will be more distinctive.

3. **Anti-pattern specification may be a key mechanism** — The most specification-literate participant was the only one to explicitly constrain AI defaults, suggesting this is a learnable skill that could moderate homogenization.

4. **Experience is not a proxy for specification literacy** — Professional design experience does not predict prompt sophistication, supporting the argument that specification literacy is a distinct and emerging competency.

5. **AI delegation amplifies homogenization risk** — Using AI to write prompts for AI removes human design intent from the specification process entirely.

---

## 6. Limitations

- **Sample size (n=6):** Patterns are descriptive, not generalizable. No statistical significance can be claimed.
- **Self-report bias:** Confidence and pattern avoidance are self-assessed; actual output differentiation requires visual analysis (reported in the main paper).
- **Single brief:** All participants responded to the same product brief; generalizability to other domains is unknown.
- **No output comparison in this analysis:** This analysis examines prompts and self-reports only. Comparison of actual AI-generated outputs from these prompts is presented in the main paper.
- **P4 did not write a prompt:** Their meta-description provides insight into their approach but cannot be compared structurally to other prompts.
