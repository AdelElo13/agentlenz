# X/Twitter Search Queries — AgentFinOps Prospect Finding

Use the "Latest" tab for all searches (not Top). Filter mentally for people with technical roles at companies that would have real AI spend.

---

## Category 1 — People Complaining About AI API Costs

People expressing direct pain about AI API bills. High intent — they're already feeling the problem.

```
"openai bill" OR "anthropic bill" -is:retweet lang:en
```

```
"api costs" "ai" ("too expensive" OR "out of control" OR "surprised" OR "shocked") -is:retweet
```

```
"llm costs" OR "llm billing" OR "llm spend" -is:retweet lang:en
```

```
"gpt-4 costs" OR "gpt4 costs" ("month" OR "budget" OR "expensive") -is:retweet
```

```
"claude api" costs ("budget" OR "expensive" OR "bill") -is:retweet
```

```
"ai api" ("budget" OR "spending" OR "cost per") -is:retweet lang:en
```

```
"token costs" ("month" OR "weekly" OR "daily") -is:retweet lang:en
```

```
"prompt costs" OR "inference costs" ("production" OR "scaling") -is:retweet
```

---

## Category 2 — People Discussing AI Agent Budgets and Cost Management

People thinking about cost at the architecture level. Slightly more technical, but highly relevant.

```
"agent costs" OR "agentic costs" -is:retweet lang:en
```

```
"ai agents" ("cost" OR "expensive" OR "budget") -is:retweet lang:en
```

```
("langchain" OR "langgraph" OR "autogen" OR "crewai") "costs" -is:retweet lang:en
```

```
"multi-agent" ("cost" OR "billing" OR "tokens") -is:retweet lang:en
```

```
"ai workflow" ("cost" OR "expensive" OR "spending") -is:retweet lang:en
```

```
"token budget" OR "token limit" ("production" OR "scaling") -is:retweet
```

```
"cost per call" OR "cost per run" "llm" -is:retweet lang:en
```

---

## Category 3 — Active LLM Builders

People building with LLM APIs who may not have hit cost pain yet, but will. Good for warm outreach on the agent-building angle.

```
"building with" ("openai" OR "anthropic" OR "claude" OR "gpt-4") -is:retweet lang:en
```

```
"shipped" OR "launched" ("ai agent" OR "llm app" OR "ai product") -is:retweet lang:en
```

```
"in production" ("gpt-4" OR "claude" OR "llm" OR "openai") -is:retweet lang:en
```

```
"built an agent" OR "building an agent" ("openai" OR "anthropic" OR "claude") -is:retweet
```

```
from:swyx OR from:simonw OR from:karpathy -is:retweet
```
*(Monitor replies to these accounts — the people who reply and comment are active builders)*

```
"openai" OR "anthropic" "production" ("million tokens" OR "thousands of calls" OR "at scale") -is:retweet
```

---

## Category 4 — Specific Pain Points

Searches for people with adjacent problems that AgentFinOps solves — cost visibility, unexpected bills, optimization work.

```
"optimizing" ("llm" OR "openai" OR "claude") ("costs" OR "tokens" OR "spend") -is:retweet
```

```
"reduced" ("llm costs" OR "openai costs" OR "ai costs") -is:retweet lang:en
```

```
"prompt caching" OR "model routing" ("costs" OR "savings") -is:retweet lang:en
```

```
"switched from gpt-4" OR "switched to claude" OR "switched to haiku" (cost OR cheaper OR savings) -is:retweet
```

```
"ai observability" OR "llm observability" -is:retweet lang:en
```

---

## How to Qualify a Prospect in 60 Seconds

Before DMing, quickly check:

1. **Role signal** — Are they an engineer, engineering lead, founder, or CTO? Skip marketers and non-technical accounts.
2. **Company signal** — Do they work somewhere with real AI spend (startup with funding, mid-size tech company, AI-native product)? Personal projects are lower priority.
3. **Recency** — Did the relevant tweet happen in the last 30 days? Older = colder.
4. **Engagement pattern** — Do they respond to DMs? (Check if their replies are public — if they reply to others, they'll likely reply to you.)
5. **Specificity** — The more specific their complaint or question, the warmer the lead. "My OpenAI bill was $3K this month and I don't know why" is better than "AI is expensive."

---

## Saved Search Tips

- Save the high-signal queries in X's advanced search or a third-party tool (TweetDeck, Typefully)
- Run searches every morning during the high-volume outreach phase (weeks 1–2)
- Keep a note of accounts you've already DMed — X doesn't show this clearly
- Bookmark tweets that are good prospect signals even if you can't DM that day
