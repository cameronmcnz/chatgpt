---
layout: post
title: "Roast"
---

# ROAST

ROAST is the prompt engineering reminder that your first draft is not sacred. It is just the opening act.

This template helps you turn a rough AI answer into something sharper by asking the model to inspect its own work, point out what is weak, and then improve it. In other words, instead of hoping for perfection on round one, you run a quality check. Very glamorous, very practical, very much how real work gets done.

## What the template means

| Letter or word | Prompt ingredient | What it does |
|---|---|---|
| R, Review | Evaluation | Ask the model to look back over the output and check it as a whole. |
| O, Observe | Evaluation | Notice specific issues, patterns, missing parts, or awkward spots. |
| A, Assess | Evaluation | Judge quality against criteria such as clarity, accuracy, tone, or usefulness. |
| S, Suggest | Feedback | Propose concrete improvements, not just vague criticism. |
| T, Transform | Method | Revise the original answer into a better version based on the review. |

## Why this template works

ROAST works because it separates improvement into clear steps.

A lot of beginners write follow-up prompts like, "Make this better." That can work, but it often produces random changes. Better in what way? Clearer? Shorter? More persuasive? More accurate? Less robotic? The model has to guess, and guessing is where quality goes to take a coffee break.

ROAST fixes that.

It gives the AI a sequence:
1. **Review** the output.
2. **Observe** what stands out.
3. **Assess** it using criteria.
4. **Suggest** specific fixes.
5. **Transform** the draft into a stronger version.

This is part of the **Improvement Loops** stage of prompt engineering. The core lesson here is simple: good prompting is iterative. You do not just prompt once and stare at the result like it was faxed down from the heavens. You inspect, improve, and prompt again.

## 3 sample prompts

### Sample prompt 1: Formal version

> REVIEW: Examine the following email draft for clarity, tone, grammar, and professionalism.  
> OBSERVE: Identify specific problems, including awkward phrasing, missing information, or anything that may confuse the reader.  
> ASSESS: Rate the draft on a scale of 1 to 10 for clarity, professionalism, and persuasiveness, and briefly explain each score.  
> SUGGEST: Provide a short list of precise improvements.  
> TRANSFORM: Rewrite the email using those improvements.  
>   
> Draft:  
> "Hi team, just checking in because we need to maybe move some deadlines around due to a few issues. Let me know what you think. We should probably discuss soon."

**How the template shows up:**
- **R, Review:** The prompt explicitly asks the model to examine the email for clarity, tone, grammar, and professionalism.
- **O, Observe:** It asks for specific problems such as awkward phrasing and missing information.
- **A, Assess:** It requires scores with explanations, which forces evaluation instead of vague opinions.
- **S, Suggest:** It asks for a short list of precise improvements.
- **T, Transform:** It ends by asking for a rewritten version of the email.

**Why it improves the prompt:**
This version is strong because every improvement step is spelled out. The model is less likely to skip straight to rewriting without explaining what is wrong first. That matters, especially if you want to learn from the edit instead of just accepting a mystery makeover. It also creates a mini quality-control process, like having an editor who is slightly less dramatic than a newspaper copy desk.

### Sample prompt 2: Semi-structured version

> I wrote a product description for a reusable water bottle. Help me improve it with a ROAST-style review.  
> - Look over it for clarity and sales appeal  
> - Point out anything vague, repetitive, or unconvincing  
> - Judge how well it would work for online shoppers  
> - Give me 5 specific suggestions  
> - Then rewrite it in a cleaner, more persuasive style  
>   
> Draft:  
> "This water bottle is really great for lots of people and can be used in many places. It has a good design and helps you stay hydrated all day."

**How the template shows up:**
- **R, Review:** "Look over it for clarity and sales appeal" starts the evaluation.
- **O, Observe:** "Point out anything vague, repetitive, or unconvincing" asks the model to notice concrete weaknesses.
- **A, Assess:** "Judge how well it would work for online shoppers" adds a performance standard.
- **S, Suggest:** "Give me 5 specific suggestions" requests actionable feedback.
- **T, Transform:** "Rewrite it in a cleaner, more persuasive style" completes the improvement loop.

**Why it improves the prompt:**
This version is more relaxed, but still structured enough to guide the model. It is useful when you want a practical editing pass without turning your prompt into a legal contract. The prompt tells the model what to check, who the text is for, and how to improve it. That usually leads to a rewrite that is tighter and more useful than simply saying, "Can you polish this?"

### Sample prompt 3: Natural version

> Read this paragraph like an editor, tell me what feels weak or unclear, explain how well it would work for busy readers, give me a few smart fixes, and then rewrite it so it sounds sharper and easier to trust:  
> "Our training program offers many benefits for staff and helps teams do better work in different situations."

**How the template shows up:**
- **R, Review:** "Read this paragraph like an editor" asks for a full check of the draft.
- **O, Observe:** "Tell me what feels weak or unclear" covers specific observations.
- **A, Assess:** "Explain how well it would work for busy readers" evaluates the text against an audience need.
- **S, Suggest:** "Give me a few smart fixes" asks for concrete feedback.
- **T, Transform:** "Rewrite it so it sounds sharper and easier to trust" requests the revised version.

**Why it improves the prompt:**
This version sounds natural, which is great when you do not want to feel like you are filling out prompt tax forms. Even though the template is not labeled, the logic is still there. That means you get the benefits of ROAST without sounding robotic. It is a good reminder that structure can live under the surface. Like good office organization, nobody applauds it, but everything works better.

## Warnings and extra tips

ROAST is useful, but it is not magic.

- **Do not skip the original goal.** The model needs to know what the text is trying to do. A sales page, apology email, and project summary should not be judged by the same standards.
- **Too much evaluation can create clutter.** If the task is tiny, asking for five layers of analysis may be overkill. You do not need a formal review board for a two-sentence caption.
- **Be careful with vague quality words.** Terms like "better," "stronger," or "more professional" can mean almost anything. Add criteria such as concise, friendly, persuasive, accurate, or easy to skim.
- **Transformation can drift.** Sometimes the rewrite changes the meaning too much. If accuracy matters, tell the model to preserve the original intent and facts.
- **The model may confidently critique bad assumptions.** If the original content contains incorrect facts, the AI might improve the writing without fixing the truth. If accuracy matters, add a fact-check request.
- **ROAST is best after a draft exists.** This is an improvement-loop technique, not usually the best first step for creating something from scratch.

A good extra move is to ask for the output in stages. For example, first request the review and suggestions only. Then, if you agree with the feedback, ask for the transformation. That gives you more control and fewer surprise rewrites.

## Quick summary

ROAST helps you improve prompts by turning revision into a process: **Review, Observe, Assess, Suggest, Transform**. It teaches a simple but powerful lesson, the first answer is not the finish line.

Try ROAST on something you already have: an email, a LinkedIn summary, a product description, or a paragraph from a report. Run one draft through the five steps and compare the before and after. That is where prompt engineering starts to feel less like guesswork and more like skill.

