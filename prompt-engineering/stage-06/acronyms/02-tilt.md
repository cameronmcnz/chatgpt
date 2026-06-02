---
layout: post
title: "Tilt"
---

# TILT

TILT is for the moment when you do not want ChatGPT to just give you an answer, you want it to think with you. It helps you rotate the problem, inspect it, surface the compromises, and poke holes in the assumptions before you commit. Basically, it is the difference between "pick something" and "help me avoid a dumb decision."

## What the template means

| Letter or word | Prompt ingredient | What it does |
|---|---|---|
| **T, Take another angle** | Perspective Shift | Forces the model to look at the issue from a different viewpoint, lens, or stakeholder position. |
| **I, Inspect** | Evaluation | Examines the idea, option, or plan more carefully instead of accepting it at face value. |
| **L, List trade-offs** | Trade-offs | Identifies the upsides, downsides, risks, and consequences of each choice. |
| **T, Test assumptions** | Critical Thinking | Checks what is being taken for granted and asks whether those assumptions are actually true. |

## Why this template works

Most weak prompts ask for a conclusion too early. That is like hiring a consultant who walks into the room, glances at one spreadsheet, and immediately announces a grand strategy. Very confident, very dramatic, not always very useful.

TILT improves prompts because it slows the model down in the right way:

- **Take another angle** makes the model consider alternative viewpoints.
- **Inspect** pushes beyond a surface-level reaction.
- **List trade-offs** keeps the answer realistic, because good decisions usually involve compromise.
- **Test assumptions** reduces the chance that the whole answer is built on a shaky premise.

This template is especially useful in the analysis and decision-making stage. Use it when you are comparing tools, evaluating plans, making a recommendation, or pressure-testing an idea before you act on it.

## 3 sample prompts

### Sample prompt 1: Formal version

> **TILT:**
>  
> **TAKE ANOTHER ANGLE:** Evaluate whether a small business should adopt a four-day workweek from the perspective of the owner, employees, and customers.  
> **INSPECT:** Assess likely effects on productivity, scheduling, morale, and service quality.  
> **LIST TRADE-OFFS:** Identify the main benefits, drawbacks, risks, and operational compromises.  
> **TEST ASSUMPTIONS:** Point out assumptions behind the idea, including assumptions about employee output, customer expectations, and staffing flexibility.  
> **OUTPUT FORMAT:** End with a balanced recommendation in one short paragraph.

**How the template shows up:**
- **T, Take another angle:** The prompt explicitly asks for three perspectives, owner, employees, and customers.
- **I, Inspect:** It asks for careful assessment of productivity, scheduling, morale, and service quality.
- **L, List trade-offs:** It directly requests benefits, drawbacks, risks, and compromises.
- **T, Test assumptions:** It asks the model to identify hidden assumptions behind the plan.

**Why it improves the prompt:**
This version is strong because it prevents a simplistic yes-or-no answer. Instead of saying "a four-day workweek is good" or "bad," the model has to examine the decision from multiple sides, evaluate real effects, and challenge the premises. That usually leads to a more credible recommendation, and fewer "sounds nice in theory" moments.

### Sample prompt 2: Semi-structured version

> I am choosing between Zoom, Microsoft Teams, and Google Meet for a remote training program.
>
> - Look at this from the perspective of an IT manager and from the perspective of a non-technical trainer.
> - Inspect each option for ease of use, security, recording features, and cost.
> - List the main trade-offs, not just the strengths.
> - Test any assumptions people often make about "the best" video platform.
> - Finish by recommending one option for a small company with limited tech support.

**How the template shows up:**
- **T, Take another angle:** The prompt asks for two different viewpoints, IT manager and non-technical trainer.
- **I, Inspect:** It gives specific evaluation criteria, ease of use, security, recording features, and cost.
- **L, List trade-offs:** It explicitly asks for trade-offs, not just selling points.
- **T, Test assumptions:** It tells the model to question common beliefs about what makes a platform "best."

**Why it improves the prompt:**
Without TILT, the model might just produce a generic feature comparison. With TILT, the answer becomes more decision-ready. It accounts for stakeholder differences, weighs practical pros and cons, and avoids blindly repeating common assumptions like "the most popular tool is automatically the right one." Spoiler: popularity is not a business strategy.

### Sample prompt 3: Natural version

> I am thinking about taking a lower-paying job that is fully remote instead of keeping my higher-paying office job. Help me think it through from more than one point of view, look closely at the real pros and cons, and call out any assumptions I might be making about money, stress, commute time, career growth, and work-life balance. Then give me your honest recommendation.

**How the template shows up:**
- **T, Take another angle:** "From more than one point of view" signals a perspective shift.
- **I, Inspect:** "Look closely" asks for evaluation rather than a quick opinion.
- **L, List trade-offs:** "Real pros and cons" asks for trade-offs.
- **T, Test assumptions:** "Call out any assumptions I might be making" directly asks for critical thinking.

**Why it improves the prompt:**
This casual version still works because the core TILT moves are built into normal language. The model is guided to think more deeply without sounding robotic or overly technical. That makes it ideal for real-life decisions, especially personal or professional choices where emotions, convenience, and long-term consequences all get tangled together.

## Warnings and extra tips

TILT is powerful, but it is not magic. A few things to watch for:

- **Do not skip the subject matter details.** TILT gives a thinking structure, but you still need to name the actual decision, options, or context.
- **Too many angles can become clutter.** If you ask for ten perspectives, seven trade-offs, and a philosophical reflection on capitalism, you may get a messy answer. Pick the most relevant angles.
- **Assumptions need context.** If the model has no facts, it will test assumptions in a generic way. Give background when possible.
- **This is not enough for high-stakes decisions by itself.** TILT is great for analysis, but it does not replace legal advice, medical advice, financial planning, or actual evidence from the real world.
- **Ask for a recommendation if you want one.** Otherwise, the model may stay neutral forever, like a committee that has discovered snacks but not conclusions.
- **Use follow-up prompts.** After a TILT response, ask things like:
  - "Which trade-off matters most?"
  - "What assumption is most dangerous?"
  - "What would change your recommendation?"

## Quick summary

TILT helps you get better decision support from ChatGPT by doing four things: shift perspective, inspect carefully, list trade-offs, and test assumptions. It turns vague analysis into something sharper, more balanced, and more useful.

Try it next on a real decision you are facing, a software choice, a work process, a hiring plan, or even a personal career question. Pick one issue, write a quick TILT prompt, and see what changes when the model stops guessing and starts thinking.

