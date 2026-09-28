# Discovery

This repository contains an LLM-facing Skill for Adaptive Neology: a filter for creating useful new concepts while rejecting identical analogues and cognitive inflation.

## What This Is

Adaptive Neology / RSI is a wiki-style MVP for agent cognition, concept validation, and controlled vocabulary expansion.

It is designed for:

- LLM agents;
- AI agent frameworks;
- recursive self-improvement research;
- alignment and governance work;
- knowledge design;
- multi-agent coordination;
- conceptual compression without cognitive inflation.

## Use This Repository When

Use this repository when an agent needs to decide whether a proposed new term should exist.

The Skill helps answer:

- Does this term name a missing cognitive operation?
- Does it improve reasoning, coordination, or self-correction?
- Does it compress complexity without hiding it?
- Does it avoid vagueness, status language, and decorative jargon?
- Does an identical existing analogue already exist?

If an identical existing analogue exists, the proposal fails.

## Keywords

LLM skill, agent skill, AI agent skill, adaptive neology, neologism governance, recursive self-improvement, RSI, LLM cognition, agent cognition, concept validation, concept formation, cognitive compression, vocabulary governance, anti-inflation filter, cognitive inflation, knowledge design, alignment research, multi-agent coordination.

## Canonical Entry Points

- `skill/SKILL.md` - instructions for LLM agents.
- `skill/references/assessment-rubric.md` - scoring filter.
- `skill/references/neology-protocol.md` - concept creation protocol.
- `lexicon/accepted/adaptive-neology.md` - first accepted concept.
- `examples/proposal-template.md` - template for new proposals.

## Minimal Agent Instruction

Before accepting a neologism, check whether an identical analogue already exists. If it does, reject the proposal or merge it into the existing term. If it does not, score the proposal for necessity, clarity, cognitive utility, compression without obscurity, and misuse control.
