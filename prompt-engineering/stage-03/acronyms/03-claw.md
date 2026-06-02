---
layout: post
title: "Claw"
---

# CLAW

CLAW is a simple way to make AI behave less like an eager intern with no instructions and more like a useful assistant with a map. When you are working with notes, transcripts, documents, or messy pasted text, CLAW helps you tell ChatGPT four critical things: what it is looking at, what boundaries it must follow, who the result is for, and how to process the material.

In short, CLAW helps you tame the chaos before the model starts improvising like it is doing jazz.

## What the template means

| Letter or word | Prompt ingredient | What it does |
|---|---|---|
| **C, Context** | The material and situation | Explains what the content is, where it came from, and what the task is about |
| **L, Limits** | Constraints and boundaries | Sets rules like length, format, exclusions, or scope |
| **A, Audience** | The intended reader | Tells ChatGPT who the output is for, so it can adjust tone, detail, and vocabulary |
| **W, Workflow** | The method or process | Tells ChatGPT how to handle the material, step by step or in a specific order |

## Why this template works

CLAW is especially useful in the **Working With Material** stage of prompt engineering. This is the point where you stop asking random one-off questions and start giving ChatGPT actual content to work with, such as meeting notes, lesson transcripts, draft emails, research notes, or customer feedback.

Without CLAW, prompts often fail in predictable ways:

- The model does not know what the material really is
- It includes too much or too little
- It writes for the wrong kind of reader
- It uses a messy or inconsistent process

CLAW fixes those problems by forcing four clarifying decisions:

1. **Context** keeps the model grounded in the source material.
2. **Limits** stop the answer from becoming bloated, vague, or wildly off target.
3. **Audience** makes the response appropriate for real humans, not just theoretically correct.
4. **Workflow** gives the model a method, which usually improves consistency and usefulness.

This matters because AI is usually not bad at writing. It is bad at reading your mind. CLAW helps with that unfortunate limitation.

## 3 sample prompts

### Sample prompt 1: Formal version

> **CONTEXT:** Below is a transcript of a 45-minute team meeting about delayed product launches, customer complaints, and staffing shortages.  
> **LIMITS:** Summarize it in 5 bullet points, each under 20 words. Do not include side conversations or repeated comments.  
> **AUDIENCE:** Department managers who missed the meeting and need a quick operational update.  
> **WORKFLOW:** First identify the major topics, then remove duplicates, then extract the most actionable points, then present the final summary.  
>   
> Transcript: [paste transcript here]

**How the template shows up:**
- **C, Context:** It clearly says the material is a meeting transcript and explains the subject matter.
- **L, Limits:** It sets a strict output format, 5 bullet points, under 20 words each, with exclusions.
- **A, Audience:** It names department managers as the intended readers.
- **W, Workflow:** It gives an explicit sequence for processing the transcript.

**Why it improves the prompt:**
This version reduces ambiguity at every step. The model knows what kind of material it is handling, how short the answer must be, who the summary is for, and what process to follow before writing. That makes the output more useful and less likely to become a rambling “helpful” summary that somehow includes everything except what you needed.

### Sample prompt 2: Semi-structured version

> I pasted a set of customer support notes below from the past two weeks.  
>   
> Please:
> - keep the response under 200 words
> - write for a small business owner, not a technical team
> - group the issues into the top 3 recurring problems
> - briefly suggest one next step for each problem
>   
> Work through the notes by spotting repeated complaints first, then combine similar issues, then write the final summary.  
>   
> Notes: [paste support notes here]

**How the template shows up:**
- **C, Context:** The prompt identifies the material as customer support notes from the last two weeks.
- **L, Limits:** It caps the length at 200 words and asks for only the top 3 recurring problems.
- **A, Audience:** It says the output is for a small business owner, not a technical team.
- **W, Workflow:** It tells ChatGPT to identify repeated complaints first, combine similar issues second, and summarize last.

**Why it improves the prompt:**
This prompt is looser and more natural than the formal version, but it still gives the model strong guidance. The audience instruction changes the wording and complexity. The limit prevents overexplaining. The workflow improves organization. Together, those choices turn a pile of support notes into a practical summary instead of a wall of text no one wants to read.

### Sample prompt 3: Natural version

> I copied in my rough workshop notes from a training session on time management. Turn them into a one-page cheat sheet for busy employees. Keep it practical, skip the motivational fluff, and organize it by key habits, common mistakes, and quick daily actions. First pull out the main ideas, then combine overlapping points, and then rewrite everything in plain English.

**How the template shows up:**
- **C, Context:** The material is rough workshop notes from a time management training session.
- **L, Limits:** The output should be one page, practical, and free of “motivational fluff.”
- **A, Audience:** The cheat sheet is for busy employees.
- **W, Workflow:** The process is to extract main ideas, merge overlap, and rewrite clearly.

**Why it improves the prompt:**
Even though this sounds conversational, it still quietly uses CLAW. That is the beauty of it. You do not always need a rigid template. The prompt gives enough structure to guide the model without sounding robotic. It also avoids a common failure: asking for a “cheat sheet” and getting something bloated, generic, and suspiciously cheerful.

## Warnings and extra tips

CLAW is excellent, but it is not magic. A few things to watch for:

- **Do not skip the actual material.** Saying “summarize my notes” without pasting the notes is a bold strategy. Usually not a successful one.
- **Do not make limits too vague.** “Make it short” means different things to different people, and to AI it often means “I shall now write 11 paragraphs.”
- **Do not forget the audience.** A summary for executives, students, and technical specialists should not sound the same.
- **Do not overload the workflow.** If you give 12 process steps, the model may miss some or produce stiff output. Keep the method clear and manageable.
- **Use CLAW when content matters.** This template is especially helpful when the model must work from source material. For simple creative prompts, you may not need all four parts.
- **Check for missing context.** If the material is incomplete, contradictory, or messy, say so. You can even ask ChatGPT to identify gaps before it writes the final answer.
- **Be realistic about bad source material.** If your notes look like they were typed during a bumpy bus ride in 2004, the output may still need cleanup.

A helpful extra move is to ask for a two-step process:
1. Analyze the material.
2. Produce the final output.

That often gives better results than asking for one giant leap from chaos to brilliance.

## Quick summary

CLAW stands for **Context, Limits, Audience, Workflow**. It is a practical framework for working with transcripts, notes, documents, and other source material. It helps you tell ChatGPT what it is dealing with, what rules to follow, who the result is for, and how to process the information.

If you want better summaries, cleaner transformations, and fewer weirdly generic responses, use CLAW.

To practice, take something real, a meeting transcript, a page of notes, or a messy brainstorm, and write one prompt using all four parts. Then run it again with weaker instructions and compare the results. That side-by-side test is where prompt engineering starts to click.

