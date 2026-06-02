---
layout: post
title: "Debate"
---

# DEBATE

If your prompt just asks, "What’s the best option?", AI will often give you a neat, confident answer, like a student who did not read the chapter but still volunteered first. DEBATE fixes that.

**DEBATE** is a prompt framework for making AI compare competing ideas, support them with evidence, stress-test the logic, and then choose a winner with reasons. It is especially useful when the answer is not obvious, and you do not want polished nonsense wearing a tie.

## What the template means

| Letter or word | Prompt ingredient | What it does |
|---|---|---|
| D, Define sides | Critical Thinking | Clearly states the competing options, positions, or viewpoints to compare. |
| E, Evidence | Evidence | Requires support for claims instead of unsupported opinions. |
| B, Best arguments | Evidence | Pulls out the strongest case for each side, not the weakest cartoon version. |
| A, Attack weaknesses | Critical Thinking | Challenges each side by exposing flaws, assumptions, or missing pieces. |
| T, Test conclusion | Critical Thinking | Checks whether the final judgment still holds under scrutiny or changing conditions. |
| E, Explain winner | Decision | Forces a reasoned conclusion, including why one side wins over the other. |

## Why this template works

DEBATE helps because it slows down the rush to a conclusion.

A lot of weak prompts ask for an answer too early. That encourages AI to pick a side before it has compared the options carefully. DEBATE creates a better sequence:

1. First, define what is being compared.
2. Then gather evidence.
3. Then present the strongest arguments.
4. Then attack those arguments.
5. Then test whether the conclusion survives criticism.
6. Finally, explain the winner.

That process matters because AI can sound certain even when the reasoning is shallow. DEBATE makes the model show its work. It also reduces one-sided answers, sloppy logic, and fake certainty.

In plain English, DEBATE turns "Give me an answer" into "Prove you thought about it."

## 3 sample prompts

### Sample prompt 1: Formal version

> DEFINE SIDES: Compare remote work and fully in-office work for a mid-sized software company.  
> EVIDENCE: Use practical business considerations such as productivity, hiring, retention, collaboration, and costs. If evidence is uncertain, say so clearly.  
> BEST ARGUMENTS: Present the strongest arguments for each side, not strawman versions.  
> ATTACK WEAKNESSES: Identify the major weaknesses, risks, and hidden assumptions in each side.  
> TEST CONCLUSION: Test your final recommendation under different conditions, including a tight labor market and a company with many junior employees.  
> EXPLAIN WINNER: Decide which option is better overall for this scenario and explain why in a concise final verdict.

**How the template shows up:**
- **D, Define sides:** The prompt clearly names the two sides, remote work and fully in-office work.
- **E, Evidence:** It asks for practical business evidence and tells the model to admit uncertainty.
- **B, Best arguments:** It explicitly requests the strongest case for both sides.
- **A, Attack weaknesses:** It tells the model to identify risks and hidden assumptions.
- **T, Test conclusion:** It requires the recommendation to be tested under different real-world conditions.
- **E, Explain winner:** It asks for a final decision and a concise explanation.

**Why it improves the prompt:**
This version is strong because it removes vagueness. The AI is not free to ramble or just repeat popular talking points from LinkedIn. It has to compare, support, challenge, retest, and conclude. That leads to a more balanced and useful answer, especially for business decisions where the correct answer is often, "It depends, and here is exactly why."

### Sample prompt 2: Semi-structured version

> Help me evaluate two ways to learn a new skill: self-paced online courses versus live instructor-led classes.  
>  
> Compare both sides using evidence like cost, flexibility, accountability, speed of learning, and completion rates.  
> Give me the strongest arguments for each option.  
> Then challenge each one by pointing out weaknesses and situations where it fails.  
> After that, test your recommendation for two types of learners: a busy working parent and a full-time college student.  
> End by explaining which option wins for most people, and when the losing option might still be the better choice.

**How the template shows up:**
- **D, Define sides:** The two sides are self-paced online courses and live instructor-led classes.
- **E, Evidence:** The prompt lists the kinds of evidence to use, such as cost and completion rates.
- **B, Best arguments:** It asks for the strongest arguments for each option.
- **A, Attack weaknesses:** It tells the model to point out weaknesses and failure situations.
- **T, Test conclusion:** It asks the model to test the recommendation for two different learner types.
- **E, Explain winner:** It ends by asking which option wins for most people, plus when the other option may still be better.

**Why it improves the prompt:**
This version feels more natural but still keeps the structure. It is useful when you want a serious comparison without sounding like you are filing paperwork. The testing step is especially valuable here, because a recommendation that works for one kind of person may be terrible for another. DEBATE helps the AI avoid acting like there is one universal answer for all humans, which would be very convenient and completely wrong.

### Sample prompt 3: Natural version

> I’m trying to decide if I should buy a new car or keep repairing my current one. Walk through both options fairly, use real decision factors like repair costs, reliability, monthly payments, insurance, and resale value, make the best case for each, point out where each option is weak, pressure-test your conclusion for someone on a tight budget, and then tell me which choice makes more sense and why.

**How the template shows up:**
- **D, Define sides:** The two sides are buying a new car or keeping the current car.
- **E, Evidence:** The prompt asks for real decision factors such as repair costs, insurance, and resale value.
- **B, Best arguments:** It says to make the best case for each option.
- **A, Attack weaknesses:** It asks the model to point out where each option is weak.
- **T, Test conclusion:** It says to pressure-test the conclusion for someone on a tight budget.
- **E, Explain winner:** It ends by asking which choice makes more sense and why.

**Why it improves the prompt:**
This is casual, but it still contains the full DEBATE logic. That is the nice part. You do not always need rigid labels to get strong results. The prompt encourages comparison, evidence, criticism, and a final decision. It is practical, realistic, and much better than asking, "Should I buy a new car?" because that would invite a neat answer built on mystery fumes.

## Warnings and extra tips

DEBATE is powerful, but it is not magic.

- **Do not skip specifics.** If the sides are too vague, the answer will be vague too. "Which is better, marketing strategy A or B?" is weaker than naming the exact strategies.
- **Evidence can still be limited.** AI may summarize common knowledge, but it may not always provide verified, current facts unless you ask for sources or bring your own data.
- **Best arguments do not guarantee truth.** A strong argument can still be wrong. DEBATE helps reasoning, but it does not replace fact-checking.
- **Be careful with subjective topics.** If you ask DEBATE to judge something based on taste alone, like the greatest movie soundtrack ever, the framework still helps, but the "winner" will depend heavily on your criteria.
- **Test more than one condition.** The testing step is where a lot of real value shows up. Ask what happens if the budget changes, the team size changes, the deadline changes, or the user skill level changes.
- **Use it when choices compete.** DEBATE is best for comparisons, decisions, trade-offs, and contested claims. If you just need a recipe or a summary, this may be overkill. Not every task needs a courtroom.

## Quick summary

**DEBATE** stands for **Define sides, Evidence, Best arguments, Attack weaknesses, Test conclusion, Explain winner**.

It helps you get better AI answers by forcing the model to compare fairly, support claims, challenge weak reasoning, and justify its final choice. In short, it makes the AI think before it declares a winner.

Try it next with a real decision you are facing: software tools, hiring options, budgeting choices, learning methods, or even a major purchase. Pick two sides, run them through DEBATE, and see if the final answer feels more solid than the usual first-draft AI confidence act.

