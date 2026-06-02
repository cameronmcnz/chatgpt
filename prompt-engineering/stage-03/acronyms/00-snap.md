---
layout: post
title: "Snap"
---

# SNAP

SNAP is a simple way to work with real material instead of tossing vague requests at ChatGPT and hoping for magic. You give it content, tell it what to pull out, say how to use it, then clean up the result. Quick, practical, and much less chaotic than the average meeting notes document.

In this stage of prompt engineering, you are not just asking for ideas. You are asking ChatGPT to do something useful with actual material like notes, transcripts, emails, reports, or rough drafts.

## What the template means

| Letter | Prompt ingredient | What it does |
|---|---|---|
| S | **Summarize** | Pulls out the main ideas from the source material so the response starts with the essentials. |
| N | **Narrow** | Limits the focus to a specific angle, topic, audience, section, or goal. |
| A | **Apply** | Tells ChatGPT what method or task to perform with the selected material, such as rewrite, compare, outline, convert, or explain. |
| P | **Polish** | Refines the output so it is clearer, cleaner, shorter, friendlier, more professional, or better formatted. |

## Why this template works

SNAP works because it matches how people actually handle information.

First, you **summarize** so you are not drowning in details. Then you **narrow** so the model does not wander off like a GPS from 2004. Next, you **apply** a method so ChatGPT knows what job it is doing. Finally, you **polish** so the result sounds like something you can actually use.

Without SNAP, prompts often sound like this: “Here are my notes. Make them better.” That is technically a request. It is also a great way to get a response that is broad, inconsistent, or weirdly confident.

With SNAP, your prompt becomes more intentional:
- What matters most?
- What specific part should the model focus on?
- What should it do with that material?
- What should the final output look like?

That combination makes prompts clearer, faster to reuse, and easier to improve.

## 3 sample prompts

### Sample prompt 1: Formal version

> **SUMMARIZE:** Review the meeting notes below and extract the main decisions, unresolved issues, and next steps.  
> **NARROW:** Focus only on items related to the Q3 product launch timeline. Ignore budget and hiring discussion.  
> **APPLY:** Convert the selected information into a clear executive briefing with 3 sections: Key Decisions, Open Risks, Recommended Actions.  
> **POLISH:** Write in a professional tone, use concise bullet points, and keep the output under 250 words.  
>   
> **Source material:**  
> [Paste meeting notes here]

**How the template shows up:**
- **S, Summarize:** “Extract the main decisions, unresolved issues, and next steps” asks for the essential points.
- **N, Narrow:** “Focus only on items related to the Q3 product launch timeline” limits the scope.
- **A, Apply:** “Convert the selected information into a clear executive briefing” gives the method.
- **P, Polish:** “Professional tone, concise bullet points, under 250 words” refines the final result.

**Why it improves the prompt:**
This version is strong because every part of the task is visible. ChatGPT knows what to pull from the notes, what to ignore, what format to use, and how polished the answer should be. That reduces rambling and makes the output immediately usable for a manager or stakeholder. Basically, it saves you from cleaning up a messy summary after the fact.

### Sample prompt 2: Semi-structured version

> I pasted a customer interview transcript below.  
>   
> - Give me the big picture first  
> - Then focus only on complaints about onboarding  
> - Turn those complaints into a list of recurring pain points with short explanations  
> - End with a polished version I can paste into a product team Slack update  
> - Keep the tone clear and professional, but not stiff  
>   
> Transcript:  
> [Paste transcript here]

**How the template shows up:**
- **S, Summarize:** “Give me the big picture first” asks for an overall summary.
- **N, Narrow:** “Focus only on complaints about onboarding” cuts down the scope.
- **A, Apply:** “Turn those complaints into a list of recurring pain points with short explanations” defines the task.
- **P, Polish:** “End with a polished version I can paste into a product team Slack update” shapes the final presentation and tone.

**Why it improves the prompt:**
This prompt feels more natural, but it still follows the SNAP logic. It starts broad, then zooms in, then transforms the content into a useful format, then smooths it out for a real audience. That flow helps ChatGPT avoid mixing summary, analysis, and writing style into one mushy blob. Technical term: less mush.

### Sample prompt 3: Natural version

> I pasted my rough webinar notes below. Can you pull out the main points, focus on the parts about common beginner mistakes, turn that into a short teaching outline, and clean it up so it sounds like a confident workshop handout?

**How the template shows up:**
- **S, Summarize:** “Pull out the main points” requests a summary.
- **N, Narrow:** “Focus on the parts about common beginner mistakes” tells ChatGPT what slice matters.
- **A, Apply:** “Turn that into a short teaching outline” gives a specific method.
- **P, Polish:** “Clean it up so it sounds like a confident workshop handout” adds refinement and tone.

**Why it improves the prompt:**
This is the casual version people actually type. It does not use formal labels, but it still includes all four SNAP moves. That makes it easy to remember and easy to use in everyday work. You can say it naturally and still get a structured result. Nice when you want useful output without sounding like you are filing a tax form.

## Warnings and extra tips

SNAP is useful, but it is not magic confetti.

Here are a few things to watch for:

- **Do not skip the source material.** SNAP works best when ChatGPT has something real to work with. If you say “summarize my notes” but never paste the notes, you are asking for improv.
- **Do not make “narrow” too vague.** “Focus on the important parts” is weak. Important to whom? Better: “focus on customer objections about price.”
- **Apply needs a real method.** If you only say “make it better,” the model has to guess. Better verbs are: outline, compare, rewrite, categorize, convert, simplify, extract, or prioritize.
- **Polish should be specific.** Tone, length, format, reading level, and audience all help. “Make it polished” is okay, but “make it polished for a one-minute team update” is much better.
- **SNAP may not be enough for complex jobs.** If you are handling long reports, multiple files, or a detailed workflow, you may need extra instructions for organization, chunking, or step-by-step processing.
- **Watch for lost nuance.** Summarizing and narrowing can remove context. If precision matters, ask the model to preserve exact wording for sensitive points or include direct quotes.
- **Check the final answer against the source.** A polished summary can still be wrong. A tidy mistake is still a mistake, just better dressed.

## Quick summary

SNAP stands for **Summarize, Narrow, Apply, Polish**. It helps you take messy material, focus it, do something useful with it, and shape the result into something clear and usable.

If your prompt starts with real content and ends with a result you can actually send, share, or study, SNAP is doing its job.

Try it next with something ordinary: meeting notes, a transcript, a long email thread, or your own rough draft. Paste it in, run through SNAP, and see how much better the output gets when you stop being vague and start being specific.

