---
layout: post
title: "Refine"
---

# REFINE

REFINE is what you use when the first AI answer is... fine. Not great, not terrible, just sitting there like office coffee from 1997. The whole point is simple: do not stop at the first draft. Review it, judge it, fix it, improve it, narrow it, and make the model explain the result clearly.

This template fits the **Improvement Loops** stage of prompt engineering, where the big lesson is this: better prompts often come from better follow-up prompts.

## What the template means

| Letter or word | Prompt ingredient | What it does |
|---|---|---|
| **R, Review** | Evaluation | Tells the model to inspect the current answer and notice strengths, weaknesses, or issues. |
| **E, Evaluate** | Evaluation | Asks the model to judge quality using criteria, scores, or standards instead of vague opinions. |
| **F, Fix** | Refinement | Directs the model to correct errors, weak wording, missing details, or bad structure. |
| **I, Improve** | Feedback | Pushes the model to suggest or apply upgrades so the result becomes more useful. |
| **N, Narrow** | Summarization | Reduces scope, trims fluff, and focuses the answer on the most important points. |
| **E, Explain** | Teaching Level | Makes the model show its reasoning or present the result at a clear learning level. |

## Why this template works

REFINE works because most weak prompts fail in one of two ways:

1. They ask for an answer, but never check the quality.
2. They ask for improvements, but give no method for improving anything.

REFINE solves both problems. It turns prompting into a loop:

- **Review** what came back.
- **Evaluate** it against real standards.
- **Fix** what is broken.
- **Improve** what is merely average.
- **Narrow** the answer so it becomes focused.
- **Explain** the final result so the user can actually understand and use it.

This is especially useful when the AI gives you something that is too wordy, too vague, too confident, or weirdly polished while still missing the point. AI can do that. A lot. It is like getting a report that looks impressive until you read sentence three.

## 3 sample prompts

### Sample prompt 1: Formal version

> REVIEW: Review the following draft email for clarity, tone, and professionalism.  
> EVALUATE: Score it from 1 to 10 for clarity, conciseness, and effectiveness, and briefly justify each score.  
> FIX: Correct awkward wording, grammar issues, and unclear requests.  
> IMPROVE: Strengthen the email so it sounds confident, polite, and action-oriented.  
> NARROW: Keep it under 120 words and focus on only one main request.  
> EXPLAIN: After rewriting, explain the top 3 changes in plain language for a workplace beginner.  
>
> Draft email:  
> "Hi team, I just wanted to kind of follow up on the project because there are a few things still moving around and I was hoping maybe we could get some updates when people have time."

**How the template shows up:**
- **R, Review:** The prompt explicitly asks the model to review the draft for clarity, tone, and professionalism.
- **E, Evaluate:** It requires scores and justifications, which creates measurable evaluation.
- **F, Fix:** It tells the model to correct wording, grammar, and unclear requests.
- **I, Improve:** It asks for a stronger version with a confident, polite, action-oriented tone.
- **N, Narrow:** It limits the email to 120 words and one main request.
- **E, Explain:** It asks for the top three changes in plain language for a beginner.

**Why it improves the prompt:**
This version is strong because it removes ambiguity. The model is not left guessing what “make this better” means. It has quality criteria, editing goals, length limits, and an explanation target. That usually produces a cleaner result and a useful mini-lesson at the same time.

### Sample prompt 2: Semi-structured version

> I wrote a short blog intro about time management.  
>
> - Review it for weak spots  
> - Evaluate it on clarity and usefulness  
> - Fix anything repetitive or vague  
> - Improve the opening so it grabs attention  
> - Narrow it to 3 sentences  
> - Explain what changed and why in simple terms  
>
> Draft:  
> "Managing time is important in life and work. People often have many tasks to do, and that can be stressful. Good time management can help people do better."

**How the template shows up:**
- **R, Review:** “Review it for weak spots” starts the quality check.
- **E, Evaluate:** “Evaluate it on clarity and usefulness” gives the model criteria.
- **F, Fix:** “Fix anything repetitive or vague” targets common writing problems.
- **I, Improve:** “Improve the opening so it grabs attention” adds a specific upgrade.
- **N, Narrow:** “Narrow it to 3 sentences” forces focus and brevity.
- **E, Explain:** “Explain what changed and why in simple terms” adds teachable feedback.

**Why it improves the prompt:**
This semi-structured format feels more natural than a formal template, but it still guides the model through a full improvement loop. It works well when you want better output without sounding like you are filing taxes. You get critique, revision, compression, and a short explanation, all in one go.

### Sample prompt 3: Natural version

> Here’s my product description for a reusable water bottle. Please look it over, tell me what is weak about it, tighten the wording, make it more persuasive, keep only the most important selling points, and then explain your changes like you’re teaching a smart beginner.  
>
> "This water bottle is very good for many people and has a nice design. It can be used in lots of places and is helpful for daily life."

**How the template shows up:**
- **R, Review:** “Look it over” asks the model to inspect the draft.
- **E, Evaluate:** “Tell me what is weak about it” creates an informal evaluation step.
- **F, Fix:** “Tighten the wording” signals repair and cleanup.
- **I, Improve:** “Make it more persuasive” asks for stronger marketing language.
- **N, Narrow:** “Keep only the most important selling points” narrows the focus.
- **E, Explain:** “Explain your changes like you’re teaching a smart beginner” sets the teaching level.

**Why it improves the prompt:**
This version proves you do not need rigid labels to use REFINE well. Even casual wording can contain all six ingredients. The result is usually better because the model is asked to critique, revise, focus, and teach, instead of just rewriting blindly.

## Warnings and extra tips

REFINE is powerful, but a few things can still go sideways:

- **Do not skip the original goal.** If you only ask the model to improve something, it may improve the wrong thing. Better grammar is useless if the message still misses the point.
- **Too much evaluation can create bloat.** If you ask for review, scoring, explanations, comparisons, and five versions, the response may become huge and annoying. Sometimes you want a mechanic, not a documentary.
- **Narrowing too early can remove useful detail.** First get the ideas right, then compress them.
- **Explain does not mean expose hidden chain-of-thought.** Ask for a short, practical explanation of changes, not an endless internal monologue.
- **REFINE is best after a draft exists.** It shines when you already have text, an answer, a plan, or an output to improve. If you are starting from nothing, another template or structure may be a better first step.
- **Use real criteria when possible.** Instead of “make it better,” try “make it clearer for customers,” “shorten it to 100 words,” or “make it sound more professional.”

A good practical trick is to run REFINE in two rounds:
1. First round, review and diagnose.
2. Second round, apply the fixes and improvements.

That often gives better results than trying to do everything in one giant prompt.

## Quick summary

REFINE teaches one of the most important prompt engineering habits: **the first answer is a draft, not a verdict**.

Use it to:
- **Review** the output
- **Evaluate** it with criteria
- **Fix** the weak parts
- **Improve** the quality
- **Narrow** the focus
- **Explain** the changes clearly

If you want to practice, take any email, paragraph, social post, or product description you already wrote and run it through REFINE. Start with something ordinary. The boring stuff is actually perfect practice. That is where you really notice the upgrade.

