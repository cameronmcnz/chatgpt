---
layout: post
title: "Check"
---

# CHECK

CHECK is the prompt template for when you want the AI to stop sounding slick and start being useful. It is your quality-control checklist for research, fact-heavy answers, and anything that could go confidently off a cliff.

If a normal prompt says, "Tell me stuff," CHECK says, "Tell me stuff, show your work, stay in bounds, and format it so I can actually use it."

## What the template means

| Letter or word | Prompt ingredient | What it does |
|---|---|---|
| C, Context | Context | Gives the background, topic, goal, or situation so the AI knows what kind of answer you need. |
| H, Hallucination warning | Guardrails | Tells the AI not to guess, invent facts, or fake certainty. It should admit uncertainty when needed. |
| E, Evidence | Evidence | Requires support for claims, such as sources, citations, examples, or clear reasoning. |
| C, Constraints | Limits | Sets boundaries like length, scope, reading level, timeframe, or what to include and exclude. |
| K, Keep format | Format | Tells the AI exactly how to structure the answer so it is easy to review or reuse. |

## Why this template works

CHECK is useful because AI often sounds more confident than it deserves. That is not evil, it is just annoying. Especially when you are asking about research, recommendations, summaries, comparisons, or decisions.

This template forces five healthy habits:

1. **Add context** so the AI knows your real task.
2. **Warn against hallucination** so it is less likely to invent details.
3. **Ask for evidence** so claims are supported instead of floating around like office rumors.
4. **Set constraints** so the answer does not become a novel, a mess, or both.
5. **Keep a format** so you can scan, compare, and verify the response quickly.

In short, CHECK helps you get answers that are clearer, safer, and easier to trust, or at least easier to question.

## 3 sample prompts

### Sample prompt 1: Formal version

> CONTEXT: I am comparing project management tools for a 20-person marketing team that works remotely and collaborates across time zones.  
> HALLUCINATION WARNING: Do not invent features, prices, or reviews. If you are unsure about any claim, label it clearly as uncertain.  
> EVIDENCE: Compare Asana, Trello, and Monday.com using widely known features and provide supporting reasoning for each comparison point.  
> CONSTRAINTS: Limit the answer to 300 words. Focus only on ease of use, collaboration features, and likely fit for a small remote team.  
> KEEP FORMAT: Present the answer as a table with columns for Tool, Strengths, Weaknesses, Best Fit, and Confidence Level.

**How the template shows up:**
- **C, Context:** The prompt explains the team size, industry, and remote-work situation.
- **H, Hallucination warning:** It explicitly says not to invent features, prices, or reviews, and to label uncertainty.
- **E, Evidence:** It asks for supporting reasoning for each comparison point.
- **C, Constraints:** It limits the answer to 300 words and narrows the focus to three criteria.
- **K, Keep format:** It requires a table with specific columns.

**Why it improves the prompt:**
This version makes the AI act less like a random opinion machine and more like a careful assistant. The context narrows the recommendation. The hallucination warning reduces fake specifics. The evidence requirement pushes the model to justify comparisons. The constraints keep it focused. The format makes it easy to review side by side, which is exactly what you want in a decision prompt.

### Sample prompt 2: Semi-structured version

> I need a quick summary of whether standing desks improve productivity for office workers.  
>  
> Please:
> - mention where evidence is strong, weak, or mixed
> - do not present guesses as facts
> - keep the explanation under 5 bullet points
> - include a short section called "What we know" and another called "What is still uncertain"

**How the template shows up:**
- **C, Context:** The topic is standing desks and productivity for office workers.
- **H, Hallucination warning:** The prompt says not to present guesses as facts.
- **E, Evidence:** It asks the AI to show where evidence is strong, weak, or mixed.
- **C, Constraints:** It limits the response to 5 bullet points.
- **K, Keep format:** It asks for two named sections, "What we know" and "What is still uncertain."

**Why it improves the prompt:**
Without CHECK, the AI might give a polished but vague health-and-productivity speech. This prompt tells it to separate solid findings from shaky ones. That matters, because research questions often have mixed results. The structure also helps the reader spot uncertainty instead of accidentally treating everything as proven.

### Sample prompt 3: Natural version

> I am thinking about switching to a high-protein diet to lose weight. Give me a simple explanation of the likely benefits and risks, tell me which points are well supported versus still debated, do not make up medical claims, keep it brief, and put the answer in a short pros and cons list with a final note about what I should ask my doctor.

**How the template shows up:**
- **C, Context:** The user explains the real situation, considering a high-protein diet for weight loss.
- **H, Hallucination warning:** The prompt says not to make up medical claims.
- **E, Evidence:** It asks which points are well supported versus still debated.
- **C, Constraints:** It says to keep it brief.
- **K, Keep format:** It requests a pros and cons list plus a final note about what to ask a doctor.

**Why it improves the prompt:**
This casual version still uses CHECK, just without the big labels. It helps the AI avoid turning a health question into fake certainty. It also encourages balanced output instead of one-sided hype. For personal decisions, that balance is a big deal. A clean pros-and-cons format makes the answer easier to think about and discuss with a real professional.

## Warnings and extra tips

CHECK is powerful, but it is not magic. A few things to watch for:

- **AI can still be wrong.** Even with guardrails, it may produce outdated, incomplete, or shaky information.
- **Evidence quality matters.** If you ask for evidence but do not specify source quality, you might get weak support dressed up nicely.
- **Too many constraints can choke the answer.** If you demand deep evidence, short length, and a super rigid format, something will probably suffer.
- **Context must be relevant.** Extra background is helpful only if it changes the answer. Do not dump your entire autobiography into the prompt.
- **Format should serve the task.** A table is great for comparison. A checklist is great for action steps. A paragraph is sometimes enough. Do not force a spreadsheet vibe onto everything.
- **For serious topics, verify externally.** Medical, legal, financial, and technical decisions still need trusted human-reviewed sources. CHECK helps you ask better questions. It does not replace actual expertise. Sorry, no template can do that.

A useful bonus move is to ask for a **confidence level** or a **list of assumptions** after the first answer. That is often where the hidden weak spots show up.

## Quick summary

CHECK stands for **Context, Hallucination warning, Evidence, Constraints, Keep format**. It helps you write prompts that are clearer, more grounded, and much harder for the AI to bluff its way through.

If a prompt matters, CHECK it.

To practice, try this on something you already care about: compare two tools, summarize a health claim, or ask about a work decision. First write a basic prompt, then rewrite it with CHECK and compare the results. That side-by-side test is where the light bulb usually turns on.

