# CAB Discovery Call Script — 15 Minutes

**Purpose:** Understand their AI cost problem deeply, assess fit, and make the CAB ask.
**Not a demo.** You will ask questions, take notes, and pitch the CAB at the end.
**Target outcome:** They agree to sign the LOI, or you get a clear no.

---

## Before the Call

Send a short calendar invite note:
```
Looking forward to chatting. Quick heads up: this is mostly me asking questions about your setup — not a product demo. Come ready to complain about AI costs if that's on your radar.

Rough agenda:
- 2 min: quick context on what I'm building
- 8 min: your situation, what you've tried, what's still broken
- 5 min: the ask (Customer Advisory Board)

Talk soon.
```

Have open: a notes doc, their Twitter/LinkedIn profile, any tweets or posts you referenced in the DM.

---

## Opening — 2 Minutes

**Goal:** Set context quickly, give them confidence this is worth their time, make them feel heard before anything else.

> "Hey [name], really appreciate you taking the time. I'll be quick about what I'm building, and then I want to spend most of this call understanding your situation — so I'll flip it to you pretty fast.
>
> Two sentences on AgentLens: it's an AI agent cost optimization platform. The core problem I'm solving is that engineering teams running LLM workloads often have no visibility into where the money is actually going — which agents, which prompts, which calls — and no real levers to control it without tearing apart the architecture.
>
> I'm at an early stage — still validating the problem before I build too much. That's exactly why I'm talking to people like you.
>
> Before I ask anything: does that problem space resonate at all, or is cost not really on your radar?"

*[If they say it doesn't resonate: "Totally fair — what are the bigger headaches right now?" Pivot to learning mode. Still finish the call.]*

---

## Discovery — 8 Minutes

**Goal:** Understand their actual situation. Ask these questions in a natural conversation — not as an interrogation. Pick the ones most relevant based on what they said in the opening.

### On their AI usage
- "What are you actually running? Like — are these batch jobs, real-time user-facing features, internal tools, or a mix?"
- "Which APIs are you calling? OpenAI, Anthropic, something else? Are you mixing providers?"
- "Roughly what does your AI API spend look like monthly? Order of magnitude is fine — I'm not collecting data, just trying to understand the scale."

### On cost visibility
- "How do you know how much each thing costs right now? Is there any attribution, or does it just show up as one number on the bill?"
- "Has a bill ever surprised you? Like a run that cost way more than you expected?"
- "If I asked you 'how much did [specific agent or feature] cost last month' — could you answer that?"

### On what they've tried
- "Have you done anything to get costs under control? Prompt caching, model switching, batching, building your own tracking?"
- "What worked? What felt like duct tape?"
- "Is this a problem you've got budget to solve, or is it more a 'we just live with it' situation?"

### On pain
- "If you could wave a wand and fix one thing about how you manage AI costs today, what would it be?"
- "Is this primarily a visibility problem, a control problem, or a 'we just need to spend less' problem?"
- "Who on your team actually owns this problem? Is it you, a platform team, finance?"

**Listen for:**
- "We have no idea where the money goes" — strong signal
- "I built a spreadsheet / scraper to track it" — they care enough to hack something, prime for real tooling
- "Our infra costs are fine but AI is unpredictable" — budget variance pain
- "We switched from GPT-4 to [cheaper model] but had to test everything" — cost/quality tradeoff pain

**Notes to take:** What they said costs the most, what tooling they're using, what they've tried, what would make their life better. You'll use this in the LOI follow-up and product direction.

---

## The Ask — 5 Minutes

**Goal:** Explain the CAB clearly, make the ask directly, handle objections.

### Transition into the ask

> "This has been really helpful — I'm hearing [summarize 1-2 things you learned]. That's exactly the kind of nuance I need to get right.
>
> I want to be straight with you about where I am and what I'm looking for.
>
> I'm putting together a Customer Advisory Board — 10 people total. The idea comes from a framework called Micaia: before I build too much, I want 10 people who have the real problem, who will use an early version, and who will tell me honestly when I'm wrong. In exchange, those 10 people get the product at 70% off for life.
>
> It's not a contract — you're not committing to buy anything. You sign a one-page Letter of Interest that basically says: 'I'm interested in this product, I'll use it when it's ready, I'll give feedback, and I'm okay being listed as an early customer.' That's it."

### The CAB pitch (exact language)

> "Here's the deal as clearly as I can state it:
>
> You get: 70% off AgentLens for life — whatever the eventual pricing is, you pay 30% of it, forever.
>
> I get: you use the product when it's ready, you tell me what's broken and what's missing, and I can say 'AgentLens is being used by engineers at [company]' when I talk to investors and other customers.
>
> The LOI is non-binding. If the product never ships, you've lost nothing. If it ships and it's not useful to you, you walk away. The discount is only meaningful if the product is worth something to you.
>
> I'm looking for people who actually have the problem and will give me unfiltered feedback — not people who want to be polite and tell me it's great."

### The direct ask

> "Based on what you've told me today — does this sound like something you'd want to be part of?"

*[Give them space to answer. Don't fill the silence.]*

---

## Handling Objections

**"I need to think about it."**
> "Totally fair. What would help you decide? Is it about the product, the timing, something else?"
> If they're genuinely interested: "I can send you the LOI to look at — it's one page, nothing binding. Sometimes seeing it makes it easier to decide."

**"What does the product actually do? I haven't seen anything."**
> "Fair question. Honestly, I don't want to demo anything that isn't real yet — I'd rather build the right thing than show you a pretty mockup. What I can tell you is the core capability: [describe your actual current state honestly]. The CAB is partly how I figure out what the full product needs to be."

**"What's the timeline? When would I actually use it?"**
> "I'm targeting [your honest timeline] for first access for CAB members. If that's too far out, I'd rather you tell me now — I don't want someone to sign an LOI and then feel like it was a waste of time."

**"70% off what? You don't have pricing yet."**
> "Correct — pricing is TBD. What I can promise is that the 70% is off whatever we charge everyone else. It'll be in the LOI. If the pricing ends up being unreasonable, the discount makes it reasonable. And you're not committed to buy either way."

**"I'm not the decision-maker for tools."**
> "That makes sense. Is this the kind of thing you'd want to bring to them, or is it not worth your time to do that? I'd rather know now than have you feel stuck in the middle."

---

## Close

If they say yes:
> "That's great. I'll send you the LOI today — it's short, you can sign it digitally. Once it's signed, I'll add you to the CAB Slack/group and we'll be in touch as things develop. Any questions before I let you go?"

If they say no:
> "I appreciate you being straight with me. Can I ask — is it the product, the timing, or something else? I'm genuinely trying to figure out where I'm wrong."
> Then: "Mind if I stay in touch? If anything changes or I make progress you'd find interesting, I'll reach out."

---

## After the Call

Within 2 hours:
- Send thank-you note referencing 1-2 specific things they said
- If they said yes: attach the LOI
- If they said maybe: include the LOI anyway with "no pressure to sign — just easier to decide if you can see it"
- Update the tracker

Notes to record: their current spend, what they've tried, their biggest pain point, which DM template worked, what objections came up.
