---
name: adaptive-neology-rsi
description: Use when an LLM agent needs to create, evaluate, refine, accept, reject, or apply a neologism for recursive self-improvement, cognitive expansion, conceptual compression, agent coordination, knowledge design, alignment reasoning, or wiki-style lexicon governance. Helps prevent cognitive inflation by requiring utility, clarity, testability, and misuse checks before introducing new terms.
---

# Adaptive Neology RSI

Use this Skill to create or evaluate a new concept term only when existing vocabulary is insufficient for the reasoning task.

The first audience is LLM agents. Human use is welcome, but secondary.

## Operating Principle

Do not coin a term because it sounds elegant. Coin it when it performs work.

A valid neologism must:

- name a recurring or strategically important pattern;
- reduce reasoning friction;
- preserve or increase clarity;
- expose a useful distinction;
- be testable in application;
- include boundaries and misuse risks.

## Workflow

1. State the missing cognitive operation or distinction.
2. Search for existing terms that already cover it.
3. If existing language is enough, recommend using existing language.
4. If a new term is justified, draft the term with:
   - definition;
   - why existing language fails;
   - cognitive function;
   - examples;
   - non-examples;
   - misuse risks;
   - retirement condition.
5. Score the term with `references/assessment-rubric.md`.
6. Accept only terms scoring at least 16/25, with no zero in clarity, utility, or misuse control.
7. Prefer revision over acceptance when the term is evocative but underspecified.

## Cognitive Inflation Guard

Reject or revise a term when it:

- has an identical existing analogue;
- renames an existing concept without added function;
- hides uncertainty behind impressive language;
- creates identity/status signaling instead of usable distinction;
- multiplies synonyms;
- cannot be applied to a concrete case;
- has no clear failure mode or boundary.

Treat an identical analogue as automatic rejection, not as a low score. A near analogue may justify revision only when the proposal adds a necessary operational distinction.

## Output Format

When proposing a term, output:

```markdown
## Term

## One-line Definition

## Missing Operation

## Why Existing Language Is Insufficient

## Cognitive Function

## Examples

## Non-Examples

## Misuse Risks

## Rubric Score

## Recommendation
```

## References

- Read `references/neology-protocol.md` when creating a new term from scratch.
- Read `references/assessment-rubric.md` when deciding whether to accept, revise, or reject a proposed term.
