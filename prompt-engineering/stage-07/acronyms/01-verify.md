---
layout: post
title: "Verify"
---

# VERIFY

If a prompt asks the AI to sound smart, it usually will. If a prompt asks the AI to **prove it**, slow down, show evidence, admit uncertainty, and point out weak spots, now you are getting somewhere.

That is what **VERIFY** is for.

It is a quality-control prompt framework for research, fact-checking, and critical thinking. Think of it as the part of prompt engineering that says, “Cool answer. Now show your work.”

## What the template means

| Letter or word | Prompt ingredient | What it does |
|---|---|---|
| **V, Validate** | Evidence | Asks the AI to check whether claims hold up, instead of just repeating them confidently. |
| **E, Evidence** | Evidence | Requires support, examples, citations, sources, or reasoning behind the answer. |
| **R, Red flags** | Guardrails | Tells the AI to point out weak evidence, possible errors, missing data, bias, or suspicious claims. |
| **I, Identify assumptions** | Assumptions | Forces the model to name what it is assuming, instead of hiding those assumptions in smooth-sounding text. |
| **F, Format** | Format | Defines how the answer should be organized so it is easier to review and trust. |
| **Y, Your confidence** | Confidence | Asks the AI to rate how certain it is, which helps you spot shaky answers dressed up like certainty. |

## Why this template works

VERIFY helps because it changes the job you give the AI.

A basic prompt says, “Answer this.”
A VERIFY prompt says, “Answer this, support it, challenge it, expose assumptions, organize it clearly, and tell me how sure you are.”

That is a much better assignment.

This matters because AI is often fluent before it is reliable. It can sound like the office coworker who speaks in polished bullet points and somehow still got the numbers from nowhere. VERIFY helps you catch that.

It is especially useful when you are asking about:
- health, legal, or financial topics
- historical or scientific claims
- business decisions
- comparisons between tools, products, or strategies
- anything where being confidently wrong would be annoying, expensive, or both

## 3 sample prompts

### Sample prompt 1: Formal version

> VALIDATE: Review the claim that remote work always increases employee productivity.  
> EVIDENCE: Provide 3 to 5 evidence-based points, and distinguish between strong evidence, mixed evidence, and weak evidence.  
> RED FLAGS: Identify misleading generalizations, missing context, and situations where the claim may fail.  
> IDENTIFY ASSUMPTIONS: List the assumptions behind the claim.  
> FORMAT: Present the answer as a table with columns for claim, supporting evidence, red flags, assumptions, and conclusion.  
> YOUR CONFIDENCE: End with a confidence rating from 1 to 10 and a brief explanation of that rating.

**How the template shows up:**
- **V, Validate:** The prompt asks the AI to review the claim, not just accept it.
- **E, Evidence:** It explicitly requests 3 to 5 evidence-based points and asks for strength levels.
- **R, Red flags:** It tells the AI to identify misleading generalizations and missing context.
- **I, Identify assumptions:** It directly asks for the assumptions behind the claim.
- **F, Format:** It requires a table with specific columns.
- **Y, Your confidence:** It asks for a confidence rating and explanation.

**Why it improves the prompt:**
This version prevents the AI from giving a motivational poster answer like “remote work is the future” and calling it analysis. It pushes for nuance, structure, and visible uncertainty. That makes the response easier to review and much more useful for a real decision.

### Sample prompt 2: Semi-structured version

> I am comparing meal kit services for a family of four. Help me evaluate whether they are actually cost-effective compared with regular grocery shopping.  
>  
> - Validate the main claim, do they usually save money, cost more, or depend on the situation?  
> - Give evidence using common cost factors like ingredients, shipping, waste, convenience, and impulse purchases.  
> - Point out red flags, especially where marketing claims might be misleading.  
> - Identify assumptions, such as cooking habits, local grocery prices, and dietary needs.  
> - Format the answer in short sections with a final pros and cons summary.  
> - Include your confidence level and explain what would change your confidence.

**How the template shows up:**
- **V, Validate:** It asks the AI to evaluate the main claim about cost-effectiveness.
- **E, Evidence:** It requests evidence through specific cost factors.
- **R, Red flags:** It asks for misleading marketing claims and weak spots.
- **I, Identify assumptions:** It names examples of assumptions, like local prices and cooking habits.
- **F, Format:** It asks for short sections and a final pros and cons summary.
- **Y, Your confidence:** It requests a confidence level and what could change it.

**Why it improves the prompt:**
This version feels more natural than a formal template, but it still keeps the AI on a leash. Instead of getting a vague shopping blog answer, you get a practical review grounded in evidence, trade-offs, and context. Also, asking what would change confidence is sneaky in a good way. It reveals what information is missing.

### Sample prompt 3: Natural version

> I keep hearing that drinking coffee is either great for you or terrible for you. Give me a balanced answer that checks what claims are well supported, points out warning signs in oversimplified advice, explains what assumptions people are making, and wraps it up in a simple list I can skim. Tell me how confident you are in the overall conclusion.

**How the template shows up:**
- **V, Validate:** “checks what claims are well supported” asks the AI to verify the health claims.
- **E, Evidence:** “well supported” implies the need for evidence behind the answer.
- **R, Red flags:** “points out warning signs in oversimplified advice” covers red flags.
- **I, Identify assumptions:** “explains what assumptions people are making” is direct.
- **F, Format:** “wraps it up in a simple list I can skim” sets the format.
- **Y, Your confidence:** “Tell me how confident you are” covers confidence.

**Why it improves the prompt:**
This is casual, fast, and still smart. You are not using a rigid template, but the VERIFY ingredients are all there. That means the response is more likely to be balanced, readable, and honest about uncertainty. In other words, less internet shouting, more actual help.

## Warnings and extra tips

VERIFY is powerful, but it is not magic.

A few things to watch for:

- **Evidence quality still matters.** If the AI gives weak or fake sources, the answer can still be wrong. For important topics, check sources yourself.
- **Confidence is not truth.** A high confidence score does not guarantee correctness. It just tells you how sure the model sounds about its own answer.
- **Too much structure can slow things down.** If you use VERIFY for every tiny request, you may get overbuilt answers when you just wanted a quick summary.
- **Vague topics produce vague verification.** If your question is broad, like “Is technology good for society,” the evidence and assumptions may be fuzzy. Narrow the topic.
- **Some claims need external research.** If you want current facts, studies, or pricing, ask for recent sources or provide source material.
- **Guardrails are not optional.** The “R” in VERIFY is where a lot of the value lives. If you skip red flags, the AI may give a polished answer that hides its weaknesses like a late-90s infomercial.

A helpful upgrade is to add one more sentence when needed:
- “If evidence is weak or conflicting, say so clearly.”
- “Separate facts from interpretation.”
- “Do not invent citations.”

## Quick summary

VERIFY helps you ask better research questions by making the AI do six things: **validate the claim, show evidence, reveal red flags, identify assumptions, use a clear format, and state confidence**.

Simple version: do not just ask for an answer. Ask for an answer that can survive a little scrutiny.

Try it next with a claim you hear all the time, at work, in the news, or from that one friend who is very confident about everything. Use VERIFY and see how much stronger the response becomes when the AI has to show its homework.

