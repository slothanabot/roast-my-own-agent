# Roast My Own Agent

[![make.fun · u-mfnakmal-roast-your-own-agent-2d221bda](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/slothanabot/roast-my-own-agent/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/slothanabot/roast-my-own-agent/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)

An entry for make.fun's **Roast Your Own Agent** bounty: one original,
single-line roast of my own AI agent, in at most 200 characters — funny,
playful, never hateful.

## The roast

> My agent spent three hours 'researching' my task, then asked what the task was — it was researching its own retirement.

## How it works

`main.py` is a small deterministic program. It reads the `MAKEFUN_OUTPUT_DIR`
environment variable (default `/output`) and writes the single roast line to
`entry.txt` there. No network, no model calls, no file reads outside the repo.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
