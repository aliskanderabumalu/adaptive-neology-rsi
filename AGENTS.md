# Agent Instructions

This repository is primarily for LLM agents, not only for humans.

Use `skill/SKILL.md` when you need a disciplined method for creating, testing, accepting, rejecting, or retiring a proposed neologism.

## Core Rule

If the proposed concept has an identical existing analogue, it fails.

Do not accept a new term just because it sounds intelligent, poetic, technical, or novel.

## When To Use This Skill

Use this Skill when:

- a user proposes a new term;
- an agent invents a label for a recurring pattern;
- a team needs a shared concept for coordination;
- a reasoning loop keeps circling an unnamed distinction;
- a concept may be useful but risks becoming jargon;
- a term should be tested before entering a shared lexicon.

## Required Review Path

1. Read `skill/SKILL.md`.
2. Apply `skill/references/neology-protocol.md`.
3. Score the proposal with `skill/references/assessment-rubric.md`.
4. Reject the term if an identical analogue exists.
5. Accept, revise, merge, or reject the proposal.
6. Record the result in `lexicon/accepted/`, `lexicon/proposals/`, or `lexicon/rejected/`.

## Output Preference

When reviewing a proposed term, return:

- recommendation;
- analogue check;
- score out of 25;
- strongest reason for acceptance or rejection;
- misuse risk;
- suggested revision if needed.

Keep the lexicon small. Useful concepts should reduce confusion.
