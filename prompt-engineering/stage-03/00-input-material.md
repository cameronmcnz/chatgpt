---
layout: post
title: "Input Material"
---

# Input Material

Input material is the stuff you hand to ChatGPT so it has something real to work with. It is the raw content behind the request, such as a document, transcript, notes, pasted text, or source information. If your prompt is the instruction, input material is the evidence locker.

## What this term means

In prompt engineering, **input material** means the content ChatGPT should use when answering.

That content might be:

- a meeting transcript
- an email draft
- research notes
- a policy document
- a blog post
- customer feedback
- a spreadsheet summary
- pasted text from another source

The key idea is simple: instead of asking ChatGPT to guess, you give it the actual material you want it to analyze, rewrite, summarize, organize, or extract from.

For example, there is a big difference between:

- “Summarize this meeting.”
- “Summarize the following meeting transcript and list action items.”

The second version gives ChatGPT real input material to work with. That usually leads to a more accurate and useful response, which is nice, because guesswork is fun mostly in game shows and not in work.

## Why it improves a prompt

Input material improves a prompt because it gives the model context.

Without input material, ChatGPT often has to fill in gaps based on general patterns. Sometimes that works. Sometimes it confidently invents details like an intern trying to sound busy in a status meeting.

When you provide input material, you help the model:

- stay grounded in the actual content
- respond more specifically
- reduce irrelevant assumptions
- extract facts, themes, or actions more accurately
- match your real situation instead of a generic one

In practical prompt engineering, input material acts like the source text. Your instruction tells ChatGPT **what to do**, and the input material tells it **what to do it with**.

A useful pattern is:

**Task + Input Material + Output Instructions**

For example:

- Task: Summarize
- Input material: Meeting transcript
- Output instructions: Use 5 bullet points and list decisions separately

That structure makes prompts clearer and easier to control.

## Similar words you might see

People may use several similar terms for input material. They usually mean roughly the same thing, depending on context:

- **Material**
- **Input**
- **Source**
- **Document**
- **Transcript**
- **Notes**

These are not always perfectly interchangeable, but they point to the same idea: the content ChatGPT should use as the basis for its answer.

## 3 sample prompts

### Sample prompt 1

> Summarize the following transcript into 5 bullet points, then list any action items by owner and deadline.  
>   
> Transcript:  
> [paste meeting transcript here]

This prompt uses **input material** by supplying a transcript for ChatGPT to analyze. The task is not floating around in empty space. It is attached to a specific source.

Using input material improves the prompt because the summary and action items will come from the actual meeting content, not from vague assumptions about what meetings usually sound like. That means fewer invented details and more useful output.

### Sample prompt 2

> Rewrite the following email draft so it sounds professional but still warm. Keep the message under 150 words.  
>   
> Email draft:  
> [paste email here]

Here, the input material is the original email draft. ChatGPT is not being asked to create a brand new email from thin air. It is being asked to transform the content you provided.

This improves the prompt because the rewrite stays tied to your original message, intent, and facts. Without the input material, ChatGPT would have to guess what the email is supposed to say, which is a great way to get a polished answer to the wrong problem.

### Sample prompt 3

> Review the notes below and identify the top 3 customer complaints, the likely root causes, and 2 recommendations for improvement.  
>   
> Notes:  
> [paste support notes or feedback here]

This prompt uses input material in the form of notes. The notes are the source ChatGPT should inspect before identifying patterns and making recommendations.

Using input material improves the prompt because it grounds the analysis in actual customer feedback. Instead of giving generic advice like “improve communication” and “do better,” the model can connect its answer to the specific issues in the notes.

## Quick summary

Input material is the part of the prompt that gives ChatGPT something concrete to work on. If instructions are the recipe, input material is the pile of ingredients, and yes, the results are usually better when you remember to bring those too.

